#!/usr/bin/env python3
"""
score.py — Scores an accessibility audit against the scoring rubric.

Reads a JSON audit payload with per-criterion scores and computes a weighted
composite score, letter grade, and per-criterion feedback.

Dependencies: Python 3.10+ standard library only.

Usage:
    python3 score.py                          # interactive prompts
    python3 score.py --json audit.json        # from JSON file
    python3 score.py -o report.json           # write JSON report to file
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

CRITERIA: list[dict] = [
    {"name": "Automated Coverage", "weight": 0.15,
     "description": "Breadth and accuracy of automated accessibility scanning"},
    {"name": "Manual Testing Depth", "weight": 0.25,
     "description": "Thoroughness of assistive technology testing (keyboard, screen reader, magnification, reduced motion)"},
    {"name": "Finding Classification", "weight": 0.20,
     "description": "Accuracy of WCAG criterion mapping, severity rating, and affected-population assessment"},
    {"name": "Remediation Specificity", "weight": 0.25,
     "description": "Actionability of recommendations with design-level fixes and owner assignments"},
    {"name": "Report Clarity", "weight": 0.15,
     "description": "Structured presentation with executive summary and compliance scorecard"},
]

GRADE_BANDS: list[dict] = [
    {"grade": "A+", "min": 9.0, "max": 10.0, "label": "Exceptional",
     "action": "Approve and schedule periodic re-audit at 6-month cadence"},
    {"grade": "A", "min": 8.0, "max": 8.99, "label": "Strong",
     "action": "Approve with follow-up on flagged AT gaps within next sprint"},
    {"grade": "B", "min": 7.0, "max": 7.99, "label": "Good",
     "action": "Approve conditionally; strengthen remediation plan before handoff"},
    {"grade": "C", "min": 5.0, "max": 6.99, "label": "Adequate",
     "action": "Revise audit; expand manual testing before releasing findings"},
    {"grade": "D", "min": 3.0, "max": 4.99, "label": "Weak",
     "action": "Rework with dedicated assistive technology testing sessions"},
    {"grade": "F", "min": 0.0, "max": 2.99, "label": "Failing",
     "action": "Halt and commission a full accessibility audit engagement"},
]


def get_grade(score: float) -> dict:
    for band in GRADE_BANDS:
        if band["min"] <= score <= band["max"]:
            return band
    return GRADE_BANDS[-1]


def score_audit(scores: dict[str, float]) -> dict:
    """Compute composite score from per-criterion scores."""
    results = []
    composite = 0.0

    for criterion in CRITERIA:
        name = criterion["name"]
        raw = scores.get(name, 0.0)
        raw = max(0.0, min(10.0, float(raw)))
        weighted = raw * criterion["weight"]
        composite += weighted
        results.append({
            "criterion": name,
            "weight": criterion["weight"],
            "raw_score": raw,
            "weighted_score": round(weighted, 2),
            "description": criterion["description"],
        })

    composite = round(composite, 2)
    grade = get_grade(composite)

    return {
        "composite_score": composite,
        "grade": grade["grade"],
        "label": grade["label"],
        "recommended_action": grade["action"],
        "criteria_results": results,
        "wcag_coverage_note": _wcag_note(scores),
    }


def _wcag_note(scores: dict[str, float]) -> str:
    manual = scores.get("Manual Testing Depth", 0)
    auto = scores.get("Automated Coverage", 0)
    if manual < 5 and auto >= 7:
        return "Warning: automated-only bias detected. Manual AT testing is critically underrepresented."
    if manual >= 8 and auto < 5:
        return "Warning: manual testing strong but automated scanning gaps may miss programmatic violations."
    return "Coverage balance between automated and manual testing is acceptable."


def interactive_prompt() -> dict[str, float]:
    print("Score each criterion 0-10:\n")
    scores = {}
    for c in CRITERIA:
        while True:
            try:
                val = float(input(f"  {c['name']} ({c['weight']:.0%}): "))
                if 0 <= val <= 10:
                    scores[c["name"]] = val
                    break
                print("    Score must be 0-10.")
            except ValueError:
                print("    Enter a number.")
    return scores


def main() -> None:
    args = sys.argv[1:]
    scores: dict[str, float] = {}

    if "--json" in args:
        idx = args.index("--json") + 1
        if idx < len(args):
            data = json.loads(Path(args[idx]).read_text(encoding="utf-8"))
            scores = data if isinstance(data, dict) else data.get("scores", {})
        else:
            print("Error: --json requires a file path", file=sys.stderr)
            sys.exit(1)
    else:
        scores = interactive_prompt()

    result = score_audit(scores)
    output = json.dumps(result, indent=2)

    if "-o" in args:
        out_idx = args.index("-o") + 1
        if out_idx < len(args):
            Path(args[out_idx]).write_text(output + "\n", encoding="utf-8")
            print(f"Report written to {args[out_idx]}")
        else:
            print("Error: -o requires a filename", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
