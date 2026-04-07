#!/usr/bin/env python3
"""
run.py — Validate sales GTM activation readiness and produce pipeline waterfall targets.

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

# Pipeline coverage multiplier (pipeline needed per $1 of revenue target)
DEFAULT_COVERAGE_RATIO = 3.5

# Required enablement materials before launch
REQUIRED_ENABLEMENT = [
    "talk_tracks",
    "battle_cards",
    "demo_environment",
    "pricing_one_pager",
    "objection_handler",
]

# Required components for activation package
REQUIRED_ACTIVATION_COMPONENTS = [
    "pipeline_targets_set",
    "outreach_sequences_built",
    "territory_assignments_done",
    "enablement_complete",
    "launch_date_confirmed",
]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["segment_name", "revenue_target", "launch_date"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "revenue_target" in data and data["revenue_target"] <= 0:
        errors.append("revenue_target must be positive")
    return errors


def compute_pipeline_targets(revenue_target: float, coverage_ratio: float, avg_deal_size: float, weeks: int) -> dict:
    required_pipeline = revenue_target * coverage_ratio
    deals_needed = round(required_pipeline / avg_deal_size) if avg_deal_size > 0 else 0
    weekly_target = round(deals_needed / weeks) if weeks > 0 else 0
    return {
        "revenue_target": revenue_target,
        "coverage_ratio": coverage_ratio,
        "required_pipeline": round(required_pipeline),
        "avg_deal_size": avg_deal_size,
        "deals_needed": deals_needed,
        "activation_weeks": weeks,
        "weekly_pipeline_deals": weekly_target,
    }


def run_activation_check(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    coverage_ratio = data.get("pipeline_coverage_ratio", DEFAULT_COVERAGE_RATIO)
    avg_deal = data.get("avg_deal_size", 25000)
    weeks = data.get("activation_weeks", 8)

    pipeline_model = compute_pipeline_targets(
        data["revenue_target"], coverage_ratio, avg_deal, weeks
    )

    # Assess enablement readiness
    enablement_provided = set(data.get("enablement_ready", []))
    enablement_missing = [e for e in REQUIRED_ENABLEMENT if e not in enablement_provided]

    # Assess activation components
    activation_status = data.get("activation_components", {})
    components_missing = [c for c in REQUIRED_ACTIVATION_COMPONENTS if not activation_status.get(c, False)]

    if components_missing or enablement_missing:
        verdict = "NOT_READY"
        recommendation = f"Activation blocked — {len(components_missing)} activation components and {len(enablement_missing)} enablement items missing"
    else:
        verdict = "READY"
        recommendation = "Sales activation ready — all components and enablement materials in place"

    result = {
        "segment": data["segment_name"],
        "launch_date": data["launch_date"],
        "verdict": verdict,
        "recommendation": recommendation,
        "pipeline_waterfall": pipeline_model,
        "enablement_status": {
            "ready": list(enablement_provided),
            "missing": enablement_missing,
        },
        "activation_components": {
            "complete": [c for c in REQUIRED_ACTIVATION_COMPONENTS if activation_status.get(c, False)],
            "missing": components_missing,
        },
        "personas": data.get("target_personas", []),
        "rep_count": data.get("rep_count", 0),
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
