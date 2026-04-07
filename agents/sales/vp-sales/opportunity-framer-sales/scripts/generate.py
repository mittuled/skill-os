#!/usr/bin/env python3
"""
generate.py — Generate a sales opportunity frame brief for a beachhead segment.

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

MOTION_TYPES = ["product-led", "enterprise", "consultative-hybrid", "self-serve"]

MEDDIC_CRITERIA = [
    "metrics",
    "economic_buyer",
    "decision_criteria",
    "decision_process",
    "identify_pain",
    "champion",
]

ACV_BANDS = {
    "smb": {"min": 5_000, "max": 25_000, "motion": "product-led"},
    "mid-market": {"min": 25_001, "max": 100_000, "motion": "consultative-hybrid"},
    "enterprise": {"min": 100_001, "max": 1_000_000, "motion": "enterprise"},
}


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    required = ["segment_name", "segment_tier", "pain_points", "competitors", "value_metric"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "segment_tier" in data and data["segment_tier"] not in ACV_BANDS:
        errors.append(f"segment_tier must be one of: {list(ACV_BANDS.keys())}")
    if "competitors" in data and len(data["competitors"]) < 1:
        errors.append("competitors must contain at least one entry")
    return errors


def generate_opportunity_frame(data: dict) -> dict:
    """Generate a sales opportunity frame brief."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    tier = data["segment_tier"]
    band = ACV_BANDS[tier]
    motion = data.get("preferred_motion", band["motion"])
    competitors = data["competitors"]

    buyer_personas = data.get("buyer_personas", [
        {"role": "Economic Buyer", "title": "VP or above", "priority": "ROI and risk"},
        {"role": "Champion", "title": "Team lead or manager", "priority": "Adoption ease"},
        {"role": "Technical Evaluator", "title": "Architect or engineer", "priority": "Integration fit"},
    ])

    competitive_matrix = [
        {
            "competitor": c,
            "win_themes": data.get("win_themes", {}).get(c, ["faster time-to-value", "better support"]),
            "loss_themes": data.get("loss_themes", {}).get(c, ["price sensitivity", "incumbent inertia"]),
        }
        for c in competitors
    ]

    stage_gates = {
        "1-discovery": {"meddic": ["identify_pain", "metrics"], "exit_criteria": "Pain confirmed, ROI estimate shared"},
        "2-qualification": {"meddic": ["economic_buyer", "champion"], "exit_criteria": "Champion identified, EB access confirmed"},
        "3-evaluation": {"meddic": ["decision_criteria", "decision_process"], "exit_criteria": "Eval criteria aligned, timeline agreed"},
        "4-proposal": {"meddic": MEDDIC_CRITERIA, "exit_criteria": "Proposal accepted, legal review started"},
        "5-close": {"meddic": MEDDIC_CRITERIA, "exit_criteria": "Contract signed, kickoff scheduled"},
    }

    result = {
        "segment_profile": {
            "name": data["segment_name"],
            "tier": tier,
            "acv_range": band,
            "pain_points": data["pain_points"],
            "buying_committee": buyer_personas,
        },
        "competitive_positioning": {
            "value_proposition": f"Outcome-based: {data.get('value_proposition', 'reduce ' + data['pain_points'][0] + ' by measurable outcome')}",
            "matrix": competitive_matrix,
        },
        "deal_structure": {
            "pricing_model": data.get("pricing_model", "per-seat"),
            "value_metric": data["value_metric"],
            "acv_target": band["max"] // 2,
            "discount_guardrail_pct": 20,
            "contract_term_months": 12,
        },
        "sales_motion": {
            "type": motion,
            "stage_gates": stage_gates,
        },
        "enablement_brief_ready": True,
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_opportunity_frame(data)
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
