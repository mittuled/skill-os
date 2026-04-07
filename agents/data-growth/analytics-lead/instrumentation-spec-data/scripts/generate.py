#!/usr/bin/env python3
"""
generate.py — Generate a complete instrumentation spec defining event names, properties, and trigger conditions.

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

UNIVERSAL_PROPERTIES = [
    {"name": "user_id", "type": "string", "required": True, "description": "Unique user identifier"},
    {"name": "anonymous_id", "type": "string", "required": True, "description": "Pre-login anonymous session ID"},
    {"name": "timestamp", "type": "datetime", "required": True, "description": "ISO 8601 UTC event timestamp"},
    {"name": "session_id", "type": "string", "required": True, "description": "Session identifier"},
    {"name": "platform", "type": "string", "required": True, "description": "web | ios | android | server"},
]

TRIGGER_TEMPLATES = {
    "page_view": "Fired when the user navigates to or loads the page",
    "button_click": "Fired when the user clicks the button element",
    "form_submit": "Fired when the user submits the form successfully (after client validation passes)",
    "api_call": "Fired server-side when the API endpoint responds with a success status",
    "state_change": "Fired when the application state transitions to the specified state",
}

REQUIRED_FIELDS = ["spec_name", "feature_name", "events"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "events" in data:
        for event in data["events"]:
            if "name" not in event:
                errors.append("Each event must have a 'name' field")
            if "trigger" not in event:
                errors.append(f"Event '{event.get('name', '?')}' must have a 'trigger' field")
    return errors


def generate_spec(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    events = data["events"]
    spec_events = []

    for event in events:
        name = event["name"]
        custom_props = event.get("properties", [])
        all_props = UNIVERSAL_PROPERTIES + [
            {"name": p["name"], "type": p.get("type", "string"), "required": p.get("required", True), "description": p.get("description", "")}
            for p in custom_props
        ]

        spec_events.append({
            "event_name": name,
            "trigger_condition": event["trigger"],
            "firing_location": event.get("firing_location", "client"),
            "properties": all_props,
            "property_count": len(all_props),
            "sample_call": f"analytics.track('{name}', {{ user_id, timestamp, session_id, platform, {', '.join(p['name'] for p in custom_props)} }})",
            "query_example": f"SELECT COUNT(*) FROM events WHERE event_name = '{name}' AND DATE(timestamp) = CURRENT_DATE()",
        })

    return {
        "error": None,
        "result": {
            "spec_name": data["spec_name"],
            "feature_name": data["feature_name"],
            "version": "1.0",
            "total_events": len(spec_events),
            "events": spec_events,
            "universal_properties": UNIVERSAL_PROPERTIES,
            "implementation_notes": [
                "Universal properties must be present on every event — use a shared event wrapper",
                "Server-side events are authoritative for revenue and signup events",
                "All events must be validated in staging before production rollout",
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_spec(data)
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
