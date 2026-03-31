#!/usr/bin/env python3
"""
generate.py — Generate an ML system architecture design including feature pipeline, training infra, and serving topology.

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

SERVING_PATTERNS = {
    "real_time": {"latency_target_ms": 50, "infrastructure": "model server (TorchServe/TF Serving)", "caching": "feature cache required"},
    "near_real_time": {"latency_target_ms": 500, "infrastructure": "REST API with model server", "caching": "feature cache recommended"},
    "batch": {"latency_target_ms": None, "infrastructure": "batch job scheduler (Airflow/Prefect)", "caching": "precomputed feature store"},
}

FEATURE_STORE_REQUIREMENTS = {
    "high_cardinality": "Dedicated feature store (Feast/Tecton) required for entity lookups",
    "time_series": "Point-in-time correct feature retrieval required to prevent data leakage",
    "streaming": "Online feature store with streaming ingestion (Kafka → Redis/DynamoDB)",
    "simple": "In-memory feature computation at serving time is sufficient",
}

REQUIRED_FIELDS = ["system_name", "task_type", "serving_pattern", "feature_sources"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "serving_pattern" in data and data["serving_pattern"] not in SERVING_PATTERNS:
        errors.append(f"serving_pattern must be one of {list(SERVING_PATTERNS.keys())}")
    return errors


def generate_architecture(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    serving = SERVING_PATTERNS[data["serving_pattern"]]
    feature_sources = data["feature_sources"]
    feature_complexity = data.get("feature_complexity", "simple")

    architecture = {
        "system_name": data["system_name"],
        "task_type": data["task_type"],
        "components": {
            "feature_pipeline": {
                "offline_store": "Data warehouse (BigQuery/Redshift) for training feature materialisation",
                "online_store": "Redis or DynamoDB for low-latency feature serving" if data["serving_pattern"] != "batch" else "Not required",
                "feature_sources": feature_sources,
                "feature_store_note": FEATURE_STORE_REQUIREMENTS.get(feature_complexity, FEATURE_STORE_REQUIREMENTS["simple"]),
                "transformation_layer": "dbt for offline transforms; Flink/Spark Streaming for real-time",
            },
            "training_infrastructure": {
                "orchestration": "Kubeflow Pipelines or Airflow DAG",
                "compute": data.get("training_compute", "GPU cluster (spot instances for cost)"),
                "experiment_tracking": "MLflow or Weights & Biases",
                "model_registry": "MLflow Registry with staging/production stages",
                "data_versioning": "DVC or Delta Lake versioning",
            },
            "serving_infrastructure": {
                "serving_pattern": data["serving_pattern"],
                "infrastructure": serving["infrastructure"],
                "latency_target_ms": serving["latency_target_ms"],
                "caching_strategy": serving["caching"],
                "scaling": "Horizontal pod autoscaling on prediction volume",
            },
            "monitoring": {
                "prediction_logging": "Log all predictions with input features to object store",
                "drift_detection": "Statistical tests (PSI, KS) on feature distributions weekly",
                "performance_tracking": "Business metric correlation with model outputs",
                "alerting": "Alert when accuracy drops >5% or drift score exceeds threshold",
            },
        },
        "architecture_decisions": [
            f"Serving pattern: {data['serving_pattern']} — {serving['infrastructure']}",
            f"Feature complexity: {feature_complexity} — {FEATURE_STORE_REQUIREMENTS.get(feature_complexity, '')}",
            "Separate offline and online feature computation paths to prevent training-serving skew",
            "Model registry gates all promotions — no direct-to-production deployments",
        ],
        "risks": [
            "Training-serving skew if offline and online feature transforms diverge",
            "Feature staleness in online store during ingestion pipeline failures",
            "Model version pinning required to prevent unintended rollouts",
        ],
    }

    return {"error": None, "result": architecture}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_architecture(data)
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
