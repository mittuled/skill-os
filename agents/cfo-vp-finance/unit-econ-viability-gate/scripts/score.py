#!/usr/bin/env python3
"""
unit-econ-viability-gate — Evaluate unit economics viability as a go/no-go gate.
Input (JSON via stdin or -i):
  {
    "company": str,
    "segment": str,           # e.g. "Enterprise", "SMB", "Self-Serve"
    "gross_margin_pct": float,
    "arpu_monthly": float,    # average revenue per customer per month
    "avg_contract_months": float,  # expected lifetime in months
    "cac": float,             # fully-loaded customer acquisition cost
    "churn_rate_monthly_pct": float,  # monthly churn rate %
    "runway_months": int,
    "target_payback_months": int,
    "downside_scenarios": {
      "churn_increase_pp": float,   # additional churn in pp (e.g. 2 for +2pp)
      "cac_inflation_pct": float,   # % increase in CAC (e.g. 20 for +20%)
      "margin_compression_pp": float  # gross margin decrease in pp (e.g. 5 for -5pp)
    }
  }
Output: Gate decision memo as Markdown.
"""

import json
import sys
import argparse
import math

# Gate thresholds (Bessemer / SaaS Capital industry standards)
LTV_CAC_PASS = 3.0           # minimum acceptable
LTV_CAC_STRONG = 5.0         # strong signal
PAYBACK_PASS_MONTHS = 18     # maximum acceptable in most cases
PAYBACK_CONDITIONAL_MONTHS = 24  # max for conditional pass
GROSS_MARGIN_FLOOR = 55.0    # below this, no pass possible
RUNWAY_PAYBACK_RATIO = 0.6   # payback must be < 60% of runway


def fmt_usd(amount: float) -> str:
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.2f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.1f}K"
    return f"${amount:.0f}"


def fmt_pct(value: float) -> str:
    return f"{value:.1f}%"


def validate_input(data: dict) -> list[str]:
    required = [
        "company", "segment", "gross_margin_pct", "arpu_monthly",
        "avg_contract_months", "cac", "churn_rate_monthly_pct",
        "runway_months", "target_payback_months", "downside_scenarios"
    ]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    downside_required = ["churn_increase_pp", "cac_inflation_pct", "margin_compression_pp"]
    if "downside_scenarios" in data:
        for sub in downside_required:
            if sub not in data["downside_scenarios"]:
                errors.append(f"Missing downside_scenarios.{sub}")
    return errors


def compute_ltv(arpu_monthly: float, gross_margin_pct: float, churn_monthly_pct: float) -> float:
    """LTV = ARPU × Gross Margin / Monthly Churn Rate"""
    if churn_monthly_pct <= 0:
        return float("inf")
    return arpu_monthly * (gross_margin_pct / 100) / (churn_monthly_pct / 100)


def compute_payback(cac: float, arpu_monthly: float, gross_margin_pct: float) -> float:
    """Payback = CAC / (ARPU × Gross Margin)"""
    contribution = arpu_monthly * (gross_margin_pct / 100)
    if contribution <= 0:
        return float("inf")
    return cac / contribution


def assess_scenario(
    label: str,
    arpu: float,
    gm_pct: float,
    cac: float,
    churn_monthly_pct: float,
    runway: int,
    target_payback: int,
) -> dict:
    ltv = compute_ltv(arpu, gm_pct, churn_monthly_pct)
    ltv_cac = ltv / cac if cac > 0 else 0
    payback = compute_payback(cac, arpu, gm_pct)

    # Determine verdict contribution
    if gm_pct < GROSS_MARGIN_FLOOR:
        verdict = "FAIL"
        notes = [f"Gross margin {fmt_pct(gm_pct)} below floor {fmt_pct(GROSS_MARGIN_FLOOR)}"]
    elif ltv_cac < LTV_CAC_PASS:
        verdict = "FAIL"
        notes = [f"LTV/CAC {ltv_cac:.2f}x below minimum {LTV_CAC_PASS}x"]
    elif payback > PAYBACK_CONDITIONAL_MONTHS:
        verdict = "FAIL"
        notes = [f"Payback {payback:.1f}mo exceeds conditional maximum {PAYBACK_CONDITIONAL_MONTHS}mo"]
    elif payback > runway * RUNWAY_PAYBACK_RATIO:
        verdict = "CONDITIONAL PASS"
        notes = [f"Payback ({payback:.1f}mo) exceeds {RUNWAY_PAYBACK_RATIO*100:.0f}% of runway ({runway}mo)"]
    elif payback > PAYBACK_PASS_MONTHS:
        verdict = "CONDITIONAL PASS"
        notes = [f"Payback {payback:.1f}mo above target {target_payback}mo — acceptable but monitor"]
    elif ltv_cac < LTV_CAC_STRONG:
        verdict = "PASS"
        notes = ["LTV/CAC meets minimum but has room to improve"]
    else:
        verdict = "PASS"
        notes = ["All metrics above thresholds"]

    return {
        "label": label,
        "ltv": ltv,
        "ltv_cac": ltv_cac,
        "payback_months": payback,
        "gross_margin_pct": gm_pct,
        "verdict": verdict,
        "notes": notes,
    }


def identify_key_driver(base: dict, scenarios: list[dict]) -> str:
    """Identify which variable most impacts LTV/CAC across scenarios."""
    ltv_cac_base = base["ltv_cac"]
    deltas = {}
    for s in scenarios:
        delta = abs(s["ltv_cac"] - ltv_cac_base)
        deltas[s["label"]] = delta
    if not deltas:
        return "Insufficient scenario data"
    worst = max(deltas, key=lambda k: deltas[k])
    return worst


def score(data: dict) -> str:
    company = data["company"]
    segment = data["segment"]
    ds = data["downside_scenarios"]

    # Base scenario
    base = assess_scenario(
        "Base",
        data["arpu_monthly"],
        data["gross_margin_pct"],
        data["cac"],
        data["churn_rate_monthly_pct"],
        data["runway_months"],
        data["target_payback_months"],
    )

    # Churn stress
    churn_stress = assess_scenario(
        "Churn +{:.0f}pp".format(ds["churn_increase_pp"]),
        data["arpu_monthly"],
        data["gross_margin_pct"],
        data["cac"],
        data["churn_rate_monthly_pct"] + ds["churn_increase_pp"],
        data["runway_months"],
        data["target_payback_months"],
    )

    # CAC inflation stress
    cac_stress = assess_scenario(
        "CAC +{:.0f}%".format(ds["cac_inflation_pct"]),
        data["arpu_monthly"],
        data["gross_margin_pct"],
        data["cac"] * (1 + ds["cac_inflation_pct"] / 100),
        data["churn_rate_monthly_pct"],
        data["runway_months"],
        data["target_payback_months"],
    )

    # Margin compression stress
    margin_stress = assess_scenario(
        "Margin -{:.0f}pp".format(ds["margin_compression_pp"]),
        data["arpu_monthly"],
        data["gross_margin_pct"] - ds["margin_compression_pp"],
        data["cac"],
        data["churn_rate_monthly_pct"],
        data["runway_months"],
        data["target_payback_months"],
    )

    all_scenarios = [base, churn_stress, cac_stress, margin_stress]
    key_driver = identify_key_driver(base, [churn_stress, cac_stress, margin_stress])

    # Overall gate decision
    fail_count = sum(1 for s in all_scenarios if s["verdict"] == "FAIL")
    conditional_count = sum(1 for s in all_scenarios if s["verdict"] == "CONDITIONAL PASS")

    if base["verdict"] == "FAIL":
        gate_verdict = "FAIL"
    elif fail_count >= 2:
        gate_verdict = "FAIL"
    elif fail_count == 1 or base["verdict"] == "CONDITIONAL PASS" or conditional_count >= 2:
        gate_verdict = "CONDITIONAL PASS"
    else:
        gate_verdict = "PASS"

    def scenario_row(s: dict) -> str:
        ltv_str = fmt_usd(s["ltv"]) if s["ltv"] != float("inf") else "∞"
        payback_str = f"{s['payback_months']:.1f}mo" if s["payback_months"] != float("inf") else "∞"
        return (
            f"| {s['label']} | {ltv_str} | {s['ltv_cac']:.2f}x | "
            f"{payback_str} | {fmt_pct(s['gross_margin_pct'])} | {s['verdict']} |"
        )

    # Break-even thresholds
    min_arpu_for_pass = data["cac"] * (data["churn_rate_monthly_pct"] / 100) * LTV_CAC_PASS / (data["gross_margin_pct"] / 100)
    max_cac_for_pass = compute_ltv(data["arpu_monthly"], data["gross_margin_pct"], data["churn_rate_monthly_pct"]) / LTV_CAC_PASS

    conditions_list = []
    for s in all_scenarios:
        for note in s["notes"]:
            if s["verdict"] != "PASS":
                conditions_list.append(f"[{s['label']}] {note}")

    conditions_md = "\n".join(f"{i+1}. {c}" for i, c in enumerate(conditions_list)) if conditions_list else "None"

    monitoring_triggers = [
        f"| Monthly churn exceeds | {fmt_pct(data['churn_rate_monthly_pct'] + ds['churn_increase_pp'])} | Re-run gate |",
        f"| CAC exceeds | {fmt_usd(max_cac_for_pass)} | Re-run gate |",
        f"| Gross margin falls below | {fmt_pct(data['gross_margin_pct'] - ds['margin_compression_pp'])} | Re-run gate |",
        f"| LTV/CAC falls below | {LTV_CAC_PASS}x for 2 consecutive months | Board notification |",
    ]

    lines = [
        f"# Unit Economics Gate Decision: {segment} — {company}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Company | {company} |",
        f"| Segment | {segment} |",
        f"| Gate Decision | {gate_verdict} |",
        f"| Runway | {data['runway_months']} months |",
        f"| Target Payback | {data['target_payback_months']} months |",
        f"| Primary Risk Driver | {key_driver} |",
        f"| Skill | unit-econ-viability-gate |",
        "",
        "## Scenario Analysis",
        "",
        "| Scenario | LTV | LTV/CAC | Payback | Gross Margin | Verdict |",
        "|----------|-----|---------|---------|--------------|---------|",
    ] + [scenario_row(s) for s in all_scenarios] + [
        "",
        "## Break-Even Thresholds",
        "",
        f"- Minimum ARPU for LTV/CAC ≥ {LTV_CAC_PASS}x: **{fmt_usd(min_arpu_for_pass)}/month**",
        f"- Maximum CAC for LTV/CAC ≥ {LTV_CAC_PASS}x: **{fmt_usd(max_cac_for_pass)}**",
        f"- Gross margin floor: **{fmt_pct(GROSS_MARGIN_FLOOR)}**",
        "",
        "## Sensitivity Matrix — LTV/CAC Impact",
        "",
        "| Stress Variable | Change | LTV/CAC Impact | Primary Driver |",
        "|-----------------|--------|----------------|----------------|",
        f"| Monthly churn | +{ds['churn_increase_pp']:.0f}pp | "
        f"{churn_stress['ltv_cac'] - base['ltv_cac']:+.2f}x | "
        f"{'Yes' if key_driver == churn_stress['label'] else 'No'} |",
        f"| CAC | +{ds['cac_inflation_pct']:.0f}% | "
        f"{cac_stress['ltv_cac'] - base['ltv_cac']:+.2f}x | "
        f"{'Yes' if key_driver == cac_stress['label'] else 'No'} |",
        f"| Gross margin | -{ds['margin_compression_pp']:.0f}pp | "
        f"{margin_stress['ltv_cac'] - base['ltv_cac']:+.2f}x | "
        f"{'Yes' if key_driver == margin_stress['label'] else 'No'} |",
        "",
        f"## Gate Decision: {gate_verdict}",
        "",
        "**Conditions and required actions:**",
        conditions_md,
        "",
        "## Monitoring Triggers",
        "",
        "| Trigger | Threshold | Action |",
        "|---------|-----------|--------|",
    ] + monitoring_triggers

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Unit economics viability gate")
    parser.add_argument("-i", "--input", help="Input JSON file (default: stdin)")
    parser.add_argument("-o", "--output", help="Output Markdown file (default: stdout)")
    args = parser.parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    errors = validate_input(data)
    if errors:
        print("Input validation errors:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    output = score(data)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Gate memo written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
