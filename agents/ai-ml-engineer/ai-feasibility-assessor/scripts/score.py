#!/usr/bin/env python3
"""
score.py — Assess AI/ML feasibility across data readiness, compute, and timeline dimensions.

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

# Feasibility dimensions and scoring rubric
FEASIBILITY_CRITERIA = {
    "data_volume": {
        "weight": 0.25,
        "description": "Labelled training examples available",
        "levels": {
            "large": 10,       # >100k labelled examples
            "medium": 7,       # 10k-100k labelled examples
            "small": 4,        # 1k-10k labelled examples
            "insufficient": 1, # <1k labelled examples
        },
    },
    "label_quality": {
        "weight": 0.20,
        "description": "Label accuracy and consistency",
        "levels": {
            "high": 10,      # <5% noise, consistent annotation
            "medium": 6,     # 5-15% noise or partial coverage
            "low": 3,        # >15% noise or significant gaps
            "none": 0,       # No labels — unsupervised only
        },
    },
    "compute_budget": {
        "weight": 0.15,
        "description": "Training compute budget relative to task complexity",
        "levels": {
            "sufficient": 10,
            "constrained": 6,
            "severely_constrained": 2,
        },
    },
    "latency_feasibility": {
        "weight": 0.20,
        "description": "Whether latency requirements are achievable with chosen architecture",
        "levels": {
            "relaxed": 10,    # >1s acceptable
            "moderate": 7,    # 100ms-1s
            "strict": 4,      # 10-100ms
            "real_time": 2,   # <10ms
        },
    },
    "problem_complexity": {
        "weight": 0.20,
        "description": "Whether ML is the right tool vs simpler alternatives",
        "levels": {
            "clear_ml_win": 10,       # Patterns too complex for rules
            "ml_adds_value": 7,        # ML improves over heuristics
            "marginal_benefit": 4,     # Heuristics almost as good
            "rules_sufficient": 1,     # Deterministic solution exists
        },
    },
}

TASK_TYPES = ["classification", "regression", "ranking", "generation", "anomaly_detection", "recommendation"]
REQUIRED_FIELDS = ["problem_name", "task_type", "criteria_ratings"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "task_type" in data and data["task_type"] not in TASK_TYPES:
        errors.append(f"task_type must be one of {TASK_TYPES}")
    if "criteria_ratings" in data:
        for criterion in FEASIBILITY_CRITERIA:
            if criterion not in data["criteria_ratings"]:
                errors.append(f"Missing criteria rating for: {criterion}")
    return errors


def assess_feasibility(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    ratings = data["criteria_ratings"]
    total_score = 0.0
    criterion_scores = {}

    for criterion, config in FEASIBILITY_CRITERIA.items():
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

    # Feasibility verdict
    if total_score >= 7.5:
        verdict = "GO — feasible with current constraints"
    elif total_score >= 5.5:
        verdict = "CONDITIONAL GO — feasible if specified conditions are met"
    elif total_score >= 3.5:
        verdict = "NO-GO — significant blockers; revisit after addressing gaps"
    else:
        verdict = "NO-GO — consider rule-based or heuristic alternative"

    # Identify blockers
    blockers = []
    for criterion, scores in criterion_scores.items():
        if scores["raw_score"] <= 2:
            blockers.append(f"{criterion}: {scores['level']} — this is a critical blocker")

    # Recommended alternatives if score is low
    alternatives = []
    if ratings.get("problem_complexity") == "rules_sufficient":
        alternatives.append("Implement a deterministic rule-based system — faster, cheaper, and interpretable")
    if ratings.get("data_volume") in ["small", "insufficient"]:
        alternatives.append("Consider few-shot learning with a foundation model, or collect more labelled data before training")

    return {
        "error": None,
        "result": {
            "problem_name": data["problem_name"],
            "task_type": data["task_type"],
            "feasibility_score": round(total_score, 2),
            "verdict": verdict,
            "criterion_scores": criterion_scores,
            "blockers": blockers,
            "alternatives": alternatives,
            "estimated_timeline_weeks": data.get("estimated_timeline_weeks"),
            "risks": data.get("risks", []),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = assess_feasibility(data)
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
