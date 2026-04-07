#!/usr/bin/env python3
"""
run.py — Run regression test suite and produce a release recommendation.

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

SEVERITY_LEVELS = ["critical", "high", "medium", "low"]
BLOCKING_SEVERITIES = {"critical", "high"}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["release_name", "test_results", "suite_type"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def run_regression(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    results = data["test_results"]
    total = len(results)
    passed = [t for t in results if t.get("passed", False)]
    failed = [t for t in results if not t.get("passed", False)]

    genuine_regressions = [
        t for t in failed if t.get("failure_type") == "genuine_regression"
    ]
    blocking_regressions = [
        t for t in genuine_regressions if t.get("severity") in BLOCKING_SEVERITIES
    ]

    pass_rate = round(len(passed) / total * 100, 1) if total else 0

    if not genuine_regressions:
        recommendation = "APPROVE_RELEASE"
    elif not blocking_regressions:
        recommendation = "CONDITIONAL_RELEASE"
    else:
        recommendation = "HOLD_RELEASE"

    result = {
        "release": data["release_name"],
        "suite_type": data["suite_type"],
        "recommendation": recommendation,
        "summary": {
            "total": total,
            "passed": len(passed),
            "failed": len(failed),
            "pass_rate_pct": pass_rate,
            "genuine_regressions": len(genuine_regressions),
            "blocking_regressions": len(blocking_regressions),
        },
        "blocking_defects": blocking_regressions,
        "non_blocking_defects": [t for t in genuine_regressions if t not in blocking_regressions],
        "flaky_count": sum(1 for t in failed if t.get("failure_type") == "flaky_test"),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_regression(data)
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
