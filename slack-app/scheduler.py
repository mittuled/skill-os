"""APScheduler-based loop that runs enabled rituals on their cron schedule.

Scheduled runs iterate every user who has a given ritual enabled. On-demand
runs (triggered from App Home or the slash command) execute a single user
synchronously. Every run is recorded in the audit log.
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from slack_sdk import WebClient

from rituals import REGISTRY, Ritual, RitualContext
from storage import Storage

logger = logging.getLogger(__name__)


class RitualScheduler:
    def __init__(self, slack_client: WebClient, storage: Storage):
        self._scheduler = BackgroundScheduler(timezone="UTC")
        self._slack = slack_client
        self._storage = storage

    def start(self) -> None:
        for ritual in REGISTRY.values():
            if not ritual.default_cron:
                continue
            self._scheduler.add_job(
                self._run_ritual_for_all_enabled,
                CronTrigger.from_crontab(ritual.default_cron),
                args=[ritual.name],
                id=f"ritual_{ritual.name}",
                replace_existing=True,
            )
        self._scheduler.start()
        logger.info("Scheduler started with %d rituals", len(REGISTRY))

    def shutdown(self) -> None:
        self._scheduler.shutdown(wait=False)

    def trigger_for_user(self, ritual_name: str, slack_user_id: str) -> None:
        """Run a ritual for a single user on demand (synchronous)."""
        ritual = REGISTRY.get(ritual_name)
        if ritual is None:
            raise ValueError(f"Unknown ritual: {ritual_name}")
        pref = self._storage.get_preference(slack_user_id, ritual_name) or {}
        config = pref.get("config", {})
        self._execute(ritual, slack_user_id, config)

    def _run_ritual_for_all_enabled(self, ritual_name: str) -> None:
        ritual = REGISTRY.get(ritual_name)
        if ritual is None:
            return
        for pref in self._storage.list_enabled(ritual_name):
            user_id = pref["slack_user_id"]
            try:
                self._execute(ritual, user_id, pref["config"])
            except Exception as e:  # noqa: BLE001 — record and continue
                logger.exception(
                    "Ritual %s failed for %s", ritual_name, user_id
                )
                self._storage.record_run(
                    slack_user_id=user_id,
                    ritual_name=ritual_name,
                    status="error",
                    output_preview=str(e),
                )

    def _execute(self, ritual: Ritual, user_id: str, config: dict) -> None:
        started = datetime.now(tz=timezone.utc)
        ctx = RitualContext(
            slack_user_id=user_id,
            slack_client=self._slack,
            config=config,
        )
        result = ritual.run(ctx)
        self._storage.record_run(
            slack_user_id=user_id,
            ritual_name=ritual.name,
            status="ok" if result.success else "error",
            output_preview=result.summary if result.success else (result.error or ""),
            started_at=started,
        )
