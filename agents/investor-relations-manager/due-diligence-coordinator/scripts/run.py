#!/usr/bin/env python3
"""
run.py — Coordinate due diligence requests, assign owners, and track completion.

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

# Standard diligence categories with default owners
DILIGENCE_CATEGORIES = {
    "corporate": {"label": "Corporate & Legal", "default_owner": "General Counsel"},
    "financials": {"label": "Financials", "default_owner": "CFO"},
    "commercial": {"label": "Commercial & Sales", "default_owner": "VP Sales / CEO"},
    "product_tech": {"label": "Product & Technology", "default_owner": "CTO"},
    "team_hr": {"label": "Team & HR", "default_owner": "COO / CEO"},
    "ip": {"label": "Intellectual Property", "default_owner": "General Counsel"},
    "regulatory": {"label": "Regulatory & Compliance", "default_owner": "General Counsel / COO"},
    "customer": {"label": "Customer References", "default_owner": "VP Customer Success"},
    "market": {"label": "Market & Competitive", "default_owner": "CEO / CPO"},
}

# Item statuses
VALID_STATUSES = ["pending", "in_progress", "complete", "blocked", "not_applicable"]

# Completion thresholds
COMPLETE_THRESHOLD = 85
NEAR_COMPLETE_THRESHOLD = 65


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "investor_name" not in data:
        errors.append("Missing required field: investor_name")
    if "items" not in data or not isinstance(data["items"], list) or not data["items"]:
        errors.append("Missing required field: items (non-empty list of diligence items)")
    return errors


def run_diligence_tracker(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    investor = data["investor_name"]
    items = data["items"]
    target_close_date = data.get("target_close_date", "")

    # Process items
    processed_items = []
    by_category: dict[str, list] = {}
    overdue_items = []
    blocked_items = []

    for item in items:
        category = item.get("category", "corporate")
        status = item.get("status", "pending")
        if status not in VALID_STATUSES:
            status = "pending"
        default_owner = DILIGENCE_CATEGORIES.get(category, {}).get("default_owner", "CEO")
        owner = item.get("owner", default_owner)
        days_outstanding = item.get("days_outstanding", 0)
        is_overdue = days_outstanding > 7 and status in ("pending", "in_progress")
        processed = {
            "item": item["item"],
            "category": category,
            "category_label": DILIGENCE_CATEGORIES.get(category, {}).get("label", category),
            "owner": owner,
            "status": status,
            "days_outstanding": days_outstanding,
            "overdue": is_overdue,
            "notes": item.get("notes", ""),
        }
        processed_items.append(processed)
        by_category.setdefault(category, []).append(processed)
        if is_overdue:
            overdue_items.append(processed)
        if status == "blocked":
            blocked_items.append(processed)

    # Compute completion stats
    applicable = [i for i in processed_items if i["status"] != "not_applicable"]
    complete = [i for i in applicable if i["status"] == "complete"]
    completion_pct = round(len(complete) / len(applicable) * 100) if applicable else 0

    if completion_pct >= COMPLETE_THRESHOLD:
        overall_status = "NEAR_CLOSE"
    elif completion_pct >= NEAR_COMPLETE_THRESHOLD:
        overall_status = "IN_PROGRESS"
    else:
        overall_status = "EARLY_STAGE"

    # Category summaries
    category_summaries = []
    for cat_key, cat_items in by_category.items():
        cat_complete = sum(1 for i in cat_items if i["status"] == "complete")
        cat_applicable = [i for i in cat_items if i["status"] != "not_applicable"]
        cat_pct = round(cat_complete / len(cat_applicable) * 100) if cat_applicable else 100
        category_summaries.append({
            "category": DILIGENCE_CATEGORIES.get(cat_key, {}).get("label", cat_key),
            "total": len(cat_items),
            "complete": cat_complete,
            "completion_pct": cat_pct,
        })

    return {
        "error": None,
        "result": {
            "company": company,
            "investor": investor,
            "target_close_date": target_close_date,
            "overall_status": overall_status,
            "completion_pct": completion_pct,
            "total_items": len(processed_items),
            "complete_items": len(complete),
            "overdue_items": overdue_items,
            "blocked_items": blocked_items,
            "category_summaries": category_summaries,
            "all_items": processed_items,
            "summary": (
                f"Diligence for {company} / {investor}: {completion_pct}% complete "
                f"({len(complete)}/{len(applicable)} items). Status: {overall_status}. "
                f"{len(overdue_items)} overdue, {len(blocked_items)} blocked."
                + (f" Target close: {target_close_date}." if target_close_date else "")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_diligence_tracker(data)
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
