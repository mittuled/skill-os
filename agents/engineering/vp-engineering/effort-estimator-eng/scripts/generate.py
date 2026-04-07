#!/usr/bin/env python3
"""
generate.py — Generate an engineering effort estimate with confidence intervals and risk buffers.

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

COMPLEXITY_MULTIPLIERS = {"simple": 1.0, "medium": 1.5, "complex": 2.5}
RISK_BUFFERS = {"low": 1.2, "medium": 1.5, "high": 2.0}
CONFIDENCE_INTERVALS = {"low": (0.5, 2.0), "medium": (0.7, 1.4), "high": (0.85, 1.15)}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["project_name", "work_streams", "team_velocity_points_per_sprint", "risk_level"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "risk_level" in data and data["risk_level"] not in RISK_BUFFERS:
        errors.append(f"risk_level must be one of: {list(RISK_BUFFERS.keys())}")
    if "work_streams" in data:
        for i, ws in enumerate(data["work_streams"]):
            for f in ["name", "complexity", "base_points"]:
                if f not in ws:
                    errors.append(f"WorkStream[{i}] missing field: {f}")
    return errors


def generate_estimate(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    velocity = data["team_velocity_points_per_sprint"]
    risk_level = data["risk_level"]
    buffer = RISK_BUFFERS[risk_level]
    ci_low_mult, ci_high_mult = CONFIDENCE_INTERVALS[risk_level]

    work_streams = []
    total_base = 0
    for ws in data["work_streams"]:
        base = ws["base_points"]
        complexity = ws.get("complexity", "medium")
        multiplier = COMPLEXITY_MULTIPLIERS.get(complexity, 1.5)
        adjusted = round(base * multiplier)
        total_base += adjusted
        work_streams.append({
            "name": ws["name"],
            "complexity": complexity,
            "base_points": base,
            "adjusted_points": adjusted,
            "notes": ws.get("notes", ""),
        })

    buffered_total = round(total_base * buffer)
    sprints_expected = round(buffered_total / velocity, 1)
    sprints_low = round((total_base * ci_low_mult * buffer) / velocity, 1)
    sprints_high = round((total_base * ci_high_mult * buffer) / velocity, 1)

    result = {
        "project": data["project_name"],
        "work_streams": work_streams,
        "estimate": {
            "base_points": total_base,
            "buffered_points": buffered_total,
            "risk_buffer_multiplier": buffer,
            "risk_level": risk_level,
            "sprints_expected": sprints_expected,
            "confidence_interval_sprints": f"{sprints_low}–{sprints_high}",
        },
        "assumptions": data.get("assumptions", [
            f"Team velocity: {velocity} points/sprint",
            f"Risk buffer: {risk_level} ({buffer}x)",
            "Estimates do not include integration, testing, or deployment overhead beyond complexity multiplier",
        ]),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_estimate(data)
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
