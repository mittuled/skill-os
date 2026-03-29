#!/usr/bin/env python3
"""Score a performance-budget-setter exercise against the scoring rubric.

Usage:
    echo '{"critical_path_identification": 8, "baseline_measurement": 8, "budget_threshold_quality": 8, "enforcement_policy": 8}' | python3 score.py
"""

import json
import sys

CRITERIA: dict[str, float] = {
    "critical_path_identification": 0.2,
    "baseline_measurement": 0.25,
    "budget_threshold_quality": 0.3,
    "enforcement_policy": 0.25,
}

GRADE_BANDS: list[tuple[str, float, float, str, str]] = [
    ("A+", 9.0, 10.0, "Exceptional", "Budget ready for PRD integration and CI enforcement"),
    ("A", 8.0, 8.9, "Strong", "Budget viable with minor enforcement setup remaining"),
    ("B", 7.0, 7.9, "Good", "Validate baseline measurements before finalising targets"),
    ("C", 5.0, 6.9, "Adequate", "Instrumentation gaps — add APM coverage before setting budgets"),
    ("D", 3.0, 4.9, "Weak", "Insufficient data — instrument critical paths first"),
    ("F", 0.0, 2.9, "Failing", "No performance budget defined"),
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
        "skill": "performance-budget-setter",
        "scores": {k: data[k] for k in CRITERIA},
        "weights": CRITERIA,
        "composite_score": round(composite, 2),
        **grade_info,
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
