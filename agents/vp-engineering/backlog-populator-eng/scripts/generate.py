#!/usr/bin/env python3
"""
generate.py — Generate a prioritized engineering backlog from an approved specification.

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

PRIORITY_LABELS = {1: "P1-critical", 2: "P2-high", 3: "P3-medium", 4: "P4-low"}
SIZE_LABELS = {"XS": 1, "S": 2, "M": 5, "L": 8, "XL": 13}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["project_name", "spec_reference", "deliverables"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "deliverables" in data:
        for i, d in enumerate(data["deliverables"]):
            for f in ["name", "acceptance_criteria", "size"]:
                if f not in d:
                    errors.append(f"Deliverable[{i}] missing field: {f}")
    return errors


def generate_backlog(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    tasks = []
    task_counter = 1
    for d in data["deliverables"]:
        points = SIZE_LABELS.get(d["size"], 5)
        priority = d.get("priority", 2)
        is_critical_path = d.get("critical_path", False)
        tasks.append({
            "task_id": f"ENG-{task_counter:03d}",
            "title": d["name"],
            "acceptance_criteria": d["acceptance_criteria"],
            "size": d["size"],
            "story_points": points,
            "priority": PRIORITY_LABELS.get(priority, "P2-high"),
            "critical_path": is_critical_path,
            "dependencies": d.get("dependencies", []),
            "external_blockers": d.get("external_blockers", []),
            "spec_reference": data["spec_reference"],
            "status": "ready_for_sprint_planning",
        })
        task_counter += 1

    # Sort: critical path first, then by priority
    tasks.sort(key=lambda t: (not t["critical_path"], list(PRIORITY_LABELS.values()).index(t["priority"])))

    external_blockers = [t for t in tasks if t["external_blockers"]]
    total_points = sum(t["story_points"] for t in tasks)

    result = {
        "project": data["project_name"],
        "spec_reference": data["spec_reference"],
        "total_tasks": len(tasks),
        "total_story_points": total_points,
        "external_blockers": [
            {"task": t["task_id"], "blockers": t["external_blockers"]}
            for t in external_blockers
        ],
        "backlog": tasks,
        "warnings": (
            ["Some tasks have external blockers — resolve before sprint planning"] if external_blockers else []
        ),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_backlog(data)
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
