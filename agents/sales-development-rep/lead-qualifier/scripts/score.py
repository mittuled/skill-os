#!/usr/bin/env python3
"""
score.py — Score a lead using BANT framework and produce tier assignment with recommended action.

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

# BANT dimension weights (must sum to 1.0)
BANT_WEIGHTS = {
    "budget": 0.25,
    "authority": 0.25,
    "need": 0.30,
    "timeline": 0.20,
}

# Score thresholds for tier assignment
TIER_THRESHOLDS = [
    (8.0, "hot", "Immediate outreach within 24 hours"),
    (6.0, "warm", "Schedule outreach after filling data gaps"),
    (3.0, "cold", "Assign to nurture sequence; re-qualify on trigger event"),
    (0.0, "disqualified", "Archive with disqualification reason; set re-evaluation date"),
]

# MEDDIC modifier
MEDDIC_CONFIRMED_BOOST = 1.1  # 4+ elements confirmed
MEDDIC_UNKNOWN_PENALTY = 0.9  # 2+ elements unknown


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    required = ["company_name", "bant_scores"]
    for f in required:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "bant_scores" in data:
        for dim in BANT_WEIGHTS:
            if dim not in data["bant_scores"]:
                errors.append(f"bant_scores missing dimension: {dim}")
            elif not (0 <= data["bant_scores"][dim] <= 10):
                errors.append(f"bant_scores.{dim} must be 0–10")
    return errors


def assign_tier(score: float) -> tuple[str, str]:
    for threshold, tier, action in TIER_THRESHOLDS:
        if score >= threshold:
            return tier, action
    return "disqualified", "Archive"


def score_lead(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    bant = data["bant_scores"]
    composite = sum(bant[dim] * BANT_WEIGHTS[dim] for dim in BANT_WEIGHTS)

    # MEDDIC modifier (optional)
    meddic = data.get("meddic_assessment", {})
    confirmed = sum(1 for v in meddic.values() if v == "confirmed")
    unknown = sum(1 for v in meddic.values() if v == "unknown")

    modifier = 1.0
    if composite >= 6.0:
        if confirmed >= 4:
            modifier = MEDDIC_CONFIRMED_BOOST
        elif unknown >= 2:
            modifier = MEDDIC_UNKNOWN_PENALTY

    final_score = min(10.0, round(composite * modifier, 2))
    tier, default_action = assign_tier(final_score)

    result = {
        "company": data["company_name"],
        "composite_score": final_score,
        "bant_breakdown": {
            dim: {
                "score": bant[dim],
                "weight": BANT_WEIGHTS[dim],
                "contribution": round(bant[dim] * BANT_WEIGHTS[dim], 2),
                "evidence": data.get("evidence", {}).get(dim, ""),
            }
            for dim in BANT_WEIGHTS
        },
        "meddic_modifier": modifier,
        "tier": tier,
        "recommended_action": data.get("recommended_action", default_action),
        "disqualification_reason": data.get("disqualification_reason", "") if tier == "disqualified" else None,
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_lead(data)
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
