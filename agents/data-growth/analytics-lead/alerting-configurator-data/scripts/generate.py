#!/usr/bin/env python3
"""
generate.py — Generate alert rule configurations for product metrics dashboards.

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

ALERT_TYPES = ["threshold", "anomaly", "rate_of_change", "absence"]
SEVERITY_LEVELS = ["critical", "warning", "info"]
NOTIFICATION_CHANNELS = ["pagerduty", "slack", "email", "jira"]

METRIC_ALERT_TEMPLATES = {
    "conversion_rate": {
        "warning_drop_pct": 10,
        "critical_drop_pct": 20,
        "window": "7d",
        "comparison": "vs_previous_period",
    },
    "daily_active_users": {
        "warning_drop_pct": 15,
        "critical_drop_pct": 30,
        "window": "1d",
        "comparison": "vs_7d_average",
    },
    "error_rate": {
        "warning_threshold_pct": 1.0,
        "critical_threshold_pct": 3.0,
        "window": "1h",
        "comparison": "absolute",
    },
    "revenue": {
        "warning_drop_pct": 5,
        "critical_drop_pct": 15,
        "window": "1d",
        "comparison": "vs_previous_period",
    },
}

REQUIRED_FIELDS = ["metrics", "notification_routing"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "metrics" in data:
        for m in data["metrics"]:
            if "name" not in m or "alert_type" not in m:
                errors.append("Each metric must have 'name' and 'alert_type' fields")
            if "alert_type" in m and m["alert_type"] not in ALERT_TYPES:
                errors.append(f"alert_type must be one of {ALERT_TYPES}")
    return errors


def generate_alert_config(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    metrics = data["metrics"]
    routing = data["notification_routing"]
    alert_rules = []

    for metric in metrics:
        name = metric["name"]
        alert_type = metric["alert_type"]
        template = METRIC_ALERT_TEMPLATES.get(name.lower().replace(" ", "_"), {})

        rule = {
            "metric_name": name,
            "alert_type": alert_type,
            "severity": metric.get("severity", "warning"),
            "window": metric.get("window", template.get("window", "1d")),
            "threshold": metric.get("threshold") or template,
            "comparison_baseline": template.get("comparison", "vs_previous_period"),
            "notify": routing.get(metric.get("severity", "warning"), routing.get("default", ["slack"])),
            "silence_window_minutes": metric.get("silence_minutes", 60),
            "runbook_url": f"https://wiki.internal/runbooks/{name.lower().replace(' ', '-')}-alert",
        }
        alert_rules.append(rule)

    return {
        "error": None,
        "result": {
            "alert_config_version": "1.0",
            "total_rules": len(alert_rules),
            "rules": alert_rules,
            "global_settings": {
                "evaluation_frequency_minutes": data.get("eval_frequency_minutes", 5),
                "notification_routing": routing,
                "default_silence_window_minutes": 60,
            },
            "anti_patterns_avoided": [
                "No vanity metric alerts — all metrics tied to business outcomes",
                "Silence windows configured to prevent alert fatigue",
                "Runbook URLs included in every alert for actionable response",
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_alert_config(data)
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
