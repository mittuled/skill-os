#!/usr/bin/env python3
"""
score.py — Analyse revenue funnel stages for conversion bottlenecks and velocity issues.

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

# Benchmark conversion rates by stage (industry SaaS benchmarks)
STAGE_BENCHMARKS = {
    "mql_to_sql": {"benchmark_pct": 20.0, "warning_threshold_pct": 15.0},
    "sql_to_opportunity": {"benchmark_pct": 55.0, "warning_threshold_pct": 45.0},
    "opportunity_to_proposal": {"benchmark_pct": 60.0, "warning_threshold_pct": 50.0},
    "proposal_to_closed_won": {"benchmark_pct": 30.0, "warning_threshold_pct": 20.0},
    "closed_won_to_expanded": {"benchmark_pct": 40.0, "warning_threshold_pct": 30.0},
}

# Severity of bottleneck
BOTTLENECK_SEVERITY = {
    "critical": "Below warning threshold — immediate investigation required",
    "warning": "Below benchmark — monitor and investigate",
    "healthy": "At or above benchmark",
}

# Average time-in-stage benchmarks (days)
VELOCITY_BENCHMARKS_DAYS = {
    "mql_to_sql": 3,
    "sql_to_opportunity": 7,
    "opportunity_to_proposal": 14,
    "proposal_to_closed_won": 21,
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    if "stages" not in data:
        errors.append("Missing required field: stages")
        return errors
    for i, s in enumerate(data["stages"]):
        for f in ["name", "conversion_rate_pct", "avg_days_in_stage"]:
            if f not in s:
                errors.append(f"stages[{i}] missing field: {f}")
        if "conversion_rate_pct" in s and not (0 <= s["conversion_rate_pct"] <= 100):
            errors.append(f"stages[{i}].conversion_rate_pct must be 0-100")
    return errors


def assess_stage(stage: dict) -> dict:
    name = stage["name"]
    rate = stage["conversion_rate_pct"]
    days = stage["avg_days_in_stage"]

    benchmark = STAGE_BENCHMARKS.get(name, {})
    bench_rate = benchmark.get("benchmark_pct", None)
    warn_threshold = benchmark.get("warning_threshold_pct", None)

    # Determine conversion health
    if bench_rate is not None:
        if rate < (warn_threshold or 0):
            conv_status = "critical"
        elif rate < bench_rate:
            conv_status = "warning"
        else:
            conv_status = "healthy"
        conv_delta = round(rate - bench_rate, 1)
    else:
        conv_status = "no_benchmark"
        conv_delta = None

    # Determine velocity health
    vel_bench = VELOCITY_BENCHMARKS_DAYS.get(name)
    if vel_bench is not None:
        velocity_status = "slow" if days > vel_bench * 1.5 else "normal"
        velocity_delta_days = days - vel_bench
    else:
        velocity_status = "no_benchmark"
        velocity_delta_days = None

    return {
        "stage": name,
        "conversion_rate_pct": rate,
        "benchmark_pct": bench_rate,
        "conversion_delta_pct": conv_delta,
        "conversion_status": conv_status,
        "avg_days_in_stage": days,
        "velocity_status": velocity_status,
        "velocity_delta_days": velocity_delta_days,
        "volume_in": stage.get("volume_in", None),
        "volume_out": stage.get("volume_out", None),
        "segment_notes": stage.get("segment_notes", ""),
    }


def analyse_funnel(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    stages = [assess_stage(s) for s in data["stages"]]

    bottlenecks = [s for s in stages if s["conversion_status"] in ("critical", "warning")]
    bottlenecks.sort(key=lambda x: ["critical", "warning", "healthy", "no_benchmark"].index(x["conversion_status"]))

    critical_count = sum(1 for s in stages if s["conversion_status"] == "critical")
    warning_count = sum(1 for s in stages if s["conversion_status"] == "warning")

    if critical_count > 0:
        verdict = "PIPELINE_AT_RISK"
        summary = f"{critical_count} critical bottleneck(s) — immediate investigation required"
    elif warning_count > 0:
        verdict = "PIPELINE_DEGRADED"
        summary = f"{warning_count} stage(s) below benchmark — monitor and investigate"
    else:
        verdict = "PIPELINE_HEALTHY"
        summary = "All funnel stages at or above benchmark"

    result = {
        "analysis_period": data.get("analysis_period", ""),
        "verdict": verdict,
        "summary": summary,
        "stages": stages,
        "bottlenecks": [
            {
                "stage": s["stage"],
                "severity": s["conversion_status"],
                "conversion_rate_pct": s["conversion_rate_pct"],
                "benchmark_pct": s["benchmark_pct"],
                "delta_pct": s["conversion_delta_pct"],
                "recommended_action": data.get("recommendations", {}).get(s["stage"], "Investigate root cause"),
            }
            for s in bottlenecks
        ],
        "total_pipeline_volume": data.get("total_pipeline_volume", None),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = analyse_funnel(data)
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
