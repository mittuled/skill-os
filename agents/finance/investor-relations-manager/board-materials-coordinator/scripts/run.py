#!/usr/bin/env python3
"""
run.py — Coordinate board meeting materials preparation and distribution.

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

# Standard board materials sections with default owners
STANDARD_SECTIONS = [
    {"key": "executive_summary", "label": "Executive Summary", "default_owner": "CEO", "required": True},
    {"key": "financial_review", "label": "Financial Review", "default_owner": "CFO", "required": True},
    {"key": "kpi_dashboard", "label": "KPI Dashboard", "default_owner": "CFO", "required": True},
    {"key": "product_update", "label": "Product Update", "default_owner": "CPO", "required": True},
    {"key": "engineering_update", "label": "Engineering Update", "default_owner": "CTO", "required": False},
    {"key": "sales_update", "label": "Sales & GTM Update", "default_owner": "CBO / VP Sales", "required": True},
    {"key": "strategy_discussion", "label": "Strategic Discussion Topics", "default_owner": "CEO / Board", "required": False},
    {"key": "consent_items", "label": "Consent Items", "default_owner": "General Counsel", "required": False},
    {"key": "appendix", "label": "Appendix", "default_owner": "IR Manager", "required": False},
]

# Distribution lead time target (business days before meeting)
DISTRIBUTION_LEAD_DAYS = 5

# Valid section statuses
VALID_STATUSES = ["complete", "in_progress", "pending", "not_applicable"]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "meeting_date" not in data:
        errors.append("Missing required field: meeting_date")
    if "sections" not in data or not isinstance(data["sections"], list):
        errors.append("Missing required field: sections (list of section status objects)")
    return errors


def run_materials_coordinator(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    meeting_date = data["meeting_date"]
    sections_input = data["sections"]
    directors = data.get("directors", [])
    logistics = data.get("logistics", {})
    current_date = data.get("current_date", "")

    # Index submitted sections
    sections_by_key = {s.get("key", ""): s for s in sections_input}

    # Build complete section list
    section_results = []
    complete_count = 0
    incomplete_required = []
    all_incomplete = []

    for std in STANDARD_SECTIONS:
        submitted = sections_by_key.get(std["key"], {})
        status = submitted.get("status", "pending")
        if status not in VALID_STATUSES:
            status = "pending"
        owner = submitted.get("owner", std["default_owner"])
        notes = submitted.get("notes", "")
        is_applicable = status != "not_applicable"
        is_complete = status == "complete"

        if is_complete and is_applicable:
            complete_count += 1
        if std["required"] and not is_complete and is_applicable:
            incomplete_required.append(std["label"])
        if not is_complete and is_applicable:
            all_incomplete.append({
                "section": std["label"],
                "owner": owner,
                "status": status,
                "required": std["required"],
                "notes": notes,
            })

        section_results.append({
            "section": std["label"],
            "key": std["key"],
            "required": std["required"],
            "owner": owner,
            "status": status,
            "notes": notes,
        })

    applicable = [s for s in section_results if s["status"] != "not_applicable"]
    total_applicable = len(applicable)
    progress_pct = round(complete_count / total_applicable * 100) if total_applicable else 0

    if incomplete_required:
        overall_status = "INCOMPLETE"
    elif progress_pct == 100:
        overall_status = "READY_TO_DISTRIBUTE"
    elif progress_pct >= 75:
        overall_status = "NEAR_COMPLETE"
    else:
        overall_status = "IN_PROGRESS"

    return {
        "error": None,
        "result": {
            "company": company,
            "meeting_date": meeting_date,
            "current_date": current_date,
            "distribution_lead_time_days": DISTRIBUTION_LEAD_DAYS,
            "overall_status": overall_status,
            "progress_pct": progress_pct,
            "complete_sections": complete_count,
            "total_applicable_sections": total_applicable,
            "sections": section_results,
            "incomplete_required_sections": incomplete_required,
            "all_incomplete_sections": all_incomplete,
            "directors": directors,
            "logistics": logistics,
            "summary": (
                f"Board materials for {company} (meeting: {meeting_date}): "
                f"{overall_status}. {progress_pct}% complete ({complete_count}/{total_applicable} sections). "
                + (f"{len(incomplete_required)} required section(s) outstanding: {', '.join(incomplete_required)}."
                   if incomplete_required else "All required sections complete.")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_materials_coordinator(data)
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
