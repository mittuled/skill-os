#!/usr/bin/env python3
"""
generate.py — Generate a go-to-market plan with channel mix, phased timeline, and budget allocation.

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

# Channel ROI multipliers (pipeline generated per $1 spent, relative index)
CHANNEL_ROI_INDEX = {
    "paid_search": 2.8,
    "content_seo": 4.5,
    "paid_social": 1.9,
    "events": 3.2,
    "partner_referral": 5.0,
    "pr_earned": 6.0,
    "email_nurture": 4.0,
    "webinars": 3.5,
    "outbound_email": 2.0,
    "community": 2.5,
}

PHASE_NAMES = ["pre_launch", "launch", "post_launch"]

# Typical phase budget weighting
PHASE_BUDGET_WEIGHTS = {
    "pre_launch": 0.20,
    "launch": 0.50,
    "post_launch": 0.30,
}


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    required = ["product_name", "launch_date", "revenue_target", "marketing_budget", "channels", "icp_summary"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "channels" in data:
        unknown = [c for c in data["channels"] if c not in CHANNEL_ROI_INDEX]
        if unknown:
            errors.append(f"Unknown channels: {unknown}. Known: {list(CHANNEL_ROI_INDEX.keys())}")
    return errors


def build_channel_priority_matrix(channels: list[str], budget: float) -> list[dict]:
    """Rank channels by ROI index and allocate budget proportionally."""
    selected = {c: CHANNEL_ROI_INDEX[c] for c in channels if c in CHANNEL_ROI_INDEX}
    total_roi = sum(selected.values())
    matrix = []
    for rank, (ch, roi) in enumerate(sorted(selected.items(), key=lambda x: -x[1]), 1):
        alloc = round((roi / total_roi) * budget, 0)
        expected_pipeline = round(alloc * roi, 0)
        matrix.append({
            "rank": rank,
            "channel": ch,
            "roi_index": roi,
            "budget_allocation": alloc,
            "budget_pct": round((roi / total_roi) * 100, 1),
            "expected_pipeline_contribution": expected_pipeline,
        })
    return matrix


def build_timeline(launch_date: str, channels: list[str]) -> dict:
    """Build a phased GTM timeline."""
    # Simple offset-based timeline from launch date
    return {
        "pre_launch": {
            "description": "Awareness build and asset preparation",
            "typical_duration": "4–6 weeks before launch",
            "channel_activities": {c: "Build assets, set up campaigns, brief teams" for c in channels},
            "gate": "All assets approved and staged; sales briefed",
        },
        "launch": {
            "description": "Coordinated multi-channel activation",
            "launch_date": launch_date,
            "channel_activities": {c: "Activate campaigns, publish content, run PR outreach" for c in channels},
            "gate": "All channels live; war room monitoring active",
        },
        "post_launch": {
            "description": "Optimization and scale",
            "typical_duration": "4–8 weeks post-launch",
            "channel_activities": {c: "Optimize based on performance data; double down on winners" for c in channels},
            "gate": "Performance review complete; reallocations approved",
        },
    }


def generate_gtm_plan(data: dict) -> dict:
    """Generate the full GTM plan."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    channels = data["channels"]
    budget = data["marketing_budget"]
    revenue_target = data["revenue_target"]

    channel_matrix = build_channel_priority_matrix(channels, budget)
    timeline = build_timeline(data["launch_date"], channels)

    # Phase budget allocations
    phase_budgets = {
        phase: round(budget * weight, 0)
        for phase, weight in PHASE_BUDGET_WEIGHTS.items()
    }

    # KPIs derived from revenue target
    pipeline_target = revenue_target * 4  # assume 25% win rate
    mql_target = round(pipeline_target / data.get("avg_deal_size", 50000) * 4)

    objectives = [
        {"objective": "Pipeline contribution", "kpi": f"${pipeline_target:,.0f} marketing-sourced pipeline", "owner": "VP Marketing"},
        {"objective": "Brand awareness", "kpi": f"{data.get('awareness_target_pct', 15)}% unaided awareness in ICP", "owner": "Brand team"},
        {"objective": "Lead volume", "kpi": f"{mql_target} MQLs from launch through post-launch phase", "owner": "Demand Gen"},
        {"objective": "Win rate support", "kpi": "Sales deck and battlecard delivered pre-launch", "owner": "Product Marketing"},
    ]

    result = {
        "product": data["product_name"],
        "launch_date": data["launch_date"],
        "icp_summary": data["icp_summary"],
        "gtm_objectives": objectives,
        "channel_priority_matrix": channel_matrix,
        "phased_timeline": timeline,
        "budget_by_phase": phase_budgets,
        "total_expected_pipeline": sum(c["expected_pipeline_contribution"] for c in channel_matrix),
        "cross_functional_sign_off_required": ["CBO", "VP Sales", "VP Product", "VP Engineering (for readiness)"],
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_gtm_plan(data)
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
