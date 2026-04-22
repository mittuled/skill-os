---
name: cs-health-monitor
description: >
  This skill monitors the health of the customer portfolio using usage, NPS,
  and support signal data. Use when asked to track customer health, identify
  at-risk accounts, or build health score dashboards. Also consider when churn
  is increasing without early warning. Suggest when the user manages accounts
  without a systematic health scoring framework.
department: customer-success
agent: cs-manager
version: 1.0.0
complexity: medium
related-skills:
  - sla-definer-cs
  - expansion-motion-designer-cs
  - cs-signal-extractor
triggers:
  - "customer health"
  - "health-score-monitor"
  - "CS health score"
  - "churn risk"
---

# cs-health-monitor

## Agent: CS Manager

L2 customer success manager (1x) responsible for CS cohort selection, release readiness, health monitoring, and case study extraction.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Monitors the health of the customer portfolio using usage metrics, NPS scores, and support signal data to identify at-risk accounts and expansion opportunities.

## When to Use

- When the CS team needs a systematic way to monitor customer health across the portfolio.
- When churn is increasing and the team needs early warning indicators to intervene before cancellation.
- When periodic health reviews are due and portfolio-level trends need analysis.

## Workflow

1. **Define Health Score Model**: Establish the health score components: product usage metrics (login frequency, feature adoption, usage depth), sentiment signals (NPS, CSAT, support ticket sentiment), and engagement indicators (QBR attendance, response times). Define weights and thresholds. Deliverable: health score model specification.
2. **Collect Health Data**: Aggregate data from product analytics, NPS surveys, support systems, and CSM notes. Ensure data freshness and completeness. Deliverable: consolidated health dataset per account.
3. **Calculate and Classify**: Compute health scores per account. Classify into health tiers: healthy, at-risk, and critical. Deliverable: health scorecard with tier assignments.
4. **Analyze Portfolio Trends**: Identify portfolio-level patterns -- declining segments, common risk factors, and improvement trends. Deliverable: portfolio health trend analysis.
5. **Trigger Interventions**: For at-risk and critical accounts, trigger appropriate interventions: CSM outreach, executive sponsor engagement, or product support escalation. Deliverable: intervention assignments with priority and timeline.

## Anti-Patterns

- **Lagging indicators only**: Building health scores entirely from outcomes (churn, ticket volume) rather than leading indicators (usage decline, engagement drop). *Why*: by the time lagging indicators fire, the customer has already decided to leave; leading indicators enable proactive intervention.
- **Score without action**: Computing health scores without defined intervention playbooks for each tier. *Why*: knowing an account is at-risk is useless without a clear response; scores must trigger action.
- **Ignoring qualitative signals**: Relying solely on quantitative data without incorporating CSM observations and customer sentiment. *Why*: data captures behavior but misses context; a customer may show healthy usage while internally planning a competitor migration.

## Output

**On success**: Produces a portfolio health report containing per-account health scores, tier classifications, portfolio trend analysis, and intervention assignments. Delivered to CSMs and the Head of Customer Success.

**On failure**: Report which accounts could not be scored (missing data, incomplete integrations), what partial health picture was assembled, and what data sources need to be connected.

## Related Skills

- [`sla-definer-cs`](../../../customer-success/head-of-customer-success/sla-definer-cs/SKILL.md) -- SLA adherence is a component of health scoring.
- [`expansion-motion-designer-cs`](../../../customer-success/head-of-customer-success/expansion-motion-designer-cs/SKILL.md) -- Healthy accounts with expansion signals feed into the expansion motion.
- [`cs-signal-extractor`](../../../customer-success/customer-success-manager/cs-signal-extractor/SKILL.md) -- Qualitative signals from CSM interactions supplement health score data.
