#!/usr/bin/env python3
"""
pricing-finaliser-finance — CFO sign-off on pricing proposals.
Input (JSON via stdin or -i):
  {
    "company": str,
    "product": str,
    "proposed_tiers": [
      {
        "name": str,              # e.g. "Starter", "Growth", "Enterprise"
        "price_monthly": float,
        "cogs_per_unit": float,   # fully-loaded cost to serve per seat/unit
        "expected_mix_pct": float # expected % of new customers on this tier
      }
    ],
    "current_blended_gross_margin_pct": float,
    "target_gross_margin_pct": float,
    "max_discount_pct": float,        # max allowed discount from list price
    "current_arr": float,
    "projected_new_arr_year1": float, # projected ARR from new pricing in Y1
    "churn_risk_pct": float,          # estimated % of existing base at risk of downgrade/churn
    "competitive_price_floor": float  # lowest viable price given competitive dynamics
  }
Output: Pricing sign-off decision as Markdown.
"""

import json
import sys
import argparse

# CFO pricing thresholds
GROSS_MARGIN_HARD_FLOOR = 55.0       # % — below this, REJECTED regardless of other factors
GROSS_MARGIN_SOFT_FLOOR = 65.0       # % — below this, CONDITIONAL
DISCOUNT_HARD_CEILING = 40.0         # % — max ever allowed without CFO override
CHURN_RISK_HARD_CEILING = 15.0       # % — above this triggers conditional at minimum
DOWNSIDE_ADOPTION_HAIRCUT = 0.70     # assume 70% of projected in downside scenario
UPSIDE_ADOPTION_BOOST = 1.20         # assume 120% of projected in upside scenario


def fmt_usd(amount: float) -> str:
    if amount >= 1_000_000:
        return f"${amount/1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount/1_000:.0f}K"
    return f"${amount:.0f}"


def fmt_pct(value: float) -> str:
    return f"{value:.1f}%"


def validate_input(data: dict) -> list[str]:
    required = [
        "company", "product", "proposed_tiers",
        "current_blended_gross_margin_pct", "target_gross_margin_pct",
        "max_discount_pct", "current_arr", "projected_new_arr_year1",
        "churn_risk_pct", "competitive_price_floor"
    ]
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "proposed_tiers" in data:
        mix_total = sum(t.get("expected_mix_pct", 0) for t in data["proposed_tiers"])
        if abs(mix_total - 100) > 1:
            errors.append(f"Tier expected_mix_pct must sum to 100 (got {mix_total:.1f})")
    if "max_discount_pct" in data and data["max_discount_pct"] > DISCOUNT_HARD_CEILING:
        errors.append(
            f"max_discount_pct {data['max_discount_pct']}% exceeds hard ceiling of {DISCOUNT_HARD_CEILING}% — "
            "requires board approval"
        )
    return errors


def compute_blended_margin(tiers: list[dict]) -> float:
    """Weighted average gross margin across tiers by expected mix."""
    total = 0.0
    for tier in tiers:
        price = tier["price_monthly"]
        cogs = tier["cogs_per_unit"]
        mix = tier["expected_mix_pct"] / 100
        margin = ((price - cogs) / price * 100) if price > 0 else 0
        total += margin * mix
    return total


def revenue_scenarios(data: dict) -> dict:
    base = data["projected_new_arr_year1"]
    churn_impact = data["current_arr"] * data["churn_risk_pct"] / 100
    return {
        "upside": base * UPSIDE_ADOPTION_BOOST,
        "base": base,
        "downside": base * DOWNSIDE_ADOPTION_HAIRCUT,
        "churn_at_risk": churn_impact,
        "net_base": base - churn_impact,
        "net_downside": base * DOWNSIDE_ADOPTION_HAIRCUT - churn_impact,
    }


def determine_verdict(
    blended_margin: float,
    target_margin: float,
    churn_risk: float,
    max_discount: float,
    min_tier_margin: float,
) -> tuple[str, list[str]]:
    conditions = []
    hard_block = False

    if blended_margin < GROSS_MARGIN_HARD_FLOOR:
        hard_block = True
        conditions.append(
            f"Blended gross margin {fmt_pct(blended_margin)} is below hard floor "
            f"of {fmt_pct(GROSS_MARGIN_HARD_FLOOR)} — pricing is not viable"
        )

    if min_tier_margin < GROSS_MARGIN_HARD_FLOOR:
        hard_block = True
        conditions.append(
            f"At least one tier has gross margin below hard floor of "
            f"{fmt_pct(GROSS_MARGIN_HARD_FLOOR)} — restructure before approval"
        )

    if hard_block:
        return "REJECTED", conditions

    if blended_margin < GROSS_MARGIN_SOFT_FLOOR:
        conditions.append(
            f"Blended margin {fmt_pct(blended_margin)} is below target {fmt_pct(target_margin)} — "
            "must define a path to margin recovery (e.g. COGS reduction roadmap)"
        )

    if churn_risk > CHURN_RISK_HARD_CEILING:
        conditions.append(
            f"Churn risk {fmt_pct(churn_risk)} exceeds threshold {fmt_pct(CHURN_RISK_HARD_CEILING)} — "
            "must have a migration/grandfathering plan for existing customers"
        )

    if max_discount > 25:
        conditions.append(
            f"Discount ceiling {fmt_pct(max_discount)} is high — require sales manager approval "
            "for all discounts above 20%"
        )

    if conditions:
        return "APPROVED WITH CONDITIONS", conditions

    return "APPROVED", []


def score(data: dict) -> str:
    tiers = data["proposed_tiers"]
    blended_margin = compute_blended_margin(tiers)
    tier_margins = [
        ((t["price_monthly"] - t["cogs_per_unit"]) / t["price_monthly"] * 100)
        for t in tiers if t["price_monthly"] > 0
    ]
    min_tier_margin = min(tier_margins) if tier_margins else 0

    scenarios = revenue_scenarios(data)
    verdict, conditions = determine_verdict(
        blended_margin,
        data["target_gross_margin_pct"],
        data["churn_risk_pct"],
        data["max_discount_pct"],
        min_tier_margin,
    )

    tier_table = "\n".join(
        f"| {t['name']} | {fmt_usd(t['price_monthly'])}/mo | "
        f"{fmt_usd(t['cogs_per_unit'])}/mo | "
        f"{fmt_pct((t['price_monthly'] - t['cogs_per_unit']) / t['price_monthly'] * 100 if t['price_monthly'] > 0 else 0)} | "
        f"{fmt_pct(t['expected_mix_pct'])} |"
        for t in tiers
    )

    conditions_md = (
        "\n".join(f"{i+1}. {c}" for i, c in enumerate(conditions))
        if conditions else "None"
    )

    verdict_display = f"**{verdict}**"

    lines = [
        f"# Pricing Sign-Off Memo: {data['product']} — {data['company']}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Company | {data['company']} |",
        f"| Product | {data['product']} |",
        f"| Decision | {verdict} |",
        f"| Current ARR | {fmt_usd(data['current_arr'])} |",
        f"| Target Gross Margin | {fmt_pct(data['target_gross_margin_pct'])} |",
        f"| Skill | pricing-finaliser-finance |",
        "",
        "## Proposed Pricing Tiers",
        "",
        "| Tier | Price | COGS | Gross Margin | Expected Mix |",
        "|------|-------|------|--------------|--------------|",
        tier_table,
        "",
        f"**Blended gross margin**: {fmt_pct(blended_margin)} "
        f"(target: {fmt_pct(data['target_gross_margin_pct'])}, "
        f"floor: {fmt_pct(GROSS_MARGIN_HARD_FLOOR)})",
        "",
        "## Margin Impact Analysis",
        "",
        f"- Blended gross margin at proposed pricing: **{fmt_pct(blended_margin)}**",
        f"- Current blended gross margin: **{fmt_pct(data['current_blended_gross_margin_pct'])}**",
        f"- Margin delta: **{fmt_pct(blended_margin - data['current_blended_gross_margin_pct'])}** "
        f"({'improvement' if blended_margin >= data['current_blended_gross_margin_pct'] else 'degradation'})",
        f"- Lowest tier gross margin: **{fmt_pct(min_tier_margin)}**",
        "",
        "## Revenue Scenarios",
        "",
        "| Scenario | New ARR | Churn at Risk | Net ARR Impact |",
        "|----------|---------|---------------|----------------|",
        f"| Upside | {fmt_usd(scenarios['upside'])} | {fmt_usd(scenarios['churn_at_risk'])} | {fmt_usd(scenarios['upside'] - scenarios['churn_at_risk'])} |",
        f"| Base | {fmt_usd(scenarios['base'])} | {fmt_usd(scenarios['churn_at_risk'])} | {fmt_usd(scenarios['net_base'])} |",
        f"| Downside | {fmt_usd(scenarios['downside'])} | {fmt_usd(scenarios['churn_at_risk'])} | {fmt_usd(scenarios['net_downside'])} |",
        "",
        "## Discount Policy",
        "",
        f"- Maximum discount ceiling: **{fmt_pct(data['max_discount_pct'])}**",
        f"- Competitive price floor: **{fmt_usd(data['competitive_price_floor'])}/month**",
        f"- Churn risk on existing base: **{fmt_pct(data['churn_risk_pct'])}** of current ARR ({fmt_usd(scenarios['churn_at_risk'])})",
        "",
        "## CFO Decision",
        "",
        f"### {verdict_display}",
        "",
        "**Conditions:**",
        conditions_md,
        "",
        "## Monitoring Triggers",
        "",
        "| Trigger | Threshold | Action |",
        "|---------|-----------|--------|",
        f"| Blended margin drops below | {fmt_pct(GROSS_MARGIN_SOFT_FLOOR)} | Immediate CFO review |",
        f"| Discount utilization exceeds | {fmt_pct(data['max_discount_pct'] * 0.8)} | Flag to sales leadership |",
        f"| Churn rate on migrated accounts exceeds | {fmt_pct(CHURN_RISK_HARD_CEILING)} | Emergency pricing review |",
        f"| Tier mix shifts more than | 15pp from projections | Reforecast and CFO update |",
    ]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="CFO pricing sign-off")
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
        print(f"Sign-off memo written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
