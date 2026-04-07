#!/usr/bin/env python3
"""Score sales signal themes by revenue impact."""
import json
import sys

CRITERIA = {
    "frequency": {
        "weight": 0.25,
        "description": "How often this theme appears across deals in the analysis period",
    },
    "pipeline_value_impact": {
        "weight": 0.30,
        "description": "Total pipeline value of deals where this theme appeared",
    },
    "win_rate_delta": {
        "weight": 0.25,
        "description": "Win rate difference for deals with vs. without this theme",
    },
    "cycle_time_impact": {
        "weight": 0.20,
        "description": "Average deal cycle extension caused by this theme (inverse score)",
    },
}

GRADE_BANDS = [
    {"grade": "A+", "min": 9.0, "max": 10.0, "label": "Critical", "action": "Immediate cross-functional escalation; Product, Marketing, and Sales leadership alignment required this quarter"},
    {"grade": "A", "min": 8.0, "max": 8.9, "label": "High Impact", "action": "Schedule dedicated product review session; draft positioning update for Marketing within 2 weeks"},
    {"grade": "B", "min": 7.0, "max": 7.9, "label": "Significant", "action": "Include in quarterly roadmap review; update objection handler and battle cards"},
    {"grade": "C", "min": 5.0, "max": 6.9, "label": "Moderate", "action": "Monitor for escalation; document workarounds; include in next quarterly synthesis"},
    {"grade": "D", "min": 3.0, "max": 4.9, "label": "Low Impact", "action": "Log for trend tracking; no immediate action required"},
    {"grade": "F", "min": 0.0, "max": 2.9, "label": "Negligible", "action": "Archive; revisit only if frequency increases next quarter"},
]


def score(evidence: dict) -> dict:
    """Score a signal theme by revenue impact."""
    scores = {}
    for name, cfg in CRITERIA.items():
        raw = float(evidence.get(name, 0))
        raw = max(0.0, min(10.0, raw))
        scores[name] = {"raw": raw, "weighted": round(raw * cfg["weight"], 2)}
    composite = round(sum(s["weighted"] for s in scores.values()), 2)
    grade = next(
        (g for g in GRADE_BANDS if g["min"] <= composite <= g["max"]),
        GRADE_BANDS[-1],
    )
    return {
        "theme": evidence.get("theme", "[Unknown Theme]"),
        "composite": composite,
        "grade": grade["grade"],
        "label": grade["label"],
        "action": grade["action"],
        "criteria_scores": scores,
    }


if __name__ == "__main__":
    data = json.load(sys.stdin) if not sys.stdin.isatty() else json.loads(sys.argv[1])
    # Support scoring a single theme or a list of themes
    if isinstance(data, list):
        results = [score(item) for item in data]
        results.sort(key=lambda x: x["composite"], reverse=True)
        print(json.dumps(results, indent=2))
    else:
        print(json.dumps(score(data), indent=2))
