#!/usr/bin/env python3
"""
score.py — Scores an email optimisation programme against the performance rubric.

Reads JSON from stdin with per-criterion scores (0-10), computes weighted composite,
assigns a grade, and outputs a JSON report.

Usage:
    echo '{"hypothesis_quality": 8, "test_design_rigour": 7, ...}' | python3 score.py
"""

from __future__ import annotations

import json
import sys

CRITERIA: dict[str, float] = {
    "hypothesis_quality": 0.20,
    "test_design_rigour": 0.25,
    "statistical_discipline": 0.25,
    "business_impact_measurement": 0.20,
    "knowledge_compounding": 0.10,
}

GRADE_BANDS: list[tuple[float, float, str, str]] = [
    (9.0, 10.0, "A+", "Exceptional"),
    (8.0, 8.9, "A", "Strong"),
    (7.0, 7.9, "B", "Good"),
    (5.0, 6.9, "C", "Adequate"),
    (3.0, 4.9, "D", "Weak"),
    (0.0, 2.9, "F", "Failing"),
]


def compute_grade(composite: float) -> tuple[str, str]:
    for low, high, grade, label in GRADE_BANDS:
        if low <= composite <= high:
            return grade, label
    return "F", "Failing"


def main() -> None:
    raw = sys.stdin.read().strip()
    if not raw:
        print(json.dumps({"error": "No input provided. Send JSON via stdin."}))
        sys.exit(1)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"Invalid JSON: {e}"}))
        sys.exit(1)

    scores: dict[str, float] = {}
    for criterion in CRITERIA:
        val = data.get(criterion)
        if val is None:
            print(json.dumps({"error": f"Missing criterion: {criterion}"}))
            sys.exit(1)
        if not (0 <= float(val) <= 10):
            print(json.dumps({"error": f"Score out of range for {criterion}: {val}"}))
            sys.exit(1)
        scores[criterion] = float(val)

    composite = sum(scores[c] * w for c, w in CRITERIA.items())
    composite = round(composite, 2)
    grade, label = compute_grade(composite)

    report = {
        "skill": "email-performance-optimiser",
        "scores": scores,
        "weights": CRITERIA,
        "composite_score": composite,
        "grade": grade,
        "label": label,
        "criteria_breakdown": [
            {
                "criterion": c,
                "score": scores[c],
                "weight": w,
                "weighted_score": round(scores[c] * w, 2),
            }
            for c, w in CRITERIA.items()
        ],
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
