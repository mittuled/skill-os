#!/usr/bin/env python3
"""
run.py — Run the board meeting preparation workflow, tracking materials and logistics.

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

# Standard board deck sections with owners
BOARD_DECK_SECTIONS = [
    {"section": "Executive Summary", "owner": "CEO"},
    {"section": "KPI Dashboard", "owner": "CFO"},
    {"section": "Financial Review (P&L, burn, runway)", "owner": "CFO"},
    {"section": "Product Update", "owner": "CPO"},
    {"section": "Engineering Update", "owner": "CTO"},
    {"section": "Go-to-Market Update", "owner": "CBO"},
    {"section": "Strategic Discussion Topics", "owner": "CEO"},
    {"section": "Consent Items", "owner": "General Counsel"},
]

# Days before meeting for distribution (best practice)
DISTRIBUTION_TARGET_DAYS = 5


def validate_input(data: dict) -> list[str]:
    errors = []
    if "meeting_date" not in data:
        errors.append("Missing required field: meeting_date")
    if "section_statuses" not in data or not isinstance(data["section_statuses"], dict):
        errors.append("Missing required field: section_statuses (dict)")
    return errors


def run_board_prep(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    meeting_date = data["meeting_date"]
    statuses = data["section_statuses"]
    agenda = data.get("agenda_items", [])
    directors = data.get("directors", [])
    logistics = data.get("logistics", {})
    notes = data.get("notes", {})

    section_results = []
    missing_sections = []
    complete_count = 0

    for s in BOARD_DECK_SECTIONS:
        key = s["section"].lower().replace(" ", "_").replace("(", "").replace(")", "").replace(",", "")
        status = statuses.get(key, "pending")
        if status == "complete":
            complete_count += 1
        else:
            missing_sections.append({"section": s["section"], "owner": s["owner"], "status": status})

        section_results.append({
            "section": s["section"],
            "owner": s["owner"],
            "status": status,
            "note": notes.get(key, ""),
        })

    total = len(BOARD_DECK_SECTIONS)
    pct = round((complete_count / total) * 100)

    if complete_count == total:
        overall = "READY_FOR_DISTRIBUTION"
    elif missing_sections:
        overall = "MATERIALS_INCOMPLETE"
    else:
        overall = "IN_PROGRESS"

    return {
        "error": None,
        "result": {
            "meeting_date": meeting_date,
            "directors": directors,
            "overall_status": overall,
            "sections_complete": complete_count,
            "sections_total": total,
            "percent_complete": pct,
            "section_results": section_results,
            "missing_sections": missing_sections,
            "agenda_items": agenda,
            "logistics": logistics,
            "distribution_target": f"At least {DISTRIBUTION_TARGET_DAYS} business days before meeting",
            "summary": (
                f"Board prep for {meeting_date}: {pct}% complete. "
                f"{len(missing_sections)} section(s) outstanding. "
                f"Status: {overall}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_board_prep(data)
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
