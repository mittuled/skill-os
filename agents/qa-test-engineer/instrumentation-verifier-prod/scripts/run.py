#!/usr/bin/env python3
"""
run.py — Verify production instrumentation signals fire correctly after deployment.

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


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["release_name", "verification_results"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    return errors


def run_prod_instrumentation_check(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    results = data["verification_results"]
    total = len(results)
    verified = [r for r in results if r.get("verified", False) and not r.get("payload_issue")]
    missing = [r for r in results if not r.get("verified", False)]
    payload_issues = [r for r in results if r.get("payload_issue", False)]
    all_ok = not missing and not payload_issues

    if all_ok:
        recommendation = "INSTRUMENTATION_HEALTHY"
    elif missing:
        recommendation = "INVESTIGATE_MISSING_SIGNALS"
    else:
        recommendation = "FIX_PAYLOAD_ISSUES"

    result = {
        "release": data["release_name"],
        "recommendation": recommendation,
        "summary": {
            "total": total,
            "healthy": len(verified),
            "missing": len(missing),
            "payload_issues": len(payload_issues),
        },
        "missing_signals": [{"signal": r["signal_name"], "type": r.get("signal_type"), "notes": r.get("notes", "")} for r in missing],
        "payload_issues": [{"signal": r["signal_name"], "detail": r.get("payload_issue_detail", "")} for r in payload_issues],
        "rollback_recommended": len(missing) > len(verified),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_prod_instrumentation_check(data)
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
