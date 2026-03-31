#!/usr/bin/env python3
"""
run.py — Plan and execute peer review platform management across G2, Capterra, and similar sites.

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

PLATFORMS = ["g2", "capterra", "trustradius", "trustpilot", "getapp", "software_advice"]
CAMPAIGN_TYPES = ["initial_review_drive", "quarterly_refresh", "competitive_response", "award_nomination"]

REVIEW_REQUEST_CHANNELS = {
    "email": {"conversion_rate_pct": 12, "notes": "Post-QBR or post-NPS win best timing"},
    "in_app": {"conversion_rate_pct": 8, "notes": "Show prompt after user achieves first value milestone"},
    "cs_outreach": {"conversion_rate_pct": 25, "notes": "CSM-led personal ask; highest conversion but doesn't scale"},
    "sales_close": {"conversion_rate_pct": 15, "notes": "Request review in close call as part of customer success handoff"},
}

REQUIRED_FIELDS = ["platforms", "campaign_type", "target_review_count", "current_review_counts"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    for platform in data.get("platforms", []):
        if platform not in PLATFORMS:
            errors.append(f"Unknown platform: {platform}. Must be one of {PLATFORMS}")
    if "campaign_type" in data and data["campaign_type"] not in CAMPAIGN_TYPES:
        errors.append(f"campaign_type must be one of {CAMPAIGN_TYPES}")
    return errors


def plan_review_campaign(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    platforms = data["platforms"]
    target_count = data["target_review_count"]
    current_counts = data["current_review_counts"]

    platform_plans = []
    for platform in platforms:
        current = current_counts.get(platform, 0)
        gap = max(0, target_count - current)
        platform_plans.append({
            "platform": platform,
            "current_reviews": current,
            "target_reviews": target_count,
            "gap": gap,
            "estimated_outreach_needed": round(gap / (REVIEW_REQUEST_CHANNELS["email"]["conversion_rate_pct"] / 100)),
            "priority": "high" if gap > current else "medium",
        })

    # Best channel recommendation
    channel_plan = []
    for channel, config in REVIEW_REQUEST_CHANNELS.items():
        channel_plan.append({
            "channel": channel,
            "conversion_rate_pct": config["conversion_rate_pct"],
            "best_timing": config["notes"],
        })

    return {
        "error": None,
        "result": {
            "campaign_type": data["campaign_type"],
            "platform_plans": platform_plans,
            "recommended_channels": sorted(channel_plan, key=lambda x: -x["conversion_rate_pct"])[:3],
            "campaign_timeline_weeks": 8 if data["campaign_type"] == "initial_review_drive" else 4,
            "compliance_reminders": [
                "Never incentivise reviews with discounts or gifts — violates platform terms of service",
                "Do not pre-screen customers before asking for reviews (sending only to known promoters)",
                "Always allow customers to leave any star rating — do not guide to 5-star only",
            ],
            "g2_grid_criteria": {
                "satisfaction_score": "Based on review ratings — target overall score > 4.2",
                "market_presence": "Based on review count, employee count, and social reach",
                "grid_tier": "Enterprise Grid Leader requires >25 reviews and score >4.0 from enterprise-segment reviewers",
            } if "g2" in platforms else {},
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = plan_review_campaign(data)
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
