#!/usr/bin/env python3
"""
run.py — Run an inter-phase retrospective and generate a structured findings and action item report.

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

FINDING_CATEGORIES = ["process", "technical", "communication", "tooling", "resourcing"]
IMPACT_LEVELS = ["high", "medium", "low"]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["phase_name", "velocity_actual", "velocity_planned", "findings"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "findings" in data:
        for i, f in enumerate(data["findings"]):
            for field in ["category", "description", "type", "impact"]:
                if field not in f:
                    errors.append(f"Finding[{i}] missing field: {field}")
    return errors


def run_retrospective(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    velocity_completion = round(data["velocity_actual"] / data["velocity_planned"] * 100, 1) if data["velocity_planned"] else 0

    findings = data["findings"]
    went_well = [f for f in findings if f["type"] == "went_well"]
    needs_improvement = [f for f in findings if f["type"] == "needs_improvement"]

    # Categorize by domain
    by_category: dict[str, list] = {c: [] for c in FINDING_CATEGORIES}
    for f in needs_improvement:
        cat = f.get("category", "process")
        if cat in by_category:
            by_category[cat].append(f)

    # Generate action items from high-impact improvement findings
    action_items = []
    for i, f in enumerate([x for x in needs_improvement if x.get("impact") == "high"], 1):
        action_items.append({
            "id": f"ACTION-{i:02d}",
            "finding": f["description"][:80],
            "action": f.get("suggested_action", f"Address: {f['description'][:60]}"),
            "owner": f.get("owner", "TBD"),
            "deadline": f.get("deadline", "Next phase Sprint 1"),
            "success_metric": f.get("success_metric", "No recurrence in next phase"),
        })

    ownerless = [a for a in action_items if a["owner"] == "TBD"]

    result = {
        "phase": data["phase_name"],
        "velocity_summary": {
            "planned": data["velocity_planned"],
            "actual": data["velocity_actual"],
            "completion_rate_pct": velocity_completion,
        },
        "findings_summary": {
            "total": len(findings),
            "went_well": len(went_well),
            "needs_improvement": len(needs_improvement),
        },
        "went_well": [f["description"] for f in went_well],
        "findings_by_category": {k: v for k, v in by_category.items() if v},
        "action_items": action_items,
        "warnings": (
            [f"{len(ownerless)} action items have no owner — assign before next sprint"] if ownerless else []
        ),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_retrospective(data)
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
