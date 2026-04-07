#!/usr/bin/env python3
"""
generate.py — Generate a design brief from a product specification.

Usage:
    echo '<json>' | python3 generate.py
    python3 generate.py < input.json
    python3 generate.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# Standard acceptance criteria categories for design briefs
ACCEPTANCE_CRITERIA_CATEGORIES = [
    "States covered (empty, loading, error, success, edge cases)",
    "Responsive breakpoints addressed",
    "Accessibility checks passed (WCAG 2.1 AA)",
    "Design system compliance verified",
    "Content requirements met (all copy finalized)",
    "Interaction states documented (hover, focus, active, disabled)",
]


def validate_input(data: dict) -> list[str]:
    errors = []
    required = ["feature_name", "problem_statement", "target_users", "in_scope_surfaces"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    return errors


def generate_design_brief(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    feature = data["feature_name"]
    problem = data["problem_statement"]
    users = data["target_users"]
    surfaces = data["in_scope_surfaces"]
    constraints = data.get("design_constraints", [])
    interaction_requirements = data.get("interaction_requirements", [])
    accessibility_targets = data.get("accessibility_targets", "WCAG 2.1 AA minimum")
    content_requirements = data.get("content_requirements", [])
    gaps_resolved = data.get("gaps_resolved", [])
    open_questions = data.get("open_questions", [])

    # Build acceptance criteria from standard categories + any custom ones
    acceptance_criteria = ACCEPTANCE_CRITERIA_CATEGORIES[:]
    for custom in data.get("custom_acceptance_criteria", []):
        acceptance_criteria.append(custom)

    return {
        "error": None,
        "result": {
            "feature": feature,
            "problem_statement": problem,
            "target_users": users,
            "in_scope_surfaces": surfaces,
            "design_constraints": constraints,
            "interaction_requirements": interaction_requirements,
            "accessibility_targets": accessibility_targets,
            "content_requirements": content_requirements,
            "gaps_resolved": gaps_resolved,
            "open_questions": open_questions,
            "acceptance_criteria": acceptance_criteria,
            "summary": (
                f"Design brief generated for '{feature}'. "
                f"{len(surfaces)} surface(s) in scope. "
                f"{len(open_questions)} open question(s) require resolution before design begins."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_design_brief(data)
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
