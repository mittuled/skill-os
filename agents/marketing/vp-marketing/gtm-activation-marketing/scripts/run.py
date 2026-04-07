#!/usr/bin/env python3
"""
run.py — Run the GTM activation checklist validating all channel launch readiness criteria.

Usage:
    echo '<json>' | python3 run.py
    python3 run.py < input.json
    python3 run.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# Required asset types per channel
CHANNEL_REQUIRED_ASSETS = {
    "paid_search": ["landing_page", "ad_creatives", "utm_tracking", "conversion_pixel"],
    "content_seo": ["blog_posts", "landing_page", "utm_tracking"],
    "paid_social": ["ad_creatives", "landing_page", "utm_tracking", "pixel_firing"],
    "email": ["email_sequence", "unsubscribe_link", "utm_tracking"],
    "events": ["event_page", "registration_flow", "follow_up_sequence"],
    "pr": ["press_release", "media_list", "spokesperson_brief"],
    "webinars": ["webinar_registration_page", "reminder_sequence", "slide_deck"],
    "sales_enablement": ["sales_deck", "one_pager", "competitive_battlecard"],
}

# Minimum required checks to approve channel for launch
CRITICAL_CHECKS = ["landing_page", "utm_tracking", "ad_creatives", "conversion_pixel"]

# Launch phases
LAUNCH_PHASES = ["pre_launch", "launch_day", "post_launch_48h", "retrospective"]


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    required = ["campaign_name", "launch_date", "channels"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "channels" in data:
        for ch_entry in data["channels"]:
            for f in ["channel", "assets_ready"]:
                if f not in ch_entry:
                    errors.append(f"Channel entry missing field: {f}")
    return errors


def evaluate_channel(ch_entry: dict) -> dict:
    """Evaluate a single channel's readiness for activation."""
    channel = ch_entry["channel"]
    assets_ready = set(ch_entry.get("assets_ready", []))
    required = set(CHANNEL_REQUIRED_ASSETS.get(channel, []))
    missing = required - assets_ready
    critical_missing = [a for a in CRITICAL_CHECKS if a in missing]

    ready = len(missing) == 0
    blocking = len(critical_missing) > 0

    return {
        "channel": channel,
        "status": "ready" if ready else ("blocked" if blocking else "conditional"),
        "assets_required": sorted(required),
        "assets_ready": sorted(assets_ready),
        "assets_missing": sorted(missing),
        "critical_blockers": critical_missing,
        "owner": ch_entry.get("owner", "unassigned"),
    }


def run_activation_check(data: dict) -> dict:
    """Run the full GTM activation readiness check."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    channel_results = [evaluate_channel(ch) for ch in data["channels"]]

    ready_count = sum(1 for c in channel_results if c["status"] == "ready")
    blocked_count = sum(1 for c in channel_results if c["status"] == "blocked")
    conditional_count = sum(1 for c in channel_results if c["status"] == "conditional")
    total = len(channel_results)

    all_critical_blockers = [
        f"{c['channel']}: {', '.join(c['critical_blockers'])}"
        for c in channel_results if c["critical_blockers"]
    ]

    if blocked_count == 0 and conditional_count == 0:
        launch_decision = "GO — all channels are ready for activation"
        launch_status = "approved"
    elif blocked_count == 0:
        launch_decision = f"CONDITIONAL — {conditional_count} channel(s) have non-critical gaps; launch can proceed with risk acknowledgement"
        launch_status = "conditional"
    else:
        launch_decision = f"NO-GO — {blocked_count} channel(s) have critical blockers that must be resolved before launch"
        launch_status = "blocked"

    war_room_checklist = [
        "Monitor real-time dashboard from launch T-minus 1 hour",
        "Verify all UTM parameters are tracking in analytics within 30 minutes of go-live",
        "Confirm form fills are routing to CRM and triggering MQL scoring",
        "Check ad delivery metrics every 2 hours for the first 24 hours",
        "Escalate tracking failures to marketing ops within 30 minutes",
        "Log all issues and resolutions in the war room incident log",
    ]

    result = {
        "campaign": data["campaign_name"],
        "launch_date": data["launch_date"],
        "launch_decision": launch_decision,
        "launch_status": launch_status,
        "readiness_summary": {
            "total_channels": total,
            "ready": ready_count,
            "conditional": conditional_count,
            "blocked": blocked_count,
        },
        "channel_results": channel_results,
        "critical_blockers": all_critical_blockers,
        "war_room_checklist": war_room_checklist,
        "activation_sequence": data.get("activation_sequence", list(CHANNEL_REQUIRED_ASSETS.keys())),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_activation_check(data)
    output = json.dumps(result, indent=2)
    args = sys.argv[1:]
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(output + "\n", encoding="utf-8")
        else:
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
