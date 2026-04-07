#!/usr/bin/env python3
"""Score a launch-checklist-runner exercise against the scoring rubric.

Usage:
    echo '{"checklist_completeness": 8, "verification_rigour": 8, "blocker_escalation": 8, "readiness_recommendation": 8}' | python3 score.py
"""

import json
import sys

CRITERIA: dict[str, float] = {
    "checklist_completeness": 0.25,
    "verification_rigour": 0.3,
    "blocker_escalation": 0.25,
    "readiness_recommendation": 0.2,
}

GRADE_BANDS: list[tuple[str, float, float, str, str]] = [
    ("A+", 9.0, 10.0, "Exceptional", "All items pass — authorise launch"),
    ("A", 8.0, 8.9, "Strong", "Minor non-blocking items open — authorise with monitoring"),
    ("B", 7.0, 7.9, "Good", "Conditional go — resolve flagged items within 48 hours"),
    ("C", 5.0, 6.9, "Adequate", "Multiple failures — schedule re-run after remediation"),
    ("D", 3.0, 4.9, "Weak", "Critical blockers — no-go until resolved"),
    ("F", 0.0, 2.9, "Failing", "No checklist run performed"),
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
        "skill": "launch-checklist-runner",
        "scores": {k: data[k] for k in CRITERIA},
        "weights": CRITERIA,
        "composite_score": round(composite, 2),
        **grade_info,
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
