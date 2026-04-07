#!/usr/bin/env python3
"""
score.py — Computes a composite marketing audit score from per-criterion ratings.

Purpose: Accepts a JSON object with scores for each of the five marketing audit
         dimensions, computes weighted scores, determines the composite grade,
         and outputs a structured JSON result.

Dependencies: Python 3.10+ standard library only (no external packages).

Usage:
    echo '{"brand_health": 7, "channel_performance": 8, "content_quality": 6, "funnel_efficiency": 7, "martech_utilisation": 5}' | python3 score.py
    python3 score.py < scores.json
    python3 score.py --json < scores.json         # explicit JSON output
    python3 score.py -o report.json < scores.json  # write to file
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CRITERIA: dict[str, float] = {
    "brand_health": 0.20,
    "channel_performance": 0.25,
    "content_quality": 0.20,
    "funnel_efficiency": 0.20,
    "martech_utilisation": 0.15,
}

GRADE_BANDS: list[tuple[float, float, str, str]] = [
    (9.0, 10.0, "A+", "Exceptional"),
    (8.0, 8.9, "A", "Strong"),
    (7.0, 7.9, "B", "Good"),
    (5.0, 6.9, "C", "Adequate"),
    (3.0, 4.9, "D", "Weak"),
    (0.0, 2.9, "F", "Failing"),
]


def validate_scores(data: dict) -> list[str]:
    """Validate input scores and return a list of errors."""
    errors: list[str] = []
    for key in CRITERIA:
        if key not in data:
            errors.append(f"Missing required criterion: {key}")
        else:
            val = data[key]
            if not isinstance(val, (int, float)):
                errors.append(f"Invalid type for {key}: expected number, got {type(val).__name__}")
            elif not (0 <= val <= 10):
                errors.append(f"Score out of range for {key}: {val} (must be 0-10)")
    return errors


def compute_grade(composite: float) -> tuple[str, str]:
    """Return (grade, label) for a composite score."""
    for low, high, grade, label in GRADE_BANDS:
        if low <= composite <= high:
            return grade, label
    return "F", "Failing"


def score(data: dict) -> dict:
    """Compute weighted scores and composite grade."""
    errors = validate_scores(data)
    if errors:
        return {"error": errors, "composite": None, "grade": None}

    breakdown: list[dict] = []
    composite = 0.0

    for criterion, weight in CRITERIA.items():
        raw = float(data[criterion])
        weighted = round(raw * weight, 4)
        composite += weighted
        breakdown.append({
            "criterion": criterion,
            "weight": weight,
            "raw_score": raw,
            "weighted_score": weighted,
        })

    composite = round(composite, 2)
    grade, label = compute_grade(composite)

    return {
        "error": None,
        "breakdown": breakdown,
        "composite": composite,
        "grade": grade,
        "label": label,
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON input: {exc}"}), file=sys.stdout)
        sys.exit(1)

    result = score(data)
    output = json.dumps(result, indent=2)

    args = sys.argv[1:]
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(output + "\n", encoding="utf-8")
            print(f"Report written to {args[idx]}")
        else:
            print("Error: -o requires a filename", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
