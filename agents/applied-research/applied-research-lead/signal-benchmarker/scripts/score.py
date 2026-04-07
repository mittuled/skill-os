#!/usr/bin/env python3
"""
score.py — Benchmark company metrics against industry standards and comparable-stage peers.

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

# SaaS industry benchmarks by company stage (ARR-based)
BENCHMARKS = {
    "seed_to_series_a": {  # $0-$2M ARR
        "net_revenue_retention_pct": {"p25": 85, "p50": 100, "p75": 115, "label": "NRR"},
        "gross_margin_pct": {"p25": 55, "p50": 68, "p75": 75, "label": "Gross Margin"},
        "monthly_churn_rate_pct": {"p25": 3.0, "p50": 2.0, "p75": 1.2, "label": "Monthly Churn (lower is better)"},
        "arr_growth_rate_pct": {"p25": 80, "p50": 150, "p75": 300, "label": "ARR YoY Growth"},
        "cac_payback_months": {"p25": 30, "p50": 18, "p75": 12, "label": "CAC Payback (lower is better)"},
    },
    "series_a_to_b": {  # $2-$10M ARR
        "net_revenue_retention_pct": {"p25": 95, "p50": 110, "p75": 125, "label": "NRR"},
        "gross_margin_pct": {"p25": 60, "p50": 70, "p75": 78, "label": "Gross Margin"},
        "monthly_churn_rate_pct": {"p25": 2.0, "p50": 1.5, "p75": 0.8, "label": "Monthly Churn"},
        "arr_growth_rate_pct": {"p25": 60, "p50": 100, "p75": 200, "label": "ARR YoY Growth"},
        "cac_payback_months": {"p25": 24, "p50": 15, "p75": 10, "label": "CAC Payback"},
    },
    "series_b_plus": {  # $10M+ ARR
        "net_revenue_retention_pct": {"p25": 100, "p50": 115, "p75": 130, "label": "NRR"},
        "gross_margin_pct": {"p25": 65, "p50": 73, "p75": 80, "label": "Gross Margin"},
        "monthly_churn_rate_pct": {"p25": 1.5, "p50": 1.0, "p75": 0.5, "label": "Monthly Churn"},
        "arr_growth_rate_pct": {"p25": 40, "p50": 70, "p75": 150, "label": "ARR YoY Growth"},
        "cac_payback_months": {"p25": 20, "p50": 13, "p75": 8, "label": "CAC Payback"},
    },
}

LOWER_IS_BETTER = ["monthly_churn_rate_pct", "cac_payback_months"]
REQUIRED_FIELDS = ["company_stage", "metrics"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "company_stage" in data and data["company_stage"] not in BENCHMARKS:
        errors.append(f"company_stage must be one of {list(BENCHMARKS.keys())}")
    return errors


def score_benchmarks(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    stage = data["company_stage"]
    benchmarks = BENCHMARKS[stage]
    metrics = data["metrics"]
    results = []

    for metric_name, value in metrics.items():
        if metric_name not in benchmarks:
            continue
        bench = benchmarks[metric_name]
        lower_better = metric_name in LOWER_IS_BETTER

        if lower_better:
            if value <= bench["p75"]:
                percentile = "top quartile"
            elif value <= bench["p50"]:
                percentile = "above median"
            elif value <= bench["p25"]:
                percentile = "below median"
            else:
                percentile = "bottom quartile"
        else:
            if value >= bench["p75"]:
                percentile = "top quartile"
            elif value >= bench["p50"]:
                percentile = "above median"
            elif value >= bench["p25"]:
                percentile = "below median"
            else:
                percentile = "bottom quartile"

        results.append({
            "metric": bench["label"],
            "your_value": value,
            "p25": bench["p25"],
            "p50": bench["p50"],
            "p75": bench["p75"],
            "percentile_position": percentile,
            "lower_is_better": lower_better,
        })

    top_quartile = sum(1 for r in results if r["percentile_position"] == "top quartile")
    below_median = [r for r in results if r["percentile_position"] in ["below median", "bottom quartile"]]

    return {
        "error": None,
        "result": {
            "company_stage": stage,
            "metrics_benchmarked": len(results),
            "top_quartile_count": top_quartile,
            "benchmark_results": results,
            "improvement_opportunities": [r["metric"] for r in below_median],
            "overall_health": "strong" if top_quartile >= len(results) * 0.6 else ("mixed" if top_quartile >= len(results) * 0.3 else "concerning"),
            "benchmark_source": "Median benchmarks from Bessemer, a16z, and OpenView SaaS surveys 2024-2025",
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_benchmarks(data)
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
