#!/usr/bin/env python3
"""
generate.py — Build or recalibrate the lead scoring model for MQL/SQL handoff.

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

# Standard scoring dimensions
SCORING_DIMENSIONS = {
    "firmographic": {
        "label": "Firmographic Fit",
        "weight": 35,
        "fields": {
            "company_size": {"ideal": "51-500 employees", "points": {"ideal": 15, "acceptable": 8, "poor": 0}},
            "industry": {"ideal": "ICP industry match", "points": {"ideal": 12, "acceptable": 6, "poor": 0}},
            "geography": {"ideal": "Target region", "points": {"ideal": 8, "acceptable": 4, "poor": 0}},
        },
    },
    "role_fit": {
        "label": "Role & Persona Fit",
        "weight": 25,
        "fields": {
            "job_title": {"ideal": "VP/Director/Head of target function", "points": {"ideal": 15, "acceptable": 8, "poor": 0}},
            "seniority": {"ideal": "Manager+", "points": {"ideal": 10, "acceptable": 5, "poor": 0}},
        },
    },
    "behavioral": {
        "label": "Behavioral Engagement",
        "weight": 30,
        "fields": {
            "demo_request": {"label": "Requested a demo", "points": 25},
            "pricing_page": {"label": "Visited pricing page", "points": 15},
            "content_download": {"label": "Downloaded gated content", "points": 10},
            "webinar_attended": {"label": "Attended a webinar", "points": 8},
            "email_clicks": {"label": "Clicked 3+ marketing emails", "points": 6},
            "return_visit": {"label": "Returned to site within 7 days", "points": 5},
        },
    },
    "negative": {
        "label": "Disqualifying Signals",
        "weight": 10,
        "fields": {
            "competitor": {"label": "Works at known competitor", "points": -30},
            "student": {"label": "Student email domain (.edu)", "points": -20},
            "free_email": {"label": "Free email provider (gmail, yahoo, etc.)", "points": -10},
            "job_seeker": {"label": "Job title includes intern/student/unemployed", "points": -15},
        },
    },
}

# MQL threshold
MQL_THRESHOLD_DEFAULT = 50
SQL_THRESHOLD_DEFAULT = 75


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "icp" not in data:
        errors.append("Missing required field: icp (ideal customer profile description)")
    return errors


def generate_scoring_model(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    icp = data["icp"]
    mql_threshold = data.get("mql_threshold", MQL_THRESHOLD_DEFAULT)
    sql_threshold = data.get("sql_threshold", SQL_THRESHOLD_DEFAULT)
    custom_behavioral = data.get("custom_behavioral_signals", [])
    sample_leads = data.get("sample_leads", [])

    # Build model definition
    model_dimensions = []
    for dim_key, dim in SCORING_DIMENSIONS.items():
        if dim_key == "behavioral":
            fields = list(dim["fields"].items())
            for cb in custom_behavioral:
                fields.append((cb["signal"], {"label": cb["signal"], "points": cb.get("points", 5)}))
            model_dimensions.append({
                "dimension": dim["label"],
                "weight_pct": dim["weight"],
                "signals": [{"signal": k, "label": v["label"], "points": v["points"]} for k, v in fields],
            })
        elif dim_key == "negative":
            model_dimensions.append({
                "dimension": dim["label"],
                "weight_pct": dim["weight"],
                "signals": [{"signal": k, "label": v["label"], "points": v["points"]} for k, v in dim["fields"].items()],
            })
        else:
            model_dimensions.append({
                "dimension": dim["label"],
                "weight_pct": dim["weight"],
                "criteria": {k: v for k, v in dim["fields"].items()},
            })

    # Score sample leads if provided
    scored_leads = []
    for lead in sample_leads:
        score = 0
        reasons = []
        # Behavioral signals
        for sig, sig_data in SCORING_DIMENSIONS["behavioral"]["fields"].items():
            if lead.get(sig):
                score += sig_data["points"]
                reasons.append(f"+{sig_data['points']}: {sig_data['label']}")
        # Custom behavioral
        for cb in custom_behavioral:
            if lead.get(cb["signal"]):
                pts = cb.get("points", 5)
                score += pts
                reasons.append(f"+{pts}: {cb['signal']}")
        # Negative signals
        for sig, sig_data in SCORING_DIMENSIONS["negative"]["fields"].items():
            if lead.get(sig):
                score += sig_data["points"]
                reasons.append(f"{sig_data['points']}: {sig_data['label']}")
        # Firmographic approximation
        if lead.get("company_size_fit") == "ideal":
            score += 15
        elif lead.get("company_size_fit") == "acceptable":
            score += 8
        if lead.get("role_fit") == "ideal":
            score += 15
        elif lead.get("role_fit") == "acceptable":
            score += 8

        status = "SQL" if score >= sql_threshold else ("MQL" if score >= mql_threshold else "Non-MQL")
        scored_leads.append({
            "name": lead.get("name", ""),
            "score": score,
            "status": status,
            "scoring_reasons": reasons,
        })

    return {
        "error": None,
        "result": {
            "company": company,
            "icp": icp,
            "mql_threshold": mql_threshold,
            "sql_threshold": sql_threshold,
            "model_dimensions": model_dimensions,
            "sample_lead_scores": scored_leads,
            "review_cadence": "Recalibrate quarterly or when MQL-to-SQL conversion drops below 30%",
            "summary": (
                f"Lead scoring model for {company}: MQL threshold={mql_threshold}, SQL threshold={sql_threshold}. "
                f"{len(model_dimensions)} scoring dimensions. "
                + (f"{len(scored_leads)} sample lead(s) scored." if scored_leads else "No sample leads provided.")
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_scoring_model(data)
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
