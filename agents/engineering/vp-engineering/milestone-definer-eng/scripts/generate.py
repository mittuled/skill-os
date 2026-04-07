#!/usr/bin/env python3
"""
generate.py — Generate an engineering milestone register with success criteria.

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


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["project_name", "milestones"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "milestones" in data:
        for i, m in enumerate(data["milestones"]):
            for f in ["name", "target_date", "success_criteria"]:
                if f not in m:
                    errors.append(f"Milestone[{i}] missing field: {f}")
            if not isinstance(m.get("success_criteria", []), list):
                errors.append(f"Milestone[{i}] success_criteria must be a list")
    return errors


def generate_milestone_register(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    milestones = []
    for i, m in enumerate(data["milestones"]):
        criteria = m["success_criteria"]
        # Check for vanity milestones (activity-based rather than outcome-based)
        vanity_signals = ["complete", "done", "finished", "implemented"]
        has_vanity = any(
            any(s in c.lower() for s in vanity_signals) and "returns" not in c.lower() and "%" not in c
            for c in criteria
        )
        milestones.append({
            "id": f"M{i+1:02d}",
            "name": m["name"],
            "target_date": m["target_date"],
            "responsible_team": m.get("responsible_team", "Engineering"),
            "success_criteria": criteria,
            "criteria_count": len(criteria),
            "dependencies": m.get("dependencies", []),
            "type": m.get("type", "delivery"),
            "vanity_milestone_warning": has_vanity,
        })

    vanity_count = sum(1 for m in milestones if m["vanity_milestone_warning"])

    result = {
        "project": data["project_name"],
        "total_milestones": len(milestones),
        "milestones": milestones,
        "warnings": (
            [f"{vanity_count} milestone(s) may have activity-based criteria — verify they test outcomes, not activities"]
            if vanity_count else []
        ),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_milestone_register(data)
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
