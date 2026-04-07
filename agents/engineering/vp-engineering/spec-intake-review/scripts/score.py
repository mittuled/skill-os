#!/usr/bin/env python3
"""
score.py — Score incoming feature specifications for engineering readiness.

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

REVIEW_CRITERIA = {
    "user_stories_or_jtbd": {"weight": 20, "description": "Clear user stories or jobs-to-be-done present"},
    "acceptance_criteria": {"weight": 25, "description": "Acceptance criteria defined for each requirement"},
    "success_metrics": {"weight": 15, "description": "Measurable success metrics specified"},
    "non_functional_requirements": {"weight": 20, "description": "Performance, security, accessibility NFRs present"},
    "scope_clarity": {"weight": 10, "description": "In-scope and out-of-scope explicitly defined"},
    "edge_cases": {"weight": 10, "description": "Edge cases and error states documented"},
}

VERDICT_THRESHOLDS = [
    (80, "ACCEPTED", "Spec is ready for engineering planning"),
    (60, "RETURNED_FOR_REVISION", "Spec requires targeted improvements before engineering planning"),
    (0, "ESCALATED", "Spec has fundamental gaps requiring cross-functional alignment"),
]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    if "spec_name" not in data:
        errors.append("Missing required field: spec_name")
    if "scores" not in data:
        errors.append("Missing required field: scores")
        return errors
    for criterion in REVIEW_CRITERIA:
        if criterion not in data["scores"]:
            errors.append(f"Missing score: {criterion}")
        elif not (0 <= data["scores"][criterion] <= 100):
            errors.append(f"Score for {criterion} must be 0–100")
    return errors


def score_spec(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    raw = data["scores"]
    total = sum(raw[c] * REVIEW_CRITERIA[c]["weight"] / 100 for c in REVIEW_CRITERIA)

    verdict, rationale = "ESCALATED", "Spec has fundamental gaps"
    for threshold, v, r in VERDICT_THRESHOLDS:
        if total >= threshold:
            verdict, rationale = v, r
            break

    criteria_results = {
        c: {
            "score": raw[c],
            "weight": REVIEW_CRITERIA[c]["weight"],
            "contribution": round(raw[c] * REVIEW_CRITERIA[c]["weight"] / 100, 1),
            "notes": data.get("notes", {}).get(c, ""),
        }
        for c in REVIEW_CRITERIA
    }

    failed_criteria = [c for c in REVIEW_CRITERIA if raw[c] < 50]

    result = {
        "spec": data["spec_name"],
        "total_score": round(total, 1),
        "verdict": verdict,
        "rationale": rationale,
        "criteria_scores": criteria_results,
        "failed_criteria": failed_criteria,
        "open_questions": data.get("open_questions", []),
        "action_items": data.get("action_items", [f"Address: {c}" for c in failed_criteria]),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_spec(data)
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
