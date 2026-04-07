#!/usr/bin/env python3
"""
run.py — Manage the fundraising process pipeline, investor stages, and timeline.

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

# Fundraising pipeline stages in order
PIPELINE_STAGES = [
    "target",
    "intro_requested",
    "first_meeting",
    "second_meeting",
    "diligence",
    "term_sheet",
    "closed",
    "passed",
]

# Stage weights for funnel analysis (likelihood of closing from each stage)
STAGE_CLOSE_PROBABILITY = {
    "target": 0.05,
    "intro_requested": 0.10,
    "first_meeting": 0.15,
    "second_meeting": 0.25,
    "diligence": 0.50,
    "term_sheet": 0.80,
    "closed": 1.00,
    "passed": 0.00,
}

# Standard fundraise timeline by round
STANDARD_TIMELINE_WEEKS = {
    "pre_seed": 8,
    "seed": 12,
    "series_a": 20,
    "series_b": 24,
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "round_type" not in data or data.get("round_type") not in STANDARD_TIMELINE_WEEKS:
        errors.append(f"Missing or invalid field: round_type ({'/'.join(STANDARD_TIMELINE_WEEKS.keys())})")
    if "investors" not in data or not isinstance(data["investors"], list):
        errors.append("Missing required field: investors (list)")
    return errors


def run_fundraising_process(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    round_type = data["round_type"]
    investors = data["investors"]
    target_raise = data.get("target_raise_usd", 0)
    weeks_elapsed = data.get("weeks_elapsed", 0)

    # Process investor pipeline
    pipeline: dict[str, list] = {stage: [] for stage in PIPELINE_STAGES}
    term_sheets = []
    active_investors = []

    for inv in investors:
        stage = inv.get("stage", "target")
        if stage not in PIPELINE_STAGES:
            stage = "target"
        entry = {
            "name": inv["name"],
            "firm": inv.get("firm", ""),
            "stage": stage,
            "check_size_usd": inv.get("check_size_usd", 0),
            "last_contact": inv.get("last_contact", ""),
            "days_since_contact": inv.get("days_since_contact", 0),
            "notes": inv.get("notes", ""),
            "close_probability": STAGE_CLOSE_PROBABILITY[stage],
        }
        pipeline[stage].append(entry)
        if stage == "term_sheet":
            term_sheets.append(entry)
        if stage not in ("passed", "closed"):
            active_investors.append(entry)

    # Compute weighted expected raise
    expected_raise = sum(
        inv["check_size_usd"] * inv["close_probability"]
        for inv in active_investors
        if inv["check_size_usd"] > 0
    )

    # Identify stale conversations (no contact in 14+ days, not passed)
    stale = [inv for inv in active_investors if inv["days_since_contact"] > 14]

    # Compute funnel summary
    funnel_summary = []
    for stage in PIPELINE_STAGES:
        count = len(pipeline[stage])
        if count > 0:
            funnel_summary.append({"stage": stage, "count": count})

    # Progress assessment
    standard_weeks = STANDARD_TIMELINE_WEEKS[round_type]
    pct_time_elapsed = round(weeks_elapsed / standard_weeks * 100) if standard_weeks else 0
    closed_count = len(pipeline["closed"])
    closed_amount = sum(inv["check_size_usd"] for inv in pipeline["closed"])
    pct_raised = round(closed_amount / target_raise * 100) if target_raise else 0

    if closed_count > 0 and pct_raised >= 80:
        status = "ON_TRACK_TO_CLOSE"
    elif term_sheets:
        status = "TERM_SHEETS_RECEIVED"
    elif pct_time_elapsed > 75 and not term_sheets:
        status = "AT_RISK"
    else:
        status = "IN_PROCESS"

    return {
        "error": None,
        "result": {
            "company": company,
            "round_type": round_type,
            "status": status,
            "target_raise_usd": target_raise,
            "closed_amount_usd": closed_amount,
            "pct_raised": pct_raised,
            "expected_raise_usd": round(expected_raise),
            "weeks_elapsed": weeks_elapsed,
            "standard_timeline_weeks": standard_weeks,
            "pct_time_elapsed": pct_time_elapsed,
            "funnel_summary": funnel_summary,
            "term_sheets": term_sheets,
            "stale_conversations": stale,
            "total_active_investors": len(active_investors),
            "summary": (
                f"Fundraising for {company} ({round_type}): {status}. "
                f"{closed_amount:,.0f} USD closed of {target_raise:,.0f} USD target ({pct_raised}%). "
                f"{len(active_investors)} active investors, {len(term_sheets)} term sheet(s). "
                f"{len(stale)} stale conversation(s)."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_fundraising_process(data)
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
