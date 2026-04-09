"""SQLite storage for user ritual preferences and run history.

Single-workspace MVP. Two tables:
- user_preferences: which rituals each user has enabled, plus their config
- ritual_runs: audit log of every ritual execution
"""
from __future__ import annotations

import json
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

DEFAULT_DB_PATH = Path(os.environ.get("DATABASE_PATH", "./skillos-slack.db"))

SCHEMA = """
CREATE TABLE IF NOT EXISTS user_preferences (
    slack_user_id TEXT NOT NULL,
    ritual_name TEXT NOT NULL,
    enabled INTEGER NOT NULL DEFAULT 0,
    schedule_cron TEXT,
    config_json TEXT,
    updated_at TEXT NOT NULL,
    PRIMARY KEY (slack_user_id, ritual_name)
);

CREATE TABLE IF NOT EXISTS ritual_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slack_user_id TEXT NOT NULL,
    ritual_name TEXT NOT NULL,
    started_at TEXT NOT NULL,
    finished_at TEXT,
    status TEXT NOT NULL,
    output_preview TEXT
);

CREATE INDEX IF NOT EXISTS ritual_runs_user_idx
    ON ritual_runs(slack_user_id, started_at DESC);
"""


def _utcnow_iso() -> str:
    return datetime.now(tz=timezone.utc).isoformat()


class Storage:
    def __init__(self, path: Path | str = DEFAULT_DB_PATH):
        self.path = Path(path)
        self._init_schema()

    @contextmanager
    def _conn(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _init_schema(self) -> None:
        with self._conn() as conn:
            conn.executescript(SCHEMA)

    def get_preference(
        self, slack_user_id: str, ritual_name: str
    ) -> dict[str, Any] | None:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT * FROM user_preferences "
                "WHERE slack_user_id = ? AND ritual_name = ?",
                (slack_user_id, ritual_name),
            ).fetchone()
        if row is None:
            return None
        return {
            "slack_user_id": row["slack_user_id"],
            "ritual_name": row["ritual_name"],
            "enabled": bool(row["enabled"]),
            "schedule_cron": row["schedule_cron"],
            "config": json.loads(row["config_json"] or "{}"),
            "updated_at": row["updated_at"],
        }

    def list_enabled(self, ritual_name: str) -> list[dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute(
                "SELECT * FROM user_preferences "
                "WHERE ritual_name = ? AND enabled = 1",
                (ritual_name,),
            ).fetchall()
        return [
            {
                "slack_user_id": r["slack_user_id"],
                "ritual_name": r["ritual_name"],
                "enabled": True,
                "schedule_cron": r["schedule_cron"],
                "config": json.loads(r["config_json"] or "{}"),
            }
            for r in rows
        ]

    def set_preference(
        self,
        slack_user_id: str,
        ritual_name: str,
        enabled: bool,
        schedule_cron: str | None = None,
        config: dict[str, Any] | None = None,
    ) -> None:
        with self._conn() as conn:
            conn.execute(
                """INSERT INTO user_preferences
                   (slack_user_id, ritual_name, enabled, schedule_cron,
                    config_json, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ON CONFLICT(slack_user_id, ritual_name) DO UPDATE SET
                     enabled = excluded.enabled,
                     schedule_cron = excluded.schedule_cron,
                     config_json = excluded.config_json,
                     updated_at = excluded.updated_at""",
                (
                    slack_user_id,
                    ritual_name,
                    1 if enabled else 0,
                    schedule_cron,
                    json.dumps(config or {}),
                    _utcnow_iso(),
                ),
            )

    def record_run(
        self,
        slack_user_id: str,
        ritual_name: str,
        status: str,
        output_preview: str = "",
        started_at: datetime | None = None,
    ) -> None:
        start_iso = (started_at or datetime.now(tz=timezone.utc)).isoformat()
        with self._conn() as conn:
            conn.execute(
                """INSERT INTO ritual_runs
                   (slack_user_id, ritual_name, started_at, finished_at,
                    status, output_preview)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    slack_user_id,
                    ritual_name,
                    start_iso,
                    _utcnow_iso(),
                    status,
                    (output_preview or "")[:500],
                ),
            )

    def recent_runs(
        self, slack_user_id: str, limit: int = 10
    ) -> list[dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute(
                """SELECT ritual_name, started_at, finished_at,
                          status, output_preview
                   FROM ritual_runs
                   WHERE slack_user_id = ?
                   ORDER BY started_at DESC
                   LIMIT ?""",
                (slack_user_id, limit),
            ).fetchall()
        return [dict(r) for r in rows]
