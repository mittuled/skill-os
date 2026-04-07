#!/usr/bin/env python3
"""
score.py — Score emerging technology trends for product relevance, maturity, and investment priority.

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

TECHNOLOGY_MATURITY = {
    "innovation_trigger": {"score": 3, "horizon": "3-5 years", "description": "Pre-production; proof of concept only"},
    "peak_of_inflated_expectations": {"score": 5, "horizon": "2-4 years", "description": "Hype cycle peak; early adopters only"},
    "trough_of_disillusionment": {"score": 6, "horizon": "1-3 years", "description": "Realism setting in; only strong use cases survive"},
    "slope_of_enlightenment": {"score": 8, "horizon": "1-2 years", "description": "Real-world validation; mainstream adoption approaching"},
    "plateau_of_productivity": {"score": 9, "horizon": "now", "description": "Mainstream adoption; proven in production"},
}

RELEVANCE_CRITERIA = {
    "core_product_impact": {"weight": 0.35, "description": "Does this technology directly enhance our core product value?"},
    "customer_demand": {"weight": 0.25, "description": "Are customers asking for this capability?"},
    "competitive_pressure": {"weight": 0.20, "description": "Are competitors adopting this to gain advantage?"},
    "implementation_feasibility": {"weight": 0.20, "description": "Can our team realistically implement this within 12 months?"},
}

REQUIRED_FIELDS = ["technology_name", "maturity_stage", "relevance_ratings"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "maturity_stage" in data and data["maturity_stage"] not in TECHNOLOGY_MATURITY:
        errors.append(f"maturity_stage must be one of {list(TECHNOLOGY_MATURITY.keys())}")
    if "relevance_ratings" in data:
        for criterion in RELEVANCE_CRITERIA:
            if criterion not in data["relevance_ratings"]:
                errors.append(f"Missing relevance rating: {criterion}")
    return errors


def score_trend(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    maturity = TECHNOLOGY_MATURITY[data["maturity_stage"]]
    ratings = data["relevance_ratings"]
    total_score = 0.0
    criterion_scores = {}

    for criterion, config in RELEVANCE_CRITERIA.items():
        raw = ratings.get(criterion, 5)
        weighted = raw * config["weight"]
        total_score += weighted
        criterion_scores[criterion] = {
            "raw_score": raw, "weighted_score": round(weighted, 2),
            "description": config["description"],
        }

    # Combine relevance with maturity
    maturity_factor = maturity["score"] / 10
    combined_score = total_score * 0.7 + maturity_factor * 10 * 0.3

    if combined_score >= 7.5:
        recommendation = "INVEST — build capability now"
    elif combined_score >= 5.5:
        recommendation = "MONITOR — track and plan for 12-24 month adoption"
    elif combined_score >= 3.5:
        recommendation = "WATCH — revisit when maturity advances or customer demand grows"
    else:
        recommendation = "IGNORE — not relevant to current product direction"

    return {
        "error": None,
        "result": {
            "technology_name": data["technology_name"],
            "maturity_stage": data["maturity_stage"],
            "maturity_description": maturity["description"],
            "adoption_horizon": maturity["horizon"],
            "relevance_score": round(total_score, 2),
            "combined_score": round(combined_score, 2),
            "recommendation": recommendation,
            "criterion_scores": criterion_scores,
            "risks": data.get("risks", []),
            "opportunities": data.get("opportunities", []),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_trend(data)
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
