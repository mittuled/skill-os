---
name: revenue-impact-monitor
description: >
  This skill monitors the revenue impact of product, pricing, and operational changes.
  Use when asked to track how a recent change affected revenue, quantify the ARR impact
  of a product launch or pricing adjustment, or set up revenue impact monitoring for a
  new initiative. Also consider when changes ship without a baseline revenue measurement.
  Suggest when the user is launching changes without a plan to measure revenue impact.
department: finance
agent: finance-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../../fpa-analyst/monthly-variance-analyser/SKILL.md
  - ../north-star-metric-reviewer-finance/SKILL.md
---

# revenue-impact-monitor

## Agent: Finance Manager

L2 finance manager (1x) responsible for business model review, financial risk assessment, revenue impact monitoring, and north star metric oversight.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Monitors the revenue impact of product, pricing, and operational changes by establishing baselines, tracking actuals, and attributing revenue movements to specific initiatives.

## When to Use

- When a product launch, pricing change, or operational initiative needs ongoing revenue impact tracking.
- When monthly actuals show unexpected revenue movement and the source needs attribution to specific changes.
- When leadership requests a retrospective on the financial impact of a completed initiative.

## Workflow

1. **Baseline Establishment**: Define the pre-change revenue baseline using trailing 3-month averages for MRR, ARR, ARPU, and expansion/contraction rates. Document the expected impact from the financial model. Deliverable: baseline snapshot with expected impact range.
2. **Monitoring Framework Setup**: Define the metrics to track, measurement frequency, attribution methodology (cohort-based, A/B, before/after), and reporting cadence. Identify confounding variables that could distort attribution. Deliverable: monitoring plan with attribution methodology.
3. **Periodic Measurement**: Measure actual revenue impact at defined intervals (weekly for first month, monthly thereafter). Decompose revenue movement into change-attributed and organic components. Deliverable: revenue impact report with attribution breakdown.
4. **Variance Investigation**: When actual impact deviates from expected by more than 10%, investigate root causes. Distinguish between timing effects, adoption curve lag, and genuine underperformance. Deliverable: variance analysis with root cause findings.
5. **Impact Summary**: At the defined evaluation point, produce a final impact assessment comparing actual vs. expected revenue impact with lessons learned for future initiatives. Deliverable: initiative impact summary with recommendation for continuation, adjustment, or rollback.

## Anti-Patterns

- **Missing baseline**: Starting to measure revenue impact after the change has already shipped without a pre-change baseline. *Why*: without a clean baseline, attribution becomes guesswork and the impact assessment loses credibility.
- **Correlation as causation**: Attributing all revenue movement in the post-change period to the initiative without controlling for seasonality, market trends, or concurrent changes. *Why*: false attribution leads to doubling down on ineffective initiatives or killing effective ones.
- **Monitoring without action triggers**: Tracking revenue impact as a reporting exercise without defining thresholds that trigger intervention (scale up, adjust, or roll back). *Why*: monitoring without response capability turns finance into a spectator rather than a strategic partner.

## Output

**On success**: Produces a revenue impact report containing the baseline comparison, attribution breakdown, variance analysis, and initiative impact summary. Delivered to the CFO, product leadership, and the initiative owner.

**On failure**: Report which metrics could not be measured (e.g., attribution impossible due to concurrent changes), what partial measurement was achieved, and what must change for future initiatives to be measurable. Include recommendations for improving impact measurement infrastructure.

## Related Skills

- [`monthly-variance-analyser`](../../fpa-analyst/monthly-variance-analyser/SKILL.md) -- Provides the broader variance context that revenue impact monitoring feeds into.
- [`north-star-metric-reviewer-finance`](../north-star-metric-reviewer-finance/SKILL.md) -- Evaluates whether revenue impact aligns with the company's north star metric trajectory.
