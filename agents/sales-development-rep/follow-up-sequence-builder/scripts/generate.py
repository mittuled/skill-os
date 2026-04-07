#!/usr/bin/env python3
"""
generate.py — Generate a contextual follow-up sequence for a specific sales scenario.

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

# Follow-up scenarios with cadence (days from last engagement) and touch count
SCENARIOS = {
    "post_demo": {
        "cadence_days": [0, 1, 3, 7, 14],
        "tone": "warm and confident",
        "urgency": "moderate",
        "description": "Prospect attended a demo; did not schedule next step",
    },
    "post_content": {
        "cadence_days": [0, 3, 7],
        "tone": "educational and low-pressure",
        "urgency": "low",
        "description": "Prospect downloaded content or attended webinar",
    },
    "post_meeting": {
        "cadence_days": [0, 2, 5, 10],
        "tone": "direct and action-oriented",
        "urgency": "high",
        "description": "Prospect had a discovery call; no next step scheduled",
    },
    "re_engagement": {
        "cadence_days": [0, 7, 21, 45],
        "tone": "curious and zero-pressure",
        "urgency": "low",
        "description": "Prospect went silent after active conversation",
    },
    "event_follow_up": {
        "cadence_days": [0, 1, 3, 7],
        "tone": "warm and personal",
        "urgency": "moderate",
        "description": "Met prospect at conference or industry event",
    },
}

# Exit criteria defaults by scenario
EXIT_CRITERIA = {
    "post_demo": {"max_no_response_days": 14, "max_touches": 5},
    "post_content": {"max_no_response_days": 7, "max_touches": 3},
    "post_meeting": {"max_no_response_days": 10, "max_touches": 4},
    "re_engagement": {"max_no_response_days": 45, "max_touches": 4},
    "event_follow_up": {"max_no_response_days": 7, "max_touches": 4},
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["prospect_name", "company", "scenario"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "scenario" in data and data["scenario"] not in SCENARIOS:
        errors.append(f"scenario must be one of: {list(SCENARIOS.keys())}")
    return errors


def build_follow_up(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    scenario_key = data["scenario"]
    scenario = SCENARIOS[scenario_key]
    exit_crit = EXIT_CRITERIA[scenario_key]
    touches_input = data.get("touches", [])

    cadence = scenario["cadence_days"]
    sequence = []
    for i, day in enumerate(cadence):
        touch_data = touches_input[i] if i < len(touches_input) else {}
        sequence.append({
            "touch_number": i + 1,
            "day": day,
            "channel": "email" if i % 2 == 0 else "linkedin",
            "value_add": touch_data.get("value_add", f"Touch {i + 1} — {scenario['tone']}"),
            "body_preview": touch_data.get("body_preview", ""),
            "cta": touch_data.get("cta", ""),
        })

    result = {
        "prospect": data["prospect_name"],
        "company": data["company"],
        "scenario": scenario_key,
        "scenario_description": scenario["description"],
        "tone": scenario["tone"],
        "urgency": scenario["urgency"],
        "total_touches": len(sequence),
        "sequence": sequence,
        "exit_criteria": {
            "max_touches_without_response": exit_crit["max_touches"],
            "max_days_without_response": exit_crit["max_no_response_days"],
            "exit_action": data.get("exit_action", "Archive and move to nurture track"),
            "escalation_trigger": data.get("escalation_trigger", "Job change or competitor announcement"),
        },
        "engagement_context": data.get("engagement_context", ""),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = build_follow_up(data)
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
