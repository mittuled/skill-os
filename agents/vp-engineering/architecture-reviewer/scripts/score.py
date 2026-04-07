#!/usr/bin/env python3
"""
score.py — Score an architecture proposal for soundness, scalability, standards alignment, and operational risk.

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

# Scoring criteria and weights (must sum to 100)
SCORING_CRITERIA = {
    "structural_soundness": {
        "weight": 30,
        "description": "Component boundaries, data flow clarity, failure domains, SPOF avoidance",
    },
    "scalability": {
        "weight": 25,
        "description": "Horizontal/vertical scaling assumptions, 3x headroom vs SLO, capacity planning",
    },
    "standards_alignment": {
        "weight": 25,
        "description": "Tech radar adherence, observability (logging/metrics/tracing), security posture",
    },
    "operational_risk": {
        "weight": 20,
        "description": "Deployment complexity, rollback strategy, migration safety, on-call burden",
    },
}

VERDICT_THRESHOLDS = [
    (80, "APPROVED", "Architecture is sound; proceed with implementation"),
    (60, "CHANGES_REQUESTED", "Architecture requires targeted improvements before approval"),
    (0, "REJECTED", "Architecture has critical flaws; a redesign is required"),
]

# Required review elements — their absence flags structural gaps
REQUIRED_ELEMENTS = [
    "threat_model",
    "observability_plan",
    "rollback_strategy",
    "capacity_projections",
    "failure_mode_analysis",
]


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    if "scores" not in data:
        errors.append("Missing required field: scores")
        return errors
    for criterion in SCORING_CRITERIA:
        if criterion not in data["scores"]:
            errors.append(f"Missing score for criterion: {criterion}")
        elif not (0 <= data["scores"][criterion] <= 100):
            errors.append(f"Score for {criterion} must be 0–100")
    if "proposal_name" not in data:
        errors.append("Missing required field: proposal_name")
    return errors


def score_architecture(data: dict) -> dict:
    """Compute composite architecture review score and verdict."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    raw_scores = data["scores"]
    total = sum(
        raw_scores[c] * SCORING_CRITERIA[c]["weight"] / 100
        for c in SCORING_CRITERIA
    )

    # Check for missing required elements
    present_elements = set(data.get("present_elements", []))
    missing_elements = [e for e in REQUIRED_ELEMENTS if e not in present_elements]

    # Missing critical elements cap the score at 70
    if missing_elements:
        score_cap = 70.0
        total = min(total, score_cap)

    # Determine verdict
    verdict, verdict_rationale = "REJECTED", "Architecture has critical flaws"
    for threshold, v, r in VERDICT_THRESHOLDS:
        if total >= threshold:
            verdict, verdict_rationale = v, r
            break

    criterion_results = {
        c: {
            "score": raw_scores[c],
            "weight": SCORING_CRITERIA[c]["weight"],
            "weighted_contribution": round(raw_scores[c] * SCORING_CRITERIA[c]["weight"] / 100, 1),
            "description": SCORING_CRITERIA[c]["description"],
            "notes": data.get("criterion_notes", {}).get(c, ""),
        }
        for c in SCORING_CRITERIA
    }

    action_items = data.get("action_items", [])
    if missing_elements:
        for el in missing_elements:
            action_items.append(f"Add missing required element: {el.replace('_', ' ')}")

    result = {
        "proposal": data["proposal_name"],
        "total_score": round(total, 1),
        "verdict": verdict,
        "verdict_rationale": verdict_rationale,
        "capped_by_missing_elements": bool(missing_elements),
        "missing_required_elements": missing_elements,
        "criterion_scores": criterion_results,
        "action_items": action_items,
        "reviewer_notes": data.get("reviewer_notes", ""),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_architecture(data)
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
