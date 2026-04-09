"""Registry of all available rituals.

Rituals are registered here at import time. Adding a new ritual is a matter
of dropping a new file in this package, implementing the Ritual ABC, and
adding a line to REGISTRY below.
"""
from __future__ import annotations

from rituals.base import Ritual, RitualContext, RitualResult
from rituals.decision_log import DecisionLog
from rituals.followup_sweep import FollowupSweep
from rituals.morning_digest import MorningDigest
from rituals.thread_triage import ThreadTriage

REGISTRY: dict[str, Ritual] = {
    r.name: r
    for r in (
        MorningDigest(),
        FollowupSweep(),
        ThreadTriage(),
        DecisionLog(),
    )
}


def get(name: str) -> Ritual | None:
    return REGISTRY.get(name)


def all_rituals() -> list[Ritual]:
    return list(REGISTRY.values())


__all__ = [
    "REGISTRY",
    "Ritual",
    "RitualContext",
    "RitualResult",
    "all_rituals",
    "get",
]
