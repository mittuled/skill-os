---
name: adoption-tracker
description: >
  This skill tracks user adoption metrics against targets and flags underperformance requiring intervention.
  Use when a feature or product has launched and adoption needs monitoring against defined success criteria.
  Also consider when stakeholders ask whether a rollout is on track or when weekly adoption numbers are due.
  Suggest when a launch has completed but no one has checked adoption trends in the past reporting cycle.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "track adoption"
  - "monitor adoption"
  - "adoption metrics"
  - "feature adoption"
  - "user adoption tracking"
---

# adoption-tracker

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description
Tracks user adoption metrics against targets and flags underperformance requiring intervention.

## When to Use
- When a feature or product has launched and adoption targets were set during planning
- When a reporting cycle (daily, weekly, or milestone-based) requires an adoption status update
- When a stakeholder raises concern about whether users are actually engaging with a shipped feature
- When adoption appears stalled and the team needs data to decide between iterating, promoting, or deprecating

## Workflow
1. **Identify the adoption targets**: Pull the success criteria defined during launch planning — activation rate, DAU/WAU/MAU thresholds, or feature-specific engagement metrics. Confirm the measurement window and cohort scope. Deliverable: adoption target summary with metric names, baselines, targets, and reporting cadence.
2. **Collect current adoption data**: Query the analytics pipeline for actual adoption numbers across the defined metrics. Segment by cohort, plan tier, or geography as specified in the rollout plan. Deliverable: raw adoption data table with current values per metric per segment.
3. **Compare actuals to targets**: Calculate variance for each metric — percentage above or below target. Flag any metric where variance exceeds the threshold defined in the rollout plan (default: 15% below target). Deliverable: variance report with red/amber/green status per metric.
4. **Diagnose underperformance**: For any metric flagged red or amber, investigate contributing factors — onboarding drop-off, discoverability gaps, cohort-specific issues, or external timing factors. Cross-reference support tickets and feedback signals. Deliverable: root-cause hypothesis for each underperforming metric.
5. **Produce the adoption report**: Assemble findings into a structured report covering current status, trend direction, underperformance diagnoses, and recommended actions. Route to the product manager and relevant stakeholders. Deliverable: adoption tracking report with status summary, trend data, and action recommendations.
6. **Set the next check-in**: Confirm the next reporting date and any updated thresholds based on stakeholder feedback. Deliverable: calendar entry or task for the next adoption check.

## Anti-Patterns
- **Tracking vanity metrics instead of adoption signals**: Reporting page views or logins when the real question is whether users completed the target action. *Why*: Vanity metrics create false confidence — a feature can have high traffic but zero meaningful adoption if users visit and bounce.
- **Reporting numbers without diagnosis**: Delivering a dashboard of red metrics without investigating why they are red. *Why*: Data without interpretation forces stakeholders to guess, leading to reactive decisions or paralysis.
- **Ignoring cohort differences**: Reporting a single aggregate number when adoption varies dramatically by segment. *Why*: Aggregate success can mask critical failures in key cohorts (e.g., enterprise customers not adopting while free-tier users inflate the average).
- **Waiting too long to flag underperformance**: Collecting multiple cycles of below-target data before raising it. *Why*: Early intervention windows close quickly — the sooner the team knows, the more options remain for course correction.

## Output
**On success**: An adoption tracking report containing metric-by-metric status (green/amber/red), trend direction, segment breakdowns, root-cause hypotheses for any underperformance, and prioritised action recommendations — formatted for inclusion in a product review or stakeholder update.
**On failure**: Report which data sources were unavailable or which targets were undefined, what partial data was collected, and recommend specific steps to unblock (e.g., "analytics event not instrumented for feature X — coordinate with engineering to add tracking").

## Related Skills
- (none yet — cross-references added in Phase 1.6)
