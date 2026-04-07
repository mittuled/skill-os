#!/usr/bin/env python3
"""
score.py — Score model health in production across prediction quality, data drift, and latency dimensions.

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

# Alert thresholds for production model health
HEALTH_THRESHOLDS = {
    "accuracy_drop_pct": {"warning": 3.0, "critical": 7.0},
    "feature_psi": {"warning": 0.1, "critical": 0.2},  # Population Stability Index
    "prediction_drift_psi": {"warning": 0.1, "critical": 0.2},
    "p99_latency_ms_increase_pct": {"warning": 20.0, "critical": 50.0},
    "error_rate_pct": {"warning": 0.5, "critical": 2.0},
    "feature_null_rate_pct": {"warning": 5.0, "critical": 15.0},
}

REQUIRED_FIELDS = ["model_name", "monitoring_window", "current_metrics", "baseline_metrics"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    return errors


def score_model_health(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    current = data["current_metrics"]
    baseline = data["baseline_metrics"]
    alerts = []
    health_checks = {}

    # Accuracy degradation
    if "accuracy" in current and "accuracy" in baseline:
        drop_pct = ((baseline["accuracy"] - current["accuracy"]) / baseline["accuracy"]) * 100
        status = "ok"
        if drop_pct >= HEALTH_THRESHOLDS["accuracy_drop_pct"]["critical"]:
            status = "critical"
            alerts.append({"severity": "CRITICAL", "dimension": "accuracy", "message": f"Accuracy dropped {drop_pct:.1f}% — trigger immediate retraining"})
        elif drop_pct >= HEALTH_THRESHOLDS["accuracy_drop_pct"]["warning"]:
            status = "warning"
            alerts.append({"severity": "WARNING", "dimension": "accuracy", "message": f"Accuracy dropped {drop_pct:.1f}% — monitor closely"})
        health_checks["accuracy"] = {"current": current["accuracy"], "baseline": baseline["accuracy"], "drop_pct": round(drop_pct, 2), "status": status}

    # Feature drift (PSI)
    feature_psi = current.get("feature_psi")
    if feature_psi is not None:
        status = "ok"
        if feature_psi >= HEALTH_THRESHOLDS["feature_psi"]["critical"]:
            status = "critical"
            alerts.append({"severity": "CRITICAL", "dimension": "feature_drift", "message": f"Feature PSI {feature_psi:.3f} exceeds critical threshold — data distribution has shifted significantly"})
        elif feature_psi >= HEALTH_THRESHOLDS["feature_psi"]["warning"]:
            status = "warning"
            alerts.append({"severity": "WARNING", "dimension": "feature_drift", "message": f"Feature PSI {feature_psi:.3f} — moderate drift detected, schedule model review"})
        health_checks["feature_drift"] = {"psi": feature_psi, "status": status}

    # Latency degradation
    if "p99_latency_ms" in current and "p99_latency_ms" in baseline:
        increase_pct = ((current["p99_latency_ms"] - baseline["p99_latency_ms"]) / baseline["p99_latency_ms"]) * 100
        status = "ok"
        if increase_pct >= HEALTH_THRESHOLDS["p99_latency_ms_increase_pct"]["critical"]:
            status = "critical"
            alerts.append({"severity": "CRITICAL", "dimension": "latency", "message": f"p99 latency increased {increase_pct:.0f}% — SLO breach risk"})
        elif increase_pct >= HEALTH_THRESHOLDS["p99_latency_ms_increase_pct"]["warning"]:
            status = "warning"
            alerts.append({"severity": "WARNING", "dimension": "latency", "message": f"p99 latency increased {increase_pct:.0f}%"})
        health_checks["latency"] = {"current_ms": current["p99_latency_ms"], "baseline_ms": baseline["p99_latency_ms"], "increase_pct": round(increase_pct, 1), "status": status}

    # Overall health
    critical_count = sum(1 for a in alerts if a["severity"] == "CRITICAL")
    warning_count = sum(1 for a in alerts if a["severity"] == "WARNING")

    if critical_count > 0:
        overall_health = "CRITICAL — immediate action required"
        recommended_action = "Trigger emergency retraining pipeline and page on-call ML engineer"
    elif warning_count > 0:
        overall_health = "DEGRADED — review within 24 hours"
        recommended_action = "Review drift reports, schedule retraining if trend continues"
    else:
        overall_health = "HEALTHY — no action required"
        recommended_action = "Continue monitoring on regular schedule"

    return {
        "error": None,
        "result": {
            "model_name": data["model_name"],
            "monitoring_window": data["monitoring_window"],
            "overall_health": overall_health,
            "health_checks": health_checks,
            "alerts": alerts,
            "alert_counts": {"critical": critical_count, "warning": warning_count},
            "recommended_action": recommended_action,
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_model_health(data)
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
