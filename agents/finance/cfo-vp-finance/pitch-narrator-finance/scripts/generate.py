#!/usr/bin/env python3
"""
pitch-narrator-finance — Generate financial pitch narrative for investor decks.
Input (JSON via stdin or -i):
  {
    "company": str,
    "round": str,           # "Seed", "Series A", "Series B", etc.
    "raise_amount": float,  # USD
    "arr": float,
    "arr_growth_rate": float,  # annual %, e.g. 150 for 150%
    "mrr": float,
    "gross_margin_pct": float,  # e.g. 72 for 72%
    "burn_rate": float,         # monthly USD
    "runway_months": int,
    "ltv_cac": float,           # e.g. 3.2
    "cac_payback_months": int,
    "nrr": float,               # net revenue retention %, e.g. 115
    "use_of_proceeds": {        # category -> % allocation
      "Engineering": 40,
      "Sales & Marketing": 35,
      "G&A": 15,
      "Product": 10
    },
    "path_to_profitability_months": int,
    "key_customers": int,
    "logo_customers": list[str]  # optional notable names
  }
Output: Financial pitch narrative as Markdown.
"""

import json
import sys
import argparse
from typing import Any

# Investor benchmark thresholds by round (Bessemer Venture Partners / a16z data)
ROUND_BENCHMARKS = {
    "Seed": {
        "arr_min": 0,
        "arr_target": 1_000_000,
        "growth_rate_good": 100,   # % YoY
        "gross_margin_good": 60,
        "ltv_cac_good": 2.5,
        "payback_good": 24,        # months
        "nrr_good": 100,
    },
    "Series A": {
        "arr_min": 1_000_000,
        "arr_target": 3_000_000,
        "growth_rate_good": 150,
        "gross_margin_good": 65,
        "ltv_cac_good": 3.0,
        "payback_good": 18,
        "nrr_good": 105,
    },
    "Series B": {
        "arr_min": 5_000_000,
        "arr_target": 15_000_000,
        "growth_rate_good": 100,
        "gross_margin_good": 70,
        "ltv_cac_good": 3.5,
        "payback_good": 14,
        "nrr_good": 110,
    },
    "Series C": {
        "arr_min": 20_000_000,
        "arr_target": 50_000_000,
        "growth_rate_good": 75,
        "gross_margin_good": 72,
        "ltv_cac_good": 4.0,
        "payback_good": 12,
        "nrr_good": 115,
    },
}

METRIC_SIGNAL_THRESHOLDS = {
    "nrr": {"strong": 120, "good": 105, "weak": 95},
    "gross_margin": {"strong": 75, "good": 65, "weak": 55},
    "ltv_cac": {"strong": 4.0, "good": 3.0, "weak": 2.0},
    "growth_rate": {"strong": 200, "good": 100, "weak": 50},
}


def fmt_usd(amount: float) -> str:
    if amount >= 1_000_000_000:
        return f"${amount/1_000_000_000:.1f}B"
    elif amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.0f}K"
    return f"${amount:.0f}"


def signal_label(metric: str, value: float) -> str:
    t = METRIC_SIGNAL_THRESHOLDS.get(metric)
    if not t:
        return "—"
    if value >= t["strong"]:
        return "STRONG"
    elif value >= t["good"]:
        return "GOOD"
    elif value >= t["weak"]:
        return "WEAK"
    return "AT RISK"


def validate_input(data: dict) -> list[str]:
    required = [
        "company", "round", "raise_amount", "arr", "arr_growth_rate",
        "mrr", "gross_margin_pct", "burn_rate", "runway_months",
        "ltv_cac", "cac_payback_months", "nrr", "use_of_proceeds",
        "path_to_profitability_months", "key_customers"
    ]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "round" in data and data["round"] not in ROUND_BENCHMARKS:
        known = list(ROUND_BENCHMARKS.keys())
        errors.append(f"Unknown round '{data['round']}'. Use one of: {known}")
    if "use_of_proceeds" in data:
        total_pct = sum(data["use_of_proceeds"].values())
        if abs(total_pct - 100) > 1:
            errors.append(f"use_of_proceeds must sum to 100% (got {total_pct}%)")
    return errors


def assess_metric_strength(data: dict, benchmarks: dict) -> dict:
    assessments = {}

    # Growth rate
    gr = data["arr_growth_rate"]
    bench_gr = benchmarks["growth_rate_good"]
    assessments["arr_growth"] = {
        "value": f"{gr:.0f}%",
        "benchmark": f"{bench_gr:.0f}%",
        "signal": signal_label("growth_rate", gr),
    }

    # Gross margin
    gm = data["gross_margin_pct"]
    bench_gm = benchmarks["gross_margin_good"]
    assessments["gross_margin"] = {
        "value": f"{gm:.0f}%",
        "benchmark": f"{bench_gm:.0f}%",
        "signal": signal_label("gross_margin", gm),
    }

    # LTV/CAC
    ltv_cac = data["ltv_cac"]
    bench_ltv = benchmarks["ltv_cac_good"]
    assessments["ltv_cac"] = {
        "value": f"{ltv_cac:.1f}x",
        "benchmark": f"{bench_ltv:.1f}x",
        "signal": signal_label("ltv_cac", ltv_cac),
    }

    # NRR
    nrr = data["nrr"]
    bench_nrr = benchmarks["nrr_good"]
    assessments["nrr"] = {
        "value": f"{nrr:.0f}%",
        "benchmark": f"{bench_nrr:.0f}%",
        "signal": signal_label("nrr", nrr),
    }

    # CAC Payback
    payback = data["cac_payback_months"]
    bench_payback = benchmarks["payback_good"]
    payback_signal = "STRONG" if payback <= bench_payback * 0.7 else \
                     "GOOD" if payback <= bench_payback else \
                     "WEAK" if payback <= bench_payback * 1.5 else "AT RISK"
    assessments["cac_payback"] = {
        "value": f"{payback} months",
        "benchmark": f"≤{bench_payback} months",
        "signal": payback_signal,
    }

    return assessments


def identify_narrative_strengths(assessments: dict) -> list[str]:
    strengths = []
    for metric, info in assessments.items():
        if info["signal"] in ("STRONG", "GOOD"):
            label = metric.replace("_", " ").title()
            strengths.append(f"{label} ({info['value']})")
    return strengths


def identify_narrative_risks(assessments: dict) -> list[str]:
    risks = []
    for metric, info in assessments.items():
        if info["signal"] in ("WEAK", "AT RISK"):
            label = metric.replace("_", " ").title()
            risks.append(f"{label} ({info['value']}) — benchmark: {info['benchmark']}")
    return risks


def generate(data: dict) -> str:
    company = data["company"]
    round_name = data["round"]
    benchmarks = ROUND_BENCHMARKS[round_name]
    assessments = assess_metric_strength(data, benchmarks)
    strengths = identify_narrative_strengths(assessments)
    risks = identify_narrative_risks(assessments)

    arr_at_eoy = data["arr"] * (1 + data["arr_growth_rate"] / 100)
    proceeds_table = "\n".join(
        f"| {cat} | {pct}% | {fmt_usd(data['raise_amount'] * pct / 100)} |"
        for cat, pct in data["use_of_proceeds"].items()
    )
    logos = ", ".join(data.get("logo_customers", [])) or "—"

    risk_bullets = "\n".join(f"- {r}" for r in risks) if risks else "- No material risks identified against benchmarks"
    strength_bullets = "\n".join(f"- {s}" for s in strengths)

    lines = [
        f"# Financial Pitch Narrative: {company} — {round_name}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Company | {company} |",
        f"| Round | {round_name} |",
        f"| Raise Amount | {fmt_usd(data['raise_amount'])} |",
        f"| As-of Date | Current |",
        f"| Skill | pitch-narrator-finance |",
        "",
        "## Validated Metric Snapshot",
        "",
        "| Metric | Value | Benchmark | Signal |",
        "|--------|-------|-----------|--------|",
    ]
    for metric, info in assessments.items():
        label = metric.replace("_", " ").title()
        lines.append(f"| {label} | {info['value']} | {info['benchmark']} | {info['signal']} |")

    lines += [
        "",
        "### Current Traction",
        f"- **ARR**: {fmt_usd(data['arr'])} growing at {data['arr_growth_rate']:.0f}% YoY",
        f"- **MRR**: {fmt_usd(data['mrr'])}",
        f"- **Key customers**: {data['key_customers']}",
        f"- **Logo customers**: {logos}",
        "",
        "## Financial Narrative Outline",
        "",
        "### 1. Where We Are Today (Traction Proof)",
        f"{company} has reached {fmt_usd(data['arr'])} ARR, growing at {data['arr_growth_rate']:.0f}% year-over-year with "
        f"{data['key_customers']} paying customers. Gross margin of {data['gross_margin_pct']:.0f}% is consistent with "
        f"a scalable SaaS model. Net Revenue Retention of {data['nrr']:.0f}% demonstrates that existing customers are "
        "expanding their usage — the product is delivering measurable value.",
        "",
        "### 2. Where We Are Going (Growth Trajectory)",
        f"At current growth rates, {company} will exit the year at approximately {fmt_usd(arr_at_eoy)} ARR. "
        f"This {round_name} raise of {fmt_usd(data['raise_amount'])} is sized to fund {data['path_to_profitability_months']} months "
        f"of operations at the current burn rate of {fmt_usd(data['burn_rate'])}/month, extending runway to "
        f"{data['runway_months']} months and providing a clear path to the next financing milestone.",
        "",
        "### 3. Why The Economics Work (Unit Economics)",
        f"LTV/CAC of {data['ltv_cac']:.1f}x with a {data['cac_payback_months']}-month payback period confirms that each new "
        f"customer generates substantial long-term value relative to acquisition cost. At {data['gross_margin_pct']:.0f}% gross margin, "
        "contribution margin expansion is achievable as the business scales and CAC amortizes.",
        "",
        "## Finance Slide Content",
        "",
        "### Slide: Revenue Trajectory",
        f"- ARR today: **{fmt_usd(data['arr'])}**",
        f"- YoY growth: **{data['arr_growth_rate']:.0f}%**",
        f"- Projected ARR (EOY): **{fmt_usd(arr_at_eoy)}**",
        f"- MRR: **{fmt_usd(data['mrr'])}**",
        "",
        "### Slide: Unit Economics",
        f"- Gross Margin: **{data['gross_margin_pct']:.0f}%**",
        f"- LTV/CAC: **{data['ltv_cac']:.1f}x**",
        f"- CAC Payback: **{data['cac_payback_months']} months**",
        f"- Net Revenue Retention: **{data['nrr']:.0f}%**",
        "",
        "### Slide: Use of Proceeds",
        "",
        f"| Category | Allocation | Amount |",
        "|----------|-----------|--------|",
        proceeds_table,
        "",
        "### Slide: Path to Next Milestone",
        f"- Current runway: **{data['runway_months']} months**",
        f"- Monthly burn: **{fmt_usd(data['burn_rate'])}**",
        f"- Path to profitability: **{data['path_to_profitability_months']} months** (conditional on plan execution)",
        "",
        "## Narrative Strengths",
        strength_bullets if strengths else "- No metrics above benchmark thresholds",
        "",
        "## Narrative Risks (Investor Q&A Preparation)",
        risk_bullets,
        "",
        "## Assumption Appendix",
        "",
        "| Assumption | Value | Source |",
        "|-----------|-------|--------|",
        f"| ARR Growth Rate | {data['arr_growth_rate']:.0f}% | Finance model |",
        f"| Gross Margin | {data['gross_margin_pct']:.0f}% | P&L actuals |",
        f"| Monthly Burn Rate | {fmt_usd(data['burn_rate'])} | Finance model |",
        f"| LTV/CAC Ratio | {data['ltv_cac']:.1f}x | CRM + finance model |",
        f"| CAC Payback Period | {data['cac_payback_months']} months | CRM + finance model |",
        f"| Net Revenue Retention | {data['nrr']:.0f}% | Billing system |",
        "",
        "## CFO Sign-Off Checklist",
        "",
        "- [ ] All metrics traced to approved financial model (as-of date confirmed)",
        "- [ ] Projections based on bottoms-up assumptions (sales capacity, conversion rates, ACV)",
        "- [ ] No non-standard metric calculations — definitions match SaaS Capital / Bessemer conventions",
        "- [ ] Use of proceeds allocations match board-approved budget",
        "- [ ] Assumption appendix ready for investor diligence",
        "- [ ] Q&A responses prepared for all AT RISK and WEAK metrics",
    ]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate financial pitch narrative")
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

    output = generate(data)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Narrative written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
