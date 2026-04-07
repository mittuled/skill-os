#!/usr/bin/env python3
"""
score.py — Score pricing sellability based on field feedback and competitive positioning.

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

# Scoring criteria and weights (must sum to 100)
SCORING_CRITERIA = {
    "field_feedback_alignment": {
        "weight": 30,
        "description": "Pricing aligns with AE/SE field observations and objection patterns",
    },
    "willingness_to_pay_fit": {
        "weight": 30,
        "description": "List price vs average selling price gap and discount depth are within acceptable range",
    },
    "competitive_price_position": {
        "weight": 25,
        "description": "Pricing spread vs top competitors is justifiable by differentiated value",
    },
    "pipeline_impact": {
        "weight": 15,
        "description": "Proposed pricing does not materially harm active pipeline close rates",
    },
}

DISCOUNT_RISK_THRESHOLD_PCT = 20  # Discount rates above this flag sellability risk
PRICE_GAP_RISK_THRESHOLD_PCT = 25  # List vs ASP gap above this signals structural over-pricing


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    required = [
        "proposed_list_price",
        "avg_selling_price",
        "avg_discount_pct",
        "objection_frequency_pct",
        "competitor_street_prices",
        "pipeline_deals_at_risk",
        "total_pipeline_deals",
    ]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "competitor_street_prices" in data and not isinstance(data["competitor_street_prices"], dict):
        errors.append("competitor_street_prices must be a dict mapping competitor name to price")
    return errors


def score_pricing(data: dict) -> dict:
    """Score pricing sellability across all criteria."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    list_price: float = data["proposed_list_price"]
    asp: float = data["avg_selling_price"]
    discount_pct: float = data["avg_discount_pct"]
    objection_freq: float = data["objection_frequency_pct"]
    competitor_prices: dict = data["competitor_street_prices"]
    deals_at_risk: int = data["pipeline_deals_at_risk"]
    total_deals: int = data["total_pipeline_deals"]

    # Field feedback alignment (0–100): penalize high objection frequency
    field_score = max(0, 100 - (objection_freq * 1.5))
    if discount_pct > DISCOUNT_RISK_THRESHOLD_PCT:
        field_score = max(0, field_score - 20)

    # Willingness-to-pay fit: penalize large list-vs-ASP gap
    price_gap_pct = ((list_price - asp) / list_price) * 100 if list_price > 0 else 0
    wtp_score = max(0, 100 - (price_gap_pct * 2))

    # Competitive price position: average spread vs competitors
    if competitor_prices:
        spreads = [((list_price - cp) / cp) * 100 for cp in competitor_prices.values() if cp > 0]
        avg_spread = sum(spreads) / len(spreads) if spreads else 0
        # Mild premium (+5–15%) is positive; large premium (>30%) is risky; discount (<0%) is concerning
        if -10 <= avg_spread <= 20:
            comp_score = 90
        elif 20 < avg_spread <= 35:
            comp_score = 65
        elif avg_spread > 35:
            comp_score = 40
        else:
            comp_score = 75  # slight discount, still competitive
    else:
        comp_score = 50
        avg_spread = 0.0

    # Pipeline impact: fraction of deals at risk
    at_risk_pct = (deals_at_risk / total_deals * 100) if total_deals > 0 else 0
    pipeline_score = max(0, 100 - (at_risk_pct * 2.5))

    # Weighted total
    scores = {
        "field_feedback_alignment": round(field_score, 1),
        "willingness_to_pay_fit": round(wtp_score, 1),
        "competitive_price_position": round(comp_score, 1),
        "pipeline_impact": round(pipeline_score, 1),
    }
    total = sum(
        scores[k] * SCORING_CRITERIA[k]["weight"] / 100
        for k in SCORING_CRITERIA
    )

    # Sign-off recommendation
    if total >= 75:
        recommendation = "GO — pricing is sellable; approve for launch"
        sign_off = "approved"
    elif total >= 55:
        recommendation = "CONDITIONAL — pricing needs targeted adjustments before launch"
        sign_off = "conditional"
    else:
        recommendation = "NO-GO — pricing is not sellable at current structure; restructure required"
        sign_off = "blocked"

    risk_flags = []
    if discount_pct > DISCOUNT_RISK_THRESHOLD_PCT:
        risk_flags.append(f"Discount depth {discount_pct}% exceeds {DISCOUNT_RISK_THRESHOLD_PCT}% threshold — pricing pressure is structural, not tactical")
    if price_gap_pct > PRICE_GAP_RISK_THRESHOLD_PCT:
        risk_flags.append(f"List-to-ASP gap {price_gap_pct:.1f}% signals list price is aspirational, not achievable — review tier anchoring")
    if at_risk_pct > 30:
        risk_flags.append(f"{at_risk_pct:.1f}% of pipeline at risk — pricing change will impact near-term revenue attainment")

    result = {
        "total_score": round(total, 1),
        "sign_off": sign_off,
        "recommendation": recommendation,
        "criteria_scores": {
            k: {
                "score": scores[k],
                "weight": SCORING_CRITERIA[k]["weight"],
                "weighted_contribution": round(scores[k] * SCORING_CRITERIA[k]["weight"] / 100, 1),
            }
            for k in SCORING_CRITERIA
        },
        "risk_flags": risk_flags,
        "analytics": {
            "list_to_asp_gap_pct": round(price_gap_pct, 1),
            "avg_competitor_price_spread_pct": round(avg_spread, 1),
            "pipeline_at_risk_pct": round(at_risk_pct, 1),
        },
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_pricing(data)
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
