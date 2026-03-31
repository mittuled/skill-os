#!/usr/bin/env python3
"""
generate.py — Generate a structured company research profile across 8 firmographic dimensions.

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

# Confidence tiers for data freshness
CONFIDENCE_TIERS = {
    "high": "Verified from primary source within 90 days",
    "medium": "Secondary source or 91-180 days old",
    "low": "Single unverified source or older than 180 days",
}

# Buying trigger urgency taxonomy
TRIGGER_URGENCY = {
    "immediate": "Active buying signal — initiate outreach within 1 week",
    "near_term": "Likely buying window in 1-3 months — prepare and monitor",
    "long_term": "Potential future need in 3-12 months — add to nurture",
}

# All 8 firmographic dimensions
FIRMOGRAPHIC_DIMENSIONS = [
    "company_size",
    "industry",
    "funding",
    "tech_stack",
    "growth_trajectory",
    "competitive_landscape",
    "leadership_team",
    "recent_news",
]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["company_name", "dimensions"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "dimensions" in data:
        for dim in FIRMOGRAPHIC_DIMENSIONS:
            if dim not in data["dimensions"]:
                errors.append(f"dimensions missing required field: {dim}")
            else:
                entry = data["dimensions"][dim]
                if "confidence" not in entry:
                    errors.append(f"dimensions.{dim} missing confidence rating")
                elif entry["confidence"] not in CONFIDENCE_TIERS:
                    errors.append(f"dimensions.{dim}.confidence must be: high, medium, or low")
    return errors


def compute_confidence_score(dimensions: dict) -> float:
    tier_weights = {"high": 1.0, "medium": 0.6, "low": 0.2}
    scores = [tier_weights.get(dimensions[dim].get("confidence", "low"), 0.2) for dim in FIRMOGRAPHIC_DIMENSIONS if dim in dimensions]
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores) * 100, 1)


def assess_buying_triggers(triggers: list[dict]) -> list[dict]:
    assessed = []
    for t in triggers:
        urgency = t.get("urgency", "long_term")
        assessed.append({
            "trigger": t.get("description", ""),
            "urgency": urgency,
            "urgency_label": TRIGGER_URGENCY.get(urgency, "Unknown"),
            "evidence": t.get("evidence", ""),
        })
    assessed.sort(key=lambda x: ["immediate", "near_term", "long_term"].index(x["urgency"]) if x["urgency"] in ["immediate", "near_term", "long_term"] else 3)
    return assessed


def generate_profile(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    dimensions = data["dimensions"]
    confidence_score = compute_confidence_score(dimensions)
    buying_triggers = assess_buying_triggers(data.get("buying_triggers", []))

    # Identify data gaps
    data_gaps = []
    for dim in FIRMOGRAPHIC_DIMENSIONS:
        entry = dimensions.get(dim, {})
        if not entry.get("summary") or entry.get("confidence") == "low":
            data_gaps.append({
                "dimension": dim,
                "issue": "Missing or low-confidence data",
                "impact": entry.get("gap_impact", ""),
                "remediation": entry.get("gap_remediation", ""),
            })

    profile = {
        "company": data["company_name"],
        "overall_data_confidence_pct": confidence_score,
        "dimensions": {
            dim: {
                "summary": dimensions[dim].get("summary", ""),
                "confidence": dimensions[dim].get("confidence", "low"),
                "confidence_label": CONFIDENCE_TIERS.get(dimensions[dim].get("confidence", "low"), ""),
                "sources": dimensions[dim].get("sources", []),
            }
            for dim in FIRMOGRAPHIC_DIMENSIONS
            if dim in dimensions
        },
        "buying_triggers": buying_triggers,
        "immediate_triggers_count": sum(1 for t in buying_triggers if t["urgency"] == "immediate"),
        "data_gaps": data_gaps,
        "recommended_outreach_approach": data.get("recommended_outreach_approach", ""),
    }
    return {"error": None, "result": profile}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_profile(data)
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
