#!/usr/bin/env python3
"""
score.py — Audit a north star metric definition for validity, measurability, and correlation with value delivery.

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

# North star metric quality criteria
NSM_CRITERIA = {
    "value_reflection": {
        "weight": 0.25,
        "description": "Metric reflects core value delivered to users (not a business metric in disguise)",
        "levels": {"strong": 10, "moderate": 6, "weak": 3, "none": 0},
    },
    "revenue_correlation": {
        "weight": 0.20,
        "description": "Empirical correlation between metric and revenue/retention",
        "levels": {"proven": 10, "assumed": 5, "unknown": 2, "no_correlation": 0},
    },
    "measurability": {
        "weight": 0.20,
        "description": "Metric is queryable from existing instrumentation",
        "levels": {"fully_instrumented": 10, "partially_instrumented": 6, "not_instrumented": 1},
    },
    "actionability": {
        "weight": 0.20,
        "description": "Teams can run experiments and initiatives that directly move this metric",
        "levels": {"directly_actionable": 10, "indirectly_actionable": 6, "not_actionable": 2},
    },
    "leading_indicator": {
        "weight": 0.15,
        "description": "Metric changes before revenue/churn changes (leading, not lagging)",
        "levels": {"clearly_leading": 10, "mixed": 5, "lagging": 2},
    },
}

REQUIRED_FIELDS = ["metric_name", "metric_definition", "criteria_ratings"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "criteria_ratings" in data:
        for criterion in NSM_CRITERIA:
            if criterion not in data["criteria_ratings"]:
                errors.append(f"Missing rating for criterion: {criterion}")
    return errors


def score_nsm(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    ratings = data["criteria_ratings"]
    total_score = 0.0
    criterion_scores = {}

    for criterion, config in NSM_CRITERIA.items():
        level = ratings.get(criterion, "none")
        level_score = config["levels"].get(level, 0)
        weighted = level_score * config["weight"]
        total_score += weighted
        criterion_scores[criterion] = {
            "level": level, "raw_score": level_score,
            "weighted_score": round(weighted, 2),
            "description": config["description"],
        }

    if total_score >= 8.0:
        verdict = "STRONG — retain as north star metric"
    elif total_score >= 6.0:
        verdict = "ADEQUATE — address identified weaknesses"
    elif total_score >= 4.0:
        verdict = "WEAK — consider redefining the north star metric"
    else:
        verdict = "INVALID — replace with a better metric"

    weak_criteria = [c for c, s in criterion_scores.items() if s["raw_score"] <= 3]

    return {
        "error": None,
        "result": {
            "metric_name": data["metric_name"],
            "metric_definition": data["metric_definition"],
            "overall_score": round(total_score, 2),
            "verdict": verdict,
            "criterion_scores": criterion_scores,
            "weak_criteria": weak_criteria,
            "recommendations": [f"Improve {c} — currently '{criterion_scores[c]['level']}'" for c in weak_criteria],
            "current_baseline": data.get("current_baseline"),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_nsm(data)
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
