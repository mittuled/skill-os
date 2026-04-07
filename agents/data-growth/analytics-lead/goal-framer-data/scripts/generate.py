#!/usr/bin/env python3
"""
generate.py — Generate measurable analytics goals from product and business objectives.

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

METRIC_TYPES = ["conversion_rate", "retention_rate", "engagement", "revenue", "adoption", "satisfaction", "efficiency"]
TIMEFRAMES = ["weekly", "monthly", "quarterly", "annual"]

GOAL_FRAMEWORK = {
    "objective": "The business or product goal being measured",
    "key_result": "The specific measurable outcome",
    "metric_name": "Exact metric name as it appears in the data warehouse",
    "baseline": "Current measured value",
    "target": "Success threshold",
    "timeframe": "Measurement period",
    "query_approach": "How to compute this metric from raw data",
}

REQUIRED_FIELDS = ["objective", "metrics"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "metrics" in data:
        for m in data["metrics"]:
            for field in ["name", "metric_type", "baseline", "target", "timeframe"]:
                if field not in m:
                    errors.append(f"Metric '{m.get('name', '?')}' missing field: {field}")
    return errors


def frame_goals(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    metrics = data["metrics"]
    framed = []

    for m in metrics:
        baseline = m["baseline"]
        target = m["target"]
        pct_change = ((target - baseline) / max(abs(baseline), 0.001)) * 100 if baseline != target else 0

        framed.append({
            "metric_name": m["name"],
            "metric_type": m["metric_type"],
            "key_result": f"Improve {m['name']} from {baseline} to {target} ({'+' if pct_change >= 0 else ''}{pct_change:.1f}%) by end of {m['timeframe']}",
            "baseline": baseline,
            "target": target,
            "pct_change_required": round(pct_change, 1),
            "timeframe": m["timeframe"],
            "measurement_frequency": m.get("measurement_frequency", "weekly"),
            "query_approach": m.get("query_approach", f"SELECT {m['name']} FROM metrics WHERE date >= period_start GROUP BY date"),
            "success_criteria": f"{m['name']} >= {target} sustained for the final 2 weeks of the measurement period",
            "failure_threshold": f"{m['name']} < {round(baseline * 0.95, 3)} triggers initiative review",
        })

    return {
        "error": None,
        "result": {
            "objective": data["objective"],
            "team": data.get("team", "Product"),
            "goal_period": data.get("goal_period", "Q2 2026"),
            "framed_metrics": framed,
            "total_metrics": len(framed),
            "anti_patterns_checked": [
                "All metrics have numeric baselines — no 'improve engagement' without a number",
                "All targets are achievable from baseline — no moonshot without evidence",
                "Each metric has a query approach — no unqueryable goals",
            ],
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = frame_goals(data)
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
