#!/usr/bin/env python3
"""
run.py — Capture, classify, and log account signals from customer interactions.

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

SIGNAL_TYPES = ["expansion_opportunity", "churn_risk", "relationship_health", "competitive_threat", "product_feedback"]
CONFIDENCE_LEVELS = ["confirmed", "inferred", "speculative"]

INTERACTION_TYPES = ["qbr", "check_in", "support_escalation", "renewal_discussion", "ad_hoc"]

# Auto-classification hints: keyword → likely signal type
KEYWORD_HINTS = {
    "expansion_opportunity": ["more users", "scaling", "new team", "budget approved", "new use case", "more capacity"],
    "churn_risk": ["cancel", "not happy", "switching", "looking at alternatives", "too expensive", "not renewing", "disappointed"],
    "competitive_threat": ["competitor", "evaluated", "comparing", "pricing comparison", "RFP", "vendor review"],
    "product_feedback": ["feature request", "missing", "wish", "would be great if", "pain point", "workflow gap"],
    "relationship_health": ["great relationship", "executive sponsor", "team change", "new contact", "satisfied", "NPS"],
}

REQUIRED_FIELDS = ["account_name", "interaction_type", "signal_notes"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "interaction_type" in data and data["interaction_type"] not in INTERACTION_TYPES:
        errors.append(f"interaction_type must be one of {INTERACTION_TYPES}")
    if "confidence" in data and data["confidence"] not in CONFIDENCE_LEVELS:
        errors.append(f"confidence must be one of {CONFIDENCE_LEVELS}")
    return errors


def classify_signal(notes: str) -> str:
    """Auto-classify signal type based on keyword hints."""
    notes_lower = notes.lower()
    scores: dict[str, int] = {stype: 0 for stype in SIGNAL_TYPES}
    for signal_type, keywords in KEYWORD_HINTS.items():
        for keyword in keywords:
            if keyword in notes_lower:
                scores[signal_type] += 1
    best_type = max(scores, key=lambda k: scores[k])
    return best_type if scores[best_type] > 0 else "relationship_health"


def collect_signal(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    notes = data["signal_notes"]
    inferred_type = classify_signal(notes)
    signal_type = data.get("signal_type", inferred_type)
    confidence = data.get("confidence", "inferred")

    # Build CRM entry
    crm_entry = {
        "account_name": data["account_name"],
        "interaction_type": data["interaction_type"],
        "interaction_date": data.get("interaction_date", "2026-03-31"),
        "signal_type": signal_type,
        "inferred_type": inferred_type,
        "type_confirmed_by_user": "signal_type" in data,
        "confidence": confidence,
        "raw_notes": notes,
        "tags": [signal_type, data["interaction_type"], confidence],
        "follow_up_required": signal_type in ["churn_risk", "competitive_threat"],
        "synthesiser_ready": True,
    }

    recommendations = []
    if signal_type == "churn_risk":
        recommendations.append("Flag for portfolio synthesis — churn risk signals need AM lead attention within 24 hours")
    if signal_type == "competitive_threat":
        recommendations.append("Share with AM lead and product team immediately")
    if signal_type == "expansion_opportunity":
        recommendations.append("Submit to AM lead for opportunity framing")
    if confidence == "speculative":
        recommendations.append("Schedule follow-up interaction to confirm or rule out this signal")

    return {
        "error": None,
        "result": {
            "crm_entry": crm_entry,
            "signal_summary": f"{signal_type.replace('_', ' ').title()} signal ({confidence} confidence) captured from {data['interaction_type'].replace('_', ' ')} with {data['account_name']}",
            "recommendations": recommendations,
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = collect_signal(data)
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
