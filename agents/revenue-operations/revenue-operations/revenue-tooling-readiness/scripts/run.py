#!/usr/bin/env python3
"""
run.py — Validate revenue tooling readiness across CRM, billing, CPQ, and analytics before go-live.

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

# Required revenue tools
REQUIRED_TOOLS = ["crm", "billing", "analytics"]

# Blocking tools (failure = no-go)
BLOCKING_TOOLS = {"crm", "billing"}

# Readiness criteria per tool
TOOL_READINESS_CRITERIA = {
    "crm": ["data_flowing", "automations_firing", "reports_accurate", "user_access_configured"],
    "billing": ["test_invoice_sent", "payment_method_configured", "revenue_recognition_rules_set", "subscription_lifecycle_tested"],
    "cpq": ["product_catalog_loaded", "pricing_rules_configured", "discount_approval_workflow_set"],
    "analytics": ["dashboards_populated", "data_refresh_scheduled", "kpi_definitions_confirmed"],
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    if "tools" not in data:
        errors.append("Missing required field: tools")
        return errors
    for i, t in enumerate(data["tools"]):
        for f in ["name", "criteria_passed"]:
            if f not in t:
                errors.append(f"tools[{i}] missing field: {f}")
    return errors


def assess_tool(tool: dict) -> dict:
    name = tool["name"]
    passed = set(tool.get("criteria_passed", []))
    required = set(TOOL_READINESS_CRITERIA.get(name, []))
    failed = list(required - passed) if required else []
    is_blocking = name in BLOCKING_TOOLS
    completeness_pct = round(len(required - set(failed)) / len(required) * 100) if required else 100

    if failed:
        status = "FAIL"
    else:
        status = "PASS"

    return {
        "tool": name,
        "status": status,
        "is_blocking": is_blocking,
        "completeness_pct": completeness_pct,
        "criteria_passed": list(passed),
        "criteria_failed": failed,
        "issues": tool.get("issues", []),
    }


def run_tooling_check(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    tools = [assess_tool(t) for t in data["tools"]]

    # Check for missing required tools
    configured_tools = {t["tool"] for t in tools}
    missing_required = list(set(REQUIRED_TOOLS) - configured_tools)

    blocking_failures = [t for t in tools if t["is_blocking"] and t["status"] == "FAIL"]
    non_blocking_failures = [t for t in tools if not t["is_blocking"] and t["status"] == "FAIL"]

    e2e_passed = data.get("e2e_transaction_passed", False)

    if missing_required or blocking_failures or not e2e_passed:
        verdict = "NO_GO"
        recommendation = (
            "GO-LIVE BLOCKED — " +
            (f"Required tools missing: {missing_required}. " if missing_required else "") +
            (f"Blocking tool failures: {[t['tool'] for t in blocking_failures]}. " if blocking_failures else "") +
            ("End-to-end transaction test not passed." if not e2e_passed else "")
        ).strip()
    elif non_blocking_failures:
        verdict = "CONDITIONAL_GO"
        recommendation = f"Go-live permitted with tracked remediation for non-blocking tools: {[t['tool'] for t in non_blocking_failures]}"
    else:
        verdict = "GO"
        recommendation = "All revenue tooling validated — clear for go-live"

    result = {
        "go_live_date": data.get("go_live_date", ""),
        "verdict": verdict,
        "recommendation": recommendation,
        "e2e_transaction_passed": e2e_passed,
        "tools": tools,
        "missing_required_tools": missing_required,
        "blocking_failures": [t["tool"] for t in blocking_failures],
        "total_tools_checked": len(tools),
        "tools_passing": sum(1 for t in tools if t["status"] == "PASS"),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_tooling_check(data)
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
