#!/usr/bin/env python3
"""
generate.py — Generate a structured customer requirements document from discovery inputs.

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

# Standard requirements document sections
REQUIREMENTS_SECTIONS = [
    "functional_requirements",
    "technical_environment",
    "integration_requirements",
    "data_migration_requirements",
    "user_and_access_requirements",
    "acceptance_criteria",
]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "customer_name" not in data:
        errors.append("Missing required field: customer_name")
    if "discovery_notes" not in data or not isinstance(data["discovery_notes"], dict):
        errors.append("Missing required field: discovery_notes (dict with requirements sections)")
    return errors


def generate_requirements_doc(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    customer = data["customer_name"]
    notes = data["discovery_notes"]
    sales_context = data.get("sales_context", {})
    open_items = data.get("open_items", [])
    sign_off_required = data.get("sign_off_required", True)

    # Build requirements sections
    sections = {}
    missing_sections = []
    for section in REQUIREMENTS_SECTIONS:
        if section in notes and notes[section]:
            sections[section] = notes[section]
        else:
            missing_sections.append(section)

    completeness_pct = round(
        (len(sections) / len(REQUIREMENTS_SECTIONS)) * 100
    )

    status = "COMPLETE" if not missing_sections and not open_items else "DRAFT"

    return {
        "error": None,
        "result": {
            "customer": customer,
            "sales_context": sales_context,
            "requirements": sections,
            "missing_sections": missing_sections,
            "open_items": open_items,
            "completeness_percent": completeness_pct,
            "status": status,
            "sign_off_required": sign_off_required,
            "summary": (
                f"Requirements document for {customer}: {completeness_pct}% complete. "
                f"{len(missing_sections)} section(s) missing. "
                f"{len(open_items)} open item(s). "
                f"Status: {status}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_requirements_doc(data)
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
