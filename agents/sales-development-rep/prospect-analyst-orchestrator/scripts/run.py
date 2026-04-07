#!/usr/bin/env python3
"""
run.py — Orchestrate prospect analysis by aggregating company research, qualification,
and decision-maker mapping into a ranked prospect intelligence report.

Usage:
    echo '<json>' | python3 run.py
    python3 run.py < input.json
    python3 run.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# Composite score weights for final prospect ranking
RANKING_WEIGHTS = {
    "research_confidence": 0.30,   # company-researcher confidence score
    "qualification_score": 0.50,   # lead-qualifier BANT/MEDDIC score
    "accessibility_score": 0.20,   # decision-maker accessibility (1-10)
}

# Grade bands for composite prospect rank
GRADE_BANDS = [
    (8.0, "A", "Priority — begin outreach immediately"),
    (6.0, "B", "Strong candidate — include in next campaign wave"),
    (4.0, "C", "Nurture — revisit after trigger event"),
    (0.0, "D", "Deprioritize — insufficient signals for outbound ROI"),
]

# Cooling off period (days)
COOLING_OFF_DAYS = 90


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    if "prospects" not in data:
        errors.append("Missing required field: prospects")
        return errors
    for i, p in enumerate(data["prospects"]):
        for f in ["name", "research_confidence_pct", "qualification_score", "accessibility_score"]:
            if f not in p:
                errors.append(f"prospects[{i}] missing field: {f}")
        if "qualification_score" in p and not (0 <= p["qualification_score"] <= 10):
            errors.append(f"prospects[{i}].qualification_score must be 0-10")
        if "accessibility_score" in p and not (1 <= p["accessibility_score"] <= 10):
            errors.append(f"prospects[{i}].accessibility_score must be 1-10")
    return errors


def assign_grade(score: float) -> tuple[str, str]:
    for threshold, grade, action in GRADE_BANDS:
        if score >= threshold:
            return grade, action
    return "D", "Deprioritize"


def rank_prospects(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    prospects = data["prospects"]
    ranked = []
    for p in prospects:
        # Normalize research_confidence_pct to 0-10 scale
        research_norm = p["research_confidence_pct"] / 10.0
        qual = p["qualification_score"]
        access = p["accessibility_score"]

        composite = (
            research_norm * RANKING_WEIGHTS["research_confidence"]
            + qual * RANKING_WEIGHTS["qualification_score"]
            + access * RANKING_WEIGHTS["accessibility_score"]
        )

        # Penalize prospects in cooling-off
        days_since = p.get("days_since_last_contact", 999)
        cooling_off = days_since < COOLING_OFF_DAYS
        if cooling_off:
            composite = min(composite, 3.9)

        composite = round(composite, 2)
        grade, action = assign_grade(composite)

        ranked.append({
            "name": p["name"],
            "composite_score": composite,
            "component_scores": {
                "research_confidence_pct": p["research_confidence_pct"],
                "qualification_score": qual,
                "accessibility_score": access,
            },
            "grade": grade,
            "recommended_action": action,
            "cooling_off": cooling_off,
            "recommended_sequence": p.get("recommended_sequence", ""),
            "entry_point_contact": p.get("entry_point_contact", ""),
        })

    ranked.sort(key=lambda x: x["composite_score"], reverse=True)
    for i, p in enumerate(ranked):
        p["rank"] = i + 1

    grade_counts = {}
    for p in ranked:
        g = p["grade"]
        grade_counts[g] = grade_counts.get(g, 0) + 1

    result = {
        "territory": data.get("territory_name", "Unspecified"),
        "total_prospects": len(ranked),
        "grade_summary": grade_counts,
        "ranked_prospects": ranked,
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = rank_prospects(data)
    output = json.dumps(result, indent=2)
    args = sys.argv[1:]
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(output + "\n", encoding="utf-8")
        else:
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
