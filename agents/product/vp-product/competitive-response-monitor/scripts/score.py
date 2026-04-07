#!/usr/bin/env python3
"""Score a competitive response monitoring exercise.

Reads JSON from stdin with criterion scores (0-10), outputs graded result.

Usage:
    echo '{"signal_capture": 8, "customer_impact_assessment": 7, "severity_classification": 8, "response_recommendation": 9}' | python3 score.py
"""

import json
import sys

CRITERIA: dict[str, float] = {
    "signal_capture": 0.20,
    "customer_impact_assessment": 0.25,
    "severity_classification": 0.25,
    "response_recommendation": 0.30,
}

GRADE_BANDS: list[tuple[str, float, float, str, str]] = [
    ("A+", 9.0, 10.0, "Exceptional", "Execute recommended response"),
    ("A",  8.0, 8.9,  "Strong",      "Proceed with response after minor validation"),
    ("B",  7.0, 7.9,  "Good",        "Validate impact assessment before committing"),
    ("C",  5.0, 6.9,  "Adequate",    "Gather customer evidence before classifying"),
    ("D",  3.0, 4.9,  "Weak",        "Restart with structured signal capture"),
    ("F",  0.0, 2.9,  "Failing",     "Establish competitive monitoring practice"),
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
        "skill": "competitive-response-monitor",
        "scores": {k: data[k] for k in CRITERIA},
        "weights": CRITERIA,
        "composite_score": round(composite, 2),
        **grade_info,
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
