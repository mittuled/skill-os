#!/usr/bin/env python3
"""
score.py — Synthesise and score account portfolio signals to identify expansion and churn risk trends.

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

# Signal classification types
SIGNAL_TYPES = ["expansion_opportunity", "churn_risk", "relationship_health", "competitive_threat", "product_feedback"]

# Risk scoring weights for portfolio health
CHURN_RISK_INDICATORS = {
    "nps_below_6": 3,
    "usage_decline_over_20pct": 3,
    "executive_sponsor_change": 2,
    "support_escalations_open": 2,
    "competitor_evaluation": 3,
    "no_qbr_in_two_quarters": 1,
    "renewal_approaching_no_contact": 2,
}

EXPANSION_INDICATORS = {
    "usage_above_80pct": 3,
    "headcount_growth": 2,
    "new_use_case_mentioned": 2,
    "budget_cycle_open": 2,
    "champion_engaged": 1,
    "feature_request_submitted": 1,
}

REQUIRED_FIELDS = ["signals"]


def validate_input(data: dict) -> list[str]:
    errors = []
    if "signals" not in data:
        errors.append("Missing required field: signals (list of signal objects)")
        return errors
    for i, signal in enumerate(data["signals"]):
        for field in ["account_name", "signal_type", "indicators"]:
            if field not in signal:
                errors.append(f"Signal {i}: missing field '{field}'")
        if "signal_type" in signal and signal["signal_type"] not in SIGNAL_TYPES:
            errors.append(f"Signal {i}: signal_type must be one of {SIGNAL_TYPES}")
    return errors


def synthesise_signals(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    signals = data["signals"]
    account_summaries: dict[str, dict] = {}

    for signal in signals:
        account = signal["account_name"]
        if account not in account_summaries:
            account_summaries[account] = {
                "account_name": account,
                "signals": [],
                "churn_risk_score": 0,
                "expansion_score": 0,
                "signal_types": [],
            }

        acc = account_summaries[account]
        acc["signals"].append(signal)
        acc["signal_types"].append(signal["signal_type"])

        # Score based on indicators
        for indicator in signal.get("indicators", []):
            if indicator in CHURN_RISK_INDICATORS:
                acc["churn_risk_score"] += CHURN_RISK_INDICATORS[indicator]
            if indicator in EXPANSION_INDICATORS:
                acc["expansion_score"] += EXPANSION_INDICATORS[indicator]

    # Classify accounts
    portfolio_insights = []
    churn_risk_accounts = []
    expansion_accounts = []

    for account, summary in account_summaries.items():
        churn_score = summary["churn_risk_score"]
        expansion_score = summary["expansion_score"]

        if churn_score >= 5:
            churn_tier = "high"
            churn_risk_accounts.append(account)
        elif churn_score >= 2:
            churn_tier = "medium"
        else:
            churn_tier = "low"

        if expansion_score >= 5:
            expansion_tier = "high"
            expansion_accounts.append(account)
        elif expansion_score >= 2:
            expansion_tier = "medium"
        else:
            expansion_tier = "low"

        portfolio_insights.append({
            "account_name": account,
            "churn_risk": churn_tier,
            "churn_risk_score": churn_score,
            "expansion_potential": expansion_tier,
            "expansion_score": expansion_score,
            "signal_count": len(summary["signals"]),
            "signal_types_present": list(set(summary["signal_types"])),
        })

    # Sort: churn risk first, then expansion potential
    portfolio_insights.sort(key=lambda x: (-x["churn_risk_score"], -x["expansion_score"]))

    # Portfolio-level patterns
    total_accounts = len(account_summaries)
    patterns = []
    if len(churn_risk_accounts) / max(total_accounts, 1) > 0.2:
        patterns.append("SYSTEMIC RISK: >20% of portfolio shows high churn risk — investigate common causes")
    if len(expansion_accounts) > 0:
        patterns.append(f"EXPANSION PIPELINE: {len(expansion_accounts)} accounts show high expansion potential this quarter")

    return {
        "error": None,
        "result": {
            "portfolio_size": total_accounts,
            "signals_processed": len(signals),
            "high_churn_risk_accounts": churn_risk_accounts,
            "high_expansion_accounts": expansion_accounts,
            "portfolio_patterns": patterns,
            "account_summaries": portfolio_insights,
            "recommended_actions": [
                {"priority": "P1", "action": f"Immediate outreach to {a} — high churn risk"} for a in churn_risk_accounts
            ] + [
                {"priority": "P2", "action": f"Frame expansion opportunity for {a}"} for a in expansion_accounts
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = synthesise_signals(data)
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
