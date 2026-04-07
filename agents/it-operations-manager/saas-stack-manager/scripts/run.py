#!/usr/bin/env python3
"""
run.py — Manage SaaS stack: spend visibility, utilisation audit, and renewal planning.

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

# Tool categories
TOOL_CATEGORIES = [
    "communication", "engineering", "product", "sales", "marketing",
    "finance", "hr", "security", "analytics", "design", "legal", "support",
]

# Utilisation thresholds
LOW_UTILISATION_THRESHOLD = 0.40  # <40% of licensed seats active
MEDIUM_UTILISATION_THRESHOLD = 0.70

# Renewal lead time alert (days)
RENEWAL_ALERT_DAYS = 90

# Cost tiers
COST_TIER_HIGH = 10000  # $/year
COST_TIER_MEDIUM = 2000  # $/year


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "tools" not in data or not isinstance(data["tools"], list):
        errors.append("Missing required field: tools (list of SaaS tool records)")
    return errors


def run_saas_audit(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    tools = data["tools"]
    action = data.get("action", "audit")

    # Process tools
    processed = []
    low_utilisation = []
    renewal_soon = []
    total_annual_spend = 0
    by_category: dict[str, list] = {}

    for tool in tools:
        licensed_seats = tool.get("licensed_seats", 0)
        active_seats = tool.get("active_seats", licensed_seats)
        utilisation_rate = round(active_seats / licensed_seats, 2) if licensed_seats > 0 else 1.0
        annual_cost = tool.get("annual_cost_usd", 0)
        days_to_renewal = tool.get("days_to_renewal", 365)
        category = tool.get("category", "other")
        is_low = utilisation_rate < LOW_UTILISATION_THRESHOLD
        is_renewal_soon = 0 < days_to_renewal <= RENEWAL_ALERT_DAYS

        cost_per_active_seat = round(annual_cost / active_seats) if active_seats > 0 else 0
        wasted_cost = round((licensed_seats - active_seats) * (annual_cost / licensed_seats)) if licensed_seats > 0 else 0

        entry = {
            "tool_name": tool["tool_name"],
            "category": category,
            "licensed_seats": licensed_seats,
            "active_seats": active_seats,
            "utilisation_rate": utilisation_rate,
            "utilisation_label": (
                "LOW" if is_low
                else "MEDIUM" if utilisation_rate < MEDIUM_UTILISATION_THRESHOLD
                else "GOOD"
            ),
            "annual_cost_usd": annual_cost,
            "cost_per_active_seat_usd": cost_per_active_seat,
            "wasted_seat_cost_usd": wasted_cost,
            "days_to_renewal": days_to_renewal,
            "renewal_action": "REVIEW_BEFORE_RENEWAL" if is_renewal_soon else "MONITOR",
            "owner": tool.get("owner", "IT"),
            "notes": tool.get("notes", ""),
        }
        processed.append(entry)
        total_annual_spend += annual_cost
        by_category.setdefault(category, []).append(entry)

        if is_low and licensed_seats > 1:
            low_utilisation.append(entry)
        if is_renewal_soon:
            renewal_soon.append(entry)

    # Sort by annual cost desc
    processed.sort(key=lambda x: x["annual_cost_usd"], reverse=True)

    # Compute potential savings from right-sizing low-utilisation tools
    potential_savings = sum(t["wasted_seat_cost_usd"] for t in low_utilisation)

    # Category spend summary
    category_spend = []
    for cat, cat_tools in sorted(by_category.items()):
        cat_spend = sum(t["annual_cost_usd"] for t in cat_tools)
        category_spend.append({"category": cat, "tools": len(cat_tools), "annual_spend_usd": cat_spend})
    category_spend.sort(key=lambda x: x["annual_spend_usd"], reverse=True)

    return {
        "error": None,
        "result": {
            "company": company,
            "action": action,
            "total_tools": len(tools),
            "total_annual_spend_usd": total_annual_spend,
            "low_utilisation_tools": len(low_utilisation),
            "renewal_due_soon": len(renewal_soon),
            "potential_savings_usd": potential_savings,
            "tools": processed,
            "low_utilisation_list": low_utilisation,
            "renewal_soon_list": renewal_soon,
            "category_spend": category_spend,
            "summary": (
                f"SaaS stack for {company}: {len(tools)} tools, ${total_annual_spend:,.0f}/year total spend. "
                f"{len(low_utilisation)} underutilised tool(s), ${potential_savings:,.0f} potential savings. "
                f"{len(renewal_soon)} renewal(s) due within {RENEWAL_ALERT_DAYS} days."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_saas_audit(data)
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
