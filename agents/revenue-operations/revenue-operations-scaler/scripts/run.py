#!/usr/bin/env python3
"""
run.py — Audit RevOps capacity bottlenecks and produce a scaling plan.

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

# Bottleneck categories and impact weights
BOTTLENECK_IMPACT = {
    "revenue_at_risk": 3,       # Direct revenue impact
    "team_productivity_loss": 2, # Indirect cost from manual work
    "data_quality_degradation": 2,
    "reporting_latency": 1,
    "customer_experience": 3,
}

# Recommended scaling approaches by bottleneck type
SCALING_APPROACHES = {
    "manual_data_entry": "automation",
    "slow_reporting": "infrastructure_upgrade",
    "handoff_failures": "workflow_automation",
    "territory_overflow": "crm_rule_update",
    "billing_lag": "integration_fix",
    "data_inconsistency": "data_governance",
    "tool_capacity_limit": "tool_upgrade",
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    if "bottlenecks" not in data:
        errors.append("Missing required field: bottlenecks")
        return errors
    for i, b in enumerate(data["bottlenecks"]):
        for f in ["name", "type", "impact_category", "volume_at_current", "volume_projected"]:
            if f not in b:
                errors.append(f"bottlenecks[{i}] missing field: {f}")
        if "impact_category" in b and b["impact_category"] not in BOTTLENECK_IMPACT:
            errors.append(f"bottlenecks[{i}].impact_category '{b['impact_category']}' not recognised")
    return errors


def score_bottleneck(b: dict) -> dict:
    impact_weight = BOTTLENECK_IMPACT.get(b["impact_category"], 1)
    growth_ratio = b["volume_projected"] / b["volume_at_current"] if b["volume_at_current"] > 0 else 1.0
    # Higher growth ratio = more urgent to fix
    urgency_score = round(impact_weight * growth_ratio, 2)
    approach = SCALING_APPROACHES.get(b["type"], "process_redesign")

    return {
        "name": b["name"],
        "type": b["type"],
        "impact_category": b["impact_category"],
        "urgency_score": urgency_score,
        "volume_at_current": b["volume_at_current"],
        "volume_projected": b["volume_projected"],
        "growth_ratio": round(growth_ratio, 2),
        "recommended_approach": approach,
        "solution": b.get("proposed_solution", ""),
        "estimated_effort_days": b.get("estimated_effort_days", None),
    }


def run_scaling_audit(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    bottlenecks = [score_bottleneck(b) for b in data["bottlenecks"]]
    bottlenecks.sort(key=lambda x: x["urgency_score"], reverse=True)

    for i, b in enumerate(bottlenecks):
        b["priority"] = i + 1

    critical = [b for b in bottlenecks if b["urgency_score"] >= 5.0]

    result = {
        "audit_period": data.get("audit_period", ""),
        "total_bottlenecks": len(bottlenecks),
        "critical_count": len(critical),
        "bottlenecks": bottlenecks,
        "scaling_recommendation": (
            f"URGENT: {len(critical)} critical bottleneck(s) will block growth — address immediately"
            if critical else
            "Scale incrementally — address bottlenecks in priority order before volume doubles"
        ),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_scaling_audit(data)
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
