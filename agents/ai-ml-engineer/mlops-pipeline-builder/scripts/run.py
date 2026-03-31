#!/usr/bin/env python3
"""
run.py — Build and validate an MLOps pipeline configuration for automated training, evaluation, and deployment.

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

PIPELINE_STAGES = [
    {"stage": "data_validation", "gate": False, "description": "Validate data schema, volumes, and quality"},
    {"stage": "feature_engineering", "gate": False, "description": "Transform raw data into model features"},
    {"stage": "model_training", "gate": False, "description": "Train candidate model with experiment tracking"},
    {"stage": "model_evaluation", "gate": True, "description": "Evaluate against accuracy, fairness, and latency requirements"},
    {"stage": "model_registration", "gate": True, "description": "Register model artefact with version and metadata"},
    {"stage": "staging_deployment", "gate": True, "description": "Deploy to staging environment for shadow testing"},
    {"stage": "production_promotion", "gate": True, "description": "Promote to production after approval"},
]

REQUIRED_GATES = ["model_evaluation", "staging_deployment", "production_promotion"]

REQUIRED_FIELDS = ["pipeline_name", "model_name", "trigger_type", "stages_enabled"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "trigger_type" in data and data["trigger_type"] not in ["schedule", "data_drift", "manual", "webhook"]:
        errors.append("trigger_type must be one of: schedule, data_drift, manual, webhook")
    if "stages_enabled" in data:
        valid_stages = {s["stage"] for s in PIPELINE_STAGES}
        for stage in data["stages_enabled"]:
            if stage not in valid_stages:
                errors.append(f"Unknown stage: {stage}")
    return errors


def build_pipeline(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    stages_enabled = set(data["stages_enabled"])
    missing_gates = [gate for gate in REQUIRED_GATES if gate not in stages_enabled]

    warnings = []
    if missing_gates:
        warnings.append(f"Missing required gates: {missing_gates} — models can be promoted without validation")

    pipeline_stages = []
    for stage_def in PIPELINE_STAGES:
        if stage_def["stage"] in stages_enabled:
            pipeline_stages.append({
                "stage": stage_def["stage"],
                "description": stage_def["description"],
                "is_gate": stage_def["gate"],
                "requires_approval": stage_def["gate"] and stage_def["stage"] in REQUIRED_GATES,
            })

    # Build monitoring config
    monitoring_config = {
        "drift_detection": {
            "enabled": data.get("drift_monitoring", True),
            "method": "PSI (Population Stability Index) on input features",
            "threshold": 0.2,
            "frequency": "weekly",
            "action_on_trigger": "data_drift" if data.get("trigger_type") == "data_drift" else "alert_only",
        },
        "performance_monitoring": {
            "metrics_tracked": data.get("performance_metrics", ["accuracy", "p99_latency_ms", "prediction_volume"]),
            "alert_threshold": "5% drop in primary metric",
        },
    }

    return {
        "error": None,
        "result": {
            "pipeline_name": data["pipeline_name"],
            "model_name": data["model_name"],
            "trigger": {"type": data["trigger_type"], "schedule": data.get("schedule", "0 2 * * 0") if data["trigger_type"] == "schedule" else None},
            "stages": pipeline_stages,
            "gates_configured": [s["stage"] for s in pipeline_stages if s["is_gate"]],
            "warnings": warnings,
            "monitoring": monitoring_config,
            "reproducibility": {
                "data_versioning": "All training datasets versioned with hash",
                "code_versioning": "Git commit SHA pinned to every run",
                "artefact_storage": "Model artefacts stored in versioned object store",
                "experiment_tracking": "MLflow run ID linked to every model registry entry",
            },
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = build_pipeline(data)
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
