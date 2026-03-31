#!/usr/bin/env python3
"""
generate.py — Build multi-touch attribution model and credit marketing touchpoints.

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

# Attribution models with credit distribution logic
ATTRIBUTION_MODELS = {
    "first_touch": {
        "label": "First Touch",
        "description": "100% credit to the first touchpoint in the journey",
        "best_for": "Awareness channel optimization",
    },
    "last_touch": {
        "label": "Last Touch",
        "description": "100% credit to the last touchpoint before conversion",
        "best_for": "Conversion/closing channel optimization",
    },
    "linear": {
        "label": "Linear",
        "description": "Equal credit distributed across all touchpoints",
        "best_for": "Balanced view across all channels",
    },
    "time_decay": {
        "label": "Time Decay",
        "description": "More credit to touchpoints closer to conversion",
        "best_for": "Long sales cycles; recency matters",
    },
    "w_shaped": {
        "label": "W-Shaped",
        "description": "40% first touch, 40% opportunity creation, 20% split across middle touches",
        "best_for": "B2B with defined lead-to-opp stages",
    },
    "u_shaped": {
        "label": "U-Shaped (Position-Based)",
        "description": "40% first touch, 40% last touch, 20% split across middle",
        "best_for": "Emphasis on acquisition and close",
    },
}

# Standard marketing channels
STANDARD_CHANNELS = [
    "organic_search", "paid_search", "paid_social", "organic_social",
    "email", "content", "webinar", "referral", "direct", "partner",
]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "model_type" not in data or data.get("model_type") not in ATTRIBUTION_MODELS:
        errors.append(f"Missing or invalid field: model_type ({'/'.join(ATTRIBUTION_MODELS.keys())})")
    if "journeys" not in data or not isinstance(data["journeys"], list):
        errors.append("Missing required field: journeys (list of customer journey touchpoint sequences)")
    return errors


def distribute_credit(touchpoints: list[str], model: str, deal_value: float) -> dict[str, float]:
    n = len(touchpoints)
    if n == 0:
        return {}

    credits: dict[str, float] = {tp: 0.0 for tp in set(touchpoints)}

    if model == "first_touch":
        credits[touchpoints[0]] += deal_value

    elif model == "last_touch":
        credits[touchpoints[-1]] += deal_value

    elif model == "linear":
        per_touch = deal_value / n
        for tp in touchpoints:
            credits[tp] += per_touch

    elif model == "time_decay":
        # Weights: position^2 normalized
        weights = [(i + 1) ** 2 for i in range(n)]
        total_weight = sum(weights)
        for i, tp in enumerate(touchpoints):
            credits[tp] += deal_value * weights[i] / total_weight

    elif model == "u_shaped":
        if n == 1:
            credits[touchpoints[0]] += deal_value
        elif n == 2:
            credits[touchpoints[0]] += deal_value * 0.5
            credits[touchpoints[-1]] += deal_value * 0.5
        else:
            first_last = deal_value * 0.40
            middle_per = (deal_value * 0.20) / (n - 2) if n > 2 else 0
            credits[touchpoints[0]] += first_last
            credits[touchpoints[-1]] += first_last
            for tp in touchpoints[1:-1]:
                credits[tp] += middle_per

    elif model == "w_shaped":
        if n == 1:
            credits[touchpoints[0]] += deal_value
        elif n == 2:
            credits[touchpoints[0]] += deal_value * 0.5
            credits[touchpoints[-1]] += deal_value * 0.5
        else:
            mid_idx = n // 2
            credits[touchpoints[0]] += deal_value * 0.40
            credits[touchpoints[mid_idx]] += deal_value * 0.40
            remaining = deal_value * 0.20
            other_tps = [tp for i, tp in enumerate(touchpoints) if i not in (0, mid_idx)]
            per_other = remaining / len(other_tps) if other_tps else 0
            for tp in other_tps:
                credits[tp] += per_other

    return credits


def generate_attribution_model(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    model_type = data["model_type"]
    journeys = data["journeys"]
    model_config = ATTRIBUTION_MODELS[model_type]

    # Aggregate attribution across all journeys
    channel_attribution: dict[str, float] = {}
    total_revenue = 0
    journey_results = []

    for journey in journeys:
        touchpoints = journey.get("touchpoints", [])
        deal_value = journey.get("deal_value_usd", 0)
        total_revenue += deal_value

        journey_credits = distribute_credit(touchpoints, model_type, deal_value)
        for channel, credit in journey_credits.items():
            channel_attribution[channel] = channel_attribution.get(channel, 0) + credit

        journey_results.append({
            "deal_id": journey.get("deal_id", ""),
            "deal_value_usd": deal_value,
            "touchpoints": touchpoints,
            "credits": {k: round(v, 2) for k, v in journey_credits.items()},
        })

    # Compute channel share
    channel_summary = []
    for channel, attributed_revenue in sorted(channel_attribution.items(), key=lambda x: -x[1]):
        share = round(attributed_revenue / total_revenue * 100, 1) if total_revenue else 0
        channel_summary.append({
            "channel": channel,
            "attributed_revenue_usd": round(attributed_revenue, 2),
            "revenue_share_pct": share,
        })

    return {
        "error": None,
        "result": {
            "company": company,
            "model_type": model_type,
            "model_config": model_config,
            "total_revenue_attributed_usd": total_revenue,
            "channel_attribution": channel_summary,
            "journey_details": journey_results,
            "available_models": list(ATTRIBUTION_MODELS.keys()),
            "summary": (
                f"Attribution model ({model_config['label']}) for {company}: "
                f"${total_revenue:,.0f} revenue distributed across {len(channel_attribution)} channel(s) "
                f"from {len(journeys)} deal(s)."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_attribution_model(data)
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
