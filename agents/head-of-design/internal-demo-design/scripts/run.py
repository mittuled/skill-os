#!/usr/bin/env python3
"""
run.py — Run the internal design demo preparation and summary workflow.

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

# Recommended time slots (minutes) by session section
SESSION_STRUCTURE = [
    {"section": "Problem context and user need", "minutes": 5},
    {"section": "Design rationale and key decisions", "minutes": 10},
    {"section": "Live walkthrough / prototype", "minutes": 15},
    {"section": "Open questions for audience", "minutes": 10},
    {"section": "Q&A and feedback capture", "minutes": 10},
]

# Feedback categories for synthesis
FEEDBACK_CATEGORIES = [
    "Usability concerns",
    "Visual / brand alignment",
    "Scope and edge cases",
    "Engineering feasibility flags",
    "Positive validation",
]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "demo_title" not in data:
        errors.append("Missing required field: demo_title")
    if "objectives" not in data or not isinstance(data["objectives"], list):
        errors.append("Missing required field: objectives (list)")
    if "audience" not in data or not isinstance(data["audience"], list):
        errors.append("Missing required field: audience (list)")
    return errors


def run_demo_prep(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    title = data["demo_title"]
    objectives = data["objectives"]
    audience = data["audience"]
    open_questions = data.get("open_questions", [])
    feedback_raw = data.get("feedback_notes", [])
    design_artifacts = data.get("design_artifacts", [])

    # Synthesize feedback into categories
    feedback_by_category: dict[str, list[str]] = {cat: [] for cat in FEEDBACK_CATEGORIES}
    action_items = []

    for note in feedback_raw:
        category = note.get("category", "Usability concerns")
        if category not in feedback_by_category:
            category = "Usability concerns"
        feedback_by_category[category].append(note.get("comment", ""))
        if note.get("action_item"):
            action_items.append({
                "item": note["action_item"],
                "owner": note.get("owner", "TBD"),
            })

    # Build agenda
    total_minutes = sum(s["minutes"] for s in SESSION_STRUCTURE)
    agenda = [
        {"section": s["section"], "duration_min": s["minutes"]}
        for s in SESSION_STRUCTURE
    ]

    return {
        "error": None,
        "result": {
            "demo_title": title,
            "objectives": objectives,
            "audience": audience,
            "design_artifacts": design_artifacts,
            "session_agenda": agenda,
            "total_session_minutes": total_minutes,
            "open_questions": open_questions,
            "feedback_by_category": feedback_by_category,
            "action_items": action_items,
            "summary": (
                f"Demo '{title}' prepared for {len(audience)} audience group(s). "
                f"Session: {total_minutes} min. "
                f"{len(action_items)} action item(s) identified."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_demo_prep(data)
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
