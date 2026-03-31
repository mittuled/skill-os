#!/usr/bin/env python3
"""
run.py — Plan and prepare an analyst briefing with a Gartner, Forrester, or IDC analyst.

Usage:
    echo '<json>' | python3 run.py
    python3 run.py < input.json
    python3 run.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

BRIEFING_TYPES = ["introductory", "product_update", "strategy_briefing", "competitive_positioning", "evaluation_submission"]
ANALYST_FIRMS = ["Gartner", "Forrester", "IDC", "G2", "Ovum", "451_Research", "Omdia"]

BRIEFING_AGENDA_TEMPLATES = {
    "introductory": [
        {"item": "Company overview and founding story", "minutes": 10},
        {"item": "Market problem and customer pain points", "minutes": 10},
        {"item": "Product demonstration — core capabilities", "minutes": 20},
        {"item": "Traction and key customer wins", "minutes": 10},
        {"item": "Roadmap and strategic direction", "minutes": 5},
        {"item": "Q&A", "minutes": 15},
    ],
    "product_update": [
        {"item": "Context — what has changed since last briefing", "minutes": 5},
        {"item": "New product capabilities walkthrough", "minutes": 20},
        {"item": "Customer validation — quotes and case studies", "minutes": 10},
        {"item": "Competitive differentiation update", "minutes": 10},
        {"item": "Q&A", "minutes": 15},
    ],
    "strategy_briefing": [
        {"item": "Market evolution and company thesis", "minutes": 15},
        {"item": "Platform strategy and ecosystem", "minutes": 15},
        {"item": "Enterprise roadmap (12-18 months)", "minutes": 15},
        {"item": "Key partnerships and integrations", "minutes": 5},
        {"item": "Q&A", "minutes": 10},
    ],
}

REQUIRED_FIELDS = ["analyst_firm", "analyst_name", "briefing_type", "briefing_date"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "briefing_type" in data and data["briefing_type"] not in BRIEFING_TYPES:
        errors.append(f"briefing_type must be one of {BRIEFING_TYPES}")
    return errors


def plan_briefing(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    briefing_type = data["briefing_type"]
    agenda = BRIEFING_AGENDA_TEMPLATES.get(briefing_type, BRIEFING_AGENDA_TEMPLATES["introductory"])
    total_minutes = sum(a["minutes"] for a in agenda)

    prep_checklist = [
        "Research analyst's recent published reports and stated coverage priorities",
        "Pull analyst's prior commentary on competitors in the space",
        "Prepare 3 customer reference stories relevant to analyst's focus area",
        "Brief internal presenters on analyst's known positions and sensitivities",
        "Prepare competitive landscape one-pager if analyst covers the category",
        "Draft key messages to reinforce (max 3 positioning statements)",
    ]

    if briefing_type == "evaluation_submission":
        prep_checklist.extend([
            "Review evaluation criteria published by the firm",
            "Map product capabilities to each evaluation criterion",
            "Prepare customer reference list (minimum 3 referenceable accounts)",
            "Draft written responses to questionnaire if applicable",
        ])

    follow_up_tasks = [
        "Send thank-you note with any requested materials within 24 hours",
        "Log analyst's feedback, questions, and stated interests in AR CRM",
        "Schedule follow-up briefing or inquiry date if agreed",
        "Share key analyst insights with product and marketing teams",
    ]

    return {
        "error": None,
        "result": {
            "briefing_title": f"{briefing_type.replace('_', ' ').title()} Briefing — {data['analyst_name']} ({data['analyst_firm']})",
            "date": data["briefing_date"],
            "duration_minutes": total_minutes,
            "agenda": agenda,
            "prep_checklist": prep_checklist,
            "key_messages_to_reinforce": data.get("key_messages", []),
            "materials_to_prepare": ["Company deck (updated within 30 days)", "Product demo environment", "Customer case studies", "Competitive one-pager"],
            "follow_up_tasks": follow_up_tasks,
            "success_criteria": "Analyst acknowledges updated positioning and agrees to follow-up inquiry or adds company to coverage shortlist",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = plan_briefing(data)
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
