#!/usr/bin/env python3
"""
generate.py — Generate a quarterly demand generation plan with lead volume targets and channel allocation.

Usage:
    echo '<json>' | python3 generate.py
    python3 generate.py < input.json
    python3 generate.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# Default funnel conversion rates (can be overridden by input)
DEFAULT_FUNNEL = {
    "visitor_to_lead_pct": 3.0,
    "lead_to_mql_pct": 20.0,
    "mql_to_sql_pct": 30.0,
    "sql_to_opportunity_pct": 50.0,
    "opportunity_to_close_pct": 25.0,
}

# Channel benchmarks: (typical CPL, conversion MQL->SQL, velocity days)
CHANNEL_BENCHMARKS = {
    "paid_search": {"cpl": 150, "mql_sql_rate": 0.35, "velocity_days": 45},
    "content_seo": {"cpl": 40, "mql_sql_rate": 0.20, "velocity_days": 90},
    "paid_social": {"cpl": 200, "mql_sql_rate": 0.25, "velocity_days": 60},
    "events": {"cpl": 500, "mql_sql_rate": 0.50, "velocity_days": 30},
    "outbound_email": {"cpl": 60, "mql_sql_rate": 0.15, "velocity_days": 75},
    "partner_referral": {"cpl": 300, "mql_sql_rate": 0.55, "velocity_days": 25},
    "organic_social": {"cpl": 20, "mql_sql_rate": 0.10, "velocity_days": 120},
    "webinars": {"cpl": 100, "mql_sql_rate": 0.40, "velocity_days": 35},
}

EXPERIMENT_BUDGET_RESERVE_PCT = 0.175  # 17.5% (midpoint of 15–20%)


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    required = ["quarterly_revenue_target", "avg_deal_size", "channel_budget_total", "channels"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "channels" in data:
        for ch in data["channels"]:
            if ch not in CHANNEL_BENCHMARKS:
                errors.append(f"Unknown channel: {ch}. Known: {list(CHANNEL_BENCHMARKS.keys())}")
    return errors


def back_into_lead_volumes(revenue_target: float, deal_size: float, funnel: dict) -> dict:
    """Calculate required lead volumes at each funnel stage."""
    closed_deals = revenue_target / deal_size
    opportunities = closed_deals / (funnel["opportunity_to_close_pct"] / 100)
    sqls = opportunities / (funnel["sql_to_opportunity_pct"] / 100)
    mqls = sqls / (funnel["mql_to_sql_pct"] / 100)
    leads = mqls / (funnel["lead_to_mql_pct"] / 100)
    visitors = leads / (funnel["visitor_to_lead_pct"] / 100)
    return {
        "required_closed_deals": round(closed_deals, 1),
        "required_opportunities": round(opportunities, 1),
        "required_sqls": round(sqls, 1),
        "required_mqls": round(mqls, 1),
        "required_leads": round(leads, 1),
        "required_visitors": round(visitors, 1),
    }


def allocate_channels(channels: list[str], total_budget: float, lead_volumes: dict) -> list[dict]:
    """Allocate budget across channels proportional to CPL efficiency."""
    selected = {ch: CHANNEL_BENCHMARKS[ch] for ch in channels if ch in CHANNEL_BENCHMARKS}
    if not selected:
        return []

    # Weight by inverse CPL (cheaper channels get more budget proportionally)
    inv_cpl_sum = sum(1 / v["cpl"] for v in selected.values())
    experiment_reserve = total_budget * EXPERIMENT_BUDGET_RESERVE_PCT
    deployable = total_budget - experiment_reserve

    allocations = []
    required_mqls = lead_volumes["required_mqls"]
    for ch, bench in selected.items():
        weight = (1 / bench["cpl"]) / inv_cpl_sum
        budget = round(deployable * weight, 0)
        expected_leads = round(budget / bench["cpl"])
        expected_mqls = round(expected_leads * DEFAULT_FUNNEL["lead_to_mql_pct"] / 100)
        allocations.append({
            "channel": ch,
            "budget": budget,
            "budget_pct": round(weight * 100, 1),
            "expected_leads": expected_leads,
            "expected_mqls": expected_mqls,
            "cpl": bench["cpl"],
            "mql_to_sql_rate": bench["mql_sql_rate"],
            "avg_velocity_days": bench["velocity_days"],
        })

    total_expected_mqls = sum(a["expected_mqls"] for a in allocations)
    coverage_pct = round((total_expected_mqls / required_mqls) * 100, 1) if required_mqls else 0
    return allocations, experiment_reserve, coverage_pct


def generate_demand_plan(data: dict) -> dict:
    """Generate the full demand gen plan."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    funnel = {**DEFAULT_FUNNEL, **data.get("funnel_overrides", {})}
    revenue_target = data["quarterly_revenue_target"]
    deal_size = data["avg_deal_size"]
    total_budget = data["channel_budget_total"]
    channels = data["channels"]

    lead_volumes = back_into_lead_volumes(revenue_target, deal_size, funnel)
    alloc_result = allocate_channels(channels, total_budget, lead_volumes)

    if not alloc_result:
        return {"error": ["No valid channels could be allocated"], "result": None}

    allocations, experiment_reserve, coverage_pct = alloc_result

    mql_definition = data.get("mql_definition", {
        "behavioral_criteria": [
            "Visited pricing page",
            "Downloaded a high-intent asset (whitepaper, case study)",
            "Attended a product demo or webinar",
        ],
        "firmographic_criteria": [
            "Company size: 50–5000 employees",
            "Industry: matches ICP list",
            "Title: Director or above",
        ],
        "lead_score_threshold": 40,
        "handoff_sla_hours": 24,
    })

    result = {
        "quarterly_target": {
            "revenue": revenue_target,
            "avg_deal_size": deal_size,
        },
        "lead_volume_waterfall": lead_volumes,
        "channel_allocations": allocations,
        "experiment_budget_reserve": experiment_reserve,
        "mql_coverage_pct": coverage_pct,
        "mql_definition": mql_definition,
        "measurement_cadence": {
            "weekly_leading_indicators": ["impressions", "clicks", "form_fills", "email_opens"],
            "monthly_lagging_indicators": ["mqls", "sqls", "pipeline_created", "cpl_by_channel"],
            "dashboard_owner": data.get("dashboard_owner", "marketing_ops"),
        },
        "risk_flags": [
            f"MQL coverage at {coverage_pct}% of target — consider increasing budget or adding channels"
        ] if coverage_pct < 90 else [],
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_demand_plan(data)
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
