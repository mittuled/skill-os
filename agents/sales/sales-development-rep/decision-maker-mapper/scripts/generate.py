#!/usr/bin/env python3
"""
generate.py — Generate a buying committee stakeholder map for multi-threaded sales.

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

# Buying committee roles with engagement priority
BUYING_ROLES = {
    "economic_buyer": {"priority": 1, "description": "Controls budget and final approval authority"},
    "champion": {"priority": 2, "description": "Internal advocate who sells on your behalf"},
    "technical_buyer": {"priority": 3, "description": "Evaluates technical fit and implementation feasibility"},
    "user_buyer": {"priority": 4, "description": "Directly uses the product; affected by day-to-day experience"},
    "coach": {"priority": 5, "description": "Provides insider intelligence on process, politics, and timing"},
    "gatekeeper": {"priority": 6, "description": "Controls access to decision-makers; must be navigated"},
    "blocker": {"priority": 7, "description": "Opposes the purchase; must be neutralized or bypassed"},
}

# Sentiment scoring
SENTIMENT_VALUES = {"positive": 3, "neutral": 2, "negative": 1, "unknown": 0}

# Influence tiers
INFLUENCE_TIERS = {
    (5, 5): "critical",
    (4, 5): "high",
    (5, 4): "high",
    (3, 5): "high",
    (5, 3): "high",
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["account_name", "stakeholders"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "stakeholders" in data:
        for i, s in enumerate(data["stakeholders"]):
            for f in ["name", "title", "role"]:
                if f not in s:
                    errors.append(f"stakeholders[{i}] missing field: {f}")
            if "role" in s and s["role"] not in BUYING_ROLES:
                errors.append(f"stakeholders[{i}].role '{s['role']}' not in valid roles: {list(BUYING_ROLES.keys())}")
            influence = s.get("influence_score", 0)
            if not (1 <= influence <= 5):
                errors.append(f"stakeholders[{i}].influence_score must be 1-5")
    return errors


def map_stakeholders(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    stakeholders = data["stakeholders"]
    required_roles = {"economic_buyer", "champion", "technical_buyer"}
    assigned_roles = {s["role"] for s in stakeholders}
    missing_roles = required_roles - assigned_roles

    # Score and rank stakeholders
    scored = []
    for s in stakeholders:
        role_info = BUYING_ROLES[s["role"]]
        influence = s.get("influence_score", 3)
        sentiment_val = SENTIMENT_VALUES.get(s.get("sentiment", "unknown"), 0)
        engagement_priority = role_info["priority"]
        scored.append({
            "name": s["name"],
            "title": s["title"],
            "role": s["role"],
            "role_description": role_info["description"],
            "influence_score": influence,
            "sentiment": s.get("sentiment", "unknown"),
            "engagement_priority": engagement_priority,
            "approach": s.get("recommended_approach", ""),
            "background": s.get("background", ""),
        })

    # Sort by engagement priority (lower number = higher priority)
    scored.sort(key=lambda x: (x["engagement_priority"], -x["influence_score"]))

    # Identify coverage gaps
    gaps = []
    for role in missing_roles:
        gaps.append({
            "missing_role": role,
            "role_description": BUYING_ROLES[role]["description"],
            "impact": "Deal risk elevated without this role identified",
            "find_via": "LinkedIn org chart, AE relationship, executive sponsor intro",
        })

    # Identify blockers requiring strategy
    blockers = [s for s in scored if s["role"] == "blocker"]
    blocker_strategy = None
    if blockers:
        blocker_strategy = "Build champion support before engaging blockers; use economic buyer to bypass if needed"

    result = {
        "account": data["account_name"],
        "deal_stage": data.get("deal_stage", ""),
        "committee_size": len(scored),
        "coverage_completeness_pct": round((len(required_roles - missing_roles) / len(required_roles)) * 100),
        "stakeholders": scored,
        "missing_roles": gaps,
        "blocker_strategy": blocker_strategy,
        "single_thread_risk": len([s for s in scored if s["sentiment"] in ["positive", "neutral"]]) <= 1,
        "recommended_entry_point": scored[0]["name"] if scored else None,
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = map_stakeholders(data)
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
