#!/usr/bin/env python3
"""
generate.py — Generate an account management playbook with QBR templates, expansion frameworks, and renewal strategy.

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

# Playbook sections and their required components
PLAYBOOK_SECTIONS = {
    "qbr_template": {
        "title": "Quarterly Business Review Template",
        "components": [
            "health_metrics_review",
            "usage_and_adoption_analysis",
            "value_delivered_summary",
            "roadmap_alignment",
            "expansion_discussion",
            "next_quarter_commitments",
        ],
    },
    "expansion_frameworks": {
        "title": "Expansion Conversation Frameworks",
        "scenarios": ["upsell", "cross_sell", "tier_upgrade", "multi_year_renewal"],
    },
    "renewal_strategy": {
        "title": "Renewal Playbook",
        "timeline_steps": [
            {"weeks_before_renewal": 12, "action": "Begin renewal health assessment"},
            {"weeks_before_renewal": 8, "action": "Present renewal proposal and multi-year options"},
            {"weeks_before_renewal": 4, "action": "Final negotiation and procurement engagement"},
            {"weeks_before_renewal": 1, "action": "Signature chase and processing"},
        ],
    },
    "escalation_procedures": {
        "title": "Escalation Procedures",
        "triggers": [
            "NPS score below 6",
            "Support tickets unresolved >7 days",
            "Executive sponsor change",
            "Competitor evaluation started",
            "Usage drop >20% month-over-month",
        ],
    },
}

EXPANSION_OBJECTIONS = {
    "upsell": [
        {"objection": "We don't have budget this quarter", "response": "Monthly billing available; annual commit unlocks volume discount."},
        {"objection": "We haven't used what we have", "response": "Let's review adoption together and identify quick wins before discussing capacity."},
    ],
    "cross_sell": [
        {"objection": "We use a different tool for that", "response": "Integration is native — your team won't need to change workflows."},
        {"objection": "We need to evaluate options", "response": "Happy to run a 30-day pilot; setup takes under two hours."},
    ],
    "tier_upgrade": [
        {"objection": "The features don't justify the cost", "response": "Let's map the Enterprise features directly to your stated Q3 initiatives."},
    ],
    "multi_year_renewal": [
        {"objection": "Our company policy requires annual reviews", "response": "We can structure a 2-year term with an annual opt-down clause."},
    ],
}

REQUIRED_FIELDS = ["company_name", "product_name", "am_team_size", "avg_contract_value_usd"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    return errors


def generate_playbook(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    product = data["product_name"]
    acv = data["avg_contract_value_usd"]
    team_size = data["am_team_size"]

    # Scale QBR cadence based on ACV
    qbr_cadence = "quarterly" if acv >= 20000 else "bi-annual"

    playbook = {
        "playbook_title": f"{company} Account Management Playbook",
        "product": product,
        "version": "1.0",
        "qbr_cadence": qbr_cadence,
        "sections": {},
    }

    # QBR template
    playbook["sections"]["qbr_template"] = {
        "title": PLAYBOOK_SECTIONS["qbr_template"]["title"],
        "recommended_duration_minutes": 60,
        "agenda": [
            {"item": "Account health scorecard review", "minutes": 10},
            {"item": "Usage and adoption deep-dive", "minutes": 15},
            {"item": "Value delivered since last QBR", "minutes": 10},
            {"item": "Roadmap alignment and upcoming releases", "minutes": 10},
            {"item": "Expansion discussion (if applicable)", "minutes": 10},
            {"item": "Next quarter commitments and success metrics", "minutes": 5},
        ],
        "health_metrics": data.get("health_metrics", ["NPS", "DAU/MAU ratio", "feature adoption rate", "support ticket volume"]),
    }

    # Expansion frameworks
    expansion_frameworks = {}
    for scenario in PLAYBOOK_SECTIONS["expansion_frameworks"]["scenarios"]:
        expansion_frameworks[scenario] = {
            "opening_line": f"Based on your usage patterns, I wanted to share how {product} can help you achieve [specific outcome].",
            "value_anchor": "Tie to a business goal the customer stated in the last QBR.",
            "objection_handling": EXPANSION_OBJECTIONS.get(scenario, []),
        }
    playbook["sections"]["expansion_frameworks"] = expansion_frameworks

    # Renewal strategy
    playbook["sections"]["renewal_strategy"] = {
        "title": PLAYBOOK_SECTIONS["renewal_strategy"]["title"],
        "timeline": PLAYBOOK_SECTIONS["renewal_strategy"]["timeline_steps"],
        "multi_year_incentives": {
            "2_year": "5% discount + locked pricing",
            "3_year": "10% discount + locked pricing + dedicated CSM",
        },
        "risk_thresholds": {
            "low_risk": "NPS >= 8, usage trending up, no open escalations",
            "medium_risk": "NPS 6-7 or flat usage",
            "high_risk": "NPS < 6 or usage decline >15%",
        },
    }

    # Escalation procedures
    playbook["sections"]["escalation_procedures"] = {
        "title": PLAYBOOK_SECTIONS["escalation_procedures"]["title"],
        "triggers": PLAYBOOK_SECTIONS["escalation_procedures"]["triggers"],
        "escalation_path": [
            {"level": 1, "owner": "Account Manager", "response_time_hours": 24},
            {"level": 2, "owner": "Account Management Lead", "response_time_hours": 4},
            {"level": 3, "owner": "CBO / Executive Sponsor", "response_time_hours": 2},
        ],
    }

    return {"error": None, "result": playbook}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_playbook(data)
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
