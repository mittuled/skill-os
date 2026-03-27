---
name: pricing-review-runner
description: >
  This skill runs periodic pricing reviews to assess whether pricing remains competitive
  and margin-accretive. Use when asked to evaluate current pricing effectiveness, benchmark
  against competitors, or assess whether a price increase is warranted. Also consider when
  margins are declining without a recent pricing review. Suggest when the user is adjusting
  pricing without data on competitive positioning or margin impact.
department: finance
agent: fpa-analyst
version: 1.0.0
complexity: medium
related-skills:
  - ../../cfo-vp-finance/pricing-finaliser-finance/SKILL.md
  - ../unit-economics-monitor/SKILL.md
---

# pricing-review-runner

## Agent: FP&A Analyst

L2 FP&A analyst (1x) responsible for budgeting, forecasting, variance analysis, board reporting, fundraising models, and SaaS metrics.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Runs periodic pricing reviews to assess whether current pricing remains competitive, margin-accretive, and aligned with the company's value delivery and growth targets.

## When to Use

- When the quarterly or semi-annual pricing review cycle is due.
- When gross margin has declined for two or more consecutive months without a known cause.
- When competitive intelligence suggests significant pricing changes by key competitors.

## Workflow

1. **Performance Data Collection**: Pull pricing-relevant data: ACV by tier, discount frequency and depth, win/loss rates by price point, gross margin by product line, and expansion/contraction revenue by cohort. Deliverable: pricing performance data package.
2. **Competitive Benchmarking**: Compare current pricing against 3-5 direct competitors on a feature-adjusted basis. Identify where the company is priced above, at, or below market. Deliverable: competitive pricing matrix with feature mapping.
3. **Margin Analysis**: Calculate gross margin and contribution margin by tier, segment, and deal size. Identify which pricing structures are margin-accretive and which are dilutive. Deliverable: margin analysis by pricing dimension.
4. **Willingness-to-Pay Assessment**: Synthesize signals from sales (deal velocity at different price points, objection frequency), customer success (NPS by tier, churn by price sensitivity), and product (feature utilization by tier). Deliverable: willingness-to-pay summary with confidence levels.
5. **Recommendation Package**: Produce pricing adjustment recommendations with modelled revenue and margin impact for each change. Include implementation considerations (grandfathering, rollout timing, contract implications). Deliverable: pricing review report with recommendations and impact models.

## Anti-Patterns

- **Cost-plus pricing without value context**: Setting prices based solely on cost structure without considering perceived value or competitive positioning. *Why*: cost-plus pricing leaves money on the table in segments where value exceeds cost and prices out segments where it does not.
- **Reviewing pricing without win/loss data**: Evaluating pricing competitiveness without input from sales on how pricing affects deal outcomes. *Why*: financial analysis alone cannot capture buyer psychology; pricing that looks optimal on a spreadsheet may be losing deals in the field.
- **Annual-only reviews**: Reviewing pricing only during the annual planning cycle rather than on a continuous or quarterly basis. *Why*: markets move faster than annual cycles; delayed pricing adjustments compound in lost revenue or eroded margins.

## Output

**On success**: Produces a pricing review report containing performance analysis, competitive benchmarking, margin analysis, willingness-to-pay assessment, and recommendation package with impact models. Delivered to the CFO and pricing committee.

**On failure**: Report which data inputs were unavailable (e.g., no competitive pricing data, incomplete win/loss records), what partial analysis was possible, and what data collection processes need improvement for future reviews.

## Related Skills

- [`pricing-finaliser-finance`](../../cfo-vp-finance/pricing-finaliser-finance/SKILL.md) -- Provides the CFO sign-off on pricing changes recommended by this review.
- [`unit-economics-monitor`](../unit-economics-monitor/SKILL.md) -- Supplies the unit economics context that informs pricing sustainability.
