#!/usr/bin/env python3
"""
score.py — Detect and score platform capability gaps blocking engineering productivity.

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

# Platform capability domains with expected capabilities
PLATFORM_CAPABILITIES = {
    "developer_onboarding": {
        "label": "Developer Onboarding",
        "expected": [
            "Local dev environment setup <30 min",
            "Service template for new services",
            "Development environment parity with production",
            "Documentation site accessible",
        ],
    },
    "ci_cd": {
        "label": "CI/CD",
        "expected": [
            "Automated testing on PR",
            "Automated deployment to staging",
            "Automated deployment to production (with approval)",
            "Rollback mechanism",
        ],
    },
    "observability": {
        "label": "Observability",
        "expected": [
            "Centralized logging",
            "Metrics and dashboards",
            "Distributed tracing",
            "Alerting and on-call rotation",
        ],
    },
    "infrastructure": {
        "label": "Infrastructure as Code",
        "expected": [
            "All infrastructure defined in code",
            "Repeatable environment provisioning",
            "Drift detection",
            "Cost tagging and visibility",
        ],
    },
    "security_compliance": {
        "label": "Security & Compliance",
        "expected": [
            "Dependency vulnerability scanning",
            "Secret scanning in CI",
            "Access control and least privilege",
            "Audit logging",
        ],
    },
    "data_platform": {
        "label": "Data Platform",
        "expected": [
            "Data warehouse or analytics store",
            "ETL/ELT pipeline",
            "Data access governance",
            "Self-serve analytics for product and business",
        ],
    },
    "developer_self_service": {
        "label": "Developer Self-Service",
        "expected": [
            "Internal developer portal",
            "Service catalogue",
            "Self-service environment provisioning",
            "Feature flag service",
        ],
    },
}

# Severity for missing capabilities
SEVERITY_WEIGHTS = {
    "ci_cd": 30,
    "observability": 25,
    "security_compliance": 25,
    "developer_onboarding": 10,
    "infrastructure": 5,
    "data_platform": 3,
    "developer_self_service": 2,
}

# Grade bands
GRADE_BANDS = [(90, "A", "EXCELLENT"), (75, "B", "GOOD"), (60, "C", "ACCEPTABLE"), (45, "D", "AT_RISK"), (0, "F", "CRITICAL")]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "team_name" not in data:
        errors.append("Missing required field: team_name")
    if "capabilities" not in data or not isinstance(data["capabilities"], list):
        errors.append("Missing required field: capabilities (list of capability status objects)")
    return errors


def score_capabilities(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    team = data["team_name"]
    capabilities_input = data["capabilities"]

    # Index by domain
    cap_by_domain = {c.get("domain", ""): c for c in capabilities_input}

    domain_results = []
    total_weighted_score = 0
    total_weight = sum(SEVERITY_WEIGHTS.values())
    critical_gaps = []

    for domain_key, domain_config in PLATFORM_CAPABILITIES.items():
        cap_input = cap_by_domain.get(domain_key, {})
        present_capabilities = cap_input.get("present_capabilities", [])
        expected = domain_config["expected"]
        weight = SEVERITY_WEIGHTS.get(domain_key, 2)

        # Check each expected capability
        present_lower = [p.lower() for p in present_capabilities]
        met = []
        missing = []
        for exp in expected:
            if any(word in " ".join(present_lower) for word in exp.lower().split()[:3]):
                met.append(exp)
            else:
                missing.append(exp)

        pct = round(len(met) / len(expected) * 100) if expected else 100
        weighted_contribution = round(pct * weight / 100)
        total_weighted_score += weighted_contribution

        severity = "CRITICAL" if pct < 25 else ("HIGH" if pct < 50 else ("MEDIUM" if pct < 75 else "LOW"))

        entry = {
            "domain": domain_key,
            "label": domain_config["label"],
            "completeness_pct": pct,
            "weight": weight,
            "severity": severity,
            "met_capabilities": met,
            "missing_capabilities": missing,
            "notes": cap_input.get("notes", ""),
        }
        domain_results.append(entry)
        if severity in ("CRITICAL", "HIGH"):
            critical_gaps.append(entry)

    overall_score = round(total_weighted_score / total_weight * 100)
    grade_letter, grade_label = "F", "CRITICAL"
    for threshold, letter, label in GRADE_BANDS:
        if overall_score >= threshold:
            grade_letter, grade_label = letter, label
            break

    return {
        "error": None,
        "result": {
            "team": team,
            "overall_score": overall_score,
            "grade": grade_letter,
            "verdict": grade_label,
            "domain_results": domain_results,
            "critical_and_high_gaps": critical_gaps,
            "summary": (
                f"Platform capability audit for {team}: {overall_score}/100 — {grade_label}. "
                f"{len(critical_gaps)} critical/high gap(s) identified."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_capabilities(data)
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
