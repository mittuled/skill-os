#!/usr/bin/env python3
"""Score a demand-validator exercise against the scoring rubric.

Usage:
    echo '{"qualitative_input_quality": 8, "demand_question_definition": 8, "quantitative_proxy_selection": 8, "triangulation_quality": 8}' | python3 score.py
"""

import json
import sys

CRITERIA: dict[str, float] = {
    "qualitative_input_quality": 0.2,
    "demand_question_definition": 0.2,
    "quantitative_proxy_selection": 0.3,
    "triangulation_quality": 0.3,
}

GRADE_BANDS: list[tuple[str, float, float, str, str]] = [
    ("A+", 9.0, 10.0, "Exceptional", "Demand validated — proceed to build"),
    ("A", 8.0, 8.9, "Strong", "High confidence — proceed with minor data gaps noted"),
    ("B", 7.0, 7.9, "Good", "Run one additional validation round before committing"),
    ("C", 5.0, 6.9, "Adequate", "Inconclusive — design a more targeted test"),
    ("D", 3.0, 4.9, "Weak", "Insufficient evidence — restart validation with better proxies"),
    ("F", 0.0, 2.9, "Failing", "No demand validation performed"),
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
        "skill": "demand-validator",
        "scores": {k: data[k] for k in CRITERIA},
        "weights": CRITERIA,
        "composite_score": round(composite, 2),
        **grade_info,
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
