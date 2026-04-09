"""Thin Claude API wrapper used by rituals for summarization and extraction.

We default to Sonnet 4.6 for the right speed/quality trade-off for per-user
scheduled jobs. Override with SKILLOS_CLAUDE_MODEL for experiments.
"""
from __future__ import annotations

import os

from anthropic import Anthropic

DEFAULT_MODEL = os.environ.get("SKILLOS_CLAUDE_MODEL", "claude-sonnet-4-6")

_client: Anthropic | None = None


def client() -> Anthropic:
    global _client
    if _client is None:
        _client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    return _client


def summarize(system: str, user: str, max_tokens: int = 1024) -> str:
    """Run a single-turn completion against Claude and return the text.

    The rituals pass a system prompt describing the output format and a user
    prompt containing the raw Slack corpus. This wrapper is intentionally
    minimal — rituals own their own prompts.
    """
    resp = client().messages.create(
        model=DEFAULT_MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(
        block.text for block in resp.content if getattr(block, "type", None) == "text"
    ).strip()
