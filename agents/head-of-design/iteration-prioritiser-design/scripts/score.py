#!/usr/bin/env python3
"""
score.py — Score and prioritize design iteration backlog items.

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

# Scoring rubric dimensions with weights (total = 100)
RUBRIC = {
    "user_impact": {
        "label": "User Impact",
        "description": "Severity and breadth of affected users (1=minor/few, 5=critical/all)",
        "weight": 35,
    },
    "business_value": {
        "label": "Business Value",
        "description": "Effect on conversion, retention, or revenue (1=negligible, 5=significant)",
        "weight": 30,
    },
    "design_effort": {
        "label": "Design Effort (inverted)",
        "description": "Effort to implement (1=XL, 5=XS — lower effort scores higher)",
        "weight": 20,
    },
    "accessibility_severity": {
        "label": "Accessibility Severity",
        "description": "WCAG impact level (0=none, 5=WCAG AA blocker)",
        "weight": 15,
    },
}

PRIORITY_TIERS = [
    {"name": "must-do", "min_score": 70, "description": "Critical usability or accessibility issues"},
    {"name": "should-do", "min_score": 45, "description": "High-impact improvements"},
    {"name": "could-do", "min_score": 0, "description": "Nice-to-have refinements"},
]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "backlog_items" not in data or not isinstance(data["backlog_items"], list):
        errors.append("Missing required field: backlog_items (list)")
    return errors


def score_item(item: dict) -> dict:
    """Score a single backlog item."""
    scores = item.get("scores", {})
    weighted_total = 0.0
    dimension_results = []

    for dim_key, meta in RUBRIC.items():
        raw = scores.get(dim_key, 3)  # default to mid
        raw = max(1, min(5, int(raw)))
        weighted = (raw / 5) * meta["weight"]
        weighted_total += weighted
        dimension_results.append({
            "dimension": meta["label"],
            "raw_score": raw,
            "weight": meta["weight"],
            "weighted_contribution": round(weighted, 1),
        })

    final_score = round(weighted_total)

    tier = "could-do"
    for t in PRIORITY_TIERS:
        if final_score >= t["min_score"]:
            tier = t["name"]
            break

    return {
        "id": item.get("id", ""),
        "title": item.get("title", "Untitled"),
        "source": item.get("source", ""),
        "affected_surface": item.get("affected_surface", ""),
        "score": final_score,
        "tier": tier,
        "dimension_breakdown": dimension_results,
        "notes": item.get("notes", ""),
    }


def prioritize_backlog(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    items = data["backlog_items"]
    scored = [score_item(item) for item in items]
    scored.sort(key=lambda x: x["score"], reverse=True)

    tiers: dict[str, list] = {"must-do": [], "should-do": [], "could-do": []}
    for s in scored:
        tiers[s["tier"]].append(s)

    return {
        "error": None,
        "result": {
            "total_items": len(scored),
            "prioritized_backlog": scored,
            "tiers": tiers,
            "tier_summary": {
                tier: len(items) for tier, items in tiers.items()
            },
            "summary": (
                f"{len(scored)} items scored. "
                f"Must-do: {len(tiers['must-do'])}, "
                f"Should-do: {len(tiers['should-do'])}, "
                f"Could-do: {len(tiers['could-do'])}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = prioritize_backlog(data)
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
