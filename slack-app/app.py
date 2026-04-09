"""Skill OS Slack ritual automator — Bolt app entry point.

Run locally with Socket Mode:

    python app.py

Requires the following environment variables (see .env.example):
    SLACK_BOT_TOKEN, SLACK_APP_TOKEN, SLACK_SIGNING_SECRET, ANTHROPIC_API_KEY
"""
from __future__ import annotations

import logging
import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from rituals import REGISTRY, all_rituals
from scheduler import RitualScheduler
from storage import Storage

load_dotenv()

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("skillos-slack")

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
)
storage = Storage()
scheduler = RitualScheduler(slack_client=app.client, storage=storage)


# ---------- App Home view -----------------------------------------------------


def _home_view(user_id: str) -> dict:
    blocks: list[dict] = [
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "Skill OS rituals"},
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": (
                        "Recurring assistants that attack the worst parts "
                        "of Slack so you can focus. All output is sent to "
                        "your DMs — never to shared channels."
                    ),
                }
            ],
        },
        {"type": "divider"},
    ]

    for ritual in all_rituals():
        pref = storage.get_preference(user_id, ritual.name)
        enabled = bool(pref and pref["enabled"])
        status_emoji = ":large_green_circle:" if enabled else ":white_circle:"
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"{status_emoji} *{ritual.title}*\n"
                        f"{ritual.description}\n"
                        f"_Schedule: `{ritual.default_cron}` UTC_"
                    ),
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Disable" if enabled else "Enable",
                    },
                    "value": ritual.name,
                    "action_id": f"toggle_{ritual.name}",
                    "style": "danger" if enabled else "primary",
                },
            }
        )
        blocks.append(
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Run now"},
                        "value": ritual.name,
                        "action_id": f"run_{ritual.name}",
                    }
                ],
            }
        )
        blocks.append({"type": "divider"})

    runs = storage.recent_runs(user_id, limit=5)
    if runs:
        blocks.append(
            {
                "type": "header",
                "text": {"type": "plain_text", "text": "Recent runs"},
            }
        )
        for r in runs:
            blocks.append(
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": (
                                f"`{r['started_at']}` · *{r['ritual_name']}* · "
                                f"{r['status']} — {r['output_preview'] or ''}"
                            ),
                        }
                    ],
                }
            )

    return {"type": "home", "blocks": blocks}


# ---------- Event handlers ----------------------------------------------------


@app.event("app_home_opened")
def on_home_opened(event, client):  # noqa: ANN001
    user_id = event["user"]
    client.views_publish(user_id=user_id, view=_home_view(user_id))


@app.command("/skillos")
def handle_command(ack, respond, command):  # noqa: ANN001
    ack()
    text = (command.get("text") or "").strip()
    parts = text.split()
    if not parts or parts[0] == "help":
        listing = "\n".join(f"• `{r.name}` — {r.title}" for r in all_rituals())
        respond(
            "*Skill OS rituals*\n"
            f"{listing}\n\n"
            "Usage: `/skillos run <name>` to trigger a ritual now."
        )
        return
    if parts[0] == "run" and len(parts) >= 2:
        name = parts[1]
        if name not in REGISTRY:
            respond(f":warning: Unknown ritual `{name}`. Try `/skillos help`.")
            return
        respond(f":hourglass_flowing_sand: Running `{name}`…")
        try:
            scheduler.trigger_for_user(name, command["user_id"])
            respond(f":white_check_mark: `{name}` completed. Check your DMs.")
        except Exception as e:  # noqa: BLE001
            logger.exception("Manual ritual run failed")
            respond(f":x: `{name}` failed: {e}")
        return
    respond("Unrecognized subcommand. Try `/skillos help`.")


# ---------- Dynamic action handlers ------------------------------------------
# Bolt decorators need to close over the ritual name; we bind via helper
# functions so each handler captures its own name in a fresh closure.


def _bind_toggle(name: str, default_cron: str) -> None:
    @app.action(f"toggle_{name}")
    def _handler(ack, body, client):  # noqa: ANN001
        ack()
        user_id = body["user"]["id"]
        current = storage.get_preference(user_id, name)
        enabled_now = not (current and current["enabled"])
        storage.set_preference(
            slack_user_id=user_id,
            ritual_name=name,
            enabled=enabled_now,
            schedule_cron=default_cron,
            config=(current or {}).get("config", {}),
        )
        client.views_publish(user_id=user_id, view=_home_view(user_id))


def _bind_runnow(name: str) -> None:
    @app.action(f"run_{name}")
    def _handler(ack, body, client):  # noqa: ANN001
        ack()
        user_id = body["user"]["id"]
        try:
            scheduler.trigger_for_user(name, user_id)
        except Exception:  # noqa: BLE001
            logger.exception("run_now failed for %s", name)
        client.views_publish(user_id=user_id, view=_home_view(user_id))


for _ritual in all_rituals():
    _bind_toggle(_ritual.name, _ritual.default_cron)
    _bind_runnow(_ritual.name)


@app.action("triage_close")
def on_triage_close(ack, respond):  # noqa: ANN001
    ack()
    # TODO(post-MVP): persist "closed" state so the thread is suppressed
    # in future thread_triage runs.
    respond(":white_check_mark: Marked closed.")


@app.action("triage_defer")
def on_triage_defer(ack, respond):  # noqa: ANN001
    ack()
    # TODO(post-MVP): persist "defer until" timestamp.
    respond(":clock3: Deferred until tomorrow.")


# ---------- Entry point -------------------------------------------------------


def main() -> None:
    scheduler.start()
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    try:
        handler.start()
    finally:
        scheduler.shutdown()


if __name__ == "__main__":
    main()
