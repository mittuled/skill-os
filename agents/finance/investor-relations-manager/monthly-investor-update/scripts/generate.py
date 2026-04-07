#!/usr/bin/env python3
"""
generate.py — Generate a monthly investor update email.

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

# Standard investor update sections
REQUIRED_SECTIONS = ["highlights", "key_metrics", "challenges", "asks", "outlook"]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "month" not in data:
        errors.append("Missing required field: month (e.g. 'March 2026')")
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    for section in REQUIRED_SECTIONS:
        if section not in data:
            errors.append(f"Missing required field: {section}")
    if "challenges" in data and (not isinstance(data["challenges"], list) or len(data["challenges"]) == 0):
        errors.append("challenges must be a non-empty list — always include at least one lowlight")
    if "highlights" in data and len(data.get("highlights", [])) > 3:
        errors.append("highlights should contain at most 3 items")
    return errors


def generate_investor_update(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    month = data["month"]
    company = data["company_name"]
    highlights = data.get("highlights", [])
    metrics = data.get("key_metrics", {})
    challenges = data.get("challenges", [])
    asks = data.get("asks", [])
    outlook = data.get("outlook", "")
    subject_prefix = f"{company} — {month} Investor Update"

    return {
        "error": None,
        "result": {
            "subject": subject_prefix,
            "month": month,
            "company": company,
            "sections": {
                "highlights": highlights,
                "key_metrics": metrics,
                "challenges": challenges,
                "asks": asks,
                "outlook": outlook,
            },
            "word_count_guidance": "Target 400-600 words for the full update body",
            "distribution_checklist": [
                "Verify all metrics against source data",
                "CEO review for tone",
                "Send to all investors on distribution list",
                "Track delivery and open rates",
            ],
            "summary": (
                f"{month} investor update for {company}. "
                f"{len(highlights)} highlight(s), "
                f"{len(challenges)} challenge(s), "
                f"{len(asks)} ask(s)."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_investor_update(data)
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
