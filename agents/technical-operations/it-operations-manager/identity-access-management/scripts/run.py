#!/usr/bin/env python3
"""
run.py — Manage IAM policies: SSO, MFA, and access control audit.

Usage:
    echo '<json>' | python3 run.py
    python3 run.py < input.json
    python3 run.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# IAM policy requirements by company size
IAM_REQUIREMENTS = {
    "startup_small": {
        "label": "Startup (<25 employees)",
        "sso_required": True,
        "mfa_required": True,
        "privileged_access_review_months": 6,
        "user_access_review_months": 12,
    },
    "startup_medium": {
        "label": "Growth-stage (25-100 employees)",
        "sso_required": True,
        "mfa_required": True,
        "privileged_access_review_months": 3,
        "user_access_review_months": 6,
    },
    "mid_market": {
        "label": "Mid-market (100+ employees)",
        "sso_required": True,
        "mfa_required": True,
        "privileged_access_review_months": 1,
        "user_access_review_months": 3,
    },
}

# Access risk levels
ACCESS_RISK = {
    "admin": "high",
    "billing": "high",
    "production": "high",
    "staging": "medium",
    "read_only": "low",
    "standard": "low",
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "users" not in data or not isinstance(data["users"], list):
        errors.append("Missing required field: users (list)")
    if "company_size_tier" not in data or data.get("company_size_tier") not in IAM_REQUIREMENTS:
        errors.append(f"Missing or invalid field: company_size_tier ({'/'.join(IAM_REQUIREMENTS.keys())})")
    return errors


def run_iam_audit(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    users = data["users"]
    tier = data["company_size_tier"]
    requirements = IAM_REQUIREMENTS[tier]

    # Audit each user
    processed = []
    mfa_missing = []
    sso_not_enrolled = []
    stale_accounts = []
    privileged_without_review = []

    for user in users:
        mfa_enabled = user.get("mfa_enabled", False)
        sso_enrolled = user.get("sso_enrolled", False)
        access_level = user.get("access_level", "standard")
        days_since_login = user.get("days_since_login", 0)
        days_since_access_review = user.get("days_since_access_review", 0)
        is_active = user.get("is_active", True)
        risk_level = ACCESS_RISK.get(access_level, "low")

        # Check compliance
        mfa_issue = not mfa_enabled and is_active
        sso_issue = not sso_enrolled and is_active
        stale = is_active and days_since_login > 90
        review_threshold = (
            requirements["privileged_access_review_months"] * 30
            if risk_level == "high"
            else requirements["user_access_review_months"] * 30
        )
        review_overdue = days_since_access_review > review_threshold

        entry = {
            "username": user["username"],
            "name": user.get("name", ""),
            "department": user.get("department", ""),
            "access_level": access_level,
            "risk_level": risk_level,
            "mfa_enabled": mfa_enabled,
            "sso_enrolled": sso_enrolled,
            "is_active": is_active,
            "days_since_login": days_since_login,
            "days_since_access_review": days_since_access_review,
            "compliance_issues": [],
        }

        if mfa_issue:
            entry["compliance_issues"].append("MFA_NOT_ENABLED")
            mfa_missing.append(entry)
        if sso_issue:
            entry["compliance_issues"].append("NOT_ENROLLED_IN_SSO")
            sso_not_enrolled.append(entry)
        if stale:
            entry["compliance_issues"].append("STALE_ACCOUNT_90_DAYS")
            stale_accounts.append(entry)
        if review_overdue and is_active:
            entry["compliance_issues"].append("ACCESS_REVIEW_OVERDUE")
            if risk_level == "high":
                privileged_without_review.append(entry)

        processed.append(entry)

    # Overall compliance score
    active_users = [u for u in processed if u["is_active"]]
    compliant_users = [u for u in active_users if not u["compliance_issues"]]
    compliance_pct = round(len(compliant_users) / len(active_users) * 100) if active_users else 100

    if compliance_pct >= 90:
        posture = "STRONG"
    elif compliance_pct >= 70:
        posture = "ACCEPTABLE"
    else:
        posture = "AT_RISK"

    return {
        "error": None,
        "result": {
            "company": company,
            "tier": requirements["label"],
            "posture": posture,
            "compliance_pct": compliance_pct,
            "total_users": len(users),
            "active_users": len(active_users),
            "compliant_users": len(compliant_users),
            "mfa_missing": mfa_missing,
            "sso_not_enrolled": sso_not_enrolled,
            "stale_accounts": stale_accounts,
            "privileged_without_review": privileged_without_review,
            "requirements": requirements,
            "summary": (
                f"IAM audit for {company}: {posture} ({compliance_pct}% compliant). "
                f"{len(mfa_missing)} user(s) without MFA, {len(sso_not_enrolled)} not enrolled in SSO, "
                f"{len(stale_accounts)} stale account(s), {len(privileged_without_review)} privileged account(s) overdue for review."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = run_iam_audit(data)
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
