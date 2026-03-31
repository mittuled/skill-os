#!/usr/bin/env python3
"""
generate.py — Generate an implementation playbook with phases, milestones, and RACI.

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

# Standard implementation phases with default durations by complexity tier
STANDARD_PHASES = {
    "discovery": {
        "label": "Discovery & Requirements",
        "deliverables": ["Requirements document", "Customer sign-off"],
        "durations": {"smb": 1, "mid_market": 1, "enterprise": 2},
    },
    "configuration": {
        "label": "Environment Configuration",
        "deliverables": ["Provisioned environment", "SSO/auth configured"],
        "durations": {"smb": 1, "mid_market": 2, "enterprise": 3},
    },
    "integration": {
        "label": "Integration Setup",
        "deliverables": ["Connected integrations", "Data flow verified"],
        "durations": {"smb": 1, "mid_market": 2, "enterprise": 4},
    },
    "data_migration": {
        "label": "Data Migration",
        "deliverables": ["Migrated dataset", "Quality report"],
        "durations": {"smb": 1, "mid_market": 1, "enterprise": 2},
    },
    "testing": {
        "label": "Acceptance Testing",
        "deliverables": ["Test results", "Customer sign-off"],
        "durations": {"smb": 1, "mid_market": 1, "enterprise": 2},
    },
    "training": {
        "label": "Training",
        "deliverables": ["Admin training", "End-user training", "Training materials"],
        "durations": {"smb": 1, "mid_market": 1, "enterprise": 2},
    },
    "go_live": {
        "label": "Go-Live & Hypercare",
        "deliverables": ["Production launch", "Hypercare monitoring report"],
        "durations": {"smb": 1, "mid_market": 2, "enterprise": 2},
    },
}

# RACI roles
RACI_ROLES = ["Implementation Engineer", "Implementation Lead", "Customer Admin", "Customer Executive Sponsor"]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "playbook_name" not in data:
        errors.append("Missing required field: playbook_name")
    if "tier" not in data or data.get("tier") not in ("smb", "mid_market", "enterprise"):
        errors.append("Missing or invalid field: tier (smb|mid_market|enterprise)")
    return errors


def generate_playbook(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    playbook_name = data["playbook_name"]
    tier = data["tier"]
    custom_phases = data.get("custom_phases", [])
    go_live_criteria = data.get("go_live_criteria", [
        "All acceptance criteria passed",
        "Customer sign-off obtained",
        "Support team briefed",
    ])
    templates = data.get("templates", [
        "Kickoff deck", "Requirements document", "Status report", "Go-live checklist",
    ])

    # Build phase plan
    phase_plan = []
    total_weeks = 0
    for key, phase in STANDARD_PHASES.items():
        weeks = phase["durations"][tier]
        total_weeks += weeks
        phase_plan.append({
            "phase": phase["label"],
            "weeks": weeks,
            "deliverables": phase["deliverables"],
            "entry_criteria": f"{phase_plan[-1]['phase']} complete" if phase_plan else "Contract signed",
        })

    # Add any custom phases
    for cp in custom_phases:
        phase_plan.append({
            "phase": cp.get("label", "Custom Phase"),
            "weeks": cp.get("weeks", 1),
            "deliverables": cp.get("deliverables", []),
            "entry_criteria": cp.get("entry_criteria", "Previous phase complete"),
        })
        total_weeks += cp.get("weeks", 1)

    return {
        "error": None,
        "result": {
            "playbook_name": playbook_name,
            "tier": tier,
            "total_weeks": total_weeks,
            "phase_plan": phase_plan,
            "go_live_criteria": go_live_criteria,
            "template_library": templates,
            "raci_roles": RACI_ROLES,
            "summary": (
                f"Playbook '{playbook_name}' for {tier.replace('_', '-')} tier: "
                f"{len(phase_plan)} phases over {total_weeks} weeks."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_playbook(data)
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
