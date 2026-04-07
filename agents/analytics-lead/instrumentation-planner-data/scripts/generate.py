#!/usr/bin/env python3
"""
generate.py — Generate an instrumentation implementation plan including SDK selection, routing, and rollout phases.

Usage:
    echo '<json>' | python3 generate.py
    python3 generate.py < input.json
    python3 generate.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

SDK_OPTIONS = {
    "segment": {"strengths": "Unified customer data platform; 300+ integrations", "best_for": "Multi-destination event routing"},
    "amplitude": {"strengths": "Best-in-class product analytics; cohorts and retention", "best_for": "Product analytics focus"},
    "mixpanel": {"strengths": "Funnel and retention analysis; strong mobile SDK", "best_for": "Mobile-heavy products"},
    "custom": {"strengths": "Full control; no vendor lock-in", "best_for": "High compliance/privacy requirements"},
    "posthog": {"strengths": "Open-source; session replay; feature flags", "best_for": "Privacy-conscious or self-hosted setups"},
}

PLATFORMS = ["web", "ios", "android", "server", "backend_api"]

ROLLOUT_PHASES = [
    {"phase": 1, "name": "Foundation", "description": "SDK installation, identity, and session setup"},
    {"phase": 2, "name": "Core Events", "description": "High-priority events for primary user journeys"},
    {"phase": 3, "name": "Feature Events", "description": "Feature-specific event instrumentation"},
    {"phase": 4, "name": "QA and Validation", "description": "Verify data quality in staging and production"},
]

REQUIRED_FIELDS = ["plan_name", "sdk_choice", "platforms", "event_count"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "sdk_choice" in data and data["sdk_choice"] not in SDK_OPTIONS:
        errors.append(f"sdk_choice must be one of {list(SDK_OPTIONS.keys())}")
    for platform in data.get("platforms", []):
        if platform not in PLATFORMS:
            errors.append(f"platform must be one of {PLATFORMS}")
    return errors


def generate_plan(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    sdk = data["sdk_choice"]
    sdk_info = SDK_OPTIONS[sdk]
    event_count = data["event_count"]
    platforms = data["platforms"]

    # Estimate days per phase based on event count and platform count
    platform_multiplier = len(platforms) * 0.5 + 0.5
    phase_estimates = [
        {"phase": 1, "name": "Foundation", "days": round(2 * platform_multiplier)},
        {"phase": 2, "name": "Core Events", "days": round((event_count * 0.4) / 3 * platform_multiplier)},
        {"phase": 3, "name": "Feature Events", "days": round((event_count * 0.6) / 3 * platform_multiplier)},
        {"phase": 4, "name": "QA and Validation", "days": round(3 * platform_multiplier)},
    ]
    total_days = sum(p["days"] for p in phase_estimates)

    return {
        "error": None,
        "result": {
            "plan_name": data["plan_name"],
            "sdk_choice": sdk,
            "sdk_rationale": sdk_info["best_for"],
            "sdk_strengths": sdk_info["strengths"],
            "platforms": platforms,
            "event_count": event_count,
            "routing_architecture": {
                "client_to_sdk": f"{sdk} SDK on {', '.join(platforms)}",
                "sdk_to_warehouse": "Event stream → S3/GCS → BigQuery/Snowflake via SDK connector",
                "identity_resolution": "Anonymous ID → User ID on login/signup; server-side identity calls",
            },
            "rollout_phases": phase_estimates,
            "total_estimated_days": total_days,
            "sequencing_notes": [
                "Always instrument server-side events before client-side for critical business events (payments, signups)",
                "Deploy to staging first; run QA validation against spec before production rollout",
                "Backfill historical events is not possible — start instrumentation before the feature launches",
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_plan(data)
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
