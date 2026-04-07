#!/usr/bin/env python3
"""
score.py — Score multi-touch attribution data quality and produce reallocation recommendations.

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

# Attribution model types
ATTRIBUTION_MODELS = {
    "first_touch": "100% credit to first interaction",
    "last_touch": "100% credit to last interaction before conversion",
    "linear": "Equal credit across all touchpoints",
    "time_decay": "More credit to touchpoints closer to conversion",
    "custom_multi_touch": "Custom weights across defined touchpoint types",
}

# Data quality thresholds
MIN_ATTRIBUTION_COVERAGE_PCT = 85.0   # Below this = data quality warning
CRITICAL_COVERAGE_THRESHOLD_PCT = 70.0  # Below this = attribution unreliable

# Channel score weights for quality assessment
QUALITY_DIMENSIONS = {
    "utm_coverage": 0.35,
    "crm_source_accuracy": 0.30,
    "pixel_integrity": 0.20,
    "dedup_accuracy": 0.15,
}


def validate_input(data: dict) -> list[str]:
    errors: list[str] = []
    for f in ["attribution_model", "channels"]:
        if f not in data:
            errors.append(f"Missing required field: {f}")
    if "attribution_model" in data and data["attribution_model"] not in ATTRIBUTION_MODELS:
        errors.append(f"attribution_model must be one of: {list(ATTRIBUTION_MODELS.keys())}")
    if "channels" in data:
        for i, ch in enumerate(data["channels"]):
            for f in ["name", "quality_scores"]:
                if f not in ch:
                    errors.append(f"channels[{i}] missing field: {f}")
            if "quality_scores" in ch:
                for dim in QUALITY_DIMENSIONS:
                    if dim not in ch["quality_scores"]:
                        errors.append(f"channels[{i}].quality_scores missing: {dim}")
                    elif not (0 <= ch["quality_scores"][dim] <= 10):
                        errors.append(f"channels[{i}].quality_scores.{dim} must be 0-10")
    return errors


def assess_channel(channel: dict) -> dict:
    qs = channel["quality_scores"]
    composite = sum(qs[dim] * QUALITY_DIMENSIONS[dim] for dim in QUALITY_DIMENSIONS)
    composite = round(composite, 2)

    coverage_pct = channel.get("attribution_coverage_pct", 100.0)
    if coverage_pct < CRITICAL_COVERAGE_THRESHOLD_PCT:
        status = "UNRELIABLE"
        flag = "Attribution data unreliable — coverage below 70%"
    elif coverage_pct < MIN_ATTRIBUTION_COVERAGE_PCT:
        status = "WARNING"
        flag = "Attribution coverage below 85% — data quality at risk"
    elif composite >= 7.0:
        status = "HEALTHY"
        flag = None
    else:
        status = "NEEDS_IMPROVEMENT"
        flag = "Data quality below acceptable threshold"

    return {
        "channel": channel["name"],
        "quality_score": composite,
        "attribution_coverage_pct": coverage_pct,
        "status": status,
        "flag": flag,
        "quality_breakdown": {dim: qs[dim] for dim in QUALITY_DIMENSIONS},
        "attributed_revenue": channel.get("attributed_revenue", 0),
        "issues": channel.get("issues", []),
    }


def score_attribution(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    model = data["attribution_model"]
    channels = [assess_channel(ch) for ch in data["channels"]]
    channels.sort(key=lambda x: x["quality_score"])

    unreliable = [c for c in channels if c["status"] == "UNRELIABLE"]
    warnings = [c for c in channels if c["status"] == "WARNING"]

    overall_quality = round(sum(c["quality_score"] for c in channels) / len(channels), 2) if channels else 0.0

    if unreliable:
        verdict = "ATTRIBUTION_UNRELIABLE"
        recommendation = f"{len(unreliable)} channel(s) have critical data quality issues — fix before using attribution for budget decisions"
    elif warnings:
        verdict = "ATTRIBUTION_AT_RISK"
        recommendation = f"{len(warnings)} channel(s) have coverage gaps — address before quarterly review"
    else:
        verdict = "ATTRIBUTION_HEALTHY"
        recommendation = "Attribution data quality sufficient for investment decisions"

    result = {
        "attribution_model": model,
        "attribution_model_description": ATTRIBUTION_MODELS[model],
        "overall_quality_score": overall_quality,
        "verdict": verdict,
        "recommendation": recommendation,
        "channels": channels,
        "unreliable_channels": [c["channel"] for c in unreliable],
        "warning_channels": [c["channel"] for c in warnings],
        "total_attributed_revenue": sum(c.get("attributed_revenue", 0) for c in channels),
    }
    return {"error": None, "result": result}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_attribution(data)
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
