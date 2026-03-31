#!/usr/bin/env python3
"""
run.py — Align platform roadmap with product/engineering timelines and detect conflicts.

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

# Dependency types
DEPENDENCY_TYPES = {
    "blocking": "Platform work must complete before product feature can launch",
    "enabling": "Platform work unlocks or accelerates a product feature",
    "concurrent": "Platform and product work can proceed in parallel",
    "decoupled": "No dependency — platform and product independent",
}

# Risk levels for misalignment
MISALIGNMENT_RISK = {
    "blocking": "HIGH",
    "enabling": "MEDIUM",
    "concurrent": "LOW",
    "decoupled": "NONE",
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "team_name" not in data:
        errors.append("Missing required field: team_name")
    if "product_items" not in data or not isinstance(data["product_items"], list):
        errors.append("Missing required field: product_items (list)")
    if "platform_items" not in data or not isinstance(data["platform_items"], list):
        errors.append("Missing required field: platform_items (list)")
    return errors


def run_roadmap_alignment(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    team = data["team_name"]
    product_items = data["product_items"]
    platform_items = data["platform_items"]
    planning_period = data.get("planning_period", "")

    # Index platform items by ID
    platform_by_id = {p.get("id", ""): p for p in platform_items}

    # Analyze each product item for platform dependencies
    alignment_results = []
    conflicts = []
    blockers = []
    at_risk = []

    for prod in product_items:
        prod_id = prod.get("id", "")
        prod_target = prod.get("target_sprint", "")
        platform_deps = prod.get("platform_dependencies", [])
        dep_results = []

        for dep_id in platform_deps:
            plat = platform_by_id.get(dep_id, {})
            dep_type = plat.get("dependency_type", "blocking")
            plat_target = plat.get("target_sprint", "")
            risk = MISALIGNMENT_RISK.get(dep_type, "UNKNOWN")

            # Simple sprint ordering conflict detection (assumes sprint names are sortable)
            conflict = False
            if dep_type == "blocking" and plat_target and prod_target:
                conflict = plat_target > prod_target

            dep_entry = {
                "platform_item_id": dep_id,
                "platform_item": plat.get("name", dep_id),
                "dependency_type": dep_type,
                "dependency_description": DEPENDENCY_TYPES.get(dep_type, "Unknown"),
                "platform_target_sprint": plat_target,
                "conflict": conflict,
                "risk": risk,
            }
            dep_results.append(dep_entry)
            if conflict:
                conflicts.append({
                    "product_item": prod.get("name", prod_id),
                    "platform_dependency": plat.get("name", dep_id),
                    "product_target": prod_target,
                    "platform_target": plat_target,
                    "conflict_description": f"Platform delivers {plat_target} but product needs it by {prod_target}",
                })

        risk_levels = [d["risk"] for d in dep_results]
        overall_risk = "HIGH" if "HIGH" in risk_levels else ("MEDIUM" if "MEDIUM" in risk_levels else "LOW")
        has_conflict = any(d["conflict"] for d in dep_results)

        entry = {
            "product_item_id": prod_id,
            "product_item": prod.get("name", prod_id),
            "target_sprint": prod_target,
            "platform_dependencies": dep_results,
            "overall_risk": overall_risk,
            "has_conflict": has_conflict,
            "owner": prod.get("owner", ""),
            "notes": prod.get("notes", ""),
        }
        alignment_results.append(entry)
        if has_conflict:
            blockers.append(entry)
        elif overall_risk == "HIGH":
            at_risk.append(entry)

    return {
        "error": None,
        "result": {
            "team": team,
            "planning_period": planning_period,
            "total_product_items": len(product_items),
            "total_platform_items": len(platform_items),
            "conflicts_count": len(conflicts),
            "blockers_count": len(blockers),
            "at_risk_count": len(at_risk),
            "alignment_results": alignment_results,
            "conflicts": conflicts,
            "summary": (
                f"Roadmap alignment for {team} ({planning_period}): "
                f"{len(product_items)} product items reviewed against {len(platform_items)} platform items. "
                f"{len(conflicts)} conflict(s) — platform deliveries miss product timelines. "
                f"{len(at_risk)} additional item(s) at risk."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_roadmap_alignment(data)
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
