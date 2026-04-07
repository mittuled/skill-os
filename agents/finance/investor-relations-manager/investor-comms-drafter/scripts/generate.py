#!/usr/bin/env python3
"""
generate.py — Draft investor communications: updates, announcements, and ad hoc correspondence.

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

# Communication types and their required fields
COMM_TYPES = {
    "material_event": {
        "label": "Material Event Announcement",
        "required_fields": ["event_type", "event_description", "impact"],
        "tone": "factual and transparent",
    },
    "funding_announcement": {
        "label": "Funding Announcement",
        "required_fields": ["round_type", "amount_usd", "lead_investor"],
        "tone": "celebratory and forward-looking",
    },
    "executive_change": {
        "label": "Executive Appointment/Departure",
        "required_fields": ["person_name", "role", "change_type"],
        "tone": "professional and context-setting",
    },
    "adverse_event": {
        "label": "Adverse Event Disclosure",
        "required_fields": ["event_description", "impact", "response_plan"],
        "tone": "direct, transparent, and solution-focused",
    },
    "quarterly_update": {
        "label": "Quarterly Business Update",
        "required_fields": ["quarter", "highlights", "metrics"],
        "tone": "balanced — highlights and challenges",
    },
}

# Distribution audience types
AUDIENCE_TYPES = ["all_investors", "board_only", "lead_investors", "angels_only"]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "comm_type" not in data or data.get("comm_type") not in COMM_TYPES:
        errors.append(f"Missing or invalid field: comm_type ({'/'.join(COMM_TYPES.keys())})")
    if "subject" not in data:
        errors.append("Missing required field: subject (email subject line)")
    return errors


def generate_investor_comm(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    comm_type = data["comm_type"]
    comm_config = COMM_TYPES[comm_type]
    subject = data["subject"]
    audience = data.get("audience", "all_investors")
    highlights = data.get("highlights", [])
    body_notes = data.get("body_notes", "")
    metrics = data.get("metrics", [])
    asks = data.get("asks", [])
    sender_name = data.get("sender_name", "CEO")
    date = data.get("date", "")

    # Check required fields for comm type
    missing_fields = [f for f in comm_config["required_fields"] if f not in data]

    # Build structured comm
    sections = []

    # Opening paragraph
    sections.append({
        "section": "Opening",
        "content": f"[Opening paragraph — tone: {comm_config['tone']}. Lead with the most important point.]",
        "guidance": body_notes if body_notes else "State the purpose of the communication in the first sentence.",
    })

    # Highlights
    if highlights:
        sections.append({
            "section": "Highlights",
            "content": highlights,
            "guidance": "Lead with business impact, not activity.",
        })

    # Metrics
    if metrics:
        sections.append({
            "section": "Key Metrics",
            "content": metrics,
            "guidance": "Include trend direction. Flag any metric below target.",
        })

    # Asks
    if asks:
        sections.append({
            "section": "Asks",
            "content": asks,
            "guidance": "Be specific and actionable. One ask per bullet.",
        })

    # Closing
    sections.append({
        "section": "Closing",
        "content": f"— {sender_name}",
        "guidance": "Brief, warm close. Invite replies.",
    })

    distribution_note = (
        "All investors on distribution list"
        if audience == "all_investors"
        else f"Restricted distribution: {audience.replace('_', ' ')}"
    )

    return {
        "error": None,
        "result": {
            "company": company,
            "comm_type": comm_config["label"],
            "subject_line": subject,
            "audience": audience,
            "distribution_note": distribution_note,
            "date": date,
            "sections": sections,
            "missing_context": missing_fields,
            "review_checklist": [
                "CEO has reviewed and approved",
                "All metrics verified against source of truth",
                "No forward-looking statements without legal review",
                "Distribution list is current and correct",
                "Subject line is clear and specific",
            ],
            "summary": (
                f"{comm_config['label']} for {company} to {audience.replace('_', ' ')}. "
                f"Subject: '{subject}'. "
                + (f"Missing context fields: {missing_fields}." if missing_fields else "All context provided.")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_investor_comm(data)
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
