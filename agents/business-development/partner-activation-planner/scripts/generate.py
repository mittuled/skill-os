#!/usr/bin/env python3
"""
generate.py — Generate a partner activation plan with milestones, revenue targets, and enablement requirements.

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

PARTNERSHIP_TYPES = ["co_marketing", "co_selling", "integration", "reseller", "technology"]

ACTIVATION_MILESTONES = {
    "co_marketing": [
        {"week": 2, "milestone": "Partner profile live on website"},
        {"week": 4, "milestone": "Joint blog post published"},
        {"week": 6, "milestone": "Webinar or event co-hosted"},
        {"week": 12, "milestone": "First joint pipeline review"},
    ],
    "co_selling": [
        {"week": 2, "milestone": "Partner sales team briefed and battlecard distributed"},
        {"week": 4, "milestone": "First joint sales call completed"},
        {"week": 8, "milestone": "First co-sell deal in pipeline"},
        {"week": 16, "milestone": "First joint deal closed"},
    ],
    "integration": [
        {"week": 4, "milestone": "Integration specification agreed"},
        {"week": 10, "milestone": "Integration MVP built and tested"},
        {"week": 14, "milestone": "Integration launched in both marketplaces"},
        {"week": 18, "milestone": "First customer using integration"},
    ],
}

REQUIRED_FIELDS = ["partner_name", "partnership_type", "revenue_target_usd", "activation_owner"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "partnership_type" in data and data["partnership_type"] not in PARTNERSHIP_TYPES:
        errors.append(f"partnership_type must be one of {PARTNERSHIP_TYPES}")
    return errors


def generate_activation_plan(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    ptype = data["partnership_type"]
    milestones = ACTIVATION_MILESTONES.get(ptype, ACTIVATION_MILESTONES["co_selling"])

    enablement_requirements = [
        "Partner overview deck (who we are, why partner with us)",
        "Sales battlecard with competitive positioning",
        "Integration/product demo for partner sales team",
        "Joint customer case study (once first deal closes)",
        "Partner portal access with deal registration",
    ]

    return {
        "error": None,
        "result": {
            "partner_name": data["partner_name"],
            "partnership_type": ptype,
            "revenue_target_usd": data["revenue_target_usd"],
            "activation_owner": data["activation_owner"],
            "activation_start_date": data.get("start_date"),
            "milestones": milestones,
            "enablement_requirements": enablement_requirements,
            "success_metrics": {
                "pipeline_generated_usd": data["revenue_target_usd"] * 3,
                "closed_won_usd": data["revenue_target_usd"],
                "co_sell_deals": data.get("target_deals", 5),
            },
            "qbr_cadence": "Monthly for first 6 months; quarterly after steady state",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_activation_plan(data)
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
