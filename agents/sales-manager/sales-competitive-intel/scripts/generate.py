#!/usr/bin/env python3
"""
generate.py — Generate a competitive intelligence package with battle cards and win/loss analysis.

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

# Switching cost categories
SWITCHING_COST_CATEGORIES = [
    "financial",
    "operational",
    "data_migration",
    "relationship",
    "opportunity_cost",
]

# Threat level based on encounter frequency + win rate
def compute_threat_level(encounter_pct: float, win_rate_pct: float) -> str:
    if encounter_pct >= 30 and win_rate_pct < 50:
        return "critical"
    elif encounter_pct >= 20 or win_rate_pct < 50:
        return "high"
    elif encounter_pct >= 10:
        return "medium"
    return "low"


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    if "competitors" not in data:
        errors.append("Missing required field: competitors")
        return errors
    for i, c in enumerate(data["competitors"]):
        for f in ["name", "encounter_pct", "win_rate_pct"]:
            if f not in c:
                errors.append(f"competitors[{i}] missing field: {f}")
    return errors


def build_competitor_profile(competitor: dict) -> dict:
    threat = compute_threat_level(
        competitor["encounter_pct"],
        competitor["win_rate_pct"],
    )

    switching_costs = competitor.get("switching_costs", {})
    total_switching_friction = sum(switching_costs.get(cat, 0) for cat in SWITCHING_COST_CATEGORIES)
    avg_switching_friction = round(total_switching_friction / len(SWITCHING_COST_CATEGORIES), 1) if SWITCHING_COST_CATEGORIES else 0

    return {
        "name": competitor["name"],
        "threat_level": threat,
        "encounter_pct": competitor["encounter_pct"],
        "win_rate_pct": competitor["win_rate_pct"],
        "battle_card": {
            "overview": competitor.get("overview", ""),
            "strengths": competitor.get("strengths", []),
            "weaknesses": competitor.get("weaknesses", []),
            "trap_questions": competitor.get("trap_questions", []),
            "landmines": competitor.get("landmines", []),
            "talk_tracks": competitor.get("talk_tracks", []),
            "proof_points": competitor.get("proof_points", []),
        },
        "switching_costs": {
            cat: switching_costs.get(cat, 0) for cat in SWITCHING_COST_CATEGORIES
        },
        "average_switching_friction": avg_switching_friction,
        "win_loss_patterns": {
            "we_win_when": competitor.get("we_win_when", []),
            "we_lose_when": competitor.get("we_lose_when", []),
            "dangerous_deal_stages": competitor.get("dangerous_stages", []),
        },
        "refresh_recommended_days": 90,
    }


def generate_intel(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    competitors = [build_competitor_profile(c) for c in data["competitors"]]
    # Sort by threat level
    threat_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    competitors.sort(key=lambda x: threat_order.get(x["threat_level"], 4))

    critical = [c["name"] for c in competitors if c["threat_level"] == "critical"]

    result = {
        "product": data.get("product_name", ""),
        "analysis_date": data.get("analysis_date", ""),
        "total_competitors": len(competitors),
        "critical_threats": critical,
        "competitors": competitors,
        "refresh_reminder": "Battle cards should be reviewed and updated every 90 days",
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_intel(data)
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
