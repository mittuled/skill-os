#!/usr/bin/env python3
"""
score.py — Score a prospect account against the Ideal Customer Profile (ICP) rubric.

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

# ICP dimension weights (must sum to 1.0)
ICP_DIMENSION_WEIGHTS = {
    "company_size": 0.15,
    "industry_fit": 0.20,
    "technology_stack": 0.15,
    "growth_stage": 0.15,
    "pain_intensity": 0.25,
    "budget_authority": 0.10,
}

# ICP tier thresholds
ICP_TIERS = [
    (8.0, "tier_1", "Ideal — prioritize immediately; dedicated AE attention"),
    (6.0, "tier_2", "Strong fit — include in outbound; high expected conversion"),
    (4.0, "tier_3", "Marginal fit — pursue only with available capacity"),
    (0.0, "deprioritize", "Poor fit — remove from active pipeline; reallocate resources"),
]

# Disqualifying signals — if any present, cap score at 3.0
DISQUALIFYING_SIGNALS = [
    "direct_competitor",
    "recent_churn_from_same_category",
    "explicit_no_budget",
    "locked_in_competitor_contract",
]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["account_name", "icp_scores"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "icp_scores" in data:
        for dim in ICP_DIMENSION_WEIGHTS:
            if dim not in data["icp_scores"]:
                errors.append(f"icp_scores missing dimension: {dim}")
            elif not (0 <= data["icp_scores"][dim] <= 10):
                errors.append(f"icp_scores.{dim} must be 0-10")
    return errors


def assign_tier(score: float) -> tuple[str, str]:
    for threshold, tier, action in ICP_TIERS:
        if score >= threshold:
            return tier, action
    return "deprioritize", "Remove from pipeline"


def score_icp(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    scores = data["icp_scores"]
    composite = sum(scores[dim] * ICP_DIMENSION_WEIGHTS[dim] for dim in ICP_DIMENSION_WEIGHTS)

    # Check for disqualifying signals
    disqualifiers = [s for s in data.get("disqualifying_signals", []) if s in DISQUALIFYING_SIGNALS]
    if disqualifiers:
        composite = min(composite, 3.0)

    composite = round(composite, 2)
    tier, recommendation = assign_tier(composite)

    result = {
        "account": data["account_name"],
        "composite_score": composite,
        "icp_breakdown": {
            dim: {
                "score": scores[dim],
                "weight": ICP_DIMENSION_WEIGHTS[dim],
                "contribution": round(scores[dim] * ICP_DIMENSION_WEIGHTS[dim], 2),
                "notes": data.get("dimension_notes", {}).get(dim, ""),
            }
            for dim in ICP_DIMENSION_WEIGHTS
        },
        "tier": tier,
        "recommendation": recommendation,
        "disqualifying_signals": disqualifiers,
        "strongest_dimensions": [
            dim for dim in ICP_DIMENSION_WEIGHTS
            if scores[dim] >= 8
        ],
        "weak_dimensions": [
            dim for dim in ICP_DIMENSION_WEIGHTS
            if scores[dim] < 5
        ],
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_icp(data)
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
