#!/usr/bin/env python3
"""
run.py — Process and categorize sales objections, draft updated response frameworks.

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

# Objection categories
OBJECTION_CATEGORIES = {
    "pricing": "Price, cost, ROI, budget, payment terms",
    "competition": "Competitor comparison, preference for alternative",
    "product_capability": "Feature gap, technical limitation",
    "timing": "Not now, next quarter, already evaluated",
    "trust": "Vendor credibility, risk, references",
}

# Frequency thresholds for priority
HIGH_FREQUENCY_THRESHOLD = 5   # 5+ reports = high priority
MEDIUM_FREQUENCY_THRESHOLD = 2  # 2-4 reports = medium priority

# Pattern: acknowledge-reframe-evidence
def build_response_framework(objection: dict) -> dict:
    return {
        "objection": objection["text"],
        "category": objection.get("category", "uncategorized"),
        "frequency": objection.get("frequency", 1),
        "priority": (
            "high" if objection.get("frequency", 1) >= HIGH_FREQUENCY_THRESHOLD
            else "medium" if objection.get("frequency", 1) >= MEDIUM_FREQUENCY_THRESHOLD
            else "low"
        ),
        "deal_loss_correlation": objection.get("deal_loss_correlation", False),
        "response_framework": {
            "acknowledge": objection.get("acknowledge", ""),
            "reframe": objection.get("reframe", ""),
            "evidence": objection.get("evidence", ""),
        },
        "escalation_needed": objection.get("escalation_needed", False),
        "escalation_reason": objection.get("escalation_reason", ""),
    }


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    if "objections" not in data:
        errors.append("Missing required field: objections")
        return errors
    for i, o in enumerate(data["objections"]):
        if "text" not in o:
            errors.append(f"objections[{i}] missing field: text")
        if "category" in o and o["category"] not in OBJECTION_CATEGORIES:
            errors.append(f"objections[{i}].category '{o['category']}' not recognised")
    return errors


def run_objection_update(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    objections = [build_response_framework(o) for o in data["objections"]]
    # Sort: high priority + deal-loss correlation first
    objections.sort(key=lambda x: (
        0 if x["priority"] == "high" and x["deal_loss_correlation"] else
        1 if x["priority"] == "high" else
        2 if x["priority"] == "medium" else 3
    ))

    escalations = [o for o in objections if o["escalation_needed"]]
    high_priority = [o for o in objections if o["priority"] == "high"]

    result = {
        "update_source": data.get("source", ""),
        "total_objections": len(objections),
        "high_priority_count": len(high_priority),
        "escalations_needed": len(escalations),
        "objections": objections,
        "escalation_summary": [
            {"objection": o["objection"], "reason": o["escalation_reason"]}
            for o in escalations
        ],
        "changelog": data.get("changelog_notes", ""),
        "publish_to": data.get("publish_to", "sales-playbook"),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_objection_update(data)
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
