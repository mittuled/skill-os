#!/usr/bin/env python3
"""
score.py — Score design deliverables against phase gate exit criteria.

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

# Phase gate exit criteria by phase transition
PHASE_CRITERIA = {
    "discovery_to_definition": [
        {"key": "problem_statement", "label": "Problem statement defined", "blocking": True},
        {"key": "user_research", "label": "User research synthesized", "blocking": True},
        {"key": "success_metrics", "label": "Success metrics defined", "blocking": True},
        {"key": "scope_documented", "label": "In-scope surfaces documented", "blocking": False},
    ],
    "definition_to_production": [
        {"key": "user_flows", "label": "User flows complete for all in-scope surfaces", "blocking": True},
        {"key": "wireframes", "label": "Wireframes reviewed and approved", "blocking": True},
        {"key": "content_requirements", "label": "Content requirements documented", "blocking": True},
        {"key": "accessibility_targets", "label": "Accessibility targets specified", "blocking": True},
        {"key": "design_system_components", "label": "Design system components identified", "blocking": False},
    ],
    "production_to_handoff": [
        {"key": "visual_design_complete", "label": "Visual design complete for all states", "blocking": True},
        {"key": "interaction_states", "label": "All interaction states documented", "blocking": True},
        {"key": "accessibility_check", "label": "Accessibility check passed", "blocking": True},
        {"key": "design_system_compliance", "label": "Design system compliance verified", "blocking": True},
        {"key": "handoff_spec", "label": "Handoff spec annotated in Figma", "blocking": True},
        {"key": "prototype_linked", "label": "Prototype linked for engineering reference", "blocking": False},
    ],
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "project_name" not in data:
        errors.append("Missing required field: project_name")
    if "phase_transition" not in data:
        errors.append("Missing required field: phase_transition")
    if "criteria" not in data or not isinstance(data["criteria"], dict):
        errors.append("Missing required field: criteria (dict)")
    return errors


def score_phase_gate(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    project = data["project_name"]
    transition = data["phase_transition"]
    provided = data["criteria"]
    notes = data.get("notes", {})

    if transition not in PHASE_CRITERIA:
        return {
            "error": [f"Unknown phase_transition '{transition}'. Choose from: {list(PHASE_CRITERIA.keys())}"],
            "result": None,
        }

    criteria_list = PHASE_CRITERIA[transition]
    results = []
    blocking_failures = []
    advisory_findings = []

    for c in criteria_list:
        key = c["key"]
        status = provided.get(key, "incomplete")
        passed = status in ("pass", "complete", "yes", True)

        results.append({
            "criterion": c["label"],
            "blocking": c["blocking"],
            "status": "PASS" if passed else "FAIL",
            "note": notes.get(key, ""),
        })

        if not passed:
            if c["blocking"]:
                blocking_failures.append(c["label"])
            else:
                advisory_findings.append(c["label"])

    if blocking_failures:
        verdict = "BLOCKED"
    elif advisory_findings:
        verdict = "CONDITIONAL_APPROVE"
    else:
        verdict = "APPROVED"

    return {
        "error": None,
        "result": {
            "project": project,
            "phase_transition": transition,
            "verdict": verdict,
            "blocking_failures": blocking_failures,
            "advisory_findings": advisory_findings,
            "criteria_results": results,
            "summary": (
                f"{len(blocking_failures)} blocking issue(s), "
                f"{len(advisory_findings)} advisory finding(s). "
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
    result = score_phase_gate(data)
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
