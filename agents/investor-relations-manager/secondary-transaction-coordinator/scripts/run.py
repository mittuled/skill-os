#!/usr/bin/env python3
"""
run.py — Coordinate secondary transactions: ROFR, board approval, and transfer execution.

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

# Transaction types
TRANSACTION_TYPES = {
    "employee_to_buyer": "Employee selling to external buyer — requires ROFR exercise window",
    "investor_to_investor": "Investor-to-investor transfer — requires board consent per stockholder agreement",
    "tender_offer_participation": "Participation in company-sponsored tender offer",
    "rofr_exercise": "Company or existing shareholder exercises ROFR on a proposed transfer",
}

# ROFR process steps with SLA days
ROFR_PROCESS = [
    {"step": "Seller notifies company of proposed transfer with buyer details and price", "sla_days": 0},
    {"step": "Company notifies ROFR holders (investors per stockholder agreement)", "sla_days": 3},
    {"step": "ROFR window opens — holders have right to exercise at same price", "sla_days": 3},
    {"step": "ROFR window closes (typically 30 days per stockholder agreement)", "sla_days": 30},
    {"step": "Company notifies seller: ROFR exercised or waived", "sla_days": 35},
    {"step": "If waived: seller may proceed with original buyer", "sla_days": 35},
    {"step": "Board consent obtained for transfer", "sla_days": 45},
    {"step": "Share transfer executed and cap table updated", "sla_days": 50},
]

# Valid transaction statuses
VALID_STATUSES = [
    "pending_notification",
    "rofr_window_open",
    "rofr_exercised",
    "rofr_waived",
    "pending_board_consent",
    "approved",
    "rejected",
    "completed",
]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "transaction_type" not in data or data.get("transaction_type") not in TRANSACTION_TYPES:
        errors.append(f"Missing or invalid field: transaction_type ({'/'.join(TRANSACTION_TYPES.keys())})")
    if "seller_name" not in data:
        errors.append("Missing required field: seller_name")
    if "shares" not in data or not isinstance(data["shares"], int):
        errors.append("Missing required field: shares (integer)")
    return errors


def run_secondary_transaction(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    transaction_type = data["transaction_type"]
    seller = data["seller_name"]
    buyer = data.get("buyer_name", "")
    shares = data["shares"]
    price_per_share = data.get("price_per_share", 0)
    status = data.get("status", "pending_notification")
    if status not in VALID_STATUSES:
        status = "pending_notification"
    rofr_holders = data.get("rofr_holders", [])
    days_elapsed = data.get("days_elapsed", 0)
    share_class = data.get("share_class", "Common")

    # Compute transaction value
    transaction_value = round(shares * price_per_share) if price_per_share else 0

    # Determine next step based on status
    next_steps = {
        "pending_notification": "Seller must formally notify company of proposed transfer with buyer identity and proposed price per share",
        "rofr_window_open": f"ROFR window open — ROFR holders ({', '.join(rofr_holders) if rofr_holders else 'per stockholder agreement'}) have {max(0, 30 - days_elapsed)} days remaining to exercise",
        "rofr_exercised": "ROFR exercised — complete transfer to ROFR holder at agreed price; original buyer cannot proceed",
        "rofr_waived": "ROFR waived — proceed to board consent; seller may proceed with original buyer",
        "pending_board_consent": "Obtain board consent via written consent or at next board meeting; confirm transfer complies with stockholder agreement transfer restrictions",
        "approved": "Board consent obtained — execute share transfer agreement, collect signatures, update cap table",
        "rejected": "Transfer rejected by board — notify all parties; seller cannot proceed with this buyer",
        "completed": "Transaction complete — cap table updated, transfer recorded",
    }

    # Build ROFR timeline
    rofr_timeline = []
    for step in ROFR_PROCESS:
        is_past = step["sla_days"] <= days_elapsed
        rofr_timeline.append({
            "step": step["step"],
            "target_day": step["sla_days"],
            "status": "COMPLETE" if is_past else ("IN_PROGRESS" if step["sla_days"] == min(
                s["sla_days"] for s in ROFR_PROCESS if s["sla_days"] > days_elapsed - 1
            ) else "UPCOMING"),
        })

    return {
        "error": None,
        "result": {
            "company": company,
            "transaction_type": transaction_type,
            "transaction_description": TRANSACTION_TYPES[transaction_type],
            "seller": seller,
            "buyer": buyer,
            "share_class": share_class,
            "shares": shares,
            "price_per_share": price_per_share,
            "transaction_value_usd": transaction_value,
            "current_status": status,
            "days_elapsed": days_elapsed,
            "rofr_holders": rofr_holders,
            "next_action": next_steps[status],
            "rofr_timeline": rofr_timeline,
            "summary": (
                f"Secondary transaction for {company}: {seller} → {buyer or 'TBD'}, "
                f"{shares:,} {share_class} shares at ${price_per_share:.2f}/share "
                f"(${transaction_value:,.0f} total). Status: {status.upper().replace('_', ' ')}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_secondary_transaction(data)
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
