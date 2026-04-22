---
name: customer-community-health-reviewer
description: >
  This skill reviews customer community health and recommends interventions to
  improve engagement. Use when asked to assess community engagement, diagnose
  declining participation, or plan community growth. Also consider when the
  community is quiet despite a growing customer base. Suggest when the user
  launches a community without a health monitoring plan.
department: customer-success
agent: customer-programs-manager
version: 1.0.0
complexity: simple
related-skills:
  - nps-programme-manager
  - customer-advisory-board-runner
  - cs-health-monitor
triggers:
  - "community health review"
  - "review community health"
  - "community engagement audit"
  - "check community metrics"
  - "community health"
---

# customer-community-health-reviewer

## Agent: Customer Programs Manager

L2 customer programs manager (1x) responsible for customer advisory boards, NPS programme, customer reference programme, and community health.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Reviews customer community health and recommends interventions to improve engagement, retention, and peer-to-peer value exchange.

## When to Use

- When community engagement metrics need periodic review to assess health and identify issues.
- When community participation is declining and root causes need diagnosis.
- When planning community programmes and interventions need to be data-informed.

## Workflow

1. **Collect Community Metrics**: Gather data on active members, post frequency, response rates, new member onboarding, and churn. Deliverable: community metrics dashboard.
2. **Assess Health Indicators**: Evaluate metrics against health thresholds. Identify trends -- growing, stable, or declining engagement. Deliverable: community health assessment.
3. **Diagnose Issues**: For declining indicators, investigate root causes: content staleness, lack of moderation, unresolved questions, or insufficient value for members. Deliverable: issue diagnosis with root causes.
4. **Recommend Interventions**: Propose specific actions: content programmes, engagement campaigns, moderation improvements, or community events. Deliverable: intervention plan with expected impact.

## Anti-Patterns

- **Measuring vanity metrics**: Tracking member count without measuring active participation and value exchange. *Why*: a large community with no engagement provides no value; health is measured by activity, not size.
- **Top-down content only**: Relying entirely on company-produced content without fostering peer-to-peer exchange. *Why*: communities thrive when members help each other; company-only content creates a broadcast channel, not a community.
- **Ignoring negative signals**: Dismissing complaints or declining engagement as normal fluctuation. *Why*: community sentiment is a leading indicator of broader customer satisfaction; ignoring it misses early warnings.

## Output

**On success**: Produces a community health report with metrics, trend analysis, issue diagnosis, and an intervention plan. Delivered to the Head of Customer Success and marketing.

**On failure**: Report which metrics could not be collected (missing analytics, inaccessible data), what partial assessment was done, and what tooling is needed.

## Related Skills

- [`nps-programme-manager`](../nps-programme-manager/SKILL.md) -- Community sentiment correlates with NPS trends.
- [`customer-advisory-board-runner`](../customer-advisory-board-runner/SKILL.md) -- CAB members often seed community engagement.
- [`cs-health-monitor`](../../../customer-success/cs-manager/cs-health-monitor/SKILL.md) -- Community engagement can be a health score component.
