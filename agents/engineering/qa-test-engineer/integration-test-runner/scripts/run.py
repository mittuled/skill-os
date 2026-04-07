#!/usr/bin/env python3
"""
run.py — Run integration test suite and report cross-boundary failures.

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

FAILURE_TYPES = ["genuine_defect", "flaky_test", "environment_issue"]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["suite_name", "test_results"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "test_results" in data:
        for i, t in enumerate(data["test_results"]):
            for f in ["test_name", "passed"]:
                if f not in t:
                    errors.append(f"test_results[{i}] missing field: {f}")
    return errors


def run_integration_tests(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    results = data["test_results"]
    total = len(results)
    passed = [t for t in results if t["passed"]]
    failed = [t for t in results if not t["passed"]]

    genuine_defects = [t for t in failed if t.get("failure_type") == "genuine_defect"]
    flaky = [t for t in failed if t.get("failure_type") == "flaky_test"]
    env_issues = [t for t in failed if t.get("failure_type") == "environment_issue"]

    pass_rate = round(len(passed) / total * 100, 1) if total > 0 else 0

    if not genuine_defects:
        recommendation = "MERGE_APPROVED" if pass_rate >= 95 else "MERGE_WITH_CAUTION"
    else:
        recommendation = "BLOCK_MERGE"

    result = {
        "suite": data["suite_name"],
        "recommendation": recommendation,
        "summary": {
            "total": total,
            "passed": len(passed),
            "failed": len(failed),
            "pass_rate_pct": pass_rate,
        },
        "genuine_defects": genuine_defects,
        "flaky_tests": [t["test_name"] for t in flaky],
        "environment_issues": [t["test_name"] for t in env_issues],
        "defects_requiring_tickets": len(genuine_defects),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_integration_tests(data)
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
