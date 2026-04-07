#!/usr/bin/env python3
"""
run.py — Generate a model training run plan with experiment configuration and reproducibility metadata.

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

# Supported model families and their default hyperparameter search spaces
MODEL_FAMILIES = {
    "gradient_boosted_trees": {
        "default_hyperparams": {"n_estimators": 500, "max_depth": 6, "learning_rate": 0.05, "subsample": 0.8},
        "tuning_space": {"n_estimators": [200, 500, 1000], "max_depth": [4, 6, 8], "learning_rate": [0.01, 0.05, 0.1]},
    },
    "neural_network": {
        "default_hyperparams": {"hidden_layers": [256, 128, 64], "dropout": 0.2, "learning_rate": 0.001, "batch_size": 256},
        "tuning_space": {"hidden_layers": [[128, 64], [256, 128, 64]], "dropout": [0.1, 0.2, 0.3], "learning_rate": [0.0001, 0.001, 0.01]},
    },
    "logistic_regression": {
        "default_hyperparams": {"C": 1.0, "penalty": "l2", "solver": "lbfgs", "max_iter": 1000},
        "tuning_space": {"C": [0.01, 0.1, 1.0, 10.0], "penalty": ["l1", "l2"]},
    },
    "random_forest": {
        "default_hyperparams": {"n_estimators": 200, "max_depth": None, "min_samples_split": 2},
        "tuning_space": {"n_estimators": [100, 200, 500], "max_depth": [None, 10, 20]},
    },
}

REQUIRED_FIELDS = ["experiment_name", "model_family", "dataset_version", "target_column"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "model_family" in data and data["model_family"] not in MODEL_FAMILIES:
        errors.append(f"model_family must be one of {list(MODEL_FAMILIES.keys())}")
    return errors


def plan_training_run(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    model_family = data["model_family"]
    model_config = MODEL_FAMILIES[model_family]
    hyperparams = data.get("hyperparameters", model_config["default_hyperparams"])

    training_plan = {
        "experiment_name": data["experiment_name"],
        "model_family": model_family,
        "dataset": {
            "version": data["dataset_version"],
            "target_column": data["target_column"],
            "feature_columns": data.get("feature_columns", []),
            "train_split": data.get("train_split", 0.70),
            "validation_split": data.get("validation_split", 0.15),
            "test_split": round(1.0 - data.get("train_split", 0.70) - data.get("validation_split", 0.15), 2),
        },
        "hyperparameters": hyperparams,
        "hyperparameter_search": {
            "enabled": data.get("run_hyperparameter_search", False),
            "search_space": model_config["tuning_space"] if data.get("run_hyperparameter_search") else {},
            "n_trials": data.get("n_trials", 20) if data.get("run_hyperparameter_search") else 0,
            "strategy": "bayesian_optimisation",
        },
        "cross_validation": {
            "enabled": data.get("cross_validation", True),
            "folds": data.get("cv_folds", 5),
            "stratified": True,
        },
        "reproducibility": {
            "random_seed": data.get("random_seed", 42),
            "data_hash": f"sha256:{data['dataset_version']}",
            "framework_version_pins": data.get("framework_versions", {}),
        },
        "experiment_tracking": {
            "backend": "MLflow",
            "metrics_to_log": data.get("metrics_to_log", ["train_loss", "val_loss", "primary_metric"]),
            "artefacts_to_log": ["model_weights", "feature_importance", "confusion_matrix", "hyperparameter_config"],
        },
        "stopping_criteria": {
            "early_stopping_patience": data.get("early_stopping_patience", 10),
            "max_training_time_minutes": data.get("max_training_time_minutes", 120),
        },
    }

    return {"error": None, "result": training_plan}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = plan_training_run(data)
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
