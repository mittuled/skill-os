#!/usr/bin/env python3
"""
run.py — Manage secondary market transactions and employee liquidity programmes.

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

# Programme types
PROGRAMME_TYPES = {
    "tender_offer": "Company-sponsored tender offer — company or third party buys shares from employees",
    "direct_secondary": "Direct employee-to-buyer sale — requires company ROFR waiver and board approval",
    "liquidity_programme": "Structured ongoing liquidity programme — periodic tender windows",
}

# Eligibility criteria for tender offers
ELIGIBILITY_FACTORS = [
    "Minimum vesting threshold (typically 1-year cliff passed)",
    "Employment status (current employees only, or include former)",
    "Minimum holding period since exercise",
    "Maximum shares eligible per participant",
]

# Tax considerations
TAX_CONSIDERATIONS = {
    "iso": "ISO shares — qualifying disposition requires 2-year from grant, 1-year from exercise. Early sale may trigger AMT.",
    "nso": "NSO shares — ordinary income tax on spread at exercise; sale treated as capital gain/loss.",
    "rsu": "RSU — taxed as ordinary income at vesting; subsequent appreciation is capital gain.",
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "programme_type" not in data or data.get("programme_type") not in PROGRAMME_TYPES:
        errors.append(f"Missing or invalid field: programme_type ({'/'.join(PROGRAMME_TYPES.keys())})")
    if "participants" not in data or not isinstance(data["participants"], list):
        errors.append("Missing required field: participants (list)")
    return errors


def run_secondary_programme(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    programme_type = data["programme_type"]
    participants = data["participants"]
    price_per_share = data.get("price_per_share", 0)
    total_budget_usd = data.get("total_budget_usd", 0)
    programme_date = data.get("programme_date", "")

    # Process participants
    processed = []
    total_shares_eligible = 0
    total_potential_proceeds = 0
    over_budget = False

    for p in participants:
        shares_vested = p.get("shares_vested", 0)
        shares_eligible = p.get("shares_eligible", shares_vested)
        proceeds = round(shares_eligible * price_per_share) if price_per_share else 0
        share_type = p.get("share_type", "iso")
        entry = {
            "name": p["name"],
            "role": p.get("role", ""),
            "share_type": share_type,
            "shares_vested": shares_vested,
            "shares_eligible": shares_eligible,
            "potential_proceeds_usd": proceeds,
            "tax_consideration": TAX_CONSIDERATIONS.get(share_type, "Consult tax advisor"),
            "years_at_company": p.get("years_at_company", 0),
            "notes": p.get("notes", ""),
        }
        processed.append(entry)
        total_shares_eligible += shares_eligible
        total_potential_proceeds += proceeds

    if total_budget_usd and total_potential_proceeds > total_budget_usd:
        over_budget = True
        # Pro-rata reduction
        reduction_ratio = total_budget_usd / total_potential_proceeds
        for p in processed:
            p["pro_rata_shares_eligible"] = round(p["shares_eligible"] * reduction_ratio)
            p["pro_rata_proceeds_usd"] = round(p["pro_rata_shares_eligible"] * price_per_share) if price_per_share else 0

    return {
        "error": None,
        "result": {
            "company": company,
            "programme_type": programme_type,
            "programme_description": PROGRAMME_TYPES[programme_type],
            "programme_date": programme_date,
            "price_per_share": price_per_share,
            "total_budget_usd": total_budget_usd,
            "total_shares_eligible": total_shares_eligible,
            "total_potential_proceeds_usd": total_potential_proceeds,
            "over_budget": over_budget,
            "participants": processed,
            "eligibility_factors": ELIGIBILITY_FACTORS,
            "process_steps": [
                "Obtain board approval for programme",
                "Engage securities counsel for compliance review (Rule 10b5-1, tender offer rules if applicable)",
                "Notify participants with offer documents and election forms",
                "Collect elections within offer window (typically 20 business days for tender offers)",
                "Process ROFR waivers for direct secondary sales",
                "Complete transfers and update cap table",
                "Distribute proceeds to sellers",
            ],
            "summary": (
                f"{PROGRAMME_TYPES[programme_type].split(' — ')[0]} for {company}: "
                f"{len(processed)} participant(s), {total_shares_eligible:,} shares eligible. "
                f"Potential proceeds: ${total_potential_proceeds:,.0f}"
                + (f" — OVER BUDGET by ${total_potential_proceeds - total_budget_usd:,.0f} (pro-rata reduction applied)." if over_budget else ".")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_secondary_programme(data)
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
