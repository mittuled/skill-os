#!/usr/bin/env python3
"""
generate.py — Generate an engineering team allocation plan for a delivery.

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

TARGET_UTILIZATION_MIN = 0.70
TARGET_UTILIZATION_MAX = 0.80


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["project_name", "engineers", "work_streams"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def generate_allocation(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    engineers = data["engineers"]
    work_streams = data["work_streams"]

    # Simple greedy allocation: assign best-fit engineers to each work stream
    allocations = []
    engineer_load: dict[str, float] = {e["name"]: e.get("current_allocation_pct", 0) for e in engineers}

    skill_gaps = []
    for ws in work_streams:
        required_skills = set(ws.get("required_skills", []))
        capacity_needed = ws.get("capacity_pct_needed", 50)

        # Find engineers with matching skills and available capacity
        candidates = []
        for eng in engineers:
            eng_skills = set(eng.get("skills", []))
            skill_match = required_skills.issubset(eng_skills) or not required_skills
            available = 100 - engineer_load.get(eng["name"], 0)
            if skill_match and available >= capacity_needed:
                candidates.append(eng)

        if candidates:
            assigned = candidates[0]
            engineer_load[assigned["name"]] += capacity_needed
            allocations.append({
                "work_stream": ws["name"],
                "assigned_engineer": assigned["name"],
                "allocation_pct": capacity_needed,
                "skill_fit": "full" if required_skills.issubset(set(assigned.get("skills", []))) else "partial",
            })
        else:
            skill_gaps.append(ws["name"])

    # Compute utilization per engineer
    utilization = []
    for eng in engineers:
        total = engineer_load.get(eng["name"], 0)
        status = "optimal" if TARGET_UTILIZATION_MIN * 100 <= total <= TARGET_UTILIZATION_MAX * 100 else (
            "over_allocated" if total > TARGET_UTILIZATION_MAX * 100 else "under_utilized"
        )
        utilization.append({"engineer": eng["name"], "total_allocation_pct": total, "status": status})

    result = {
        "project": data["project_name"],
        "allocations": allocations,
        "utilization": utilization,
        "skill_gaps": skill_gaps,
        "warnings": [f"No available engineer for work stream: {ws}" for ws in skill_gaps],
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_allocation(data)
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
