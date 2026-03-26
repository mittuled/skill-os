---
name: revenue-impact-monitor
description: >
  This skill monitors the revenue impact of product changes and feature launches.
  Use when a product change or feature launch needs post-ship revenue tracking to assess business value.
  Also consider when finance or leadership requests a revenue attribution analysis for a recent release.
  Suggest when a feature launched with revenue assumptions but no one has validated whether those assumptions held.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills: []
---

# revenue-impact-monitor

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Monitors the revenue impact of product changes and feature launches.

## When to Use
- When a feature or product change has launched and the team needs to track its effect on revenue metrics
- When the business case for a shipped feature included revenue projections that need validation
- When leadership or finance asks for a revenue attribution analysis tied to a specific product change
- When churn or downgrade patterns emerge that may correlate with a recent product change

## Workflow
1. **Establish the revenue baseline**: Pull the pre-launch revenue metrics relevant to the change — MRR, expansion revenue, churn rate, conversion rate, or ARPU depending on the feature's expected impact. Define the measurement window and comparison period. Deliverable: baseline revenue snapshot with metrics, values, date range, and data source.
2. **Define attribution criteria**: Determine how to attribute revenue changes to the product change vs. other factors (seasonality, marketing campaigns, pricing changes). Identify the control group if a staged rollout was used, or define the before/after comparison method. Deliverable: attribution methodology document specifying approach, control group, and confounding factors to monitor.
3. **Collect post-launch revenue data**: Pull the same revenue metrics at the defined post-launch intervals (e.g., week 1, week 4, week 12). Segment by relevant dimensions — cohort, plan tier, feature adoption status. Deliverable: post-launch revenue data table matching the baseline structure.
4. **Calculate impact**: Compare post-launch metrics to baseline. Quantify the delta — incremental MRR, change in expansion rate, shift in churn rate. Apply the attribution methodology to isolate the product change's contribution. Deliverable: revenue impact calculation with attributed and unattributed components.
5. **Produce the impact report**: Assemble findings into a structured report covering baseline, methodology, results, confidence level, and recommendations. Flag any unexpected patterns (e.g., revenue up in one segment but down in another). Route to the product manager, finance, and leadership. Deliverable: revenue impact report with executive summary, detailed analysis, and action recommendations.

## Anti-Patterns
- **Claiming full attribution without controlling for other factors**: Attributing all revenue change to the product launch without accounting for concurrent marketing spend, pricing changes, or seasonality. *Why*: Over-attribution inflates perceived feature ROI and distorts future investment decisions.
- **Measuring too early**: Reporting revenue impact after one week when the feature's revenue effect takes 60-90 days to materialise. *Why*: Premature measurement either misses the impact entirely or captures noise, leading to incorrect conclusions.
- **Ignoring negative signals**: Reporting expansion revenue gains while overlooking a concurrent increase in churn or downgrade among affected users. *Why*: Net revenue impact requires both sides — positive gains offset by negative losses give the true picture.

## Output
**On success**: A revenue impact report containing baseline metrics, attribution methodology, post-launch comparisons, quantified impact with confidence level, and recommendations — formatted for product review and finance stakeholder consumption.
**On failure**: Report which revenue data was unavailable (e.g., billing system lag, missing cohort segmentation), what partial analysis was completed, and recommend a revised timeline or data request to complete the assessment.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
