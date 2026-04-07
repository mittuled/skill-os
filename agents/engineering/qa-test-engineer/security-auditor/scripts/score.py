#!/usr/bin/env python3
"""
score.py — Score a security audit by classifying findings and producing a release recommendation.

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

SEVERITY_SCORES = {"critical": 0, "high": 25, "medium": 65, "low": 90, "info": 100}
SEVERITY_BLOCKERS = {"critical", "high"}
FINDING_CATEGORIES = ["injection", "authentication", "authorization", "secrets", "configuration", "dependency", "xss", "other"]


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["audit_scope", "findings"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "findings" in data:
        for i, f in enumerate(data["findings"]):
            for field in ["title", "severity", "category"]:
                if field not in f:
                    errors.append(f"Finding[{i}] missing field: {field}")
            if f.get("severity") not in SEVERITY_SCORES:
                errors.append(f"Finding[{i}] invalid severity: {f.get('severity')}")
    return errors


def score_audit(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    findings = data["findings"]
    blocking = [f for f in findings if f["severity"] in SEVERITY_BLOCKERS]
    medium = [f for f in findings if f["severity"] == "medium"]
    low_info = [f for f in findings if f["severity"] in ("low", "info")]

    if not findings:
        score = 100
    elif not blocking and not medium:
        score = 90
    elif not blocking:
        score = 65
    else:
        score = 20

    if not blocking:
        recommendation = "RELEASE_APPROVED" if not medium else "RELEASE_WITH_TRACKED_REMEDIATION"
        verdict = "No critical or high vulnerabilities found" if not medium else f"{len(medium)} medium findings must be remediated in next sprint"
    else:
        recommendation = "RELEASE_BLOCKED"
        verdict = f"{len(blocking)} blocking vulnerability/ies found — must be fixed before release"

    by_category: dict[str, list] = {}
    for f in findings:
        cat = f.get("category", "other")
        by_category.setdefault(cat, []).append(f)

    result = {
        "scope": data["audit_scope"],
        "audit_score": score,
        "recommendation": recommendation,
        "verdict": verdict,
        "counts": {
            "critical": sum(1 for f in findings if f["severity"] == "critical"),
            "high": sum(1 for f in findings if f["severity"] == "high"),
            "medium": len(medium),
            "low_info": len(low_info),
            "total": len(findings),
        },
        "blocking_findings": blocking,
        "medium_findings": medium,
        "findings_by_category": {k: [f["title"] for f in v] for k, v in by_category.items()},
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_audit(data)
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
