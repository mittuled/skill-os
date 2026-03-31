#!/usr/bin/env python3
"""
run.py — Manage investor relationship pipeline: track, nurture, and prioritize.

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

# Relationship stage definitions
RELATIONSHIP_STAGES = [
    "identified",
    "intro_pending",
    "first_contact",
    "relationship_building",
    "warm",
    "fundraise_ready",
    "passed",
    "invested",
]

# Nurture cadence targets (days between touches) by stage
NURTURE_CADENCE_DAYS = {
    "identified": 90,
    "intro_pending": 14,
    "first_contact": 30,
    "relationship_building": 45,
    "warm": 30,
    "fundraise_ready": 7,
    "passed": 180,
    "invested": 30,
}

# Priority scoring weights
PRIORITY_WEIGHTS = {
    "thesis_fit": 35,
    "check_size_fit": 25,
    "relationship_warmth": 25,
    "portfolio_value": 15,
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "investors" not in data or not isinstance(data["investors"], list):
        errors.append("Missing required field: investors (list)")
    return errors


def run_pipeline(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    investors = data["investors"]
    target_raise_usd = data.get("target_raise_usd", 0)
    fundraise_in_weeks = data.get("fundraise_in_weeks", 0)

    # Process each investor
    processed = []
    overdue_for_touch = []
    by_stage: dict[str, list] = {s: [] for s in RELATIONSHIP_STAGES}

    for inv in investors:
        stage = inv.get("stage", "identified")
        if stage not in RELATIONSHIP_STAGES:
            stage = "identified"

        # Score priority
        thesis_fit = min(max(inv.get("thesis_fit_score", 5), 0), 10)
        check_fit = min(max(inv.get("check_size_fit_score", 5), 0), 10)
        warmth = min(max(inv.get("warmth_score", 5), 0), 10)
        portfolio_value = min(max(inv.get("portfolio_value_score", 5), 0), 10)

        priority_score = round(
            (thesis_fit * PRIORITY_WEIGHTS["thesis_fit"]
             + check_fit * PRIORITY_WEIGHTS["check_size_fit"]
             + warmth * PRIORITY_WEIGHTS["relationship_warmth"]
             + portfolio_value * PRIORITY_WEIGHTS["portfolio_value"]) / 10
        )

        cadence = NURTURE_CADENCE_DAYS.get(stage, 30)
        days_since_contact = inv.get("days_since_contact", 0)
        needs_touch = days_since_contact > cadence

        entry = {
            "name": inv["name"],
            "firm": inv.get("firm", ""),
            "stage": stage,
            "priority_score": priority_score,
            "days_since_contact": days_since_contact,
            "cadence_target_days": cadence,
            "needs_touch": needs_touch,
            "check_size_usd": inv.get("check_size_usd", 0),
            "notes": inv.get("notes", ""),
            "next_action": inv.get("next_action", "Follow up"),
        }
        processed.append(entry)
        by_stage[stage].append(entry)
        if needs_touch and stage not in ("passed",):
            overdue_for_touch.append(entry)

    # Sort by priority
    processed.sort(key=lambda x: x["priority_score"], reverse=True)
    top_priority = [p for p in processed if p["priority_score"] >= 70 and p["stage"] not in ("passed", "invested")]

    # Pipeline coverage
    potential_raise = sum(
        inv["check_size_usd"] for inv in processed
        if inv["stage"] in ("warm", "fundraise_ready", "relationship_building")
        and inv["check_size_usd"] > 0
    )

    stage_counts = {s: len(by_stage[s]) for s in RELATIONSHIP_STAGES if by_stage[s]}

    return {
        "error": None,
        "result": {
            "company": company,
            "total_investors_tracked": len(processed),
            "overdue_for_touch": overdue_for_touch,
            "top_priority_investors": top_priority,
            "stage_counts": stage_counts,
            "potential_raise_usd": potential_raise,
            "target_raise_usd": target_raise_usd,
            "coverage_ratio": round(potential_raise / target_raise_usd, 2) if target_raise_usd else None,
            "fundraise_in_weeks": fundraise_in_weeks,
            "summary": (
                f"Investor pipeline for {company}: {len(processed)} tracked, "
                f"{len(overdue_for_touch)} overdue for touch, "
                f"{len(top_priority)} top-priority active relationships. "
                f"Warm pipeline coverage: ${potential_raise:,.0f}"
                + (f" vs ${target_raise_usd:,.0f} target." if target_raise_usd else ".")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_pipeline(data)
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
