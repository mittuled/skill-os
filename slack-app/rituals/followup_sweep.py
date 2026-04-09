"""Followup sweep ritual.

Target pain point: lost follow-ups and "I meant to reply but didn't." Research
found this is the #2 complaint after overload. Runs per-user in the late
afternoon, scans channels the user is in for @mentions directed at them that
the user has not replied to, and posts an actionable list to the user's DM.
"""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

from slack_sdk.errors import SlackApiError

from llm import summarize
from rituals.base import Ritual, RitualContext, RitualResult

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are scanning Slack messages that mention a specific
user. For each item, decide whether it requires a reply from the user.

Output a markdown list. For each actionable item:
- One-line description of what is being asked
- Who is asking
- A suggested short reply, or a `[needs decision]` tag if judgment required

Ignore FYI broadcasts, celebrations, and automated alerts. Be ruthless about
what requires a reply. Max 10 items. If none, output exactly:
"Inbox zero — no pending replies." """

DEFAULT_LOOKBACK_HOURS = 12
DEFAULT_MAX_CHANNELS = 20


class FollowupSweep(Ritual):
    name = "followup_sweep"
    title = "Followup sweep"
    description = (
        "Scans mentions and questions directed at you that you haven't "
        "replied to, with suggested responses."
    )
    default_cron = "0 17 * * 1-5"  # 17:00 UTC, Mon–Fri

    def run(self, ctx: RitualContext) -> RitualResult:
        lookback = int(ctx.config.get("lookback_hours", DEFAULT_LOOKBACK_HOURS))
        max_channels = int(ctx.config.get("max_channels", DEFAULT_MAX_CHANNELS))

        try:
            mentions = self._collect_mentions(ctx, lookback, max_channels)
        except SlackApiError as e:
            return RitualResult(
                success=False, summary="Mention scan failed", error=str(e)
            )

        try:
            dm_channel = ctx.slack_client.conversations_open(
                users=ctx.slack_user_id
            )["channel"]["id"]
        except SlackApiError as e:
            return RitualResult(success=False, summary="Could not open DM", error=str(e))

        if not mentions:
            ctx.slack_client.chat_postMessage(
                channel=dm_channel,
                text="Followup sweep: inbox zero — no open mentions today.",
            )
            return RitualResult(
                success=True,
                summary="No pending mentions",
                delivered_to=dm_channel,
            )

        corpus = "\n\n".join(
            f"[#{m['channel_name']}] [{m['author']}]: {m['text']}" for m in mentions
        )
        user_prompt = (
            f"User id: {ctx.slack_user_id}\n"
            f"Lookback: {lookback}h\n\n"
            f"Mentions:\n{corpus}"
        )
        try:
            summary_text = summarize(SYSTEM_PROMPT, user_prompt, max_tokens=1024)
        except Exception as e:
            logger.exception("LLM summarization failed")
            return RitualResult(
                success=False, summary="LLM call failed", error=str(e)
            )

        ctx.slack_client.chat_postMessage(
            channel=dm_channel,
            text="Followup sweep",
            blocks=[
                {
                    "type": "header",
                    "text": {"type": "plain_text", "text": "Followup sweep"},
                },
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": summary_text},
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": f"{len(mentions)} mentions scanned · lookback {lookback}h",
                        }
                    ],
                },
            ],
        )
        return RitualResult(
            success=True,
            summary=f"Sweep delivered ({len(mentions)} mentions)",
            delivered_to=dm_channel,
        )

    def _collect_mentions(
        self, ctx: RitualContext, lookback_hours: int, max_channels: int
    ) -> list[dict]:
        oldest = (
            datetime.now(tz=timezone.utc) - timedelta(hours=lookback_hours)
        ).timestamp()
        mention_token = f"<@{ctx.slack_user_id}>"
        mentions: list[dict] = []

        channels = ctx.slack_client.users_conversations(
            user=ctx.slack_user_id,
            types="public_channel,private_channel",
            exclude_archived=True,
            limit=100,
        ).get("channels", [])

        for ch in channels[:max_channels]:
            try:
                hist = ctx.slack_client.conversations_history(
                    channel=ch["id"], oldest=str(oldest), limit=100
                )
            except SlackApiError as e:
                logger.warning(
                    "history fetch failed for #%s: %s", ch.get("name", "?"), e
                )
                continue
            for m in hist.get("messages", []):
                text = m.get("text") or ""
                if mention_token not in text:
                    continue
                if m.get("user") == ctx.slack_user_id:
                    continue
                if self._user_replied_after(
                    ctx, ch["id"], m, ctx.slack_user_id
                ):
                    continue
                mentions.append(
                    {
                        "channel_name": ch.get("name", ch["id"]),
                        "channel_id": ch["id"],
                        "ts": m["ts"],
                        "author": m.get("user", "unknown"),
                        "text": text,
                    }
                )
        return mentions

    def _user_replied_after(
        self,
        ctx: RitualContext,
        channel_id: str,
        parent: dict,
        user_id: str,
    ) -> bool:
        thread_ts = parent.get("thread_ts") or parent["ts"]
        try:
            replies = ctx.slack_client.conversations_replies(
                channel=channel_id, ts=thread_ts, limit=50
            ).get("messages", [])
        except SlackApiError:
            return False
        parent_ts_float = float(parent["ts"])
        for r in replies:
            if r.get("user") == user_id and float(r["ts"]) > parent_ts_float:
                return True
        return False
