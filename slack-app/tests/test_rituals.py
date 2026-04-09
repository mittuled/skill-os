"""Smoke tests for ritual registry, contracts, and no-op code paths.

These tests avoid any real Slack or Claude calls. They verify:
- Registry contents match expectations
- Every ritual declares the required class attributes
- Each ritual's default cron is parseable as 5-field crontab
- Morning digest's no-channels path returns cleanly
- Decision log's no-config path fails cleanly with the expected error
- Storage round-trips preferences and run history
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest

# Make the parent slack-app directory importable when running `pytest` from
# either the repo root or the slack-app directory.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from apscheduler.triggers.cron import CronTrigger  # noqa: E402

from rituals import REGISTRY, all_rituals, get  # noqa: E402
from rituals.base import Ritual, RitualContext, RitualResult  # noqa: E402
from storage import Storage  # noqa: E402


def test_registry_has_all_four_rituals():
    assert set(REGISTRY.keys()) == {
        "morning_digest",
        "followup_sweep",
        "thread_triage",
        "decision_log",
    }


@pytest.mark.parametrize("ritual", all_rituals(), ids=lambda r: r.name)
def test_ritual_has_required_attributes(ritual: Ritual):
    assert ritual.name
    assert ritual.title
    assert ritual.description
    assert ritual.default_cron
    # Parseable as 5-field crontab (raises if not)
    CronTrigger.from_crontab(ritual.default_cron)


def test_get_unknown_returns_none():
    assert get("does_not_exist") is None


def test_morning_digest_no_channels_exits_cleanly():
    ritual = get("morning_digest")
    assert ritual is not None
    mock_client = MagicMock()
    mock_client.users_conversations.return_value = {"channels": []}

    ctx = RitualContext(
        slack_user_id="U123",
        slack_client=mock_client,
        config={},
    )
    result = ritual.run(ctx)
    assert isinstance(result, RitualResult)
    assert result.success is True
    assert "No channels" in result.summary
    # No DM should have been opened or posted
    mock_client.conversations_open.assert_not_called()
    mock_client.chat_postMessage.assert_not_called()


def test_decision_log_without_config_fails_cleanly():
    ritual = get("decision_log")
    assert ritual is not None
    ctx = RitualContext(
        slack_user_id="U123",
        slack_client=MagicMock(),
        config={},  # no watch_channel_id
    )
    result = ritual.run(ctx)
    assert result.success is False
    assert "watch_channel_id" in (result.error or "")


def test_storage_roundtrip_preferences_and_runs():
    with tempfile.TemporaryDirectory() as td:
        db_path = Path(td) / "test.db"
        storage = Storage(path=db_path)

        # No preference initially
        assert storage.get_preference("U1", "morning_digest") is None
        assert storage.list_enabled("morning_digest") == []

        # Set and read back
        storage.set_preference(
            slack_user_id="U1",
            ritual_name="morning_digest",
            enabled=True,
            schedule_cron="0 9 * * *",
            config={"lookback_hours": 8},
        )
        pref = storage.get_preference("U1", "morning_digest")
        assert pref is not None
        assert pref["enabled"] is True
        assert pref["config"] == {"lookback_hours": 8}

        # Listed as enabled
        enabled = storage.list_enabled("morning_digest")
        assert len(enabled) == 1
        assert enabled[0]["slack_user_id"] == "U1"

        # Record a run and read back
        storage.record_run(
            slack_user_id="U1",
            ritual_name="morning_digest",
            status="ok",
            output_preview="Digest delivered (3 channels, 16h)",
        )
        runs = storage.recent_runs("U1")
        assert len(runs) == 1
        assert runs[0]["status"] == "ok"
        assert runs[0]["ritual_name"] == "morning_digest"

        # Disable and verify it's no longer listed
        storage.set_preference(
            slack_user_id="U1",
            ritual_name="morning_digest",
            enabled=False,
        )
        assert storage.list_enabled("morning_digest") == []
