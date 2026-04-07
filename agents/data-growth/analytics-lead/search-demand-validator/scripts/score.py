#!/usr/bin/env python3
"""
score.py — Score search demand evidence for a product concept to validate market pull.

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

DEMAND_CRITERIA = {
    "monthly_search_volume": {
        "weight": 0.30,
        "description": "Total monthly searches for primary keywords",
        "levels": {"high": 10, "medium": 6, "low": 3, "negligible": 1},
        "thresholds": {"high": 10000, "medium": 1000, "low": 100},
    },
    "trend_direction": {
        "weight": 0.25,
        "description": "Keyword search volume trend over last 12 months",
        "levels": {"growing_fast": 10, "growing": 7, "flat": 4, "declining": 1},
    },
    "keyword_intent": {
        "weight": 0.20,
        "description": "Proportion of searches with commercial/transactional intent",
        "levels": {"high_commercial": 10, "mixed_intent": 6, "informational": 3},
    },
    "competition_density": {
        "weight": 0.15,
        "description": "Number and quality of competitors in paid and organic results",
        "levels": {"low": 10, "medium": 6, "high": 3, "saturated": 1},
    },
    "category_growth_rate": {
        "weight": 0.10,
        "description": "Overall category growth rate based on industry data",
        "levels": {"hypergrowth": 10, "growing": 7, "mature": 4, "shrinking": 1},
    },
}

REQUIRED_FIELDS = ["concept_name", "primary_keywords", "criteria_ratings"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "criteria_ratings" in data:
        for criterion in DEMAND_CRITERIA:
            if criterion not in data["criteria_ratings"]:
                errors.append(f"Missing criteria rating: {criterion}")
    return errors


def score_demand(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    ratings = data["criteria_ratings"]
    total_score = 0.0
    criterion_scores = {}

    for criterion, config in DEMAND_CRITERIA.items():
        level = ratings.get(criterion, "negligible")
        level_score = config["levels"].get(level, 1)
        weighted = level_score * config["weight"]
        total_score += weighted
        criterion_scores[criterion] = {
            "level": level, "raw_score": level_score,
            "weighted_score": round(weighted, 2),
            "description": config["description"],
        }

    if total_score >= 7.5:
        verdict = "STRONG DEMAND SIGNAL — proceed with product development"
    elif total_score >= 5.5:
        verdict = "MODERATE DEMAND — validate further with customer interviews"
    elif total_score >= 3.5:
        verdict = "WEAK DEMAND — high risk; find a more specific niche or pivot"
    else:
        verdict = "NO DEMAND SIGNAL — do not build"

    return {
        "error": None,
        "result": {
            "concept_name": data["concept_name"],
            "primary_keywords": data["primary_keywords"],
            "demand_score": round(total_score, 2),
            "verdict": verdict,
            "criterion_scores": criterion_scores,
            "top_keywords": data.get("top_keywords", []),
            "estimated_monthly_searches": data.get("estimated_monthly_searches"),
            "recommendation": "Validate demand with customer discovery interviews before committing to full build" if total_score >= 5.5 else "Reconsider the product concept — demand signal is insufficient to justify investment",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_demand(data)
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
