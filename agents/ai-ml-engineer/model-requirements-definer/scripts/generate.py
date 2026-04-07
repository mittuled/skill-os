#!/usr/bin/env python3
"""
generate.py — Generate a model requirements document from business needs and constraints.

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

TASK_TYPE_DEFAULTS = {
    "classification": {"primary_metric": "AUC-ROC", "secondary_metrics": ["F1", "Precision", "Recall"]},
    "regression": {"primary_metric": "RMSE", "secondary_metrics": ["MAE", "R-squared"]},
    "ranking": {"primary_metric": "NDCG@10", "secondary_metrics": ["MAP", "MRR"]},
    "generation": {"primary_metric": "BLEU", "secondary_metrics": ["ROUGE-L", "Human eval"]},
    "anomaly_detection": {"primary_metric": "AUC-ROC", "secondary_metrics": ["Precision@K", "Recall@K"]},
}

FAIRNESS_METRICS = ["demographic_parity", "equalized_odds", "predictive_parity", "individual_fairness"]

REQUIRED_FIELDS = ["model_name", "task_type", "business_objective", "success_criteria"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "task_type" in data and data["task_type"] not in TASK_TYPE_DEFAULTS:
        errors.append(f"task_type must be one of {list(TASK_TYPE_DEFAULTS.keys())}")
    return errors


def generate_requirements(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    task_type = data["task_type"]
    metric_defaults = TASK_TYPE_DEFAULTS[task_type]
    success = data["success_criteria"]

    requirements = {
        "model_name": data["model_name"],
        "version": "1.0",
        "business_objective": data["business_objective"],
        "task_type": task_type,
        "input_schema": {
            "features": data.get("input_features", []),
            "feature_count": len(data.get("input_features", [])),
            "data_types": data.get("input_data_types", {}),
            "required_fields": data.get("required_input_fields", []),
        },
        "output_schema": {
            "type": "probability_score" if task_type in ["classification", "anomaly_detection"] else "numeric_value",
            "range": "[0, 1]" if task_type in ["classification", "anomaly_detection"] else "task-dependent",
            "format": data.get("output_format", "float"),
        },
        "accuracy_requirements": {
            "primary_metric": metric_defaults["primary_metric"],
            "minimum_threshold": success.get("min_accuracy"),
            "target_threshold": success.get("target_accuracy"),
            "secondary_metrics": metric_defaults["secondary_metrics"],
            "evaluation_dataset": data.get("evaluation_dataset_description", "Held-out test set, stratified by key segments"),
        },
        "latency_requirements": {
            "p50_ms": success.get("p50_latency_ms"),
            "p99_ms": success.get("p99_latency_ms"),
            "serving_mode": data.get("serving_mode", "synchronous"),
        },
        "fairness_requirements": {
            "applicable": data.get("fairness_required", False),
            "protected_attributes": data.get("protected_attributes", []),
            "max_disparity": success.get("max_fairness_disparity", 0.05),
            "metrics": FAIRNESS_METRICS[:2] if data.get("fairness_required") else [],
        },
        "operational_requirements": {
            "retraining_frequency": data.get("retraining_frequency", "monthly"),
            "model_size_mb_max": data.get("max_model_size_mb"),
            "interpretability": data.get("interpretability_required", False),
            "audit_logging": data.get("audit_required", False),
        },
        "acceptance_criteria": [
            f"Primary metric ({metric_defaults['primary_metric']}) ≥ {success.get('min_accuracy', 'TBD')}",
            f"p99 latency ≤ {success.get('p99_latency_ms', 'TBD')}ms",
        ] + ([f"Max fairness disparity ≤ {success.get('max_fairness_disparity', 0.05)}"] if data.get("fairness_required") else []),
    }

    return {"error": None, "result": requirements}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_requirements(data)
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
