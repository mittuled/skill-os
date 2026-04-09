"""Base contract for Slack ritual automators.

A Ritual is a recurring, per-user job that reads from Slack, optionally calls
an LLM, and writes output back (usually to the user's DM with the bot). Every
ritual subclass declares its name, schedule, and description as class
attributes and implements `run(ctx)`.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from slack_sdk import WebClient


@dataclass
class RitualContext:
    """Everything a ritual needs to execute for a single user."""

    slack_user_id: str
    slack_client: WebClient
    config: dict[str, Any] = field(default_factory=dict)


@dataclass
class RitualResult:
    """Outcome of a single ritual run, recorded in the audit log."""

    success: bool
    summary: str  # short human-readable line for App Home + run log
    delivered_to: str | None = None  # channel / DM id where output was posted
    error: str | None = None


class Ritual(ABC):
    """A recurring Slack ritual that runs per-user on a schedule or on demand."""

    name: str = ""  # unique slug, e.g. "morning_digest"
    title: str = ""  # human-readable title shown in App Home
    description: str = ""  # one-line description for App Home
    default_cron: str = ""  # default 5-field cron schedule (UTC)

    @abstractmethod
    def run(self, ctx: RitualContext) -> RitualResult:
        """Execute the ritual for a single user. Must not raise for expected
        failures — use RitualResult(success=False, error=...) instead."""
