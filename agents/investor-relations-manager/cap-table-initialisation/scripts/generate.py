#!/usr/bin/env python3
"""
generate.py — Generate initial cap table at company formation.

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

# Standard option pool percentages by stage
OPTION_POOL_GUIDANCE = {
    "pre_seed": {"recommended_pct": 10, "note": "Typical pre-seed pool; may need to expand before seed round"},
    "seed": {"recommended_pct": 15, "note": "Standard seed-stage option pool; often requested by lead investor"},
    "series_a": {"recommended_pct": 20, "note": "Series A standard; created pre-money to avoid additional dilution"},
}

# Share class types
VALID_SHARE_CLASSES = ["Common", "Founders Common", "Preferred"]

# Vesting schedule standards
STANDARD_VESTING = {
    "cliff_months": 12,
    "total_months": 48,
    "description": "4-year vesting with 1-year cliff (industry standard)",
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "founders" not in data or not isinstance(data["founders"], list) or not data["founders"]:
        errors.append("Missing required field: founders (non-empty list)")
    if "total_shares" not in data or not isinstance(data["total_shares"], int):
        errors.append("Missing required field: total_shares (integer)")
    if "stage" not in data or data.get("stage") not in OPTION_POOL_GUIDANCE:
        errors.append(f"Missing or invalid field: stage ({'/'.join(OPTION_POOL_GUIDANCE.keys())})")
    return errors


def generate_cap_table(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    founders = data["founders"]
    total_shares = data["total_shares"]
    stage = data["stage"]
    option_pool_pct = data.get("option_pool_pct", OPTION_POOL_GUIDANCE[stage]["recommended_pct"])
    incorporation_date = data.get("incorporation_date", "")

    # Validate founder equity splits sum to <= 100%
    total_founder_pct = sum(f.get("equity_pct", 0) for f in founders)
    if total_founder_pct > 100:
        return {"error": [f"Founder equity percentages sum to {total_founder_pct}% — must not exceed 100%"], "result": None}

    # Compute option pool shares
    option_pool_shares = round(total_shares * option_pool_pct / 100)
    remaining_for_founders = total_shares - option_pool_shares
    total_pct_allocated = total_founder_pct + option_pool_pct

    # Build founder rows
    founder_rows = []
    for f in founders:
        equity_pct = f.get("equity_pct", 0)
        shares = round(remaining_for_founders * equity_pct / (100 - option_pool_pct))
        founder_rows.append({
            "name": f["name"],
            "role": f.get("role", "Founder"),
            "share_class": f.get("share_class", "Founders Common"),
            "shares": shares,
            "equity_pct": round(shares / total_shares * 100, 2),
            "vesting": f.get("vesting", STANDARD_VESTING["description"]),
        })

    issued_to_founders = sum(r["shares"] for r in founder_rows)
    unissued = total_shares - issued_to_founders - option_pool_shares

    return {
        "error": None,
        "result": {
            "company": company,
            "incorporation_date": incorporation_date,
            "stage": stage,
            "total_authorized_shares": total_shares,
            "issued_founder_shares": issued_to_founders,
            "option_pool_shares": option_pool_shares,
            "option_pool_pct": option_pool_pct,
            "unissued_shares": unissued,
            "founder_table": founder_rows,
            "option_pool_guidance": OPTION_POOL_GUIDANCE[stage],
            "vesting_standard": STANDARD_VESTING,
            "total_pct_allocated": round(total_pct_allocated, 2),
            "warnings": (
                ["Unissued shares remain — consider allocating to option pool or reserving for advisors"]
                if unissued > 0 else []
            ),
            "summary": (
                f"Initial cap table for {company}: {len(founders)} founder(s), "
                f"{issued_to_founders:,} founder shares + {option_pool_shares:,} option pool "
                f"({option_pool_pct}%) out of {total_shares:,} total authorized shares."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_cap_table(data)
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
