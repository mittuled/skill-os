#!/usr/bin/env python3
"""
run.py — Manage martech stack: tool audit, integration health, and renewal planning.

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

# Martech function categories
MARTECH_CATEGORIES = {
    "marketing_automation": "Marketing Automation (MAP)",
    "crm": "CRM",
    "email": "Email Platform",
    "analytics": "Analytics & Attribution",
    "ads": "Paid Advertising",
    "seo": "SEO Tools",
    "social": "Social Media Management",
    "events_webinars": "Events & Webinars",
    "content": "Content & CMS",
    "chat_conversion": "Chat & Conversion",
    "data_enrichment": "Data Enrichment",
}

# Integration status values
INTEGRATION_STATUSES = ["active", "broken", "not_integrated", "redundant"]

# Utilisation thresholds
LOW_UTILISATION = 0.40


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "tools" not in data or not isinstance(data["tools"], list):
        errors.append("Missing required field: tools (list)")
    return errors


def run_martech_audit(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    tools = data["tools"]
    action = data.get("action", "audit")

    processed = []
    integration_issues = []
    renewal_alerts = []
    low_utilisation = []
    redundant_tools = []
    total_annual_spend = 0

    category_coverage: dict[str, list] = {}

    for tool in tools:
        category = tool.get("category", "other")
        utilisation = tool.get("utilisation_rate", 1.0)
        annual_cost = tool.get("annual_cost_usd", 0)
        days_to_renewal = tool.get("days_to_renewal", 365)
        integration_status = tool.get("crm_integration_status", "not_integrated")
        is_redundant = tool.get("redundant_with", "") != ""

        total_annual_spend += annual_cost
        category_coverage.setdefault(category, []).append(tool.get("tool_name", ""))

        entry = {
            "tool_name": tool["tool_name"],
            "category": MARTECH_CATEGORIES.get(category, category),
            "annual_cost_usd": annual_cost,
            "utilisation_rate": utilisation,
            "utilisation_label": "LOW" if utilisation < LOW_UTILISATION else ("MEDIUM" if utilisation < 0.70 else "GOOD"),
            "crm_integration_status": integration_status,
            "days_to_renewal": days_to_renewal,
            "redundant_with": tool.get("redundant_with", ""),
            "owner": tool.get("owner", "Marketing Ops"),
            "notes": tool.get("notes", ""),
        }
        processed.append(entry)

        if integration_status == "broken":
            integration_issues.append(entry)
        if 0 < days_to_renewal <= 90:
            renewal_alerts.append(entry)
        if utilisation < LOW_UTILISATION:
            low_utilisation.append(entry)
        if is_redundant:
            redundant_tools.append(entry)

    # Sort by cost descending
    processed.sort(key=lambda x: x["annual_cost_usd"], reverse=True)

    # Check for coverage gaps
    covered_categories = set(category_coverage.keys())
    all_categories = set(MARTECH_CATEGORIES.keys())
    gaps = [MARTECH_CATEGORIES[c] for c in all_categories - covered_categories]

    return {
        "error": None,
        "result": {
            "company": company,
            "action": action,
            "total_tools": len(tools),
            "total_annual_spend_usd": total_annual_spend,
            "integration_issues": len(integration_issues),
            "renewal_alerts": len(renewal_alerts),
            "low_utilisation_tools": len(low_utilisation),
            "redundant_tools": len(redundant_tools),
            "coverage_gaps": gaps,
            "tools": processed,
            "integration_issue_list": integration_issues,
            "renewal_alert_list": renewal_alerts,
            "low_utilisation_list": low_utilisation,
            "redundant_tool_list": redundant_tools,
            "summary": (
                f"Martech stack for {company}: {len(tools)} tools, ${total_annual_spend:,.0f}/year. "
                f"{len(integration_issues)} integration issue(s), {len(renewal_alerts)} renewal(s) due ≤90 days, "
                f"{len(low_utilisation)} underutilised, {len(redundant_tools)} redundant."
                + (f" Coverage gaps: {', '.join(gaps[:3])}." if gaps else "")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_martech_audit(data)
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
