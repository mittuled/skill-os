#!/usr/bin/env python3
"""Score a go-live-approver exercise against the scoring rubric.

Usage:
    echo '{"release_manifest_accuracy": 8, "acceptance_criteria_verification": 8, "cross_functional_readiness": 8, "rollback_and_risk_assessment": 8, "decision_documentation": 8}' | python3 score.py
"""

import json
import sys

CRITERIA: dict[str, float] = {
    "release_manifest_accuracy": 0.15,
    "acceptance_criteria_verification": 0.25,
    "cross_functional_readiness": 0.25,
    "rollback_and_risk_assessment": 0.2,
    "decision_documentation": 0.15,
}

GRADE_BANDS: list[tuple[str, float, float, str, str]] = [
    ("A+", 9.0, 10.0, "Exceptional", "Authorise immediate deployment"),
    ("A", 8.0, 8.9, "Strong", "Authorise with monitoring heightened for 48 hours"),
    ("B", 7.0, 7.9, "Good", "Conditional go — resolve specified items before deploy"),
    ("C", 5.0, 6.9, "Adequate", "Defer — significant readiness gaps require remediation"),
    ("D", 3.0, 4.9, "Weak", "No-go — multiple blocking issues unresolved"),
    ("F", 0.0, 2.9, "Failing", "No go-live assessment performed"),
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
        "skill": "go-live-approver",
        "scores": {k: data[k] for k in CRITERIA},
        "weights": CRITERIA,
        "composite_score": round(composite, 2),
        **grade_info,
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
