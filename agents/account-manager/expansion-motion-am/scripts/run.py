#!/usr/bin/env python3
"""
run.py — Execute an expansion motion workflow for an assigned account.

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

# Expansion motion workflow steps
WORKFLOW_STEPS = [
    {"step": 1, "name": "review_opportunity_brief", "deliverable": "Internalised opportunity context"},
    {"step": 2, "name": "prepare_proposal", "deliverable": "Tailored expansion proposal document"},
    {"step": 3, "name": "present_to_customer", "deliverable": "Customer meeting — proposal presented"},
    {"step": 4, "name": "handle_objections", "deliverable": "Objection responses documented"},
    {"step": 5, "name": "negotiate_and_close", "deliverable": "Signed expansion agreement"},
    {"step": 6, "name": "implementation_handoff", "deliverable": "Implementation handoff document"},
]

EXPANSION_TYPES = ["seat_upsell", "tier_upgrade", "cross_sell", "multi_year_renewal"]

BLOCKERS = {
    "open_support_escalation": "Resolve open escalations before proceeding with expansion conversation",
    "low_nps": "Improve NPS score before presenting expansion — unhappy customers don't buy more",
    "no_champion": "Identify and engage a customer champion before scheduling proposal meeting",
    "budget_cycle_closed": "Wait for next budget cycle to open before presenting pricing",
}

REQUIRED_FIELDS = ["account_name", "expansion_type", "opportunity_value_usd", "current_step"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "expansion_type" in data and data["expansion_type"] not in EXPANSION_TYPES:
        errors.append(f"expansion_type must be one of {EXPANSION_TYPES}")
    return errors


def run_expansion_motion(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    current_step = data["current_step"]
    blockers_present = data.get("blockers", [])
    expansion_type = data["expansion_type"]

    # Check for blockers
    active_blockers = []
    for blocker in blockers_present:
        if blocker in BLOCKERS:
            active_blockers.append({"blocker": blocker, "recommendation": BLOCKERS[blocker]})

    # Determine if motion can proceed
    blocking_issues = [b for b in active_blockers if b["blocker"] in ["open_support_escalation", "low_nps"]]
    can_proceed = len(blocking_issues) == 0

    # Find current and next steps
    current_step_detail = next((s for s in WORKFLOW_STEPS if s["step"] == current_step), None)
    next_step_detail = next((s for s in WORKFLOW_STEPS if s["step"] == current_step + 1), None)

    completed_steps = [s for s in WORKFLOW_STEPS if s["step"] < current_step]
    remaining_steps = [s for s in WORKFLOW_STEPS if s["step"] >= current_step]

    # Build proposal summary if at step 2+
    proposal_elements = None
    if current_step >= 2:
        proposal_elements = {
            "expansion_type": expansion_type,
            "value_proposition": f"Solving [customer stated problem] to achieve [business outcome]",
            "pricing": f"${data['opportunity_value_usd']:,} incremental ARR",
            "implementation_timeline": data.get("implementation_timeline_weeks", 4),
            "value_delivery_milestones": [
                "Week 1: Onboarding and configuration",
                "Week 2-3: Team training and adoption",
                "Week 4: First value metric review",
            ],
        }

    return {
        "error": None,
        "result": {
            "account_name": data["account_name"],
            "expansion_type": expansion_type,
            "opportunity_value_usd": data["opportunity_value_usd"],
            "current_step": current_step,
            "current_step_name": current_step_detail["name"] if current_step_detail else "complete",
            "can_proceed": can_proceed,
            "active_blockers": active_blockers,
            "completed_steps": [s["name"] for s in completed_steps],
            "remaining_steps": [{"step": s["step"], "name": s["name"], "deliverable": s["deliverable"]} for s in remaining_steps],
            "next_action": next_step_detail["name"] if next_step_detail and can_proceed else ("Resolve blockers first" if not can_proceed else "Motion complete"),
            "proposal_elements": proposal_elements,
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_expansion_motion(data)
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
