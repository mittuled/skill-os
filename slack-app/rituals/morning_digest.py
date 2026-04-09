"""Morning digest ritual.

Target pain point: morning catch-up overwhelm. Research found this is the
#1 complaint — users open Slack to hundreds of overnight messages with no
prioritization. This ritual runs per-user at the user's local 09:00, scans
their subscribed channels, and posts a terse summary to the user's DM with
the bot — never to a shared channel.
"""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

from slack_sdk.errors import SlackApiError

from llm import summarize
from rituals.base import Ritual, RitualContext, RitualResult

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a focused work assistant. Summarize overnight Slack
activity for a single user. Be terse. Use these sections, omit any that are
empty:

- Direct asks for you
- Decisions made
- Blockers raised
- FYI only

One bullet per item. No preamble. Max 10 bullets total."""

DEFAULT_LOOKBACK_HOURS = 16
DEFAULT_MAX_CHANNELS = 10
DEFAULT_MAX_MESSAGES_PER_CHANNEL = 30


class MorningDigest(Ritual):
    name = "morning_digest"
    title = "Morning digest"
    description = (
        "A personal summary of overnight activity in your channels, "
        "delivered to your DMs every morning."
    )
    default_cron = "0 9 * * *"  # 09:00 UTC; per-user override is future work

    def run(self, ctx: RitualContext) -> RitualResult:
        lookback = int(ctx.config.get("lookback_hours", DEFAULT_LOOKBACK_HOURS))
        max_channels = int(ctx.config.get("max_channels", DEFAULT_MAX_CHANNELS))
        max_msgs = int(
            ctx.config.get("max_messages_per_channel", DEFAULT_MAX_MESSAGES_PER_CHANNEL)
        )

        oldest_ts = (
            datetime.now(tz=timezone.utc) - timedelta(hours=lookback)
        ).timestamp()

        try:
            channels = self._list_user_channels(ctx)[:max_channels]
        except SlackApiError as e:
            return RitualResult(
                success=False, summary="Failed to list channels", error=str(e)
            )

        if not channels:
            return RitualResult(success=True, summary="No channels to summarize")

        try:
            user_info = ctx.slack_client.users_info(user=ctx.slack_user_id)
            user_name = user_info["user"].get("real_name", ctx.slack_user_id)
        except SlackApiError:
            user_name = ctx.slack_user_id

        corpus_parts: list[str] = []
        scanned = 0
        for ch in channels:
            try:
                hist = ctx.slack_client.conversations_history(
                    channel=ch["id"], oldest=str(oldest_ts), limit=max_msgs
                )
            except SlackApiError as e:
                logger.warning(
                    "history fetch failed for #%s: %s", ch.get("name", "?"), e
                )
                continue
            messages = hist.get("messages", [])
            if not messages:
                continue
            scanned += 1
            corpus_parts.append(f"# #{ch.get('name', ch['id'])}")
            for m in reversed(messages):  # chronological
                author = m.get("user", "unknown")
                text = (m.get("text") or "").strip()
                if text:
                    corpus_parts.append(f"[{author}] {text}")
            corpus_parts.append("")

        if not corpus_parts:
            summary_text = "No new activity overnight. Enjoy the quiet."
        else:
            corpus = "\n".join(corpus_parts)
            user_prompt = (
                f"User: {user_name} (slack id: {ctx.slack_user_id})\n"
                f"Lookback: {lookback}h\n\n"
                f"Activity log:\n{corpus}"
            )
            try:
                summary_text = summarize(SYSTEM_PROMPT, user_prompt, max_tokens=1024)
            except Exception as e:
                logger.exception("LLM summarization failed")
                return RitualResult(
                    success=False, summary="LLM call failed", error=str(e)
                )

        try:
            dm = ctx.slack_client.conversations_open(users=ctx.slack_user_id)
            dm_channel = dm["channel"]["id"]
            ctx.slack_client.chat_postMessage(
                channel=dm_channel,
                text="Morning digest",
                blocks=[
                    {
                        "type": "header",
                        "text": {"type": "plain_text", "text": "Morning digest"},
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
                                "text": (
                                    f"Lookback: {lookback}h · "
                                    f"{scanned}/{len(channels)} channels with activity"
                                ),
                            }
                        ],
                    },
                ],
            )
        except SlackApiError as e:
            return RitualResult(
                success=False, summary="DM delivery failed", error=str(e)
            )

        return RitualResult(
            success=True,
            summary=f"Digest delivered ({scanned} channels, {lookback}h)",
            delivered_to=dm_channel,
        )

    def _list_user_channels(self, ctx: RitualContext) -> list[dict]:
        resp = ctx.slack_client.users_conversations(
            user=ctx.slack_user_id,
            types="public_channel,private_channel",
            exclude_archived=True,
            limit=100,
        )
        return resp.get("channels", [])
