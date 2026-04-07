#!/usr/bin/env python3
"""
generate.py — Generate an engineering risk register for a delivery.

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

RISK_CATEGORIES = ["technical", "operational", "resource", "external", "security"]

# Risk score matrix: likelihood × impact
LIKELIHOOD_VALUES = {"low": 1, "medium": 2, "high": 3}
IMPACT_VALUES = {"low": 1, "medium": 2, "high": 3, "critical": 4}

RISK_SCORE_LABELS = {
    (1, 1): "minimal", (1, 2): "low", (1, 3): "medium", (1, 4): "medium",
    (2, 1): "low", (2, 2): "medium", (2, 3): "high", (2, 4): "high",
    (3, 1): "medium", (3, 2): "high", (3, 3): "critical", (3, 4): "critical",
}

MITIGATION_STRATEGIES = ["avoid", "reduce", "transfer", "accept"]


def validate_input(data: dict) -> list[str]:
    """Validate required fields."""
    errors: list[str] = []
    if "project_name" not in data:
        errors.append("Missing required field: project_name")
    if "risks" not in data or not isinstance(data["risks"], list):
        errors.append("Missing or invalid field: risks (must be a list)")
        return errors
    for i, risk in enumerate(data["risks"]):
        for f in ["description", "category", "likelihood", "impact", "mitigation_strategy", "owner"]:
            if f not in risk:
                errors.append(f"Risk[{i}] missing field: {f}")
        if risk.get("category") not in RISK_CATEGORIES:
            errors.append(f"Risk[{i}] invalid category: {risk.get('category')}. Valid: {RISK_CATEGORIES}")
        if risk.get("likelihood") not in LIKELIHOOD_VALUES:
            errors.append(f"Risk[{i}] invalid likelihood. Valid: {list(LIKELIHOOD_VALUES.keys())}")
        if risk.get("impact") not in IMPACT_VALUES:
            errors.append(f"Risk[{i}] invalid impact. Valid: {list(IMPACT_VALUES.keys())}")
        if risk.get("mitigation_strategy") not in MITIGATION_STRATEGIES:
            errors.append(f"Risk[{i}] invalid mitigation_strategy. Valid: {MITIGATION_STRATEGIES}")
    return errors


def score_risk(likelihood: str, impact: str) -> tuple[int, str]:
    """Calculate risk score and label."""
    l_val = LIKELIHOOD_VALUES[likelihood]
    i_val = IMPACT_VALUES[impact]
    score = l_val * i_val
    label = RISK_SCORE_LABELS.get((l_val, i_val), "high")
    return score, label


def generate_risk_register(data: dict) -> dict:
    """Generate a structured engineering risk register."""
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    risks = []
    for i, raw in enumerate(data["risks"]):
        score, label = score_risk(raw["likelihood"], raw["impact"])
        risks.append({
            "id": raw.get("id", f"RISK-{i+1:03d}"),
            "description": raw["description"],
            "category": raw["category"],
            "likelihood": raw["likelihood"],
            "impact": raw["impact"],
            "risk_score": score,
            "risk_level": label,
            "mitigation_strategy": raw["mitigation_strategy"],
            "mitigation_detail": raw.get("mitigation_detail", "To be defined"),
            "owner": raw["owner"],
            "status": raw.get("status", "open"),
            "target_resolution_date": raw.get("target_resolution_date", "TBD"),
        })

    # Sort by risk score descending
    risks.sort(key=lambda r: r["risk_score"], reverse=True)

    critical_count = sum(1 for r in risks if r["risk_level"] == "critical")
    high_count = sum(1 for r in risks if r["risk_level"] == "high")
    ownerless = [r["id"] for r in risks if r["owner"] in ("", "TBD", "unassigned")]

    result = {
        "project": data["project_name"],
        "phase": data.get("phase", "unspecified"),
        "register_date": data.get("register_date", "today"),
        "summary": {
            "total_risks": len(risks),
            "critical": critical_count,
            "high": high_count,
            "medium": sum(1 for r in risks if r["risk_level"] == "medium"),
            "low_or_minimal": sum(1 for r in risks if r["risk_level"] in ("low", "minimal")),
        },
        "risks": risks,
        "warnings": (
            [f"Ownerless risks detected: {ownerless} — assign owners immediately"] if ownerless else []
        ),
        "next_review_date": data.get("next_review_date", "At next phase boundary"),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_risk_register(data)
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
