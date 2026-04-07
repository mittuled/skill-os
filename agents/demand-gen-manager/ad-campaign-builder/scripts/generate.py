#!/usr/bin/env python3
"""
generate.py — Generates a structured campaign plan from input parameters.

Purpose: Accepts a JSON object with campaign parameters (objective, ICP, platforms,
         budget, targeting) and outputs a structured campaign plan skeleton with
         platform-specific configurations pre-filled.

Dependencies: Python 3.10+ standard library only (no external packages).

Usage:
    echo '{"objective": "lead_gen", "budget": 45000, "platforms": ["google", "linkedin"]}' | python3 generate.py
    python3 generate.py < params.json
    python3 generate.py -o plan.json < params.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PLATFORM_DEFAULTS: dict[str, dict] = {
    "google": {
        "name": "Google Ads",
        "min_budget": 3000,
        "campaign_types": ["Search", "Display - Remarketing", "YouTube - Awareness"],
        "ad_formats": [
            {"format": "Responsive Search Ad", "headline_limit": 30, "description_limit": 90, "variants": 3},
            {"format": "Display Banner", "dimensions": "300x250, 728x90, 160x600", "variants": 3},
        ],
        "bidding_options": ["Manual CPC", "Target CPA", "Maximise Conversions"],
    },
    "meta": {
        "name": "Meta Ads (Facebook/Instagram)",
        "min_budget": 2000,
        "campaign_types": ["Conversions - Cold", "Conversions - Retargeting", "Awareness - Broad"],
        "ad_formats": [
            {"format": "Single Image", "dimensions": "1080x1080, 1200x628", "variants": 4},
            {"format": "Video", "dimensions": "1080x1080, 1080x1920", "max_length": "60s", "variants": 3},
        ],
        "bidding_options": ["Lowest Cost", "Cost Cap", "Bid Cap"],
    },
    "linkedin": {
        "name": "LinkedIn Ads",
        "min_budget": 5000,
        "campaign_types": ["Lead Gen - Decision Makers", "Lead Gen - Practitioners", "Retargeting - Website"],
        "ad_formats": [
            {"format": "Sponsored Content", "headline_limit": 70, "intro_limit": 150, "variants": 4},
            {"format": "Message Ad", "subject_limit": 60, "body_limit": 500, "variants": 2},
        ],
        "bidding_options": ["Manual CPC", "Target Cost", "Maximum Delivery"],
    },
    "tiktok": {
        "name": "TikTok Ads",
        "min_budget": 1500,
        "campaign_types": ["Conversions - Interest", "Conversions - Lookalike", "Retargeting"],
        "ad_formats": [
            {"format": "In-Feed Video", "dimensions": "1080x1920 (9:16)", "max_length": "60s", "variants": 5},
            {"format": "Spark Ad", "dimensions": "Creator content", "variants": 3},
        ],
        "bidding_options": ["Lowest Cost", "Cost Cap", "Bid Cap"],
    },
}

BUDGET_TIERS: dict[str, float] = {
    "proven": 0.70,
    "scaling": 0.20,
    "experiment": 0.10,
}

RETARGETING_STAGES: list[dict] = [
    {"stage": 1, "name": "Re-engage", "window": "1-7 days", "freq_cap": "3/day", "creative": "Value prop + social proof"},
    {"stage": 2, "name": "Nurture", "window": "8-30 days", "freq_cap": "2/day", "creative": "Case studies + comparisons"},
    {"stage": 3, "name": "Convert", "window": "1-14 days (high intent)", "freq_cap": "4/day", "creative": "Direct offer + urgency"},
    {"stage": 4, "name": "Win-back", "window": "31-90 days", "freq_cap": "1/day", "creative": "New features + refreshed offer"},
]


def validate_input(data: dict) -> list[str]:
    """Validate campaign parameters."""
    errors: list[str] = []
    if "objective" not in data:
        errors.append("Missing required field: objective (awareness | consideration | lead_gen | conversion)")
    if "budget" not in data:
        errors.append("Missing required field: budget (monthly budget in USD)")
    elif not isinstance(data["budget"], (int, float)) or data["budget"] <= 0:
        errors.append("Budget must be a positive number")
    if "platforms" not in data:
        errors.append("Missing required field: platforms (list of: google, meta, linkedin, tiktok)")
    elif not isinstance(data["platforms"], list):
        errors.append("Platforms must be a list")
    else:
        unknown = [p for p in data["platforms"] if p not in PLATFORM_DEFAULTS]
        if unknown:
            errors.append(f"Unknown platforms: {', '.join(unknown)}. Supported: {', '.join(PLATFORM_DEFAULTS)}")
    return errors


def allocate_budget(total: float, platforms: list[str], tier_overrides: dict | None = None) -> list[dict]:
    """Allocate budget across platforms."""
    tiers = tier_overrides or {}
    allocations: list[dict] = []
    remaining = total

    for i, platform in enumerate(platforms):
        tier = tiers.get(platform, "proven" if i == 0 else ("scaling" if i == 1 else "experiment"))
        share = BUDGET_TIERS.get(tier, 0.10)
        amount = round(total * share / max(1, len([p for p in platforms if tiers.get(p, "") == tier or (tier == "proven" and i == 0)])), 2)

        if len(platforms) == 1:
            amount = total
        elif len(platforms) == 2:
            amount = round(total * (0.65 if i == 0 else 0.35), 2)
        else:
            shares = [0.55, 0.25, 0.12, 0.08]
            amount = round(total * shares[min(i, len(shares) - 1)], 2)

        min_budget = PLATFORM_DEFAULTS[platform]["min_budget"]
        if amount < min_budget:
            amount = min_budget

        allocations.append({
            "platform": platform,
            "platform_name": PLATFORM_DEFAULTS[platform]["name"],
            "monthly_budget": amount,
            "pct_of_total": round(amount / total * 100, 1),
            "tier": tier,
            "min_budget": min_budget,
            "under_minimum": amount < min_budget,
        })

    return allocations


def build_platform_plan(platform: str, budget: float, objective: str) -> dict:
    """Build platform-specific campaign plan."""
    defaults = PLATFORM_DEFAULTS[platform]
    return {
        "platform": platform,
        "platform_name": defaults["name"],
        "monthly_budget": budget,
        "campaign_types": defaults["campaign_types"],
        "ad_formats": defaults["ad_formats"],
        "recommended_bidding": defaults["bidding_options"][0] if budget < 5000 else defaults["bidding_options"][1],
        "retargeting_stages": RETARGETING_STAGES,
    }


def generate(data: dict) -> dict:
    """Generate campaign plan from parameters."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "plan": None}

    objective = data["objective"]
    budget = float(data["budget"])
    platforms = data["platforms"]
    icp = data.get("icp", {})

    allocations = allocate_budget(budget, platforms, data.get("tiers"))
    platform_plans = []
    for alloc in allocations:
        plan = build_platform_plan(alloc["platform"], alloc["monthly_budget"], objective)
        platform_plans.append(plan)

    return {
        "error": None,
        "campaign_brief": {
            "objective": objective,
            "total_monthly_budget": budget,
            "platform_count": len(platforms),
            "icp": icp,
        },
        "budget_allocation": allocations,
        "platform_plans": platform_plans,
        "retargeting_sequence": RETARGETING_STAGES,
        "measurement": {
            "primary_kpi": "Cost per MQL" if objective in ("lead_gen", "conversion") else "Cost per Impression",
            "secondary_kpi": "ROAS",
            "review_cadence": "weekly",
            "optimisation_trigger": "Pause ad groups below 1.5x ROAS after 14 days",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON input: {exc}"}))
        sys.exit(1)

    result = generate(data)
    output = json.dumps(result, indent=2)

    args = sys.argv[1:]
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(output + "\n", encoding="utf-8")
            print(f"Plan written to {args[idx]}")
        else:
            print("Error: -o requires a filename", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
