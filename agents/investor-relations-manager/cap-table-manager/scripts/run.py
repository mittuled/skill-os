#!/usr/bin/env python3
"""
run.py — Model cap table events including dilution and ownership calculations.

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


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "shareholders" not in data or not isinstance(data["shareholders"], list):
        errors.append("Missing required field: shareholders (list)")
    return errors


def compute_cap_table(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    shareholders = data["shareholders"]
    new_round = data.get("new_round", None)
    convertibles = data.get("convertibles", [])

    # Compute existing ownership
    total_shares = sum(s.get("shares", 0) for s in shareholders)
    ownership_table = []
    for s in shareholders:
        shares = s.get("shares", 0)
        pct = round((shares / total_shares) * 100, 2) if total_shares > 0 else 0
        ownership_table.append({
            "holder": s["name"],
            "share_class": s.get("share_class", "Common"),
            "shares": shares,
            "ownership_pct": pct,
        })

    # Model new round dilution if provided
    post_money_table = None
    if new_round:
        new_shares = new_round.get("new_shares", 0)
        post_total = total_shares + new_shares
        post_money_table = []
        for s in shareholders:
            shares = s.get("shares", 0)
            pct = round((shares / post_total) * 100, 2) if post_total > 0 else 0
            post_money_table.append({
                "holder": s["name"],
                "shares": shares,
                "post_money_ownership_pct": pct,
            })
        # Add new investor
        new_investor_pct = round((new_shares / post_total) * 100, 2)
        post_money_table.append({
            "holder": new_round.get("investor_name", "New Investor"),
            "shares": new_shares,
            "post_money_ownership_pct": new_investor_pct,
        })

    return {
        "error": None,
        "result": {
            "company": company,
            "total_shares_outstanding": total_shares,
            "ownership_table": ownership_table,
            "convertible_instruments": convertibles,
            "dilution_model": post_money_table,
            "new_round": new_round,
            "summary": (
                f"Cap table for {company}: {len(shareholders)} holder(s), "
                f"{total_shares:,} shares outstanding."
                + (f" Post-round total: {total_shares + (new_round or {}).get('new_shares', 0):,} shares." if new_round else "")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = compute_cap_table(data)
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
