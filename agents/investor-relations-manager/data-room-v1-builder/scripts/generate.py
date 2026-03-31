#!/usr/bin/env python3
"""
generate.py — Generate a first investor data room structure for seed-stage fundraising.

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

# Standard seed data room sections with required documents
SEED_DATA_ROOM_SECTIONS = {
    "company_overview": {
        "label": "Company Overview",
        "required_docs": ["Pitch deck", "Executive summary (2-pager)", "Company overview memo"],
        "priority": "critical",
    },
    "financials": {
        "label": "Financials",
        "required_docs": ["Financial model (12-month)", "Historical P&L", "Bank statements (last 3 months)", "Burn and runway summary"],
        "priority": "critical",
    },
    "legal": {
        "label": "Legal",
        "required_docs": ["Certificate of incorporation", "Cap table", "Founder agreements and vesting schedules", "IP assignment agreements"],
        "priority": "critical",
    },
    "product": {
        "label": "Product",
        "required_docs": ["Product roadmap", "Demo video or live demo link", "User metrics dashboard"],
        "priority": "high",
    },
    "team": {
        "label": "Team",
        "required_docs": ["Team bios and LinkedIn profiles", "Org chart", "Advisory board list"],
        "priority": "high",
    },
    "traction": {
        "label": "Traction & Metrics",
        "required_docs": ["Revenue and ARR history", "Key metrics (DAU/MAU, NRR, churn)", "Customer references list"],
        "priority": "high",
    },
    "market": {
        "label": "Market",
        "required_docs": ["Market sizing analysis", "Competitive landscape", "Go-to-market strategy"],
        "priority": "medium",
    },
}

# Completeness thresholds
COMPLETENESS_READY = 80
COMPLETENESS_PARTIAL = 50


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "documents_available" not in data or not isinstance(data["documents_available"], list):
        errors.append("Missing required field: documents_available (list of document names)")
    return errors


def generate_data_room(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    docs_available = [d.lower() for d in data.get("documents_available", [])]
    fundraising_stage = data.get("fundraising_stage", "seed")

    # Build section status
    sections = []
    total_required = 0
    total_available = 0
    critical_missing = []

    for key, section in SEED_DATA_ROOM_SECTIONS.items():
        required = section["required_docs"]
        available = []
        missing = []
        for doc in required:
            if any(word in docs_available for word in doc.lower().split()):
                available.append(doc)
            else:
                missing.append(doc)
        pct = round(len(available) / len(required) * 100) if required else 100
        total_required += len(required)
        total_available += len(available)
        if section["priority"] == "critical" and missing:
            critical_missing.extend(missing)
        sections.append({
            "section": section["label"],
            "priority": section["priority"],
            "required_count": len(required),
            "available_count": len(available),
            "completeness_pct": pct,
            "missing_documents": missing,
        })

    overall_pct = round(total_available / total_required * 100) if total_required else 0

    if overall_pct >= COMPLETENESS_READY:
        readiness = "READY_TO_SHARE"
    elif overall_pct >= COMPLETENESS_PARTIAL:
        readiness = "PARTIALLY_READY"
    else:
        readiness = "NOT_READY"

    return {
        "error": None,
        "result": {
            "company": company,
            "fundraising_stage": fundraising_stage,
            "overall_completeness_pct": overall_pct,
            "readiness": readiness,
            "sections": sections,
            "critical_missing_documents": critical_missing,
            "total_required_documents": total_required,
            "total_available_documents": total_available,
            "summary": (
                f"Data room for {company} ({fundraising_stage}): {overall_pct}% complete "
                f"({total_available}/{total_required} documents). Status: {readiness}."
                + (f" {len(critical_missing)} critical document(s) missing." if critical_missing else "")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_data_room(data)
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
