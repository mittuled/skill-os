#!/usr/bin/env python3
"""
score.py — Score and rank a prospect cohort for outbound targeting.

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

# ICP dimension weights (must sum to 1.0)
ICP_WEIGHTS = {
    "firmographic_fit": 0.35,
    "technographic_fit": 0.25,
    "intent_score": 0.30,
    "behavioral_indicators": 0.10,
}

# Minimum score thresholds
PRIORITY_THRESHOLDS = [
    (8.0, "tier_1", "Immediate outbound — high fit and strong intent"),
    (6.0, "tier_2", "Include in next campaign wave — good fit with moderate intent"),
    (4.0, "tier_3", "Nurture — fit signals present but intent low; monitor for trigger events"),
    (0.0, "excluded", "Exclude from cohort — below minimum ICP threshold"),
]

# Cooling-off period in days for recently-contacted or closed-lost accounts
COOLING_OFF_DAYS = 90


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    if "prospects" not in data:
        errors.append("Missing required field: prospects")
        return errors
    if not isinstance(data["prospects"], list) or len(data["prospects"]) == 0:
        errors.append("prospects must be a non-empty list")
        return errors
    for i, p in enumerate(data["prospects"]):
        for f in ["name", "icp_scores"]:
            if f not in p:
                errors.append(f"prospects[{i}] missing required field: {f}")
        if "icp_scores" in p:
            for dim in ICP_WEIGHTS:
                if dim not in p["icp_scores"]:
                    errors.append(f"prospects[{i}].icp_scores missing dimension: {dim}")
                elif not (0 <= p["icp_scores"][dim] <= 10):
                    errors.append(f"prospects[{i}].icp_scores.{dim} must be 0-10")
    return errors


def assign_priority(score: float) -> tuple[str, str]:
    for threshold, tier, action in PRIORITY_THRESHOLDS:
        if score >= threshold:
            return tier, action
    return "excluded", "Exclude from cohort"


def score_prospect(prospect: dict) -> dict:
    scores = prospect["icp_scores"]
    composite = sum(scores[dim] * ICP_WEIGHTS[dim] for dim in ICP_WEIGHTS)

    # Penalize accounts in cooling-off
    days_since_contact = prospect.get("days_since_last_contact", 999)
    cooling_off = days_since_contact < COOLING_OFF_DAYS
    if cooling_off:
        composite = min(composite, 3.9)  # Cap below tier_3 threshold

    final_score = round(composite, 2)
    tier, recommendation = assign_priority(final_score)

    return {
        "name": prospect["name"],
        "composite_score": final_score,
        "icp_breakdown": {
            dim: {
                "score": scores[dim],
                "weight": ICP_WEIGHTS[dim],
                "contribution": round(scores[dim] * ICP_WEIGHTS[dim], 2),
            }
            for dim in ICP_WEIGHTS
        },
        "cooling_off_applied": cooling_off,
        "days_since_last_contact": days_since_contact,
        "intent_signals": prospect.get("intent_signals", []),
        "priority_tier": tier,
        "recommendation": recommendation,
        "assigned_sdr": prospect.get("assigned_sdr", None),
    }


def score_cohort(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    scored = [score_prospect(p) for p in data["prospects"]]
    scored.sort(key=lambda x: x["composite_score"], reverse=True)

    tier_counts = {}
    for p in scored:
        tier = p["priority_tier"]
        tier_counts[tier] = tier_counts.get(tier, 0) + 1

    result = {
        "campaign": data.get("campaign_name", "Unnamed Campaign"),
        "total_prospects": len(scored),
        "tier_summary": tier_counts,
        "cohort": scored,
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_cohort(data)
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
