#!/usr/bin/env python3
"""
score.py — Score company/product name candidates across memorability, meaning, and availability criteria.

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

NAME_CRITERIA = {
    "memorability": {
        "weight": 0.25,
        "description": "Easy to remember, spell, and say aloud",
        "levels": {"excellent": 10, "good": 7, "adequate": 4, "poor": 1},
    },
    "meaning_fit": {
        "weight": 0.20,
        "description": "Name meaning or associations align with product positioning",
        "levels": {"strong_fit": 10, "moderate_fit": 6, "neutral": 3, "poor_fit": 1},
    },
    "domain_availability": {
        "weight": 0.20,
        "description": ".com domain availability",
        "levels": {"available": 10, "variant_available": 6, "expensive": 3, "unavailable": 0},
    },
    "trademark_risk": {
        "weight": 0.15,
        "description": "Risk of trademark conflict in relevant categories",
        "levels": {"clear": 10, "low_risk": 7, "medium_risk": 4, "conflict": 0},
    },
    "global_suitability": {
        "weight": 0.10,
        "description": "No negative meanings in major languages (EN/ES/FR/ZH/AR)",
        "levels": {"clean": 10, "minor_issue": 6, "major_issue": 0},
    },
    "distinctiveness": {
        "weight": 0.10,
        "description": "How unique the name is in the target market",
        "levels": {"unique": 10, "distinctive": 7, "common": 3, "generic": 1},
    },
}

REQUIRED_FIELDS = ["naming_context", "candidates"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "candidates" in data:
        for c in data["candidates"]:
            if "name" not in c or "scores" not in c:
                errors.append(f"Candidate '{c.get('name', '?')}' needs 'name' and 'scores' fields")
    return errors


def score_names(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    scored_candidates = []
    for candidate in data["candidates"]:
        name = candidate["name"]
        scores = candidate["scores"]
        total = 0.0
        criterion_breakdown = {}

        for criterion, config in NAME_CRITERIA.items():
            level = scores.get(criterion, "adequate")
            raw = config["levels"].get(level, 4)
            weighted = raw * config["weight"]
            total += weighted
            criterion_breakdown[criterion] = {
                "level": level, "raw_score": raw, "weighted_score": round(weighted, 2),
            }

        scored_candidates.append({
            "name": name,
            "total_score": round(total, 2),
            "criterion_breakdown": criterion_breakdown,
            "notes": candidate.get("notes", ""),
            "blockers": [c for c, v in criterion_breakdown.items() if v["raw_score"] == 0],
        })

    # Sort by score, but any with blockers go last
    scored_candidates.sort(key=lambda x: (-len(x["blockers"]) == 0, -x["total_score"]))

    top = scored_candidates[0] if scored_candidates else None
    recommendation = f"Recommended: {top['name']} (score: {top['total_score']}/10)" if top and not top["blockers"] else "No clear winner — all top candidates have blockers"

    return {
        "error": None,
        "result": {
            "naming_context": data["naming_context"],
            "candidates_evaluated": len(scored_candidates),
            "recommendation": recommendation,
            "ranked_candidates": scored_candidates,
            "next_steps": [
                "Verify .com domain availability for top 3 candidates",
                "Request trademark search for top 2 candidates from legal counsel",
                "Test top 3 names with 10 target customers for association and recall",
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_names(data)
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
