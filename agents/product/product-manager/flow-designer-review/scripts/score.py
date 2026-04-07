#!/usr/bin/env python3
"""Score a flow-designer-review exercise against the scoring rubric.

Usage:
    echo '{"requirements_coverage": 8, "persona_path_coverage": 8, "error_state_handling": 8, "flow_coherence": 8}' | python3 score.py
"""

import json
import sys

CRITERIA: dict[str, float] = {
    "requirements_coverage": 0.25,
    "persona_path_coverage": 0.25,
    "error_state_handling": 0.25,
    "flow_coherence": 0.25,
}

GRADE_BANDS: list[tuple[str, float, float, str, str]] = [
    ("A+", 9.0, 10.0, "Exceptional", "Flow approved — proceed to implementation"),
    ("A", 8.0, 8.9, "Strong", "Approved with minor coherence improvements"),
    ("B", 7.0, 7.9, "Good", "Revisions needed on error states or persona paths"),
    ("C", 5.0, 6.9, "Adequate", "Significant gaps in requirements coverage"),
    ("D", 3.0, 4.9, "Weak", "Major rework needed — flow does not satisfy stories"),
    ("F", 0.0, 2.9, "Failing", "No flow review performed"),
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
        "skill": "flow-designer-review",
        "scores": {k: data[k] for k in CRITERIA},
        "weights": CRITERIA,
        "composite_score": round(composite, 2),
        **grade_info,
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
