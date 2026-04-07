#!/usr/bin/env python3
"""
generate.py — Generate research roadmap inputs and open questions for product decision-making.

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

DECISION_TYPES = ["build_vs_buy", "market_entry", "pricing", "feature_prioritisation", "partnership", "platform_strategy"]
RESEARCH_METHODS = {
    "high_urgency": ["customer_interviews", "expert_interviews", "desk_research"],
    "medium_urgency": ["customer_interviews", "survey", "competitive_analysis"],
    "low_urgency": ["survey", "desk_research", "usage_data_analysis"],
}
REQUIRED_FIELDS = ["roadmap_cycle", "product_decisions"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "product_decisions" in data:
        for d in data["product_decisions"]:
            for field in ["decision", "decision_type", "urgency"]:
                if field not in d:
                    errors.append(f"Decision '{d.get('decision', '?')}' missing field: {field}")
    return errors


def generate_research_inputs(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    decisions = data["product_decisions"]
    research_inputs = []

    for decision in decisions:
        urgency = decision["urgency"]
        methods = RESEARCH_METHODS.get(urgency, RESEARCH_METHODS["medium_urgency"])
        open_questions = decision.get("open_questions", [])

        research_inputs.append({
            "decision": decision["decision"],
            "decision_type": decision["decision_type"],
            "urgency": urgency,
            "open_questions": open_questions,
            "open_questions_count": len(open_questions),
            "recommended_research_methods": methods,
            "estimated_weeks_to_answer": 2 if urgency == "high_urgency" else (4 if urgency == "medium_urgency" else 8),
            "decision_deadline": decision.get("decision_deadline"),
            "current_evidence_gap": "No research available — decision currently based on assumptions" if not decision.get("existing_research") else f"Existing: {decision['existing_research']}",
        })

    high_urgency = [r for r in research_inputs if r["urgency"] == "high_urgency"]
    total_questions = sum(r["open_questions_count"] for r in research_inputs)

    return {
        "error": None,
        "result": {
            "roadmap_cycle": data["roadmap_cycle"],
            "total_decisions_needing_research": len(research_inputs),
            "high_urgency_decisions": len(high_urgency),
            "total_open_questions": total_questions,
            "research_inputs": research_inputs,
            "prioritisation": "Address high urgency decisions first — they block planning cycle commitments",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_research_inputs(data)
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
