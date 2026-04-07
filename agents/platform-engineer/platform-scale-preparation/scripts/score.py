#!/usr/bin/env python3
"""
score.py — Score platform scalability readiness and identify bottlenecks.

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

# Scalability dimensions with weights
RUBRIC = {
    "stateless_services": {
        "label": "Stateless Services",
        "weight": 20,
        "description": "Services can scale horizontally without shared mutable state",
    },
    "database_scalability": {
        "label": "Database Scalability",
        "weight": 25,
        "description": "Database can handle projected load: read replicas, connection pooling, sharding plan",
    },
    "caching_strategy": {
        "label": "Caching Strategy",
        "weight": 15,
        "description": "Caching layer reduces database and compute load at scale",
    },
    "async_processing": {
        "label": "Async Processing",
        "weight": 15,
        "description": "Heavy workloads are offloaded to async queues or workers",
    },
    "auto_scaling": {
        "label": "Auto-Scaling",
        "weight": 15,
        "description": "Infrastructure scales automatically with load without manual intervention",
    },
    "load_testing": {
        "label": "Load Testing",
        "weight": 10,
        "description": "Load tests have been run at projected peak traffic levels",
    },
}

GRADE_BANDS = [(90, "A", "SCALE_READY"), (75, "B", "MOSTLY_READY"), (60, "C", "NEEDS_WORK"), (45, "D", "AT_RISK"), (0, "F", "NOT_READY")]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "system_name" not in data:
        errors.append("Missing required field: system_name")
    if "dimensions" not in data or not isinstance(data["dimensions"], list):
        errors.append("Missing required field: dimensions (list of scalability dimension assessments)")
    return errors


def score_scalability(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    system = data["system_name"]
    dimensions_input = data["dimensions"]
    target_load_multiplier = data.get("target_load_multiplier", 5)
    current_rps = data.get("current_rps", 0)

    # Index input dimensions
    dim_by_key = {d.get("dimension", ""): d for d in dimensions_input}

    dimension_results = []
    total_score = 0
    bottlenecks = []
    spofs = []

    for dim_key, dim_config in RUBRIC.items():
        dim_input = dim_by_key.get(dim_key, {})
        score_0_10 = min(max(dim_input.get("score", 0), 0), 10)
        is_spof = dim_input.get("is_single_point_of_failure", False)
        notes = dim_input.get("notes", "")
        mitigations = dim_input.get("mitigations", [])

        weighted = round(score_0_10 * dim_config["weight"] / 10)
        total_score += weighted

        severity = "CRITICAL" if score_0_10 < 3 else ("HIGH" if score_0_10 < 5 else ("MEDIUM" if score_0_10 < 7 else "LOW"))

        entry = {
            "dimension": dim_key,
            "label": dim_config["label"],
            "description": dim_config["description"],
            "score_0_10": score_0_10,
            "weight": dim_config["weight"],
            "weighted_score": weighted,
            "severity": severity,
            "is_single_point_of_failure": is_spof,
            "notes": notes,
            "mitigations": mitigations,
        }
        dimension_results.append(entry)

        if severity in ("CRITICAL", "HIGH"):
            bottlenecks.append(entry)
        if is_spof:
            spofs.append(entry)

    grade_letter, grade_label = "F", "NOT_READY"
    for threshold, letter, label in GRADE_BANDS:
        if total_score >= threshold:
            grade_letter, grade_label = letter, label
            break

    projected_rps = current_rps * target_load_multiplier if current_rps else None

    return {
        "error": None,
        "result": {
            "system": system,
            "total_score": total_score,
            "grade": grade_letter,
            "verdict": grade_label,
            "current_rps": current_rps,
            "target_load_multiplier": target_load_multiplier,
            "projected_rps": projected_rps,
            "dimension_results": dimension_results,
            "bottlenecks": bottlenecks,
            "single_points_of_failure": spofs,
            "summary": (
                f"Scale readiness for {system}: {total_score}/100 — {grade_label}. "
                f"{len(bottlenecks)} bottleneck(s), {len(spofs)} single point(s) of failure."
                + (f" Target: {target_load_multiplier}x current load ({projected_rps:,} RPS)." if projected_rps else "")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_scalability(data)
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
