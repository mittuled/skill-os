#!/usr/bin/env python3
"""
run.py — Run the staging validation checklist before production promotion.

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

VALIDATION_AREAS = [
    "environment_version_match",
    "data_state_representative",
    "end_to_end_test_suite",
    "cross_service_integrations",
    "background_jobs_and_async_workflows",
    "observability_logs_metrics_traces",
    "infrastructure_smoke_tests",
]

BLOCKING_AREAS = [
    "environment_version_match",
    "end_to_end_test_suite",
    "observability_logs_metrics_traces",
]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["release_name", "validation_results"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def run_staging_validation(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    results = data["validation_results"]
    area_results = []
    for area in VALIDATION_AREAS:
        status = results.get(area, {})
        passed = status.get("passed", False)
        notes = status.get("notes", "")
        blocking = area in BLOCKING_AREAS
        area_results.append({
            "area": area,
            "passed": passed,
            "blocking": blocking,
            "notes": notes,
        })

    failed_blocking = [a for a in area_results if not a["passed"] and a["blocking"]]
    failed_non_blocking = [a for a in area_results if not a["passed"] and not a["blocking"]]
    all_passed = all(a["passed"] for a in area_results)

    if all_passed:
        recommendation = "PROCEED — all validation areas passed; promote to production"
    elif not failed_blocking:
        recommendation = "PROCEED WITH CAVEATS — non-blocking failures must be tracked and resolved post-promotion"
    else:
        recommendation = f"BLOCK — {len(failed_blocking)} blocking area(s) failed; do not promote to production"

    result = {
        "release": data["release_name"],
        "recommendation": recommendation,
        "passed_areas": [a["area"] for a in area_results if a["passed"]],
        "failed_blocking": [{"area": a["area"], "notes": a["notes"]} for a in failed_blocking],
        "failed_non_blocking": [{"area": a["area"], "notes": a["notes"]} for a in failed_non_blocking],
        "area_results": area_results,
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_staging_validation(data)
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
