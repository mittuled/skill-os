#!/usr/bin/env python3
"""
run.py — Verify instrumentation signals in QA environment before staging promotion.

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

SIGNAL_TYPES = ["log_entry", "metric", "trace_span"]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["feature_name", "expected_signals"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "expected_signals" in data:
        for i, s in enumerate(data["expected_signals"]):
            for field in ["signal_name", "signal_type", "verified"]:
                if field not in s:
                    errors.append(f"expected_signals[{i}] missing field: {field}")
    return errors


def run_instrumentation_check(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    signals = data["expected_signals"]
    total = len(signals)
    passed = [s for s in signals if s["verified"] and not s.get("payload_issue", False)]
    failed = [s for s in signals if not s["verified"]]
    payload_issues = [s for s in signals if s.get("payload_issue", False)]

    blocking = failed  # all missing signals are blocking

    if not failed and not payload_issues:
        recommendation = "PROMOTE_TO_STAGING"
        verdict = "All instrumentation signals verified — ready for staging"
    elif not failed and payload_issues:
        recommendation = "FIX_THEN_PROMOTE"
        verdict = f"{len(payload_issues)} signal(s) have malformed payloads — fix before staging"
    else:
        recommendation = "BLOCK_PROMOTION"
        verdict = f"{len(failed)} signal(s) not firing — fix before staging"

    result = {
        "feature": data["feature_name"],
        "recommendation": recommendation,
        "verdict": verdict,
        "summary": {
            "total_signals": total,
            "verified": len(passed),
            "missing": len(failed),
            "payload_issues": len(payload_issues),
        },
        "failing_signals": [{"signal": s["signal_name"], "type": s["signal_type"], "notes": s.get("notes", "")} for s in failed],
        "payload_issue_signals": [{"signal": s["signal_name"], "issue": s.get("payload_issue_detail", "")} for s in payload_issues],
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_instrumentation_check(data)
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
