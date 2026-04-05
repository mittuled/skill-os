#!/usr/bin/env python3
"""
generate.py — Generate a structured sales playbook with qualification, discovery, and closing components.

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

# Minimum content requirements per playbook section
MIN_DISCOVERY_QUESTIONS = 10
MIN_OBJECTIONS_COVERED = 10
MIN_BATTLE_CARDS = 2

# Sections required in a complete playbook
REQUIRED_SECTIONS = [
    "qualification_criteria",
    "discovery_questions",
    "battle_cards",
    "objection_handler",
    "closing_playbook",
]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["product_name", "icp_segment", "motion_type"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def assess_section_completeness(data: dict) -> dict:
    discovery_q_count = len(data.get("discovery_questions", []))
    objection_count = len(data.get("objections", []))
    battle_card_count = len(data.get("battle_cards", []))

    sections = {}
    for section in REQUIRED_SECTIONS:
        if section == "discovery_questions":
            complete = discovery_q_count >= MIN_DISCOVERY_QUESTIONS
            sections[section] = {
                "complete": complete,
                "count": discovery_q_count,
                "minimum": MIN_DISCOVERY_QUESTIONS,
            }
        elif section == "objection_handler":
            complete = objection_count >= MIN_OBJECTIONS_COVERED
            sections[section] = {
                "complete": complete,
                "count": objection_count,
                "minimum": MIN_OBJECTIONS_COVERED,
            }
        elif section == "battle_cards":
            complete = battle_card_count >= MIN_BATTLE_CARDS
            sections[section] = {
                "complete": complete,
                "count": battle_card_count,
                "minimum": MIN_BATTLE_CARDS,
            }
        else:
            provided = bool(data.get(section))
            sections[section] = {"complete": provided, "provided": provided}

    return sections


def generate_playbook(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    sections = assess_section_completeness(data)
    incomplete_sections = [s for s, v in sections.items() if not v.get("complete")]

    completeness_pct = round(
        (len(REQUIRED_SECTIONS) - len(incomplete_sections)) / len(REQUIRED_SECTIONS) * 100
    )

    if incomplete_sections:
        verdict = "DRAFT"
        recommendation = f"Playbook incomplete — {len(incomplete_sections)} section(s) need more content before publishing"
    else:
        verdict = "READY_FOR_REVIEW"
        recommendation = "Playbook complete — schedule review with VP Sales and 2 senior reps before publishing"

    result = {
        "product": data["product_name"],
        "icp_segment": data["icp_segment"],
        "motion_type": data["motion_type"],
        "version": data.get("version", "1.0"),
        "verdict": verdict,
        "recommendation": recommendation,
        "completeness_pct": completeness_pct,
        "sections": sections,
        "incomplete_sections": incomplete_sections,
        "qualification_criteria": data.get("qualification_criteria", {}),
        "discovery_questions": data.get("discovery_questions", []),
        "battle_cards": data.get("battle_cards", []),
        "objections": data.get("objections", []),
        "closing_playbook": data.get("closing_playbook", {}),
        "review_required": ["VP Sales", "2 senior reps"],
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_playbook(data)
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
