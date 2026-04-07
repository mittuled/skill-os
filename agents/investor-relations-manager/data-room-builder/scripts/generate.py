#!/usr/bin/env python3
"""
generate.py — Build and audit an investor data room for Series A/B diligence.

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

# Full diligence data room sections by priority
DATA_ROOM_SECTIONS = {
    "corporate": {
        "label": "Corporate & Legal",
        "docs": [
            "Certificate of incorporation and amendments",
            "Bylaws",
            "Board minutes and consents",
            "Stockholder agreements",
            "Cap table (fully diluted)",
            "Stock option plan and agreements",
            "409A valuation",
        ],
        "priority": "critical",
    },
    "financials": {
        "label": "Financials",
        "docs": [
            "Audited financials (if applicable)",
            "Management accounts (last 12 months)",
            "Financial model (3-year projection)",
            "ARR/MRR bridge",
            "Burn rate and runway analysis",
            "Revenue recognition policy",
        ],
        "priority": "critical",
    },
    "commercial": {
        "label": "Commercial",
        "docs": [
            "Top 10 customer contracts",
            "Standard customer agreement template",
            "Sales pipeline (CRM export)",
            "Churn and NRR analysis",
            "Pricing schedule",
        ],
        "priority": "critical",
    },
    "product_tech": {
        "label": "Product & Technology",
        "docs": [
            "Product roadmap (12-month)",
            "Architecture overview",
            "Security and compliance documentation",
            "Open source licence audit",
            "Penetration test results",
        ],
        "priority": "high",
    },
    "team_hr": {
        "label": "Team & HR",
        "docs": [
            "Org chart",
            "Key employee agreements",
            "Non-compete and IP assignment agreements",
            "Compensation benchmarking",
        ],
        "priority": "high",
    },
    "ip": {
        "label": "Intellectual Property",
        "docs": [
            "Patent applications and registrations",
            "Trademark registrations",
            "IP ownership confirmation",
            "Third-party IP licences",
        ],
        "priority": "high",
    },
    "regulatory": {
        "label": "Regulatory & Compliance",
        "docs": [
            "Privacy policy",
            "Terms of service",
            "GDPR / CCPA compliance documentation",
            "Relevant licences and permits",
        ],
        "priority": "medium",
    },
}

STALENESS_THRESHOLD_DAYS = 180


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "documents" not in data or not isinstance(data["documents"], list):
        errors.append("Missing required field: documents (list of {name, section, days_since_updated})")
    return errors


def generate_data_room_audit(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    documents = data["documents"]
    round_name = data.get("round_name", "Series A")

    # Index submitted documents by section
    submitted_by_section: dict[str, list[dict]] = {}
    stale_docs = []
    for doc in documents:
        section = doc.get("section", "other")
        submitted_by_section.setdefault(section, []).append(doc)
        days = doc.get("days_since_updated", 0)
        if days > STALENESS_THRESHOLD_DAYS:
            stale_docs.append({"document": doc["name"], "days_stale": days})

    # Audit each section
    section_results = []
    total_required = 0
    total_present = 0
    critical_gaps = []

    for key, section in DATA_ROOM_SECTIONS.items():
        required_docs = section["docs"]
        section_docs = submitted_by_section.get(key, [])
        submitted_names = [d["name"].lower() for d in section_docs]
        missing = [r for r in required_docs if not any(word in " ".join(submitted_names) for word in r.lower().split()[:3])]
        present = len(required_docs) - len(missing)
        pct = round(present / len(required_docs) * 100) if required_docs else 100
        total_required += len(required_docs)
        total_present += present
        if section["priority"] == "critical" and missing:
            critical_gaps.extend(missing)
        section_results.append({
            "section": section["label"],
            "priority": section["priority"],
            "completeness_pct": pct,
            "missing_documents": missing,
        })

    overall_pct = round(total_present / total_required * 100) if total_required else 0
    status = "READY" if overall_pct >= 85 and not critical_gaps else ("NEAR_READY" if overall_pct >= 65 else "INCOMPLETE")

    return {
        "error": None,
        "result": {
            "company": company,
            "round_name": round_name,
            "overall_completeness_pct": overall_pct,
            "status": status,
            "section_audit": section_results,
            "critical_gaps": critical_gaps,
            "stale_documents": stale_docs,
            "summary": (
                f"Data room for {company} ({round_name}): {overall_pct}% complete. Status: {status}. "
                f"{len(critical_gaps)} critical gap(s), {len(stale_docs)} stale document(s)."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_data_room_audit(data)
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
