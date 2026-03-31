#!/usr/bin/env python3
"""
run.py — Run the technical onboarding workflow for a new customer implementation.

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

# Standard onboarding phases in order
ONBOARDING_PHASES = [
    {
        "phase": "environment_setup",
        "label": "Environment Setup",
        "steps": ["Provision tenant", "Configure SSO/auth", "Set user roles", "Verify login"],
    },
    {
        "phase": "integration_configuration",
        "label": "Integration Configuration",
        "steps": ["Configure each integration per catalogue guide", "Test connectivity", "Verify data flow"],
    },
    {
        "phase": "data_migration",
        "label": "Data Migration",
        "steps": ["Map source to target schema", "Run migration script", "Validate row counts and data quality"],
    },
    {
        "phase": "acceptance_testing",
        "label": "Acceptance Testing",
        "steps": ["Run acceptance criteria checklist", "Document pass/fail per criterion", "Obtain customer sign-off"],
    },
    {
        "phase": "training",
        "label": "Customer Training",
        "steps": ["Deliver admin training", "Deliver end-user training", "Provide training materials"],
    },
    {
        "phase": "go_live",
        "label": "Go-Live and Hypercare",
        "steps": ["Switch to production", "Confirm all systems operational", "Initiate hypercare period (14 days)"],
    },
]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "customer_name" not in data:
        errors.append("Missing required field: customer_name")
    if "phase_statuses" not in data or not isinstance(data["phase_statuses"], dict):
        errors.append("Missing required field: phase_statuses (dict of phase -> complete|in_progress|blocked|pending)")
    return errors


def run_onboarding(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    customer = data["customer_name"]
    phase_statuses = data["phase_statuses"]
    issues = data.get("issues", {})
    go_live_date = data.get("go_live_date", "TBD")
    engineer = data.get("engineer", "Implementation Engineer")

    phase_results = []
    blocked_phases = []
    completed_count = 0

    for p in ONBOARDING_PHASES:
        key = p["phase"]
        status = phase_statuses.get(key, "pending")
        issue_note = issues.get(key, "")

        if status == "complete":
            completed_count += 1
        elif status == "blocked":
            blocked_phases.append({"phase": p["label"], "issue": issue_note})

        phase_results.append({
            "phase": p["label"],
            "steps": p["steps"],
            "status": status,
            "issue": issue_note,
        })

    total = len(ONBOARDING_PHASES)
    pct_complete = round((completed_count / total) * 100)

    if completed_count == total:
        overall_status = "GO_LIVE_COMPLETE"
    elif blocked_phases:
        overall_status = "BLOCKED"
    else:
        overall_status = "IN_PROGRESS"

    return {
        "error": None,
        "result": {
            "customer": customer,
            "engineer": engineer,
            "go_live_date": go_live_date,
            "overall_status": overall_status,
            "phases_complete": completed_count,
            "phases_total": total,
            "percent_complete": pct_complete,
            "phase_results": phase_results,
            "blocked_phases": blocked_phases,
            "summary": (
                f"Onboarding for {customer}: {pct_complete}% complete "
                f"({completed_count}/{total} phases). "
                f"Status: {overall_status}. "
                f"Target go-live: {go_live_date}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_onboarding(data)
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
