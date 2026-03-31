#!/usr/bin/env python3
"""
score.py — Score engineering team velocity health against DORA metrics and sprint commitments.

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

# DORA metric elite/high/medium/low thresholds
DORA_THRESHOLDS = {
    "deployment_frequency_per_week": {
        "elite": 7,   # multiple per day
        "high": 1,    # weekly
        "medium": 0.25,  # monthly
        "low": 0.0,
    },
    "lead_time_to_change_hours": {
        "elite": 1,
        "high": 24,
        "medium": 168,   # 1 week
        "low": 720,      # 1 month
        "direction": "lower_is_better",
    },
    "change_failure_rate_pct": {
        "elite": 5,
        "high": 10,
        "medium": 15,
        "low": 100,
        "direction": "lower_is_better",
    },
    "mttr_hours": {
        "elite": 1,
        "high": 24,
        "medium": 168,
        "low": 720,
        "direction": "lower_is_better",
    },
}

VELOCITY_VARIANCE_RISK_THRESHOLD_PCT = 20  # >20% variance from rolling avg is a risk signal


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    required = [
        "team_name",
        "sprint_velocity_completed",
        "sprint_velocity_planned",
        "rolling_avg_velocity",
        "dora_metrics",
    ]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "dora_metrics" in data:
        for metric in ["deployment_frequency_per_week", "lead_time_to_change_hours",
                       "change_failure_rate_pct", "mttr_hours"]:
            if metric not in data["dora_metrics"]:
                errors.append(f"dora_metrics missing: {metric}")
    return errors


def score_dora_metric(metric: str, value: float) -> tuple[str, int]:
    """Score a single DORA metric, returning (tier, score_0_to_100)."""
    thresholds = DORA_THRESHOLDS[metric]
    lower_better = thresholds.get("direction") == "lower_is_better"

    if lower_better:
        if value <= thresholds["elite"]:
            return "elite", 100
        elif value <= thresholds["high"]:
            return "high", 75
        elif value <= thresholds["medium"]:
            return "medium", 50
        else:
            return "low", 25
    else:
        if value >= thresholds["elite"]:
            return "elite", 100
        elif value >= thresholds["high"]:
            return "high", 75
        elif value >= thresholds["medium"]:
            return "medium", 50
        else:
            return "low", 25


def score_velocity(data: dict) -> dict:
    """Score team velocity health across sprint and DORA dimensions."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    completed = data["sprint_velocity_completed"]
    planned = data["sprint_velocity_planned"]
    rolling_avg = data["rolling_avg_velocity"]
    dora = data["dora_metrics"]

    # Sprint velocity score
    completion_rate = (completed / planned * 100) if planned > 0 else 0
    variance_from_avg = abs((completed - rolling_avg) / rolling_avg * 100) if rolling_avg > 0 else 0

    if completion_rate >= 90:
        velocity_score = 100
    elif completion_rate >= 75:
        velocity_score = 75
    elif completion_rate >= 60:
        velocity_score = 50
    else:
        velocity_score = 25

    # DORA metric scores
    dora_results = {}
    for metric, value in dora.items():
        if metric in DORA_THRESHOLDS:
            tier, score = score_dora_metric(metric, value)
            dora_results[metric] = {"value": value, "tier": tier, "score": score}

    dora_avg_score = sum(v["score"] for v in dora_results.values()) / len(dora_results) if dora_results else 50

    # Composite score: 40% velocity, 60% DORA
    composite = round(velocity_score * 0.4 + dora_avg_score * 0.6, 1)

    risk_flags = []
    if completion_rate < 75:
        risk_flags.append(f"Sprint completion rate {completion_rate:.1f}% — below 75% threshold, investigate blockers")
    if variance_from_avg > VELOCITY_VARIANCE_RISK_THRESHOLD_PCT:
        risk_flags.append(f"Velocity variance {variance_from_avg:.1f}% from rolling average — significant trend change")
    for metric, result in dora_results.items():
        if result["tier"] == "low":
            risk_flags.append(f"DORA metric '{metric}' is LOW tier — root cause investigation required")

    interventions = data.get("interventions", [])
    if completion_rate < 60 and not interventions:
        interventions.append("Schedule sprint retrospective to identify scope or process blockers")
    if dora_results.get("change_failure_rate_pct", {}).get("tier") in ("low", "medium"):
        interventions.append("Review deployment pipeline and test coverage to reduce change failure rate")

    result = {
        "team": data["team_name"],
        "composite_velocity_score": composite,
        "sprint_metrics": {
            "completed_points": completed,
            "planned_points": planned,
            "completion_rate_pct": round(completion_rate, 1),
            "rolling_avg_velocity": rolling_avg,
            "variance_from_avg_pct": round(variance_from_avg, 1),
            "velocity_score": velocity_score,
        },
        "dora_metrics": dora_results,
        "dora_avg_score": round(dora_avg_score, 1),
        "risk_flags": risk_flags,
        "recommended_interventions": interventions,
        "health_status": (
            "HEALTHY" if composite >= 75 else
            "AT_RISK" if composite >= 55 else
            "CRITICAL"
        ),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_velocity(data)
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
