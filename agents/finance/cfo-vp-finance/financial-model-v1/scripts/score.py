#!/usr/bin/env python3
"""
score.py — Scores a financial model v1 against the scoring rubric.

Reads a YAML/text assessment file with criterion scores and produces
a composite score, grade, and improvement recommendations.

Usage:
    python3 score.py                          # interactive mode
    python3 score.py assessment.yaml          # from file
    python3 score.py --json                   # JSON output
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

CRITERIA: list[dict] = [
    {"name": "Revenue Architecture", "weight": 0.25,
     "description": "Revenue model structure, driver definitions, bottoms-up build, cohort modelling"},
    {"name": "Cost Structure Accuracy", "weight": 0.20,
     "description": "COGS and OpEx modelling, headcount-driven costs, gross margin derivation"},
    {"name": "Cash Flow Construction", "weight": 0.20,
     "description": "Cash conversion modelling, billing mix, DSO, payment timing, runway"},
    {"name": "SaaS Metrics Integration", "weight": 0.15,
     "description": "Derived metrics correctness: ARR, NRR, LTV/CAC, burn multiple"},
    {"name": "Scenario Framework", "weight": 0.20,
     "description": "Scenario analysis quality, driver sensitivity, trigger definitions"},
]

GRADE_BANDS: list[dict] = [
    {"grade": "A+", "min": 9.0, "max": 10.0, "label": "Exceptional",
     "action": "Approve for investor distribution and board reporting"},
    {"grade": "A", "min": 8.0, "max": 8.99, "label": "Strong",
     "action": "Approve with follow-up documentation within one week"},
    {"grade": "B", "min": 7.0, "max": 7.99, "label": "Good",
     "action": "Approve for internal use; remediate before investor distribution"},
    {"grade": "C", "min": 5.0, "max": 6.99, "label": "Adequate",
     "action": "Revise model; not suitable for fundraising or board decisions"},
    {"grade": "D", "min": 3.0, "max": 4.99, "label": "Weak",
     "action": "Rework from revenue architecture stage with FP&A support"},
    {"grade": "F", "min": 0.0, "max": 2.99, "label": "Failing",
     "action": "Commission a full model build before any financial decisions"},
]


@dataclass
class CriterionScore:
    name: str
    weight: float
    score: float
    weighted: float


def get_grade(composite: float) -> dict:
    for band in GRADE_BANDS:
        if band["min"] <= composite <= band["max"]:
            return band
    return GRADE_BANDS[-1]


def parse_yaml_simple(text: str) -> dict:
    """Minimal YAML-like parser for key: value pairs."""
    result: dict = {}
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip().strip('"').strip("'")
            value = value.strip().strip('"').strip("'")
            try:
                result[key] = float(value)
            except ValueError:
                result[key] = value
    return result


def score_from_dict(data: dict) -> list[CriterionScore]:
    results: list[CriterionScore] = []
    for criterion in CRITERIA:
        name = criterion["name"]
        raw = data.get(name, data.get(name.lower().replace(" ", "_"), 0.0))
        score = max(0.0, min(10.0, float(raw)))
        weighted = score * criterion["weight"]
        results.append(CriterionScore(name=name, weight=criterion["weight"],
                                       score=score, weighted=weighted))
    return results


def interactive_scoring() -> dict:
    print("Financial Model V1 — Scoring Assessment")
    print("=" * 50)
    print("Score each criterion from 0 (absent) to 10 (comprehensive).\n")
    data: dict = {}
    for criterion in CRITERIA:
        while True:
            try:
                raw = input(f"  {criterion['name']} ({criterion['weight']:.0%}): ")
                val = float(raw)
                if 0.0 <= val <= 10.0:
                    data[criterion["name"]] = val
                    break
                print("    Score must be between 0 and 10.")
            except (ValueError, EOFError):
                print("    Enter a number between 0 and 10.")
    return data


def main() -> None:
    args = sys.argv[1:]
    json_output = "--json" in args
    file_args = [a for a in args if not a.startswith("-")]

    if file_args:
        path = Path(file_args[0])
        if not path.exists():
            print(f"Error: File not found: {path}", file=sys.stderr)
            sys.exit(1)
        data = parse_yaml_simple(path.read_text(encoding="utf-8"))
    else:
        if json_output:
            print("Error: --json requires an input file", file=sys.stderr)
            sys.exit(1)
        data = interactive_scoring()

    results = score_from_dict(data)
    composite = sum(r.weighted for r in results)
    grade = get_grade(composite)

    if json_output:
        output = {
            "skill": "financial-model-v1",
            "criteria": [
                {"name": r.name, "weight": r.weight, "score": r.score,
                 "weighted": round(r.weighted, 2)}
                for r in results
            ],
            "composite_score": round(composite, 2),
            "grade": grade["grade"],
            "label": grade["label"],
            "recommended_action": grade["action"],
            "weakest_criterion": min(results, key=lambda r: r.score).name,
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"\n{'=' * 50}")
        print("FINANCIAL MODEL V1 — SCORE REPORT")
        print(f"{'=' * 50}\n")
        for r in results:
            bar = "█" * int(r.score) + "░" * (10 - int(r.score))
            print(f"  {r.name:<30} {bar} {r.score:>5.1f} × {r.weight:.0%} = {r.weighted:.2f}")
        print(f"\n  {'Composite Score:':<30} {composite:.2f} / 10.00")
        print(f"  {'Grade:':<30} {grade['grade']} — {grade['label']}")
        print(f"  {'Recommended Action:':<30} {grade['action']}")
        weakest = min(results, key=lambda r: r.score)
        print(f"\n  Priority improvement: {weakest.name} (scored {weakest.score:.1f})")


if __name__ == "__main__":
    main()
