#!/usr/bin/env python3
"""Generate a business model sketch from JSON parameters.

Reads JSON from stdin with model parameters, outputs a formatted business model summary.

Usage:
    echo '{"product_name": "TaskFlow", "arpu": 299, "cac": 1500, "monthly_churn": 0.05, "cogs_per_user": 45, "fixed_costs_monthly": 50000}' | python3 generate.py
"""

import json
import sys
from datetime import date


def calculate_unit_economics(params: dict) -> dict:
    arpu = params["arpu"]
    cac = params["cac"]
    cogs = params.get("cogs_per_user", 0)
    churn = params["monthly_churn"]
    fixed = params.get("fixed_costs_monthly", 0)

    gross_margin_pct = (arpu - cogs) / arpu if arpu > 0 else 0
    ltv = (arpu * gross_margin_pct) / churn if churn > 0 else float("inf")
    payback_months = cac / (arpu * gross_margin_pct) if (arpu * gross_margin_pct) > 0 else float("inf")
    ltv_cac_ratio = ltv / cac if cac > 0 else float("inf")
    contribution_margin = arpu - cogs
    break_even_users = fixed / contribution_margin if contribution_margin > 0 else float("inf")

    return {
        "arpu": arpu,
        "cac": cac,
        "cogs_per_user": cogs,
        "gross_margin_pct": round(gross_margin_pct * 100, 1),
        "ltv": round(ltv, 2),
        "payback_months": round(payback_months, 1),
        "ltv_cac_ratio": round(ltv_cac_ratio, 2),
        "contribution_margin": round(contribution_margin, 2),
        "break_even_users": round(break_even_users),
        "fixed_costs_monthly": fixed,
    }


def generate_sensitivity(params: dict, economics: dict) -> list[dict]:
    scenarios = []
    for label, arpu_mult, churn_mult in [("Pessimistic", 0.8, 1.5), ("Base", 1.0, 1.0), ("Optimistic", 1.2, 0.7)]:
        adj_arpu = params["arpu"] * arpu_mult
        adj_churn = params["monthly_churn"] * churn_mult
        adj_cogs = params.get("cogs_per_user", 0)
        gm = (adj_arpu - adj_cogs) / adj_arpu if adj_arpu > 0 else 0
        ltv = (adj_arpu * gm) / adj_churn if adj_churn > 0 else float("inf")
        cm = adj_arpu - adj_cogs
        be = params.get("fixed_costs_monthly", 0) / cm if cm > 0 else float("inf")
        scenarios.append({
            "scenario": label,
            "arpu": round(adj_arpu, 2),
            "churn": round(adj_churn, 4),
            "ltv": round(ltv, 2),
            "break_even_users": round(be),
        })
    return scenarios


def main() -> None:
    params = json.load(sys.stdin)
    required = ["product_name", "arpu", "cac", "monthly_churn"]
    missing = [k for k in required if k not in params]
    if missing:
        json.dump({"error": f"Missing required fields: {missing}"}, sys.stdout, indent=2)
        sys.exit(1)

    economics = calculate_unit_economics(params)
    sensitivity = generate_sensitivity(params, economics)

    result = {
        "skill": "business-model-sketcher",
        "product": params["product_name"],
        "generated_date": date.today().isoformat(),
        "unit_economics": economics,
        "sensitivity_analysis": sensitivity,
        "viability_signal": "viable" if economics["ltv_cac_ratio"] >= 3.0 else "at_risk" if economics["ltv_cac_ratio"] >= 1.5 else "not_viable",
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
