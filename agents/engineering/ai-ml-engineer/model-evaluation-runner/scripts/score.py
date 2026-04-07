#!/usr/bin/env python3
"""
score.py — Score model evaluation results across accuracy, fairness, robustness, and latency dimensions.

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

EVALUATION_DIMENSIONS = {
    "accuracy": {
        "weight": 0.35,
        "description": "Task-appropriate accuracy metric vs requirement threshold",
    },
    "fairness": {
        "weight": 0.20,
        "description": "Demographic parity and equalized odds across protected attributes",
    },
    "robustness": {
        "weight": 0.20,
        "description": "Performance on adversarial, OOD, and noisy inputs",
    },
    "latency": {
        "weight": 0.15,
        "description": "p99 inference latency vs requirement",
    },
    "baseline_improvement": {
        "weight": 0.10,
        "description": "Improvement over production baseline or heuristic",
    },
}

REQUIRED_FIELDS = ["model_name", "task_type", "metrics", "requirements"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    return errors


def score_evaluation(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    metrics = data["metrics"]
    requirements = data["requirements"]
    dimension_scores = {}
    total_score = 0.0

    # Accuracy dimension
    accuracy_metric = metrics.get("primary_accuracy")
    accuracy_threshold = requirements.get("min_accuracy")
    if accuracy_metric is not None and accuracy_threshold is not None:
        ratio = accuracy_metric / accuracy_threshold
        raw = min(10.0, ratio * 10)
        weighted = raw * EVALUATION_DIMENSIONS["accuracy"]["weight"]
        dimension_scores["accuracy"] = {
            "achieved": accuracy_metric, "required": accuracy_threshold,
            "passes": accuracy_metric >= accuracy_threshold,
            "raw_score": round(raw, 2), "weighted_score": round(weighted, 2),
        }
        total_score += weighted

    # Fairness dimension
    fairness_disparity = metrics.get("max_fairness_disparity")
    fairness_threshold = requirements.get("max_fairness_disparity", 0.05)
    if fairness_disparity is not None:
        raw = max(0.0, 10.0 - (fairness_disparity / fairness_threshold) * 5)
        weighted = raw * EVALUATION_DIMENSIONS["fairness"]["weight"]
        dimension_scores["fairness"] = {
            "max_disparity": fairness_disparity, "threshold": fairness_threshold,
            "passes": fairness_disparity <= fairness_threshold,
            "raw_score": round(raw, 2), "weighted_score": round(weighted, 2),
        }
        total_score += weighted

    # Robustness dimension
    robustness_score = metrics.get("robustness_score")
    if robustness_score is not None:
        raw = robustness_score * 10
        weighted = raw * EVALUATION_DIMENSIONS["robustness"]["weight"]
        dimension_scores["robustness"] = {
            "score": robustness_score,
            "passes": robustness_score >= requirements.get("min_robustness", 0.7),
            "raw_score": round(raw, 2), "weighted_score": round(weighted, 2),
        }
        total_score += weighted

    # Latency dimension
    p99_latency = metrics.get("p99_latency_ms")
    max_latency = requirements.get("max_p99_latency_ms")
    if p99_latency is not None and max_latency is not None:
        raw = max(0.0, 10.0 * (1 - max(0, p99_latency - max_latency * 0.5) / max_latency))
        weighted = raw * EVALUATION_DIMENSIONS["latency"]["weight"]
        dimension_scores["latency"] = {
            "achieved_ms": p99_latency, "required_ms": max_latency,
            "passes": p99_latency <= max_latency,
            "raw_score": round(raw, 2), "weighted_score": round(weighted, 2),
        }
        total_score += weighted

    # Baseline improvement
    candidate_acc = metrics.get("primary_accuracy")
    baseline_acc = metrics.get("baseline_accuracy")
    if candidate_acc is not None and baseline_acc is not None:
        improvement = (candidate_acc - baseline_acc) / max(baseline_acc, 0.001)
        raw = min(10.0, max(0.0, 5 + improvement * 50))
        weighted = raw * EVALUATION_DIMENSIONS["baseline_improvement"]["weight"]
        dimension_scores["baseline_improvement"] = {
            "candidate": candidate_acc, "baseline": baseline_acc,
            "improvement_pct": round(improvement * 100, 2),
            "passes": candidate_acc > baseline_acc,
            "raw_score": round(raw, 2), "weighted_score": round(weighted, 2),
        }
        total_score += weighted

    # Determine verdict
    hard_fails = [dim for dim, scores in dimension_scores.items() if not scores.get("passes", True)]
    if not hard_fails and total_score >= 7.0:
        verdict = "PROMOTE — all requirements met"
    elif hard_fails:
        verdict = f"REJECT — failed dimensions: {hard_fails}"
    else:
        verdict = "CONDITIONAL — review marginal dimensions before promotion"

    return {
        "error": None,
        "result": {
            "model_name": data["model_name"],
            "task_type": data["task_type"],
            "overall_score": round(total_score, 2),
            "verdict": verdict,
            "dimension_scores": dimension_scores,
            "hard_fails": hard_fails,
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_evaluation(data)
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
