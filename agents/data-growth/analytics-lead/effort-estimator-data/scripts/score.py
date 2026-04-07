#!/usr/bin/env python3
"""
score.py — Estimate analytics and data engineering effort for a product initiative.

Usage:
    echo '<json>' | python3 score.py
    python3 score.py < input.json
    python3 score.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# T-shirt size estimates in engineering days
EFFORT_ESTIMATES = {
    "instrumentation": {
        "xs": {"days": 1, "description": "1-3 new events, no new properties"},
        "s":  {"days": 3, "description": "4-10 events, standard properties"},
        "m":  {"days": 7, "description": "11-25 events, custom properties, cross-platform"},
        "l":  {"days": 14, "description": "26-50 events, new schema design required"},
        "xl": {"days": 25, "description": "50+ events, major instrumentation refactor"},
    },
    "pipeline": {
        "xs": {"days": 1, "description": "New view on existing table"},
        "s":  {"days": 3, "description": "New dbt model, existing source"},
        "m":  {"days": 7, "description": "New data source ingestion + model"},
        "l":  {"days": 14, "description": "New pipeline with backfill + testing"},
        "xl": {"days": 25, "description": "New data domain with full pipeline"},
    },
    "dashboard": {
        "xs": {"days": 1, "description": "Add metric to existing dashboard"},
        "s":  {"days": 2, "description": "New dashboard, existing metrics"},
        "m":  {"days": 5, "description": "New dashboard with new metrics"},
        "l":  {"days": 10, "description": "Executive dashboard with drill-downs"},
        "xl": {"days": 20, "description": "Self-serve analytics portal"},
    },
}

COMPLEXITY_MULTIPLIERS = {
    "low": 1.0,
    "medium": 1.3,
    "high": 1.7,
    "very_high": 2.2,
}

REQUIRED_FIELDS = ["initiative_name", "components"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "components" in data:
        for comp in data["components"]:
            if "type" not in comp or "size" not in comp:
                errors.append("Each component needs 'type' and 'size' fields")
            if "type" in comp and comp["type"] not in EFFORT_ESTIMATES:
                errors.append(f"Component type must be one of {list(EFFORT_ESTIMATES.keys())}")
            if "size" in comp and comp["size"] not in EFFORT_ESTIMATES.get(comp.get("type", ""), {}):
                errors.append(f"Component size must be one of: xs, s, m, l, xl")
    return errors


def estimate_effort(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    components = data["components"]
    complexity = data.get("complexity", "medium")
    multiplier = COMPLEXITY_MULTIPLIERS.get(complexity, 1.3)
    total_days = 0
    component_estimates = []

    for comp in components:
        comp_type = comp["type"]
        size = comp["size"]
        base_days = EFFORT_ESTIMATES[comp_type][size]["days"]
        adjusted_days = round(base_days * multiplier)
        total_days += adjusted_days
        component_estimates.append({
            "component": comp.get("name", comp_type),
            "type": comp_type,
            "size": size,
            "base_days": base_days,
            "adjusted_days": adjusted_days,
            "description": EFFORT_ESTIMATES[comp_type][size]["description"],
        })

    # Add 20% QA and testing buffer
    testing_buffer_days = round(total_days * 0.20)
    total_with_buffer = total_days + testing_buffer_days

    return {
        "error": None,
        "result": {
            "initiative_name": data["initiative_name"],
            "complexity": complexity,
            "complexity_multiplier": multiplier,
            "component_estimates": component_estimates,
            "subtotal_days": total_days,
            "testing_buffer_days": testing_buffer_days,
            "total_estimated_days": total_with_buffer,
            "total_estimated_weeks": round(total_with_buffer / 5, 1),
            "confidence": "medium — estimates assume requirements are stable and no blocking data quality issues",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = estimate_effort(data)
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
