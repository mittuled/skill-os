#!/usr/bin/env python3
"""
run.py — Operate the IT helpdesk: triage tickets, assign priorities, and generate resolution plans.

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

# Ticket categories with typical resolution steps
TICKET_CATEGORIES = {
    "password_reset": {
        "label": "Password / Account Lockout",
        "sla_hours": 1,
        "steps": [
            "Verify user identity (employee ID or manager confirmation)",
            "Reset password in SSO provider (Okta/Google)",
            "Send temporary password via secure channel (not email)",
            "Confirm user can log in",
            "Check if MFA needs re-enrollment",
        ],
    },
    "hardware_issue": {
        "label": "Hardware Issue",
        "sla_hours": 4,
        "steps": [
            "Gather symptoms: what fails, when it started, recent changes",
            "Remote diagnostic if possible (screen sharing)",
            "Determine repair vs. replacement",
            "If replacement: pull loaner from spare hardware inventory",
            "Schedule data migration if needed",
            "Document in asset tracker",
        ],
    },
    "software_install": {
        "label": "Software Installation",
        "sla_hours": 2,
        "steps": [
            "Confirm software is on approved list",
            "Check if business justification is provided for unapproved tools",
            "Deploy via MDM (Jamf/Intune) for managed devices",
            "Confirm installation and licence assignment",
        ],
    },
    "access_request": {
        "label": "Access Request",
        "sla_hours": 4,
        "steps": [
            "Confirm manager approval for requested system",
            "Verify role-based access policy allows this access",
            "Provision in SSO and target system",
            "Confirm access is working",
            "Document in access log",
        ],
    },
    "connectivity": {
        "label": "Network / Connectivity Issue",
        "sla_hours": 2,
        "steps": [
            "Confirm if issue is VPN, WiFi, or application-specific",
            "Try basic restart (device, router, VPN reconnect)",
            "Check service status pages for affected systems",
            "Escalate to network admin if infrastructure issue",
        ],
    },
    "email_issue": {
        "label": "Email / Calendar Issue",
        "sla_hours": 2,
        "steps": [
            "Check mailbox quota and sync status",
            "Re-authenticate mail client",
            "Check spam/quarantine for missing messages",
            "Verify email routing rules are not misdirecting mail",
        ],
    },
    "data_recovery": {
        "label": "Data Recovery",
        "sla_hours": 8,
        "steps": [
            "Identify source of data loss (accidental delete, device failure)",
            "Check cloud backup (Google Drive, iCloud, Backblaze)",
            "Check version history in applicable tools (Notion, Google Docs)",
            "Escalate to IT Manager if backup recovery required",
        ],
    },
    "other": {
        "label": "Other / General",
        "sla_hours": 8,
        "steps": ["Gather full issue description", "Reproduce issue if possible", "Research and resolve or escalate"],
    },
}

# Priority matrix
PRIORITY_MAP = {
    ("high", True): "P1",   # High impact, affecting multiple users
    ("high", False): "P2",  # High impact, single user
    ("medium", True): "P2",
    ("medium", False): "P3",
    ("low", True): "P3",
    ("low", False): "P4",
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "tickets" not in data or not isinstance(data["tickets"], list):
        errors.append("Missing required field: tickets (list)")
    return errors


def run_helpdesk(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    tickets = data["tickets"]

    processed = []
    by_priority: dict[str, list] = {"P1": [], "P2": [], "P3": [], "P4": []}

    for ticket in tickets:
        category = ticket.get("category", "other")
        if category not in TICKET_CATEGORIES:
            category = "other"
        cat_config = TICKET_CATEGORIES[category]
        impact = ticket.get("impact", "medium")
        affects_multiple = ticket.get("affects_multiple_users", False)
        priority = PRIORITY_MAP.get((impact, affects_multiple), "P3")
        sla_hours = cat_config["sla_hours"]

        entry = {
            "ticket_id": ticket.get("ticket_id", f"INC-{len(processed)+1:03}"),
            "requester": ticket["requester"],
            "category": cat_config["label"],
            "description": ticket.get("description", ""),
            "priority": priority,
            "sla_hours": sla_hours,
            "resolution_steps": cat_config["steps"],
            "status": ticket.get("status", "open"),
            "affects_multiple_users": affects_multiple,
        }
        processed.append(entry)
        by_priority[priority].append(entry)

    # Sort by priority
    priority_order = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}
    processed.sort(key=lambda x: priority_order[x["priority"]])

    open_tickets = [t for t in processed if t["status"] == "open"]
    p1_p2 = [t for t in processed if t["priority"] in ("P1", "P2") and t["status"] == "open"]

    return {
        "error": None,
        "result": {
            "company": company,
            "total_tickets": len(tickets),
            "open_tickets": len(open_tickets),
            "p1_p2_requiring_action": len(p1_p2),
            "priority_breakdown": {k: len(v) for k, v in by_priority.items()},
            "tickets": processed,
            "summary": (
                f"Helpdesk for {company}: {len(open_tickets)}/{len(tickets)} tickets open. "
                f"P1: {len(by_priority['P1'])}, P2: {len(by_priority['P2'])}, "
                f"P3: {len(by_priority['P3'])}, P4: {len(by_priority['P4'])}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_helpdesk(data)
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
