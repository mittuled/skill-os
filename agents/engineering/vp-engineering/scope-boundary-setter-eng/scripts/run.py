#!/usr/bin/env python3
"""
run.py — Run scope boundary enforcement for a delivery, classifying items as in/out of scope.

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

CHANGE_APPROVAL_LEVELS = {
    "minor": "Tech Lead",
    "medium": "VP Engineering",
    "major": "VP Engineering + CTO",
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["project_name", "in_scope", "out_of_scope"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def evaluate_change_requests(changes: list[dict]) -> list[dict]:
    results = []
    for req in changes:
        size = req.get("size", "minor")
        approved = req.get("impact_assessed", False) and req.get("requester_approved", False)
        results.append({
            "request_id": req.get("id", "CHANGE-?"),
            "description": req.get("description", ""),
            "size": size,
            "approval_required": CHANGE_APPROVAL_LEVELS.get(size, "VP Engineering"),
            "approved": approved,
            "decision": "APPROVED" if approved else "PENDING_REVIEW",
        })
    return results


def run_scope_boundary(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    change_log = evaluate_change_requests(data.get("change_requests", []))
    pending = [c for c in change_log if c["decision"] == "PENDING_REVIEW"]

    result = {
        "project": data["project_name"],
        "in_scope": data["in_scope"],
        "out_of_scope": data["out_of_scope"],
        "change_control_process": {
            "minor": "Tech Lead review within 24h; no timeline adjustment",
            "medium": "VP Engineering review within 48h; timeline impact assessment required",
            "major": "VP Engineering + CTO; formal scope change document required",
        },
        "change_log": change_log,
        "pending_approvals": len(pending),
        "scope_health": "CLEAN" if not pending else f"{len(pending)} change request(s) awaiting approval",
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_scope_boundary(data)
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
