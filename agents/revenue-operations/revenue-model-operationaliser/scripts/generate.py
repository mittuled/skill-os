#!/usr/bin/env python3
"""
generate.py — Generate a revenue model operationalisation spec mapping pricing to CRM stages.

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

# Supported revenue model types
REVENUE_MODEL_TYPES = {
    "subscription": "Recurring monthly/annual revenue; recognised ratably over contract term",
    "usage_based": "Revenue tied to consumption metrics; recognised as usage occurs",
    "one_time": "Point-of-sale recognition; full amount recognised at delivery",
    "milestone_based": "Revenue recognised at defined project milestones",
    "hybrid": "Combination of subscription base + usage-based overage",
}

# Recognition method descriptions
RECOGNITION_METHODS = {
    "ratable": "Spread evenly over contract period (e.g., $12K/year = $1K/month)",
    "point_of_sale": "Full amount recognised at transaction date",
    "as_earned": "Recognised as service is delivered (usage or milestone)",
    "percentage_of_completion": "Recognised proportionally to project completion",
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["model_type", "pricing_tiers", "pipeline_stage_mapping"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "model_type" in data and data["model_type"] not in REVENUE_MODEL_TYPES:
        errors.append(f"model_type must be one of: {list(REVENUE_MODEL_TYPES.keys())}")
    if "pipeline_stage_mapping" in data:
        for i, stage in enumerate(data["pipeline_stage_mapping"]):
            for f in ["stage_name", "entry_criteria", "exit_criteria", "probability_pct"]:
                if f not in stage:
                    errors.append(f"pipeline_stage_mapping[{i}] missing field: {f}")
    return errors


def generate_operationalisation(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    model_type = data["model_type"]
    stages = data["pipeline_stage_mapping"]
    tiers = data["pricing_tiers"]

    # Validate probability progression
    probs = [s["probability_pct"] for s in stages]
    non_monotonic = [
        stages[i]["stage_name"]
        for i in range(1, len(probs))
        if probs[i] < probs[i - 1]
    ]

    # Build stage specs
    stage_specs = []
    for s in stages:
        stage_specs.append({
            "stage_name": s["stage_name"],
            "entry_criteria": s["entry_criteria"],
            "exit_criteria": s["exit_criteria"],
            "probability_pct": s["probability_pct"],
            "forecast_category": s.get("forecast_category", "pipeline"),
            "required_fields": s.get("required_fields", []),
        })

    result = {
        "revenue_model_type": model_type,
        "model_description": REVENUE_MODEL_TYPES[model_type],
        "recognition_method": data.get("recognition_method", "ratable"),
        "recognition_description": RECOGNITION_METHODS.get(data.get("recognition_method", "ratable"), ""),
        "pricing_tiers": tiers,
        "pipeline_stages": stage_specs,
        "stage_count": len(stage_specs),
        "probability_progression_valid": len(non_monotonic) == 0,
        "non_monotonic_stages": non_monotonic,
        "finance_validation_required": True,
        "notes": data.get("notes", ""),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_operationalisation(data)
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
