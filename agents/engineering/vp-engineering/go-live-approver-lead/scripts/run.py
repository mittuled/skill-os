#!/usr/bin/env python3
"""
run.py — Run the VP-level go-live approval checklist for production releases.

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

# Required quality gates for go-live approval
QUALITY_GATES = [
    "tech_lead_approval_complete",
    "ci_cd_pipeline_green",
    "no_open_p0_p1_bugs",
    "regression_suite_passed",
    "test_coverage_meets_threshold",
]

# Required operational readiness checks
OPERATIONAL_CHECKS = [
    "runbooks_exist",
    "alerting_configured_to_slos",
    "rollback_procedure_documented_and_tested",
    "oncall_rotation_staffed",
]

# Risk register severity levels
RISK_LEVELS = {"low": 1, "medium": 2, "high": 3, "critical": 4}


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    required = ["release_name", "quality_gate_status", "operational_readiness", "open_risks"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    return errors


def evaluate_quality_gates(gate_status: dict) -> tuple[list[str], list[str]]:
    """Return (passed, failed) quality gate lists."""
    passed = [g for g in QUALITY_GATES if gate_status.get(g, False)]
    failed = [g for g in QUALITY_GATES if not gate_status.get(g, False)]
    return passed, failed


def evaluate_operational_readiness(ops_status: dict) -> tuple[list[str], list[str]]:
    """Return (ready, not_ready) operational check lists."""
    ready = [c for c in OPERATIONAL_CHECKS if ops_status.get(c, False)]
    not_ready = [c for c in OPERATIONAL_CHECKS if not ops_status.get(c, False)]
    return ready, not_ready


def assess_risks(open_risks: list[dict]) -> tuple[list[dict], bool]:
    """Identify unmitigated high/critical risks. Returns (high_risks, has_blocking_risk)."""
    high_risks = [
        r for r in open_risks
        if RISK_LEVELS.get(r.get("severity", "low"), 1) >= 3
        and not r.get("mitigated", False)
    ]
    blocking = any(r.get("severity") == "critical" and not r.get("accepted", False) for r in high_risks)
    return high_risks, blocking


def run_go_live_approval(data: dict) -> dict:
    """Run the full go-live approval check."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    passed_gates, failed_gates = evaluate_quality_gates(data["quality_gate_status"])
    ready_ops, not_ready_ops = evaluate_operational_readiness(data["operational_readiness"])
    high_risks, has_blocking_risk = assess_risks(data.get("open_risks", []))

    # Decision logic
    critical_blockers = failed_gates + not_ready_ops
    if has_blocking_risk:
        critical_blockers.append("Unmitigated critical risk in risk register")

    if not critical_blockers:
        decision = "APPROVED"
        rationale = "All quality gates passed, operational readiness confirmed, no blocking risks"
    elif len(critical_blockers) <= 2 and not has_blocking_risk and not failed_gates:
        decision = "CONDITIONALLY_APPROVED"
        rationale = f"Minor operational gaps ({', '.join(not_ready_ops)}) must be resolved post-launch within 48h"
    else:
        decision = "BLOCKED"
        rationale = f"Blocking criteria not met: {'; '.join(critical_blockers[:3])}"

    result = {
        "release": data["release_name"],
        "decision": decision,
        "rationale": rationale,
        "quality_gates": {
            "passed": passed_gates,
            "failed": failed_gates,
            "all_passed": len(failed_gates) == 0,
        },
        "operational_readiness": {
            "ready": ready_ops,
            "not_ready": not_ready_ops,
            "fully_ready": len(not_ready_ops) == 0,
        },
        "risk_assessment": {
            "high_unmitigated_risks": high_risks,
            "blocking_risk_present": has_blocking_risk,
        },
        "post_launch_follow_ups": data.get("post_launch_follow_ups", []),
        "approved_by": "VP Engineering",
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_go_live_approval(data)
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
