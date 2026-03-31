#!/usr/bin/env python3
"""
generate.py — Prepare SAFE note agreements and model conversion scenarios.

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

# SAFE types
SAFE_TYPES = {
    "post_money": "YC Post-Money SAFE (2018) — investor ownership fixed at signing",
    "pre_money": "YC Pre-Money SAFE (pre-2018) — dilutes alongside future SAFEs",
    "mfn": "Most Favoured Nation SAFE — adopts best terms of future SAFEs",
}

# Standard YC SAFE terms reference
STANDARD_TERMS = {
    "pro_rata_rights": "Pro-rata rights on future rounds (for investors with $50K+ SAFEs, typically)",
    "information_rights": "Annual financials upon request",
    "conversion_trigger": "Priced equity round (Series A or later), change of control, or dissolution",
}

# Conversion discount impact
DISCOUNT_RATES = [0.10, 0.15, 0.20, 0.25]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "investor_name" not in data:
        errors.append("Missing required field: investor_name")
    if "principal_usd" not in data or not isinstance(data["principal_usd"], (int, float)):
        errors.append("Missing required field: principal_usd (number)")
    if "safe_type" not in data or data.get("safe_type") not in SAFE_TYPES:
        errors.append(f"Missing or invalid field: safe_type ({'/'.join(SAFE_TYPES.keys())})")
    return errors


def generate_safe(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    investor = data["investor_name"]
    principal = data["principal_usd"]
    safe_type = data["safe_type"]
    valuation_cap = data.get("valuation_cap_usd")
    discount_rate = data.get("discount_rate", 0.20)
    pro_rata = data.get("pro_rata_rights", principal >= 50000)
    date = data.get("date", "")

    # Validate discount rate
    if not (0 < discount_rate < 1):
        return {"error": ["discount_rate must be between 0 and 1 (e.g. 0.20 for 20%)"], "result": None}

    # Model conversion scenarios
    conversion_scenarios = []
    for scenario_valuation in [5_000_000, 8_000_000, 12_000_000, 20_000_000, 30_000_000]:
        effective_price = None
        cap_price = None
        discount_price = None
        conversion_basis = None

        if valuation_cap:
            # Price per share at cap: cap / post-money shares (simplified)
            cap_price = valuation_cap
            cap_conversion_pct = round(principal / valuation_cap * 100, 2)
        else:
            cap_conversion_pct = None

        discount_price = scenario_valuation * (1 - discount_rate)
        discount_conversion_pct = round(principal / discount_price * 100, 2)

        if valuation_cap and scenario_valuation > valuation_cap:
            # Cap is better for investor
            effective_pct = cap_conversion_pct
            conversion_basis = f"Cap (${valuation_cap:,.0f})"
        else:
            effective_pct = discount_conversion_pct
            conversion_basis = f"Discount ({int(discount_rate * 100)}%)"

        conversion_scenarios.append({
            "series_a_pre_money_usd": scenario_valuation,
            "conversion_basis": conversion_basis,
            "investor_ownership_pct_post_conversion": effective_pct,
        })

    # Build SAFE summary
    terms = {
        "safe_type": SAFE_TYPES[safe_type],
        "principal_usd": principal,
        "valuation_cap_usd": valuation_cap,
        "discount_rate_pct": round(discount_rate * 100),
        "pro_rata_rights": pro_rata,
        "conversion_trigger": STANDARD_TERMS["conversion_trigger"],
        "information_rights": STANDARD_TERMS["information_rights"],
    }

    return {
        "error": None,
        "result": {
            "company": company,
            "investor": investor,
            "date": date,
            "terms": terms,
            "conversion_scenarios": conversion_scenarios,
            "execution_checklist": [
                "Obtain board consent (single-investor SAFEs typically don't require shareholder approval)",
                "Prepare SAFE using YC standard template at ycombinator.com/documents",
                "Both parties sign via DocuSign or similar",
                "Wire transfer confirmed and matched to SAFE amount",
                "Record SAFE in cap table management platform (Carta, Pulley, etc.)",
                "Send copy to company counsel and update corporate records",
            ],
            "warnings": (
                ["No valuation cap set — investor bears full dilution risk at conversion"]
                if not valuation_cap else []
            ),
            "summary": (
                f"SAFE for {investor} → {company}: ${principal:,.0f} principal, "
                f"{SAFE_TYPES[safe_type].split(' — ')[0]}. "
                + (f"Cap: ${valuation_cap:,.0f}. " if valuation_cap else "No cap. ")
                + f"Discount: {int(discount_rate * 100)}%."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_safe(data)
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
