#!/usr/bin/env python3
"""
score.py — Score a design artifact against WCAG 2.1 AA accessibility criteria.

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

# WCAG 2.1 AA criteria evaluated with weights (total = 100)
CRITERIA = {
    "contrast_normal_text": {
        "label": "Contrast ratio ≥ 4.5:1 for normal text",
        "weight": 20,
        "wcag": "1.4.3 AA",
    },
    "contrast_large_text": {
        "label": "Contrast ratio ≥ 3:1 for large text",
        "weight": 10,
        "wcag": "1.4.3 AA",
    },
    "touch_target_size": {
        "label": "Touch targets ≥ 44×44pt",
        "weight": 10,
        "wcag": "2.5.5 AAA / mobile best practice",
    },
    "color_not_sole_indicator": {
        "label": "Color is not the sole indicator of state",
        "weight": 10,
        "wcag": "1.4.1 AA",
    },
    "focus_states_documented": {
        "label": "Focus states documented for all interactive elements",
        "weight": 15,
        "wcag": "2.4.7 AA",
    },
    "focus_order_logical": {
        "label": "Focus order follows logical reading order",
        "weight": 10,
        "wcag": "2.4.3 AA",
    },
    "alt_text_specified": {
        "label": "Alt text specified for all meaningful images",
        "weight": 10,
        "wcag": "1.1.1 AA",
    },
    "aria_labels_documented": {
        "label": "ARIA labels documented for icons and controls",
        "weight": 10,
        "wcag": "4.1.2 AA",
    },
    "error_messages_descriptive": {
        "label": "Error messages descriptive and adjacent to field",
        "weight": 5,
        "wcag": "3.3.1 AA",
    },
}

PASS_THRESHOLD = 80  # minimum score for a pass verdict
CONDITIONAL_THRESHOLD = 60  # minimum for conditional-pass


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors = []
    if "artifact_name" not in data:
        errors.append("Missing required field: artifact_name")
    if "criteria" not in data or not isinstance(data["criteria"], dict):
        errors.append("Missing required field: criteria (dict of criterion_key -> 'pass'|'fail'|'na')")
    return errors


def score_accessibility(data: dict) -> dict:
    """Score the design artifact against WCAG 2.1 AA accessibility criteria."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    artifact = data["artifact_name"]
    provided = data["criteria"]
    notes = data.get("notes", {})

    results = []
    total_weight = 0
    earned_weight = 0
    findings = []

    for key, meta in CRITERIA.items():
        status = provided.get(key, "na")
        weight = meta["weight"]
        total_weight += weight

        if status == "pass":
            earned_weight += weight
            result_status = "PASS"
        elif status == "fail":
            result_status = "FAIL"
            findings.append({
                "criterion": meta["label"],
                "wcag": meta["wcag"],
                "status": "FAIL",
                "note": notes.get(key, ""),
            })
        else:  # na or unknown
            result_status = "N/A"

        results.append({
            "criterion_key": key,
            "criterion": meta["label"],
            "wcag": meta["wcag"],
            "weight": weight,
            "status": result_status,
        })

    score = round((earned_weight / total_weight) * 100) if total_weight > 0 else 0

    if score >= PASS_THRESHOLD and not findings:
        verdict = "PASS"
    elif score >= CONDITIONAL_THRESHOLD:
        verdict = "CONDITIONAL_PASS"
    else:
        verdict = "FAIL"

    return {
        "error": None,
        "result": {
            "artifact": artifact,
            "score": score,
            "verdict": verdict,
            "pass_threshold": PASS_THRESHOLD,
            "criteria_results": results,
            "findings": findings,
            "summary": f"{len(findings)} issue(s) found. Verdict: {verdict}.",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_accessibility(data)
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
