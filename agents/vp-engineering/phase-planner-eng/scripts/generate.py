#!/usr/bin/env python3
"""
generate.py — Generate an engineering phase plan with sprint timeline and critical path.

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

SLACK_BUFFER_PCT = 0.80  # target 80% sprint capacity to preserve slack


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for field in ["project_name", "phases", "team_capacity_points_per_sprint"]:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "phases" in data:
        for i, p in enumerate(data["phases"]):
            for f in ["name", "tasks"]:
                if f not in p:
                    errors.append(f"Phase[{i}] missing field: {f}")
    return errors


def generate_phase_plan(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    capacity = data["team_capacity_points_per_sprint"] * SLACK_BUFFER_PCT
    phases_output = []
    sprint_counter = 1

    for phase in data["phases"]:
        total_points = sum(t.get("points", 3) for t in phase["tasks"])
        sprints_needed = max(1, round(total_points / capacity + 0.5))
        critical_path = [t["name"] for t in phase["tasks"] if t.get("critical_path", False)]

        phases_output.append({
            "phase_name": phase["name"],
            "entry_criteria": phase.get("entry_criteria", "Previous phase exit criteria met"),
            "exit_criteria": phase.get("exit_criteria", "All tasks complete and acceptance criteria verified"),
            "total_story_points": total_points,
            "sprints_required": sprints_needed,
            "sprint_range": f"Sprint {sprint_counter}–{sprint_counter + sprints_needed - 1}",
            "critical_path_tasks": critical_path,
            "risks": phase.get("risks", []),
            "tasks": phase["tasks"],
        })
        sprint_counter += sprints_needed

    result = {
        "project": data["project_name"],
        "total_sprints": sprint_counter - 1,
        "team_effective_capacity_per_sprint": capacity,
        "phases": phases_output,
        "assumptions": [
            f"Sprint capacity set to {SLACK_BUFFER_PCT*100:.0f}% of total to preserve unplanned-work buffer",
            "All dependencies resolved before phase start unless noted",
        ],
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_phase_plan(data)
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
