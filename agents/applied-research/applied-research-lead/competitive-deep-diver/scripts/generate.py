#!/usr/bin/env python3
"""
generate.py — Generate a structured competitive analysis report for a specific competitor.

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

ANALYSIS_DIMENSIONS = [
    "product_capabilities",
    "pricing_model",
    "go_to_market",
    "technical_architecture",
    "market_positioning",
    "customer_profile",
    "strengths",
    "weaknesses",
    "strategic_moves",
]

REQUIRED_FIELDS = ["competitor_name", "analysis_date", "dimensions"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "dimensions" in data:
        for dim in ANALYSIS_DIMENSIONS[:4]:
            if dim not in data["dimensions"]:
                errors.append(f"Missing required analysis dimension: {dim}")
    return errors


def generate_analysis(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    dims = data["dimensions"]
    competitor = data["competitor_name"]

    strategic_implications = []
    if dims.get("pricing_model", {}).get("is_cheaper_than_us"):
        strategic_implications.append("Competitor is cheaper — review our pricing strategy and value-based differentiation")
    if dims.get("product_capabilities", {}).get("gaps_vs_us"):
        gaps = dims["product_capabilities"]["gaps_vs_us"]
        strategic_implications.append(f"Competitor gaps we can exploit: {', '.join(gaps)}")
    if dims.get("strategic_moves", {}).get("recent_launches"):
        strategic_implications.append("Monitor recent launches for signals of strategic direction shift")

    competitive_verdict = dims.get("overall_threat_level", "medium")
    threat_actions = {
        "critical": "Immediate competitive response required — brief CEO and product leadership",
        "high": "Develop competitive response playbook within 30 days",
        "medium": "Monitor quarterly; update battlecard within 60 days",
        "low": "Monitor semi-annually; no immediate action required",
    }

    return {
        "error": None,
        "result": {
            "competitor_name": competitor,
            "analysis_date": data["analysis_date"],
            "analyst": data.get("analyst", "Applied Research Lead"),
            "threat_level": competitive_verdict,
            "recommended_action": threat_actions.get(competitive_verdict, "Monitor quarterly"),
            "analysis_sections": {dim: dims.get(dim, "Not assessed") for dim in ANALYSIS_DIMENSIONS},
            "strategic_implications": strategic_implications,
            "win_conditions": dims.get("win_conditions", []),
            "loss_conditions": dims.get("loss_conditions", []),
            "battlecard_ready": bool(dims.get("strengths") and dims.get("weaknesses") and dims.get("win_conditions")),
            "next_review_date": data.get("next_review_date", "In 90 days"),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_analysis(data)
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
