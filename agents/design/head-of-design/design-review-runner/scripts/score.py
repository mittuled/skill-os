#!/usr/bin/env python3
"""
score.py — Score a design deliverable through a structured design review.

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

# Review criteria with weights and review types they apply to
REVIEW_CRITERIA = {
    "design_system_compliance": {
        "label": "Design System Compliance",
        "description": "Components, tokens, and patterns follow the design system",
        "weight": 20,
        "applies_to": ["wireframe", "visual", "pre_handoff"],
    },
    "accessibility_compliance": {
        "label": "Accessibility Compliance",
        "description": "Meets WCAG 2.1 AA — contrast, focus, alt text, ARIA",
        "weight": 20,
        "applies_to": ["visual", "pre_handoff"],
    },
    "interaction_completeness": {
        "label": "Interaction Completeness",
        "description": "All states documented: empty, loading, error, success, edge cases",
        "weight": 20,
        "applies_to": ["wireframe", "visual", "pre_handoff"],
    },
    "content_quality": {
        "label": "Content Quality",
        "description": "Microcopy, labels, and error messages are final — no placeholder text",
        "weight": 15,
        "applies_to": ["visual", "pre_handoff"],
    },
    "product_alignment": {
        "label": "Product Alignment",
        "description": "Design matches product spec and acceptance criteria",
        "weight": 15,
        "applies_to": ["wireframe", "visual", "pre_handoff"],
    },
    "handoff_readiness": {
        "label": "Handoff Readiness",
        "description": "Figma annotations complete, specs exported, prototype linked",
        "weight": 10,
        "applies_to": ["pre_handoff"],
    },
}

SEVERITY_LABELS = {"blocking": "🔴 BLOCKING", "advisory": "🟡 ADVISORY", "pass": "✅ PASS"}

VERDICT_PASS_THRESHOLD = 80
VERDICT_CONDITIONAL_THRESHOLD = 60


def validate_input(data: dict) -> list[str]:
    errors = []
    if "deliverable_name" not in data:
        errors.append("Missing required field: deliverable_name")
    if "review_type" not in data:
        errors.append("Missing required field: review_type (wireframe|visual|pre_handoff)")
    if "criteria" not in data or not isinstance(data["criteria"], dict):
        errors.append("Missing required field: criteria (dict of criterion_key -> pass|blocking|advisory)")
    return errors


def score_review(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    deliverable = data["deliverable_name"]
    review_type = data["review_type"]
    provided = data["criteria"]
    notes = data.get("notes", {})
    feedback_items = data.get("feedback_items", [])

    applicable = {k: v for k, v in REVIEW_CRITERIA.items() if review_type in v["applies_to"]}
    total_weight = sum(v["weight"] for v in applicable.values())
    earned_weight = 0
    criteria_results = []
    blocking_issues = []
    advisory_items = []

    for key, meta in applicable.items():
        status = provided.get(key, "advisory")
        weight = meta["weight"]

        if status == "pass":
            earned_weight += weight
            severity = "pass"
        elif status == "blocking":
            severity = "blocking"
            blocking_issues.append({
                "criterion": meta["label"],
                "note": notes.get(key, ""),
            })
        else:
            severity = "advisory"
            advisory_items.append({
                "criterion": meta["label"],
                "note": notes.get(key, ""),
            })

        criteria_results.append({
            "criterion": meta["label"],
            "description": meta["description"],
            "weight": weight,
            "status": severity,
            "severity_label": SEVERITY_LABELS[severity],
            "note": notes.get(key, ""),
        })

    score = round((earned_weight / total_weight) * 100) if total_weight > 0 else 0

    if blocking_issues:
        verdict = "REQUIRES_RE_REVIEW"
    elif score >= VERDICT_PASS_THRESHOLD:
        verdict = "APPROVED"
    elif score >= VERDICT_CONDITIONAL_THRESHOLD:
        verdict = "CONDITIONALLY_APPROVED"
    else:
        verdict = "REQUIRES_RE_REVIEW"

    return {
        "error": None,
        "result": {
            "deliverable": deliverable,
            "review_type": review_type,
            "score": score,
            "verdict": verdict,
            "criteria_results": criteria_results,
            "blocking_issues": blocking_issues,
            "advisory_items": advisory_items,
            "feedback_items": feedback_items,
            "summary": (
                f"Score: {score}/100. "
                f"Blocking: {len(blocking_issues)}. "
                f"Advisory: {len(advisory_items)}. "
                f"Verdict: {verdict}."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_review(data)
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
