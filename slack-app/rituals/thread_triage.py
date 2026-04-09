"""Thread triage ritual.

Target pain point: hidden thread unreads and "phantom badges". Research found
users report notification badges that won't clear because an unread lives in
a thread they didn't realize they were following. This ritual finds threads
the user is participating in that have gone stale (no reply in N days) and
presents them with close/defer buttons so the user can clear the mental load
in one pass.
"""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

from slack_sdk.errors import SlackApiError

from rituals.base import Ritual, RitualContext, RitualResult

logger = logging.getLogger(__name__)

DEFAULT_STALE_DAYS = 3
DEFAULT_MAX_THREADS = 15
DEFAULT_MAX_CHANNELS = 20


class ThreadTriage(Ritual):
    name = "thread_triage"
    title = "Thread triage"
    description = (
        "Lists threads you're in that have gone stale so you can close, "
        "defer, or reply in one place."
    )
    default_cron = "0 11 * * 1-5"  # 11:00 UTC, Mon–Fri

    def run(self, ctx: RitualContext) -> RitualResult:
        stale_days = int(ctx.config.get("stale_days", DEFAULT_STALE_DAYS))
        max_threads = int(ctx.config.get("max_threads", DEFAULT_MAX_THREADS))
        max_channels = int(ctx.config.get("max_channels", DEFAULT_MAX_CHANNELS))

        cutoff = datetime.now(tz=timezone.utc) - timedelta(days=stale_days)
        try:
            stale = self._find_stale_threads(ctx, cutoff, max_threads, max_channels)
        except SlackApiError as e:
            return RitualResult(
                success=False, summary="Triage scan failed", error=str(e)
            )

        try:
            dm_channel = ctx.slack_client.conversations_open(
                users=ctx.slack_user_id
            )["channel"]["id"]
        except SlackApiError as e:
            return RitualResult(success=False, summary="Could not open DM", error=str(e))

        if not stale:
            ctx.slack_client.chat_postMessage(
                channel=dm_channel,
                text="Thread triage: no stale threads. Nice.",
            )
            return RitualResult(
                success=True, summary="No stale threads", delivered_to=dm_channel
            )

        blocks: list[dict] = [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": "Thread triage"},
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"{len(stale)} threads stale for {stale_days}+ days",
                    }
                ],
            },
            {"type": "divider"},
        ]
        for t in stale:
            link = f"<{t['permalink']}|Open thread>" if t["permalink"] else "_no link_"
            blocks.append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*#{t['channel_name']}*\n{t['preview']}\n{link}",
                    },
                }
            )
            blocks.append(
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Close"},
                            "action_id": "triage_close",
                            "value": f"{t['channel_id']}:{t['thread_ts']}",
                            "style": "primary",
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Defer"},
                            "action_id": "triage_defer",
                            "value": f"{t['channel_id']}:{t['thread_ts']}",
                        },
                    ],
                }
            )

        ctx.slack_client.chat_postMessage(
            channel=dm_channel, text="Thread triage", blocks=blocks
        )
        return RitualResult(
            success=True,
            summary=f"Triage delivered ({len(stale)} stale)",
            delivered_to=dm_channel,
        )

    def _find_stale_threads(
        self,
        ctx: RitualContext,
        cutoff: datetime,
        max_threads: int,
        max_channels: int,
    ) -> list[dict]:
        results: list[dict] = []
        channels = ctx.slack_client.users_conversations(
            user=ctx.slack_user_id,
            types="public_channel,private_channel",
            exclude_archived=True,
            limit=100,
        ).get("channels", [])
        cutoff_ts = cutoff.timestamp()

        for ch in channels[:max_channels]:
            if len(results) >= max_threads:
                break
            try:
                hist = ctx.slack_client.conversations_history(
                    channel=ch["id"], limit=50
                )
            except SlackApiError:
                continue
            for m in hist.get("messages", []):
                if len(results) >= max_threads:
                    break
                # Only consider messages that started a thread (reply_count > 0)
                if not m.get("reply_count"):
                    continue
                thread_ts = m.get("thread_ts") or m["ts"]
                if not self._user_in_thread(ctx, ch["id"], thread_ts):
                    continue
                last_reply_ts = float(m.get("latest_reply", m["ts"]))
                if last_reply_ts >= cutoff_ts:
                    continue  # still active, not stale
                try:
                    perma = ctx.slack_client.chat_getPermalink(
                        channel=ch["id"], message_ts=thread_ts
                    )["permalink"]
                except SlackApiError:
                    perma = ""
                results.append(
                    {
                        "channel_id": ch["id"],
                        "channel_name": ch.get("name", ch["id"]),
                        "thread_ts": thread_ts,
                        "permalink": perma,
                        "preview": (m.get("text") or "")[:140],
                    }
                )
        return results

    def _user_in_thread(
        self, ctx: RitualContext, channel_id: str, thread_ts: str
    ) -> bool:
        try:
            replies = ctx.slack_client.conversations_replies(
                channel=channel_id, ts=thread_ts, limit=100
            ).get("messages", [])
        except SlackApiError:
            return False
        return any(r.get("user") == ctx.slack_user_id for r in replies)
