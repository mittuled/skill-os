#!/usr/bin/env python3
"""
run.py — Manage user access provisioning and deprovisioning across systems.

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

# Access request types
REQUEST_TYPES = {
    "onboarding": "New employee — full provisioning per role template",
    "offboarding": "Departing employee — full deprovisioning and access revocation",
    "role_change": "Internal transfer — adjust access to match new role",
    "additional_access": "Access expansion for existing employee",
    "access_audit": "Periodic access review and cleanup",
}

# Role-based access templates
ROLE_TEMPLATES = {
    "engineer": ["GitHub", "Slack", "Notion", "Zoom", "1Password", "AWS (dev)", "Jira"],
    "senior_engineer": ["GitHub", "Slack", "Notion", "Zoom", "1Password", "AWS (dev)", "AWS (staging)", "Jira", "PagerDuty"],
    "designer": ["Figma", "Slack", "Notion", "Zoom", "1Password", "GitHub (read-only)"],
    "product_manager": ["Jira", "Slack", "Notion", "Zoom", "1Password", "Mixpanel", "GitHub (read-only)"],
    "sales": ["Salesforce", "Slack", "Notion", "Zoom", "1Password", "Outreach"],
    "marketing": ["HubSpot", "Slack", "Notion", "Zoom", "1Password", "Mixpanel"],
    "executive": ["All systems", "Slack", "Notion", "Zoom", "1Password", "AWS (read-only)", "Salesforce", "GitHub"],
    "hr": ["Rippling", "Slack", "Notion", "Zoom", "1Password"],
    "finance": ["QuickBooks", "Slack", "Notion", "Zoom", "1Password", "Salesforce (read-only)"],
    "legal": ["Ironclad", "Slack", "Notion", "Zoom", "1Password"],
    "support": ["Intercom", "Slack", "Notion", "Zoom", "1Password"],
    "default": ["Slack", "Notion", "Zoom", "1Password"],
}

# SLA targets in hours
SLA_HOURS = {
    "onboarding": 4,
    "offboarding": 1,  # Immediate priority for security
    "role_change": 24,
    "additional_access": 8,
    "access_audit": 48,
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "request_type" not in data or data.get("request_type") not in REQUEST_TYPES:
        errors.append(f"Missing or invalid field: request_type ({'/'.join(REQUEST_TYPES.keys())})")
    if "employee_name" not in data:
        errors.append("Missing required field: employee_name")
    return errors


def run_access_provisioning(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    request_type = data["request_type"]
    employee = data["employee_name"]
    role = data.get("role", "default").lower().replace(" ", "_").replace("-", "_")
    department = data.get("department", "")
    manager = data.get("manager", "")
    start_or_end_date = data.get("date", "")
    additional_systems = data.get("additional_systems", [])
    systems_to_revoke = data.get("systems_to_revoke", [])
    notes = data.get("notes", "")

    sla = SLA_HOURS.get(request_type, 8)

    # Get access list based on request type
    if request_type == "onboarding":
        base_access = ROLE_TEMPLATES.get(role, ROLE_TEMPLATES["default"])
        access_to_grant = list(set(base_access + additional_systems))
        access_to_revoke = []
        checklist_items = [
            f"Create identity in SSO provider (Okta/Google Workspace) for {employee}",
            "Set temporary password and enforce change at first login",
            "Enrol in MFA (authenticator app) — mandatory before first login",
            f"Provision all systems per {role} role template",
            "Add to relevant Slack channels per department",
            "Send welcome email with IT onboarding guide",
            "Schedule 15-minute IT onboarding call",
            "Confirm all access is working end-of-day 1",
        ]
    elif request_type == "offboarding":
        access_to_grant = []
        access_to_revoke = systems_to_revoke if systems_to_revoke else ROLE_TEMPLATES.get(role, ROLE_TEMPLATES["default"])
        checklist_items = [
            f"Immediately revoke SSO access for {employee}",
            "Invalidate all active sessions and API tokens",
            "Transfer owned files (Google Drive, Notion, GitHub) to manager",
            "Remove from all Slack channels and shared DMs",
            "Retrieve hardware per offboarding checklist",
            "Revoke access to all SaaS applications",
            "Archive email and forward to manager for 30 days",
            "Remove from distribution lists and org chart",
            "Update cap table if applicable (equity vesting stop date)",
            "Confirm offboarding complete with HR",
        ]
    elif request_type == "role_change":
        new_role = data.get("new_role", "default").lower().replace(" ", "_")
        old_access = set(ROLE_TEMPLATES.get(role, ROLE_TEMPLATES["default"]))
        new_access = set(ROLE_TEMPLATES.get(new_role, ROLE_TEMPLATES["default"]))
        access_to_grant = list(new_access - old_access) + additional_systems
        access_to_revoke = list(old_access - new_access) + systems_to_revoke
        checklist_items = [
            f"Provision new access for {new_role} role",
            "Revoke access no longer required for new role",
            "Update department and manager in SSO provider",
            "Confirm new access is working with employee",
        ]
    else:
        access_to_grant = additional_systems
        access_to_revoke = systems_to_revoke
        checklist_items = [
            f"Grant requested access to: {', '.join(additional_systems)}",
            "Document business justification for non-standard access",
            "Manager approval obtained before provisioning",
            "Set access expiry date if temporary",
        ]

    return {
        "error": None,
        "result": {
            "company": company,
            "request_type": request_type,
            "request_description": REQUEST_TYPES[request_type],
            "employee": employee,
            "role": role,
            "department": department,
            "manager": manager,
            "date": start_or_end_date,
            "sla_hours": sla,
            "access_to_grant": access_to_grant,
            "access_to_revoke": access_to_revoke,
            "checklist": checklist_items,
            "notes": notes,
            "summary": (
                f"{REQUEST_TYPES[request_type]} for {employee} ({role}, {department}). "
                f"SLA: {sla} hours. "
                f"Systems to grant: {len(access_to_grant)}, revoke: {len(access_to_revoke)}."
                + (f" Date: {start_or_end_date}." if start_or_end_date else "")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_access_provisioning(data)
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
