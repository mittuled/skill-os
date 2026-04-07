#!/usr/bin/env python3
"""
score.py — Score email deliverability health across sender reputation, list hygiene, and config.

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

# Scoring rubric: dimension -> {weight, criteria}
RUBRIC = {
    "sender_authentication": {
        "weight": 25,
        "criteria": {
            "spf_configured": {"points": 8, "label": "SPF record configured"},
            "dkim_configured": {"points": 9, "label": "DKIM signing configured"},
            "dmarc_configured": {"points": 8, "label": "DMARC policy set (p=quarantine or reject)"},
        },
    },
    "list_hygiene": {
        "weight": 30,
        "criteria": {
            "bounce_rate_ok": {"points": 10, "label": "Hard bounce rate <2%"},
            "unsubscribe_rate_ok": {"points": 10, "label": "Unsubscribe rate <0.5%"},
            "spam_complaint_rate_ok": {"points": 10, "label": "Spam complaint rate <0.1%"},
        },
    },
    "sending_practices": {
        "weight": 25,
        "criteria": {
            "warmup_complete": {"points": 8, "label": "Domain/IP warmup complete"},
            "consistent_volume": {"points": 9, "label": "Consistent send volume (no sudden spikes)"},
            "double_optin": {"points": 8, "label": "Double opt-in used for new subscribers"},
        },
    },
    "engagement": {
        "weight": 20,
        "criteria": {
            "open_rate_ok": {"points": 7, "label": "Open rate >20%"},
            "click_rate_ok": {"points": 7, "label": "Click rate >2%"},
            "inactive_suppressed": {"points": 6, "label": "Inactive contacts (90+ days) suppressed"},
        },
    },
}

# Grade bands
GRADE_BANDS = [
    (90, "A", "EXCELLENT"),
    (75, "B", "GOOD"),
    (60, "C", "ACCEPTABLE"),
    (45, "D", "AT_RISK"),
    (0, "F", "CRITICAL"),
]

# Thresholds for auto-scoring
THRESHOLDS = {
    "hard_bounce_rate_max": 0.02,
    "unsubscribe_rate_max": 0.005,
    "spam_complaint_rate_max": 0.001,
    "open_rate_min": 0.20,
    "click_rate_min": 0.02,
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "sending_domain" not in data:
        errors.append("Missing required field: sending_domain")
    return errors


def score_deliverability(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    domain = data["sending_domain"]

    # Authentication checks
    spf = data.get("spf_configured", False)
    dkim = data.get("dkim_configured", False)
    dmarc = data.get("dmarc_configured", False)

    # Metrics
    bounce_rate = data.get("hard_bounce_rate", 0)
    unsubscribe_rate = data.get("unsubscribe_rate", 0)
    spam_rate = data.get("spam_complaint_rate", 0)
    open_rate = data.get("open_rate", 0)
    click_rate = data.get("click_rate", 0)

    # Practices
    warmup = data.get("warmup_complete", False)
    consistent = data.get("consistent_send_volume", False)
    double_optin = data.get("double_optin_used", False)
    inactive_suppressed = data.get("inactive_contacts_suppressed", False)

    # Score each criterion
    dim_scores = {}
    total_score = 0
    issues = []
    strengths = []

    criteria_results = {
        "spf_configured": spf,
        "dkim_configured": dkim,
        "dmarc_configured": dmarc,
        "bounce_rate_ok": bounce_rate <= THRESHOLDS["hard_bounce_rate_max"],
        "unsubscribe_rate_ok": unsubscribe_rate <= THRESHOLDS["unsubscribe_rate_max"],
        "spam_complaint_rate_ok": spam_rate <= THRESHOLDS["spam_complaint_rate_max"],
        "warmup_complete": warmup,
        "consistent_volume": consistent,
        "double_optin": double_optin,
        "open_rate_ok": open_rate >= THRESHOLDS["open_rate_min"],
        "click_rate_ok": click_rate >= THRESHOLDS["click_rate_min"],
        "inactive_suppressed": inactive_suppressed,
    }

    for dim_key, dim in RUBRIC.items():
        dim_earned = 0
        dim_total = sum(c["points"] for c in dim["criteria"].values())
        for crit_key, crit in dim["criteria"].items():
            passed = criteria_results.get(crit_key, False)
            if passed:
                dim_earned += crit["points"]
                strengths.append(crit["label"])
            else:
                issues.append(crit["label"])
        dim_pct = round(dim_earned / dim_total * 100) if dim_total else 100
        weighted = round(dim_pct * dim["weight"] / 100)
        dim_scores[dim_key] = {
            "label": dim_key.replace("_", " ").title(),
            "score": dim_pct,
            "weighted_contribution": weighted,
            "weight": dim["weight"],
        }
        total_score += weighted

    # Grade
    grade_letter, grade_label = "F", "CRITICAL"
    for threshold, letter, label in GRADE_BANDS:
        if total_score >= threshold:
            grade_letter, grade_label = letter, label
            break

    return {
        "error": None,
        "result": {
            "company": company,
            "sending_domain": domain,
            "total_score": total_score,
            "grade": grade_letter,
            "verdict": grade_label,
            "dimension_scores": dim_scores,
            "issues": issues,
            "strengths": strengths,
            "metrics": {
                "hard_bounce_rate": f"{round(bounce_rate * 100, 2)}%",
                "unsubscribe_rate": f"{round(unsubscribe_rate * 100, 2)}%",
                "spam_complaint_rate": f"{round(spam_rate * 100, 3)}%",
                "open_rate": f"{round(open_rate * 100, 1)}%",
                "click_rate": f"{round(click_rate * 100, 1)}%",
            },
            "summary": (
                f"Email deliverability for {domain} ({company}): {total_score}/100 — {grade_label}. "
                f"{len(issues)} issue(s) identified, {len(strengths)} criteria passing."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_deliverability(data)
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
