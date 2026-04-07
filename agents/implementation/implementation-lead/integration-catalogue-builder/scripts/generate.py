#!/usr/bin/env python3
"""
generate.py — Generate an integration catalogue entry with setup guide and limitations.

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

# Integration categories
INTEGRATION_CATEGORIES = [
    "CRM", "HRIS", "SSO / Identity", "Billing / Payments",
    "Email / Comms", "Analytics", "Storage", "ERP", "Other",
]

# Availability status values
VALID_STATUSES = ["GA", "Beta", "Deprecated", "Planned"]


def validate_input(data: dict) -> list[str]:
    errors = []
    required = ["integration_name", "category", "status", "prerequisites", "setup_steps"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "category" in data and data["category"] not in INTEGRATION_CATEGORIES:
        errors.append(f"Invalid category. Choose from: {INTEGRATION_CATEGORIES}")
    if "status" in data and data["status"] not in VALID_STATUSES:
        errors.append(f"Invalid status. Choose from: {VALID_STATUSES}")
    return errors


def generate_catalogue_entry(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    return {
        "error": None,
        "result": {
            "integration_name": data["integration_name"],
            "category": data["category"],
            "status": data["status"],
            "description": data.get("description", ""),
            "prerequisites": data["prerequisites"],
            "authentication_method": data.get("authentication_method", ""),
            "setup_steps": data["setup_steps"],
            "data_mapping": data.get("data_mapping", []),
            "limitations": data.get("limitations", []),
            "known_errors": data.get("known_errors", []),
            "product_versions": data.get("product_versions", "All versions"),
            "support_contact": data.get("support_contact", ""),
            "last_reviewed": data.get("last_reviewed", ""),
            "summary": (
                f"Integration '{data['integration_name']}' ({data['category']}) — "
                f"Status: {data['status']}. "
                f"{len(data['setup_steps'])} setup step(s). "
                f"{len(data.get('limitations', []))} known limitation(s)."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_catalogue_entry(data)
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
