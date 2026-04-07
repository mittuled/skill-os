#!/usr/bin/env python3
"""
score.py — Score developer experience (DX) across key friction areas.

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

# DX scoring rubric
RUBRIC = {
    "onboarding_speed": {
        "label": "Onboarding Speed",
        "weight": 20,
        "description": "Time for a new engineer to commit and deploy to staging",
        "benchmark": "Target: <1 day",
    },
    "local_dev_parity": {
        "label": "Local Dev / Production Parity",
        "weight": 15,
        "description": "Local environment accurately mirrors production",
        "benchmark": "Target: >90% parity",
    },
    "build_test_speed": {
        "label": "Build and Test Speed",
        "weight": 20,
        "description": "Time from code push to CI feedback (test results, lint)",
        "benchmark": "Target: <10 minutes",
    },
    "deployment_self_service": {
        "label": "Deployment Self-Service",
        "weight": 20,
        "description": "Engineers can deploy without platform team intervention",
        "benchmark": "Target: deploy to staging is fully self-service",
    },
    "docs_discoverability": {
        "label": "Documentation Discoverability",
        "weight": 10,
        "description": "Engineers can find answers to common questions without asking teammates",
        "benchmark": "Target: runbooks, ADRs, and API docs findable in <5 minutes",
    },
    "tooling_satisfaction": {
        "label": "Tooling Satisfaction",
        "weight": 15,
        "description": "Engineers report satisfaction with their tools (from survey or retrospective)",
        "benchmark": "Target: >7/10 average satisfaction score",
    },
}

GRADE_BANDS = [(90, "A", "EXCELLENT_DX"), (75, "B", "GOOD_DX"), (60, "C", "ACCEPTABLE_DX"), (45, "D", "POOR_DX"), (0, "F", "CRITICAL_DX")]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "team_name" not in data:
        errors.append("Missing required field: team_name")
    if "scores" not in data or not isinstance(data["scores"], dict):
        errors.append("Missing required field: scores (dict of dimension_key: 0-10 score)")
    return errors


def score_dx(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    team = data["team_name"]
    scores = data["scores"]
    pain_points = data.get("pain_points", [])
    team_size = data.get("team_size", 0)
    notes = data.get("notes", {})

    dimension_results = []
    total_score = 0
    high_friction = []

    for dim_key, dim_config in RUBRIC.items():
        raw_score = min(max(scores.get(dim_key, 5), 0), 10)
        weighted = round(raw_score * dim_config["weight"] / 10)
        total_score += weighted
        severity = "CRITICAL" if raw_score < 3 else ("HIGH" if raw_score < 5 else ("MEDIUM" if raw_score < 7 else "LOW"))

        entry = {
            "dimension": dim_key,
            "label": dim_config["label"],
            "description": dim_config["description"],
            "benchmark": dim_config["benchmark"],
            "score_0_10": raw_score,
            "weight": dim_config["weight"],
            "weighted_score": weighted,
            "severity": severity,
            "notes": notes.get(dim_key, ""),
        }
        dimension_results.append(entry)
        if severity in ("CRITICAL", "HIGH"):
            high_friction.append(entry)

    grade_letter, grade_label = "F", "CRITICAL_DX"
    for threshold, letter, label in GRADE_BANDS:
        if total_score >= threshold:
            grade_letter, grade_label = letter, label
            break

    # Estimate productivity impact
    productivity_friction_pct = round((100 - total_score) * 0.3)  # rough estimate

    return {
        "error": None,
        "result": {
            "team": team,
            "team_size": team_size,
            "total_score": total_score,
            "grade": grade_letter,
            "verdict": grade_label,
            "dimension_results": dimension_results,
            "high_friction_areas": high_friction,
            "pain_points": pain_points,
            "estimated_productivity_friction_pct": productivity_friction_pct,
            "summary": (
                f"DX score for {team}: {total_score}/100 — {grade_label}. "
                f"{len(high_friction)} high-friction area(s). "
                f"Estimated {productivity_friction_pct}% productivity drag."
                + (f" Team size: {team_size}." if team_size else "")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_dx(data)
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
