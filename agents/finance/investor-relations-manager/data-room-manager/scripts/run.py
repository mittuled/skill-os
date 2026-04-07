#!/usr/bin/env python3
"""
run.py — Manage data room access, document freshness, and access log audit.

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

# Access level definitions
ACCESS_LEVELS = {
    "full": "All sections visible",
    "limited": "Corporate, Financials, and Company Overview only",
    "nda_only": "Teaser/overview only — NDA not signed",
}

# Document staleness thresholds in days
STALENESS_THRESHOLDS = {
    "critical": 90,   # Corporate docs, cap table
    "financials": 30,  # Monthly management accounts
    "commercial": 60,  # Customer contracts, pipeline
    "standard": 180,   # Other documents
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "investors" not in data or not isinstance(data["investors"], list):
        errors.append("Missing required field: investors (list)")
    if "documents" not in data or not isinstance(data["documents"], list):
        errors.append("Missing required field: documents (list)")
    return errors


def run_data_room_management(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    investors = data["investors"]
    documents = data["documents"]
    action = data.get("action", "audit")

    # Audit investor access
    access_report = []
    nda_missing = []
    for inv in investors:
        nda_signed = inv.get("nda_signed", False)
        access_level = inv.get("access_level", "nda_only" if not nda_signed else "limited")
        if not nda_signed:
            nda_missing.append(inv["name"])
        access_report.append({
            "investor": inv["name"],
            "firm": inv.get("firm", ""),
            "nda_signed": nda_signed,
            "access_level": access_level,
            "access_description": ACCESS_LEVELS.get(access_level, "Unknown"),
            "last_viewed": inv.get("last_viewed", ""),
            "documents_viewed": inv.get("documents_viewed", 0),
        })

    # Audit document freshness
    stale_docs = []
    fresh_docs = []
    for doc in documents:
        doc_type = doc.get("type", "standard")
        threshold = STALENESS_THRESHOLDS.get(doc_type, STALENESS_THRESHOLDS["standard"])
        days_old = doc.get("days_since_updated", 0)
        status = "STALE" if days_old > threshold else "FRESH"
        entry = {
            "document": doc["name"],
            "type": doc_type,
            "days_since_updated": days_old,
            "threshold_days": threshold,
            "status": status,
        }
        if status == "STALE":
            stale_docs.append(entry)
        else:
            fresh_docs.append(entry)

    # Determine overall data room health
    if not stale_docs and not nda_missing:
        health = "HEALTHY"
    elif len(stale_docs) <= 2 and not nda_missing:
        health = "ATTENTION_NEEDED"
    else:
        health = "ACTION_REQUIRED"

    return {
        "error": None,
        "result": {
            "company": company,
            "action": action,
            "health": health,
            "access_report": access_report,
            "investors_without_nda": nda_missing,
            "stale_documents": stale_docs,
            "fresh_document_count": len(fresh_docs),
            "stale_document_count": len(stale_docs),
            "summary": (
                f"Data room for {company}: {health}. "
                f"{len(investors)} investor(s) with access, {len(nda_missing)} NDA(s) outstanding. "
                f"{len(stale_docs)} stale document(s) requiring refresh."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_data_room_management(data)
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
