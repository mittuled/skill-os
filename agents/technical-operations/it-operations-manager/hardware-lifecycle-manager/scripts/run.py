#!/usr/bin/env python3
"""
run.py — Manage hardware lifecycle: procurement, refresh planning, and end-of-life.

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

# Asset status lifecycle
ASSET_STATUSES = ["ordered", "deployed", "in_storage", "under_repair", "end_of_life", "disposed"]

# Refresh cycle recommendations by device type (years)
REFRESH_CYCLES = {
    "macbook_pro": 4,
    "macbook_air": 3,
    "windows_laptop": 3,
    "desktop": 5,
    "monitor": 6,
    "iphone": 3,
    "ipad": 4,
    "other": 4,
}

# Standard per-device replacement cost estimates (USD)
REPLACEMENT_COSTS = {
    "macbook_pro": 2500,
    "macbook_air": 1500,
    "windows_laptop": 1200,
    "desktop": 1800,
    "monitor": 400,
    "iphone": 900,
    "ipad": 700,
    "other": 1000,
}

# Warranty alert threshold (months before expiry)
WARRANTY_ALERT_MONTHS = 3


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "assets" not in data or not isinstance(data["assets"], list):
        errors.append("Missing required field: assets (list)")
    return errors


def run_hardware_lifecycle(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    assets = data["assets"]
    action = data.get("action", "audit")

    # Process each asset
    processed = []
    refresh_due = []
    warranty_expiring = []
    end_of_life = []
    total_value = 0

    for asset in assets:
        device_type = asset.get("device_type", "other")
        age_years = asset.get("age_years", 0)
        refresh_cycle = REFRESH_CYCLES.get(device_type, 4)
        replacement_cost = REPLACEMENT_COSTS.get(device_type, 1000)
        status = asset.get("status", "deployed")
        warranty_months_remaining = asset.get("warranty_months_remaining", 0)
        assigned_to = asset.get("assigned_to", "Unassigned")

        needs_refresh = age_years >= refresh_cycle
        warranty_alert = 0 < warranty_months_remaining <= WARRANTY_ALERT_MONTHS
        is_eol = status == "end_of_life" or age_years > refresh_cycle + 2

        entry = {
            "asset_id": asset.get("asset_id", ""),
            "device_type": device_type,
            "model": asset.get("model", ""),
            "assigned_to": assigned_to,
            "age_years": age_years,
            "status": status,
            "refresh_due": needs_refresh,
            "refresh_cycle_years": refresh_cycle,
            "warranty_months_remaining": warranty_months_remaining,
            "warranty_alert": warranty_alert,
            "replacement_cost_usd": replacement_cost,
        }
        processed.append(entry)

        if needs_refresh:
            refresh_due.append(entry)
        if warranty_alert:
            warranty_expiring.append(entry)
        if is_eol:
            end_of_life.append(entry)
        if status == "deployed":
            total_value += replacement_cost

    # Compute refresh budget
    refresh_budget = sum(REPLACEMENT_COSTS.get(a["device_type"], 1000) for a in refresh_due)

    return {
        "error": None,
        "result": {
            "company": company,
            "action": action,
            "total_assets": len(assets),
            "assets_deployed": len([a for a in processed if a["status"] == "deployed"]),
            "assets_needing_refresh": len(refresh_due),
            "assets_warranty_expiring": len(warranty_expiring),
            "assets_end_of_life": len(end_of_life),
            "estimated_refresh_budget_usd": refresh_budget,
            "fleet_replacement_value_usd": total_value,
            "refresh_due_list": refresh_due,
            "warranty_expiring_list": warranty_expiring,
            "all_assets": processed,
            "summary": (
                f"Hardware fleet for {company}: {len(assets)} assets, "
                f"{len(refresh_due)} due for refresh, "
                f"{len(warranty_expiring)} warranty expiring within {WARRANTY_ALERT_MONTHS} months. "
                f"Estimated refresh budget: ${refresh_budget:,.0f}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_hardware_lifecycle(data)
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
