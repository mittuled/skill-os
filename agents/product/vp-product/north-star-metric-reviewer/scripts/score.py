#!/usr/bin/env python3
"""Score a north-star-metric-reviewer exercise against the scoring rubric.

Usage:
    echo '{"current_metric_documentation": 8, "strategic_alignment_analysis": 8, "leading_lagging_correlation": 8, "goodhart_risk_evaluation": 8, "recommendation_quality": 8}' | python3 score.py
"""

import json
import sys

CRITERIA: dict[str, float] = {
    "current_metric_documentation": 0.15,
    "strategic_alignment_analysis": 0.25,
    "leading_lagging_correlation": 0.3,
    "goodhart_risk_evaluation": 0.15,
    "recommendation_quality": 0.15,
}

GRADE_BANDS: list[tuple[str, float, float, str, str]] = [
    ("A+", 9.0, 10.0, "Exceptional", "Ratify metric for upcoming cycle"),
    ("A", 8.0, 8.9, "Strong", "Ratify with minor measurement adjustments"),
    ("B", 7.0, 7.9, "Good", "Conduct deeper correlation analysis before ratifying"),
    ("C", 5.0, 6.9, "Adequate", "Investigate Goodhart signals before deciding"),
    ("D", 3.0, 4.9, "Weak", "Convene leadership to clarify strategic direction before reviewing"),
    ("F", 0.0, 2.9, "Failing", "No metric review performed"),
]


def compute_composite(scores: dict[str, float]) -> float:
    return sum(scores[k] * CRITERIA[k] for k in CRITERIA)


def assign_grade(composite: float) -> dict[str, str]:
    for grade, low, high, label, action in GRADE_BANDS:
        if low <= composite <= high:
            return {"grade": grade, "label": label, "recommended_action": action}
    return {"grade": "F", "label": "Failing", "recommended_action": GRADE_BANDS[-1][4]}


def main() -> None:
    data = json.load(sys.stdin)
    missing = [k for k in CRITERIA if k not in data]
    if missing:
        json.dump({"error": f"Missing criteria: {missing}"}, sys.stdout, indent=2)
        sys.exit(1)
    for k in CRITERIA:
        if not (0 <= data[k] <= 10):
            json.dump({"error": f"Score for {k} must be 0-10, got {data[k]}"}, sys.stdout, indent=2)
            sys.exit(1)
    composite = compute_composite(data)
    grade_info = assign_grade(composite)
    result = {
        "skill": "north-star-metric-reviewer",
        "scores": {k: data[k] for k in CRITERIA},
        "weights": CRITERIA,
        "composite_score": round(composite, 2),
        **grade_info,
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
