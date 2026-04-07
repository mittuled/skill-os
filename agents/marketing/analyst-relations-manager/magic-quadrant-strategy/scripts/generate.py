#!/usr/bin/env python3
"""
generate.py — Generate a Magic Quadrant / Forrester Wave submission strategy and evidence package.

Usage:
    echo '<json>' | python3 generate.py
    python3 generate.py < input.json
    python3 generate.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

EVALUATION_TYPES = ["gartner_magic_quadrant", "forrester_wave", "idc_marketscape", "g2_grid"]

MQ_AXES = {
    "gartner_magic_quadrant": {"x_axis": "Completeness of Vision", "y_axis": "Ability to Execute"},
    "forrester_wave": {"x_axis": "Strategy", "y_axis": "Current Offering"},
    "idc_marketscape": {"x_axis": "Strategies", "y_axis": "Capabilities"},
}

EVIDENCE_CATEGORIES = [
    "product_capabilities",
    "customer_references",
    "market_traction",
    "vision_and_roadmap",
    "partner_ecosystem",
    "financial_viability",
    "geographic_coverage",
]

REQUIRED_FIELDS = ["evaluation_type", "evaluation_cycle", "submission_deadline", "evidence"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "evaluation_type" in data and data["evaluation_type"] not in EVALUATION_TYPES:
        errors.append(f"evaluation_type must be one of {EVALUATION_TYPES}")
    return errors


def generate_strategy(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    eval_type = data["evaluation_type"]
    axes = MQ_AXES.get(eval_type, {"x_axis": "Strategy", "y_axis": "Execution"})
    evidence = data["evidence"]

    # Score evidence completeness
    evidence_score = {}
    for category in EVIDENCE_CATEGORIES:
        present = category in evidence and bool(evidence[category])
        evidence_score[category] = {"present": present, "strength": evidence.get(category, {}).get("strength", "unknown") if present else "missing"}

    missing = [cat for cat, v in evidence_score.items() if not v["present"]]
    completeness_pct = round((len(EVIDENCE_CATEGORIES) - len(missing)) / len(EVIDENCE_CATEGORIES) * 100)

    # Strategy recommendations
    positioning_strategy = []
    if evidence.get("customer_references", {}).get("count", 0) < 5:
        positioning_strategy.append("CRITICAL: Recruit at least 5 referenceable customers for analyst interviews — this is the highest-weighted evaluation criterion")
    if not evidence.get("vision_and_roadmap"):
        positioning_strategy.append("Develop a 24-month vision narrative that maps product roadmap to analyst-defined market direction")

    return {
        "error": None,
        "result": {
            "evaluation_type": eval_type,
            "evaluation_cycle": data["evaluation_cycle"],
            "submission_deadline": data["submission_deadline"],
            "axes": axes,
            "target_quadrant_position": data.get("target_position", "Visionaries or Challengers"),
            "evidence_completeness_pct": completeness_pct,
            "evidence_gaps": missing,
            "evidence_summary": evidence_score,
            "positioning_strategy": positioning_strategy,
            "submission_timeline": [
                {"weeks_before_deadline": 8, "task": "Complete first draft of written responses"},
                {"weeks_before_deadline": 6, "task": "Confirm customer reference list (5+ accounts)"},
                {"weeks_before_deadline": 4, "task": "Internal review and legal/exec approval"},
                {"weeks_before_deadline": 2, "task": "Final submission package ready"},
                {"weeks_before_deadline": 0, "task": "Submit via analyst portal"},
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_strategy(data)
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
