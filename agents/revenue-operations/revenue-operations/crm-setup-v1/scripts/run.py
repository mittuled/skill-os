#!/usr/bin/env python3
"""
run.py — Validate CRM setup completeness across pipeline stages, fields, automations, and integrations.

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

# Required CRM components for a v1 setup
REQUIRED_PIPELINE_STAGES = [
    "lead_qualification",
    "discovery",
    "technical_evaluation",
    "proposal",
    "negotiation",
    "closed_won",
    "closed_lost",
]

REQUIRED_DEAL_FIELDS = [
    "deal_value",
    "close_date",
    "lead_source",
    "product_line",
    "deal_owner",
    "contract_term",
]

REQUIRED_AUTOMATIONS = [
    "stage_transition_notification",
    "overdue_deal_alert",
    "new_lead_assignment",
    "closed_won_handoff_trigger",
]

REQUIRED_INTEGRATIONS = [
    "email_calendar",
    "marketing_automation",
    "billing_system",
]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["crm_platform", "pipeline_stages", "deal_fields", "automations", "integrations"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def check_components(configured: list[str], required: list[str]) -> dict:
    configured_set = set(configured)
    required_set = set(required)
    missing = list(required_set - configured_set)
    extra = list(configured_set - required_set)
    return {
        "configured": configured,
        "missing": missing,
        "extra_configured": extra,
        "completeness_pct": round((len(required_set - set(missing)) / len(required_set)) * 100) if required_set else 100,
    }


def run_crm_setup_check(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    stages = check_components(data["pipeline_stages"], REQUIRED_PIPELINE_STAGES)
    fields = check_components(data["deal_fields"], REQUIRED_DEAL_FIELDS)
    automations = check_components(data["automations"], REQUIRED_AUTOMATIONS)
    integrations = check_components(data["integrations"], REQUIRED_INTEGRATIONS)

    components = {
        "pipeline_stages": stages,
        "deal_fields": fields,
        "automations": automations,
        "integrations": integrations,
    }

    # Calculate overall completeness
    overall_pct = round(sum(c["completeness_pct"] for c in components.values()) / len(components))

    # Check end-to-end test
    e2e_passed = data.get("end_to_end_test_passed", False)

    all_missing = {k: v["missing"] for k, v in components.items() if v["missing"]}

    if all_missing or not e2e_passed:
        if not e2e_passed and not all_missing:
            verdict = "BLOCKED"
            recommendation = "All components configured but end-to-end test failed — do not go live until test passes"
        elif all_missing:
            verdict = "INCOMPLETE"
            recommendation = f"{sum(len(v) for v in all_missing.values())} required component(s) missing — configure before going live"
        else:
            verdict = "BLOCKED"
            recommendation = "Configuration incomplete and end-to-end test not passed"
    else:
        verdict = "READY"
        recommendation = "CRM v1 setup complete — all required components configured and end-to-end test passed"

    result = {
        "crm_platform": data["crm_platform"],
        "overall_completeness_pct": overall_pct,
        "verdict": verdict,
        "recommendation": recommendation,
        "end_to_end_test_passed": e2e_passed,
        "components": components,
        "missing_by_category": all_missing,
        "data_migration_status": data.get("data_migration_status", "not_started"),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_crm_setup_check(data)
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
