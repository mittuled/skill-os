"""Decision log ritual.

Target pain point: decisions made inside Slack threads get lost. Research
quoted users saying "I know the decision was made in Slack, I just can't
find it." This ritual scans a user-specified channel over a lookback window
and extracts decisions into a concise weekly summary.

MVP note: output goes to the user's DM. A follow-up will add canvas output
via `canvases.create` / `canvases.edit` so the decision log becomes a
persistent, linkable document the whole team can reference.
"""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

from slack_sdk.errors import SlackApiError

from llm import summarize
from rituals.base import Ritual, RitualContext, RitualResult

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are extracting decisions from a week of Slack channel
activity. A decision is any choice the team committed to that someone might
need to reference later.

For each decision, output one markdown bullet:
- **<short name>** — what was decided · decided by <user> · one-sentence context

Ignore chitchat, status updates, and reactions. If no decisions were made,
output exactly: "No decisions recorded this week." """

DEFAULT_LOOKBACK_DAYS = 7
DEFAULT_MAX_MESSAGES = 200


class DecisionLog(Ritual):
    name = "decision_log"
    title = "Decision log"
    description = (
        "Extracts decisions from a watched channel each week. "
        "Configure `watch_channel_id` in the ritual config."
    )
    default_cron = "0 16 * * 5"  # Fridays 16:00 UTC

    def run(self, ctx: RitualContext) -> RitualResult:
        watch_channel_id = ctx.config.get("watch_channel_id")
        if not watch_channel_id:
            return RitualResult(
                success=False,
                summary="No watched channel configured",
                error="Set `watch_channel_id` in the ritual config",
            )

        lookback_days = int(ctx.config.get("lookback_days", DEFAULT_LOOKBACK_DAYS))
        max_messages = int(ctx.config.get("max_messages", DEFAULT_MAX_MESSAGES))
        oldest_ts = (
            datetime.now(tz=timezone.utc) - timedelta(days=lookback_days)
        ).timestamp()

        try:
            hist = ctx.slack_client.conversations_history(
                channel=watch_channel_id, oldest=str(oldest_ts), limit=max_messages
            )
        except SlackApiError as e:
            return RitualResult(
                success=False, summary="History fetch failed", error=str(e)
            )

        messages = hist.get("messages", [])
        if not messages:
            return RitualResult(
                success=True, summary="No messages in window"
            )

        corpus_lines: list[str] = []
        for m in reversed(messages):
            text = (m.get("text") or "").strip()
            if not text:
                continue
            corpus_lines.append(
                f"[{m.get('user', '?')}@{m['ts']}] {text}"
            )
        corpus = "\n".join(corpus_lines)

        try:
            extracted = summarize(
                SYSTEM_PROMPT,
                f"Channel activity ({lookback_days}d):\n{corpus}",
                max_tokens=1500,
            )
        except Exception as e:
            logger.exception("LLM extraction failed")
            return RitualResult(
                success=False, summary="LLM call failed", error=str(e)
            )

        try:
            dm_channel = ctx.slack_client.conversations_open(
                users=ctx.slack_user_id
            )["channel"]["id"]
        except SlackApiError as e:
            return RitualResult(success=False, summary="Could not open DM", error=str(e))

        week_label = datetime.now(tz=timezone.utc).strftime("Week of %b %d")
        ctx.slack_client.chat_postMessage(
            channel=dm_channel,
            text="Decision log",
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": f"Decision log — {week_label}",
                    },
                },
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": extracted},
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": (
                                f"Source: <#{watch_channel_id}> · "
                                f"lookback {lookback_days}d · "
                                f"{len(messages)} messages scanned"
                            ),
                        }
                    ],
                },
            ],
        )
        return RitualResult(
            success=True,
            summary=f"Decision log generated ({lookback_days}d)",
            delivered_to=dm_channel,
        )
