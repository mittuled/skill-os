#!/usr/bin/env python3
"""
run.py — Track partner activation execution status and identify blockers.

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

ACTIVATION_STEPS = [
    {"step": 1, "name": "partner_onboarding", "description": "Welcome partner, share enablement materials, set up portal access"},
    {"step": 2, "name": "enablement_delivery", "description": "Deliver product training and sales enablement to partner team"},
    {"step": 3, "name": "joint_account_mapping", "description": "Identify overlapping customers and high-value co-sell opportunities"},
    {"step": 4, "name": "first_joint_call", "description": "Run first joint customer or prospect call with partner AE"},
    {"step": 5, "name": "deal_registration", "description": "First co-sell deal registered in both CRMs"},
    {"step": 6, "name": "first_close", "description": "First joint deal closed-won"},
    {"step": 7, "name": "steady_state", "description": "Regular pipeline reviews and QBR cadence established"},
]

REQUIRED_FIELDS = ["partner_name", "current_step", "pipeline_usd", "revenue_target_usd"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    return errors


def run_activation(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    current_step = data["current_step"]
    pipeline = data["pipeline_usd"]
    target = data["revenue_target_usd"]
    pipeline_coverage = pipeline / max(target * 3, 1)

    current = next((s for s in ACTIVATION_STEPS if s["step"] == current_step), None)
    next_step = next((s for s in ACTIVATION_STEPS if s["step"] == current_step + 1), None)
    completed = [s for s in ACTIVATION_STEPS if s["step"] < current_step]

    health = "on_track" if pipeline_coverage >= 0.5 else ("needs_attention" if pipeline_coverage >= 0.2 else "at_risk")

    blockers = data.get("blockers", [])
    recommendations = []
    if health == "at_risk":
        recommendations.append("Pipeline below 20% of 3× coverage target — schedule joint account mapping session immediately")
    if not data.get("qbr_scheduled"):
        recommendations.append("Schedule next QBR with partner before end of month")
    if current_step < 3 and data.get("weeks_since_start", 0) > 3:
        recommendations.append("Activation is behind schedule — escalate to partner champion")

    return {
        "error": None,
        "result": {
            "partner_name": data["partner_name"],
            "current_step": current_step,
            "current_step_name": current["name"] if current else "complete",
            "next_step": next_step["name"] if next_step else "Maintain steady state",
            "completed_steps": [s["name"] for s in completed],
            "pipeline_usd": pipeline,
            "revenue_target_usd": target,
            "pipeline_coverage_ratio": round(pipeline_coverage, 2),
            "activation_health": health,
            "blockers": blockers,
            "recommendations": recommendations,
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_activation(data)
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
