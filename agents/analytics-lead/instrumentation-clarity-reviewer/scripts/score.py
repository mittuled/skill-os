#!/usr/bin/env python3
"""
score.py — Audit an instrumentation spec for naming clarity, property completeness, and query coverage.

Usage:
    echo '<json>' | python3 score.py
    python3 score.py < input.json
    python3 score.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

NAMING_CONVENTION_RULES = [
    {"rule": "object_action_format", "description": "Event names follow object_action format (e.g., user_signed_up, file_uploaded)"},
    {"rule": "snake_case", "description": "All event names and property keys use snake_case"},
    {"rule": "past_tense_action", "description": "Action part is past tense (signed_up, not sign_up)"},
    {"rule": "no_generic_names", "description": "No generic names like 'clicked', 'viewed', 'event' without context"},
]

PROPERTY_REQUIREMENTS = {
    "required_universal": ["user_id", "timestamp", "session_id", "platform"],
    "required_per_event": ["event_name"],
    "recommended": ["user_cohort", "plan_tier", "feature_flag_variant"],
}

REQUIRED_FIELDS = ["spec_name", "events"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    return errors


def score_spec(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    events = data["events"]
    issues = []
    event_scores = []
    total_score = 0.0

    for event in events:
        name = event.get("name", "")
        properties = event.get("properties", [])
        prop_names = [p.get("name", "") for p in properties]
        event_issues = []
        event_score = 10.0

        # Check naming convention
        parts = name.split("_")
        if len(parts) < 2:
            event_issues.append(f"Name '{name}' should follow object_action format")
            event_score -= 2
        if name != name.lower():
            event_issues.append(f"Name '{name}' should be snake_case (all lowercase)")
            event_score -= 1

        # Check universal properties
        for req_prop in PROPERTY_REQUIREMENTS["required_universal"]:
            if req_prop not in prop_names:
                event_issues.append(f"Missing required universal property: {req_prop}")
                event_score -= 1.5

        # Check property types defined
        for prop in properties:
            if "type" not in prop:
                event_issues.append(f"Property '{prop.get('name', '?')}' has no type defined")
                event_score -= 0.5

        event_score = max(0.0, event_score)
        total_score += event_score
        issues.extend([f"{name}: {issue}" for issue in event_issues])
        event_scores.append({
            "event": name,
            "score": round(event_score, 1),
            "issues": event_issues,
        })

    avg_score = total_score / max(len(events), 1)
    if avg_score >= 8.5:
        verdict = "PASS — spec is ready for implementation"
    elif avg_score >= 6.0:
        verdict = "CONDITIONAL PASS — fix critical issues before implementation"
    else:
        verdict = "FAIL — spec requires significant revision"

    return {
        "error": None,
        "result": {
            "spec_name": data["spec_name"],
            "total_events": len(events),
            "average_score": round(avg_score, 2),
            "verdict": verdict,
            "event_scores": event_scores,
            "total_issues": len(issues),
            "critical_issues": [i for i in issues if "Missing required" in i],
            "naming_issues": [i for i in issues if "Name" in i or "snake_case" in i],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_spec(data)
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
