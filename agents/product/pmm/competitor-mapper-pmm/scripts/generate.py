#!/usr/bin/env python3
"""
generate.py — Build a structured competitive landscape map.

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

COMPETITOR_TIERS = {
    "direct": "Solves the same problem for the same buyer — head-to-head competition",
    "indirect": "Solves the same problem with a different approach or technology",
    "adjacent": "Serves the same buyer but for a different job-to-be-done",
    "emerging": "Early-stage player with potential to become direct competitor",
}

DIMENSION_WEIGHTS = {
    "target_segment_overlap": 30,
    "feature_parity": 25,
    "pricing_proximity": 20,
    "go_to_market_similarity": 15,
    "brand_strength": 10,
}

THREAT_LEVELS = {
    (80, 100): "critical",
    (60, 79): "high",
    (40, 59): "medium",
    (0, 39): "low",
}

DIFFERENTIATION_CATEGORIES = [
    "technology",
    "integrations",
    "pricing_model",
    "target_segment",
    "deployment",
    "compliance",
    "support",
    "brand",
]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "our_product" not in data or not isinstance(data["our_product"], dict):
        errors.append("Missing required field: our_product (dict with name, segment, value_prop)")
    if "competitors" not in data or not isinstance(data["competitors"], list):
        errors.append("Missing required field: competitors (list)")
    if not errors and not data["competitors"]:
        errors.append("At least one competitor is required")
    return errors


def score_threat(competitor: dict) -> int:
    score = 0
    for dimension, weight in DIMENSION_WEIGHTS.items():
        val = competitor.get("scores", {}).get(dimension, 5)
        score += int(val * weight / 10)
    return min(score, 100)


def get_threat_level(score: int) -> str:
    for (low, high), level in THREAT_LEVELS.items():
        if low <= score <= high:
            return level
    return "low"


def build_differentiation_map(our_product: dict, competitor: dict) -> dict[str, str]:
    our_strengths = our_product.get("differentiators", [])
    comp_weaknesses = competitor.get("weaknesses", [])
    comp_strengths = competitor.get("strengths", [])

    advantages = [d for d in our_strengths if d not in comp_strengths]
    vulnerabilities = [s for s in comp_strengths if s not in our_strengths]
    parity = [s for s in comp_strengths if s in our_strengths]

    return {
        "our_advantages": advantages,
        "competitor_advantages": vulnerabilities,
        "feature_parity": parity,
        "exploit_weaknesses": comp_weaknesses,
    }


def generate_battlecard_summary(our_product: dict, competitor: dict, diff_map: dict) -> str:
    name = competitor.get("name", "Competitor")
    tier = competitor.get("tier", "direct")
    advantages = diff_map.get("our_advantages", [])
    vulnerabilities = diff_map.get("competitor_advantages", [])

    summary_parts = [f"vs {name} ({tier}):"]
    if advantages:
        summary_parts.append(f"Lead with: {', '.join(advantages[:2])}")
    if vulnerabilities:
        summary_parts.append(f"Watch for: {', '.join(vulnerabilities[:2])}")
    return " | ".join(summary_parts)


def generate_competitive_map(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    our_product = data["our_product"]
    competitors = data["competitors"]

    competitor_analysis = []
    critical_threats = []
    high_threats = []

    for comp in competitors:
        threat_score = score_threat(comp)
        threat_level = get_threat_level(threat_score)
        diff_map = build_differentiation_map(our_product, comp)
        battlecard = generate_battlecard_summary(our_product, comp, diff_map)

        entry = {
            "name": comp.get("name"),
            "tier": comp.get("tier", "direct"),
            "threat_score": threat_score,
            "threat_level": threat_level,
            "segment": comp.get("segment", "unknown"),
            "pricing_model": comp.get("pricing_model", "unknown"),
            "estimated_arpu_usd": comp.get("estimated_arpu_usd"),
            "funding_stage": comp.get("funding_stage", "unknown"),
            "strengths": comp.get("strengths", []),
            "weaknesses": comp.get("weaknesses", []),
            "differentiation_map": diff_map,
            "battlecard_summary": battlecard,
            "intel_sources": comp.get("intel_sources", []),
        }
        competitor_analysis.append(entry)

        if threat_level == "critical":
            critical_threats.append(comp.get("name"))
        elif threat_level == "high":
            high_threats.append(comp.get("name"))

    # Sort by threat score descending
    competitor_analysis.sort(key=lambda x: -x["threat_score"])

    tier_summary: dict[str, list[str]] = {t: [] for t in COMPETITOR_TIERS}
    for c in competitor_analysis:
        tier = c.get("tier", "direct")
        if tier in tier_summary:
            tier_summary[tier].append(c["name"])

    strategic_recommendations = []
    if critical_threats:
        strategic_recommendations.append(
            f"URGENT: Develop dedicated battle cards for critical threats: {', '.join(critical_threats)}"
        )
    if high_threats:
        strategic_recommendations.append(
            f"Prepare win/loss differentiation messaging for: {', '.join(high_threats)}"
        )
    strategic_recommendations.append(
        "Run quarterly win/loss analysis against top-3 competitors to validate threat scores"
    )
    strategic_recommendations.append(
        "Share competitive map with sales as a living document; update on each material competitor event"
    )

    return {
        "error": None,
        "result": {
            "company": company,
            "our_product": our_product,
            "total_competitors_mapped": len(competitor_analysis),
            "tier_summary": tier_summary,
            "threat_overview": {
                "critical": critical_threats,
                "high": high_threats,
                "medium": [c["name"] for c in competitor_analysis if c["threat_level"] == "medium"],
                "low": [c["name"] for c in competitor_analysis if c["threat_level"] == "low"],
            },
            "competitor_profiles": competitor_analysis,
            "strategic_recommendations": strategic_recommendations,
            "summary": (
                f"Competitive landscape for {company}: {len(competitor_analysis)} competitors mapped. "
                f"Critical threats: {len(critical_threats)}, High threats: {len(high_threats)}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_competitive_map(data)
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
