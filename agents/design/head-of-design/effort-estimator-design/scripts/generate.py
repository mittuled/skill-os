#!/usr/bin/env python3
"""
generate.py — Generate a design effort estimate document for a feature or initiative.

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

# Complexity multipliers applied to base hours per deliverable type
DELIVERABLE_BASE_HOURS = {
    "user_flows": {"low": 4, "medium": 8, "high": 16},
    "wireframes": {"low": 8, "medium": 16, "high": 32},
    "visual_design": {"low": 8, "medium": 20, "high": 40},
    "prototype": {"low": 4, "medium": 12, "high": 24},
    "design_system_update": {"low": 4, "medium": 12, "high": 24},
    "handoff_spec": {"low": 4, "medium": 8, "high": 16},
}

# Review cycle overhead as % of production time
REVIEW_OVERHEAD_PCT = 0.35  # 35% for review and iteration cycles

CONFIDENCE_LEVELS = {
    "high": "Requirements fully defined, precedent exists",
    "medium": "Some ambiguity in requirements or novel patterns",
    "low": "Exploratory work, significant unknowns",
}


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors = []
    if "feature_name" not in data:
        errors.append("Missing required field: feature_name")
    if "deliverables" not in data or not isinstance(data["deliverables"], list):
        errors.append("Missing required field: deliverables (list of deliverable objects)")
    return errors


def generate_estimate(data: dict) -> dict:
    """Generate a design effort estimate."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    feature = data["feature_name"]
    deliverables_input = data["deliverables"]
    context = data.get("context", "")
    assumptions = data.get("assumptions", [])
    risks = data.get("risks", [])

    breakdown = []
    total_production_hours = 0

    for item in deliverables_input:
        dtype = item.get("type", "")
        complexity = item.get("complexity", "medium").lower()
        if dtype not in DELIVERABLE_BASE_HOURS:
            continue
        if complexity not in ("low", "medium", "high"):
            complexity = "medium"

        base = DELIVERABLE_BASE_HOURS[dtype][complexity]
        label = dtype.replace("_", " ").title()

        breakdown.append({
            "deliverable": label,
            "complexity": complexity,
            "production_hours": base,
            "notes": item.get("notes", ""),
        })
        total_production_hours += base

    review_hours = round(total_production_hours * REVIEW_OVERHEAD_PCT)
    total_hours = total_production_hours + review_hours

    # Derive confidence level from complexity spread
    complexities = [item.get("complexity", "medium") for item in deliverables_input]
    if "high" in complexities:
        confidence = "low"
    elif "medium" in complexities:
        confidence = "medium"
    else:
        confidence = "high"

    # T-shirt size
    if total_hours <= 16:
        tshirt = "S"
    elif total_hours <= 40:
        tshirt = "M"
    elif total_hours <= 80:
        tshirt = "L"
    else:
        tshirt = "XL"

    return {
        "error": None,
        "result": {
            "feature": feature,
            "context": context,
            "deliverable_breakdown": breakdown,
            "production_hours": total_production_hours,
            "review_and_iteration_hours": review_hours,
            "total_hours": total_hours,
            "t_shirt_size": tshirt,
            "confidence_level": confidence,
            "confidence_rationale": CONFIDENCE_LEVELS[confidence],
            "assumptions": assumptions,
            "risks": risks,
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_estimate(data)
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
