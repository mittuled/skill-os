#!/usr/bin/env python3
"""
generate.py — Generate a pricing strategy document anchored in field willingness-to-pay data.

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

# Pricing model options and value metrics
PRICING_MODELS = ["per-seat", "usage-based", "platform-fee", "outcome-based", "tiered-flat"]

VALUE_METRICS = {
    "seats": "scales with team size, good for collaboration tools",
    "api_calls": "scales with product usage, good for infrastructure/data products",
    "records_processed": "scales with data volume, good for automation/analytics",
    "revenue_managed": "aligns cost to customer outcome, good for fintech/revenue tools",
    "outcomes_delivered": "strongest value alignment, good for ROI-measurable products",
}

# Scenario labels for revenue modeling
SCENARIOS = ["aggressive", "balanced", "conservative"]

# Discount policy levels
DISCOUNT_AUTHORITY = {
    "ae": {"max_pct": 10, "approval": "self-service"},
    "vp_sales": {"max_pct": 20, "approval": "VP Sales verbal"},
    "cfo": {"max_pct": 35, "approval": "CFO written sign-off"},
    "board": {"max_pct": 50, "approval": "Board approval required"},
}


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    required = [
        "product_name",
        "segments",
        "closed_lost_pricing_rate_pct",
        "avg_discount_depth_pct",
        "recommended_value_metric",
    ]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "segments" in data:
        for seg in data["segments"]:
            for sf in ["name", "wtp_low", "wtp_high", "competitive_prices"]:
                if sf not in seg:
                    errors.append(f"Segment missing field: {sf}")
    return errors


def build_tier(seg: dict, multiplier: float) -> dict:
    """Build a pricing tier for a segment."""
    mid_wtp = (seg["wtp_low"] + seg["wtp_high"]) / 2
    list_price = round(mid_wtp * multiplier / 100) * 100  # round to nearest 100
    return {
        "segment": seg["name"],
        "list_price": list_price,
        "floor_price": round(list_price * 0.75 / 100) * 100,
        "wtp_range": [seg["wtp_low"], seg["wtp_high"]],
        "competitive_avg": round(sum(seg["competitive_prices"]) / len(seg["competitive_prices"]), 0) if seg.get("competitive_prices") else None,
        "price_vs_competitive_pct": round(((list_price / (sum(seg["competitive_prices"]) / len(seg["competitive_prices"]))) - 1) * 100, 1) if seg.get("competitive_prices") else None,
    }


def model_scenarios(segments: list[dict], tiers: list[dict], pipeline_size: int) -> list[dict]:
    """Model revenue scenarios across aggressive/balanced/conservative pricing."""
    results = []
    multipliers = {"aggressive": 1.15, "balanced": 1.0, "conservative": 0.85}
    win_rate_adjustments = {"aggressive": -0.05, "balanced": 0.0, "conservative": 0.05}
    baseline_win_rate = 0.25

    for scenario in SCENARIOS:
        m = multipliers[scenario]
        wr = max(0.05, min(0.6, baseline_win_rate + win_rate_adjustments[scenario]))
        avg_acv = sum(
            ((s["wtp_low"] + s["wtp_high"]) / 2) * m
            for s in segments
        ) / len(segments)
        projected_revenue = round(pipeline_size * wr * avg_acv)
        results.append({
            "scenario": scenario,
            "price_multiplier": m,
            "estimated_win_rate_pct": round(wr * 100, 1),
            "avg_acv": round(avg_acv, 0),
            "projected_arr": projected_revenue,
        })
    return results


def generate_pricing_strategy(data: dict) -> dict:
    """Generate a full pricing strategy document."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    segments = data["segments"]
    value_metric = data["recommended_value_metric"]
    pipeline_size = data.get("active_pipeline_deals", 30)

    # Build tiers at balanced (1.0x) multiplier
    tiers = [build_tier(s, 1.0) for s in segments]

    # Build scenario models
    scenarios = model_scenarios(segments, tiers, pipeline_size)

    # Build rate card
    rate_card = {
        seg["name"]: {
            "annual_list_price": tier["list_price"],
            "annual_floor_price": tier["floor_price"],
            "monthly_equivalent": round(tier["list_price"] / 12, 2),
        }
        for seg, tier in zip(segments, tiers)
    }

    result = {
        "product": data["product_name"],
        "recommended_value_metric": {
            "metric": value_metric,
            "rationale": VALUE_METRICS.get(value_metric, "Custom metric aligned to product value delivery"),
        },
        "pricing_model": data.get("pricing_model", "per-seat"),
        "tier_definitions": tiers,
        "rate_card": rate_card,
        "discount_policy": DISCOUNT_AUTHORITY,
        "scenario_projections": scenarios,
        "risk_signals": {
            "closed_lost_pricing_rate_pct": data["closed_lost_pricing_rate_pct"],
            "avg_discount_depth_pct": data["avg_discount_depth_pct"],
            "structural_discount_risk": data["avg_discount_depth_pct"] > 20,
            "pricing_led_loss_risk": data["closed_lost_pricing_rate_pct"] > 25,
        },
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_pricing_strategy(data)
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
