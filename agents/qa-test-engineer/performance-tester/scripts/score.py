#!/usr/bin/env python3
"""
score.py — Score performance test results against budget and produce a release verdict.

Usage:
    echo '<json>' | python3 score.py
    python3 score.py < input.json
    python3 score.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# Default performance budget thresholds (can be overridden by input)
DEFAULT_BUDGET = {
    "p50_latency_ms": 100,
    "p95_latency_ms": 300,
    "p99_latency_ms": 1000,
    "throughput_rps": 500,
    "error_rate_pct": 1.0,
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["endpoint", "measured"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "measured" in data:
        for m in ["p50_latency_ms", "p95_latency_ms", "p99_latency_ms", "throughput_rps", "error_rate_pct"]:
            if m not in data["measured"]:
                errors.append(f"measured missing metric: {m}")
    return errors


def score_performance(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    budget = {**DEFAULT_BUDGET, **data.get("budget", {})}
    measured = data["measured"]

    comparisons = {}
    violations = []

    # Latency: lower is better
    for metric in ["p50_latency_ms", "p95_latency_ms", "p99_latency_ms"]:
        actual = measured[metric]
        limit = budget[metric]
        passed = actual <= limit
        pct_over = round(((actual - limit) / limit) * 100, 1) if not passed else 0
        comparisons[metric] = {"actual": actual, "budget": limit, "passed": passed, "pct_over": pct_over}
        if not passed:
            violations.append(f"{metric}: {actual}ms vs budget {limit}ms (+{pct_over}%)")

    # Throughput: higher is better
    actual_tp = measured["throughput_rps"]
    budget_tp = budget["throughput_rps"]
    tp_passed = actual_tp >= budget_tp
    comparisons["throughput_rps"] = {"actual": actual_tp, "budget": budget_tp, "passed": tp_passed}
    if not tp_passed:
        violations.append(f"throughput: {actual_tp} rps vs budget {budget_tp} rps")

    # Error rate: lower is better
    actual_err = measured["error_rate_pct"]
    budget_err = budget["error_rate_pct"]
    err_passed = actual_err <= budget_err
    comparisons["error_rate_pct"] = {"actual": actual_err, "budget": budget_err, "passed": err_passed}
    if not err_passed:
        violations.append(f"error_rate: {actual_err}% vs budget {budget_err}%")

    if not violations:
        verdict = "PASS"
        recommendation = "Release approved — all performance budgets met"
    else:
        verdict = "FAIL"
        recommendation = f"Release blocked — {len(violations)} budget violation(s): {'; '.join(violations[:2])}"

    result = {
        "endpoint": data["endpoint"],
        "verdict": verdict,
        "recommendation": recommendation,
        "comparisons": comparisons,
        "violations": violations,
        "baseline_regression": data.get("baseline_regression", {}),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_performance(data)
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
