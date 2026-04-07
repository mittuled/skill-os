#!/usr/bin/env python3
"""
run.py — Run unit test suite and validate coverage meets threshold.

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

DEFAULT_COVERAGE_THRESHOLD = 80.0


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["suite_name", "passed", "failed", "coverage_pct"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def run_unit_tests(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    passed = data["passed"]
    failed = data["failed"]
    coverage = data["coverage_pct"]
    threshold = data.get("coverage_threshold_pct", DEFAULT_COVERAGE_THRESHOLD)
    total = passed + failed

    coverage_met = coverage >= threshold
    no_failures = failed == 0

    if no_failures and coverage_met:
        verdict = "PASS"
        recommendation = "PR approved — all tests pass and coverage threshold met"
    elif no_failures and not coverage_met:
        verdict = "COVERAGE_FAIL"
        recommendation = f"Coverage {coverage}% below {threshold}% threshold — add tests before merge"
    elif not no_failures and coverage_met:
        verdict = "TEST_FAIL"
        recommendation = f"{failed} test(s) failing — fix before merge"
    else:
        verdict = "FAIL"
        recommendation = f"{failed} test(s) failing and coverage {coverage}% below {threshold}% — both must be resolved"

    result = {
        "suite": data["suite_name"],
        "verdict": verdict,
        "recommendation": recommendation,
        "summary": {
            "total": total,
            "passed": passed,
            "failed": failed,
            "coverage_pct": coverage,
            "coverage_threshold_pct": threshold,
            "coverage_met": coverage_met,
        },
        "failing_tests": data.get("failing_tests", []),
        "coverage_delta": data.get("coverage_delta_pct", None),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_unit_tests(data)
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
