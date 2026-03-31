#!/usr/bin/env python3
"""
score.py — Score and prioritise expansion opportunities within existing accounts.

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

# Scoring rubric for expansion opportunity assessment
OPPORTUNITY_CRITERIA = {
    "usage_signal_strength": {
        "weight": 0.25,
        "description": "How clearly usage data indicates expansion readiness",
        "levels": {
            "approaching_limit": 10,
            "underutilised_premium": 8,
            "flat_usage": 5,
            "declining_usage": 2,
        },
    },
    "strategic_fit": {
        "weight": 0.20,
        "description": "Alignment between expansion option and account business needs",
        "levels": {
            "direct_business_need": 10,
            "adjacent_use_case": 7,
            "speculative_fit": 4,
            "poor_fit": 1,
        },
    },
    "revenue_potential": {
        "weight": 0.20,
        "description": "Expected incremental ARR from the expansion",
        "levels": {
            "high": 10,   # >$50k ARR uplift
            "medium": 6,  # $10k-$50k ARR uplift
            "low": 3,     # <$10k ARR uplift
        },
    },
    "account_health": {
        "weight": 0.20,
        "description": "Current health of the account relationship",
        "levels": {
            "healthy": 10,
            "neutral": 6,
            "at_risk": 2,
            "churning": 0,
        },
    },
    "close_likelihood": {
        "weight": 0.15,
        "description": "Probability of closing the expansion based on champion access and budget",
        "levels": {
            "champion_with_budget": 10,
            "champion_no_budget": 6,
            "no_champion": 3,
            "blocker_identified": 1,
        },
    },
}

REQUIRED_FIELDS = ["account_name", "expansion_type", "criteria_ratings"]


def validate_input(data: dict) -> list[str]:
    """Validate required fields and criteria ratings."""
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "criteria_ratings" in data:
        for criterion in OPPORTUNITY_CRITERIA:
            if criterion not in data["criteria_ratings"]:
                errors.append(f"Missing criteria rating for: {criterion}")
    return errors


def score_opportunity(data: dict) -> dict:
    """Score an expansion opportunity using weighted criteria."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    ratings = data["criteria_ratings"]
    total_score = 0.0
    criterion_scores = {}

    for criterion, config in OPPORTUNITY_CRITERIA.items():
        level = ratings.get(criterion, "")
        level_score = config["levels"].get(level, 0)
        weighted = level_score * config["weight"]
        total_score += weighted
        criterion_scores[criterion] = {
            "level": level,
            "raw_score": level_score,
            "weighted_score": round(weighted, 2),
            "description": config["description"],
        }

    # Determine priority tier
    if total_score >= 8.0:
        priority = "P1 — Pursue immediately"
    elif total_score >= 6.0:
        priority = "P2 — Pursue this quarter"
    elif total_score >= 4.0:
        priority = "P3 — Monitor and revisit next quarter"
    else:
        priority = "P4 — Deprioritise or address blockers first"

    # Build talking points based on top-scoring criteria
    talking_points = []
    sorted_criteria = sorted(criterion_scores.items(), key=lambda x: x[1]["raw_score"], reverse=True)
    for criterion, scores in sorted_criteria[:2]:
        if scores["raw_score"] >= 7:
            talking_points.append(f"Strong {criterion.replace('_', ' ')} supports expansion conversation")

    return {
        "error": None,
        "result": {
            "account_name": data["account_name"],
            "expansion_type": data["expansion_type"],
            "total_score": round(total_score, 2),
            "priority_tier": priority,
            "criterion_scores": criterion_scores,
            "recommended_timing": data.get("recommended_timing", "Next QBR"),
            "talking_points": talking_points,
            "flags": ["Account health at-risk — resolve issues before expanding"] if ratings.get("account_health") in ["at_risk", "churning"] else [],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_opportunity(data)
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
