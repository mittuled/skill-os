#!/usr/bin/env python3
"""
score.py — Evaluate A/B experiment results for statistical significance, sample ratio mismatch, and peeking bias.

Usage:
    echo '<json>' | python3 score.py
    python3 score.py < input.json
    python3 score.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import math
import sys
from pathlib import Path

REQUIRED_FIELDS = ["experiment_name", "control", "treatment", "confidence_level"]


def validate_input(data: dict) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    for group in ["control", "treatment"]:
        if group in data:
            for field in ["n", "conversions"]:
                if field not in data[group]:
                    errors.append(f"{group} missing field: {field}")
    if "confidence_level" in data and data["confidence_level"] not in [0.90, 0.95, 0.99]:
        errors.append("confidence_level must be 0.90, 0.95, or 0.99")
    return errors


def z_score_to_p(z: float) -> float:
    """Approximation of two-tailed p-value from z-score."""
    # Using Abramowitz and Stegun approximation
    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429
    p_coeff = 0.3275911
    t = 1.0 / (1.0 + p_coeff * abs(z))
    poly = ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t
    one_tailed = poly * math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
    return min(1.0, 2 * one_tailed)


def score_experiment(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    ctrl = data["control"]
    trt = data["treatment"]
    confidence = data["confidence_level"]
    alpha = 1.0 - confidence

    n_ctrl, n_trt = ctrl["n"], trt["n"]
    conv_ctrl, conv_trt = ctrl["conversions"], trt["conversions"]

    rate_ctrl = conv_ctrl / max(n_ctrl, 1)
    rate_trt = conv_trt / max(n_trt, 1)
    lift = (rate_trt - rate_ctrl) / max(rate_ctrl, 0.0001)

    # Pooled proportion z-test
    pooled_rate = (conv_ctrl + conv_trt) / max(n_ctrl + n_trt, 1)
    se = math.sqrt(pooled_rate * (1 - pooled_rate) * (1 / max(n_ctrl, 1) + 1 / max(n_trt, 1)))
    z = (rate_trt - rate_ctrl) / max(se, 0.0001)
    p_value = z_score_to_p(z)
    is_significant = p_value < alpha

    # Sample Ratio Mismatch check
    expected_trt_ratio = data.get("expected_treatment_ratio", 0.5)
    actual_trt_ratio = n_trt / max(n_ctrl + n_trt, 1)
    srm_flag = abs(actual_trt_ratio - expected_trt_ratio) > 0.02

    # Peeking bias flag
    days_running = data.get("days_running", None)
    min_duration = data.get("min_duration_days", 14)
    peeking_flag = days_running is not None and days_running < min_duration and is_significant

    verdict = "INCONCLUSIVE"
    if srm_flag:
        verdict = "INVALID — Sample Ratio Mismatch detected; do not ship"
    elif peeking_flag:
        verdict = "WAIT — Significant but peeking bias risk; continue until minimum duration"
    elif is_significant and lift > 0:
        verdict = "SHIP — Statistically significant positive result"
    elif is_significant and lift <= 0:
        verdict = "NO SHIP — Significant negative result"
    elif not is_significant:
        verdict = "INCONCLUSIVE — Not yet significant; continue experiment"

    return {
        "error": None,
        "result": {
            "experiment_name": data["experiment_name"],
            "control_rate": round(rate_ctrl, 4),
            "treatment_rate": round(rate_trt, 4),
            "absolute_lift": round(rate_trt - rate_ctrl, 4),
            "relative_lift_pct": round(lift * 100, 2),
            "z_score": round(z, 3),
            "p_value": round(p_value, 4),
            "confidence_level": confidence,
            "is_significant": is_significant,
            "srm_detected": srm_flag,
            "peeking_bias_risk": peeking_flag,
            "days_running": days_running,
            "verdict": verdict,
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = score_experiment(data)
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
