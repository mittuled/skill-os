---
name: north-star-metric-reviewer-data
description: >
  This skill reviews whether the north star metric remains valid and actionable. Use when asked to audit the north star definition, assess metric health, or evaluate whether the north star still correlates with business outcomes. Also consider at quarterly planning boundaries. Suggest when the north star has not moved despite significant product changes.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: medium
related-skills:
  - goal-framer-data
  - alerting-configurator-data
  - north-star-metric-reviewer
triggers:
  - "review the north star metric"
  - "is our north star still valid"
  - "audit the key metric"
  - "should we change our north star"
---

# north-star-metric-reviewer-data

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The north star metric reviewer audits the current north star metric definition to confirm it still reflects core value delivery, correlates with revenue and retention, is measurable with existing instrumentation, and remains actionable by the product and growth teams.

## When to Use

- When a quarterly planning cycle begins and the north star metric has not been reviewed in 90+ days.
- When the north star metric has remained flat despite significant product investment, suggesting it may no longer capture the right signal.
- When the business model changes (new pricing, new segment, pivot) and the existing north star may not reflect the new value proposition.
- When teams disagree on what "success" looks like because the north star definition is ambiguous.

## Workflow

1. **Retrieve current definition**: Pull the north star metric definition including calculation formula, time window, cohort scope, and data source.
2. **Validate correlation**: Run a correlation analysis between the north star metric and trailing 90-day revenue, retention rate (Day 7, Day 30), and LTV. Flag if Pearson r drops below 0.5.
3. **Test actionability**: Identify the top 3 product or growth levers that should move the north star. Check whether recent experiments targeting those levers produced measurable movement.
4. **Assess measurability**: Confirm the instrumentation required to compute the metric is live, verified, and free of data quality issues. Check for sampling bias or missing platform coverage.
5. **Evaluate clarity**: Survey 3-5 stakeholders (PM, growth, engineering) on their understanding of the metric definition. Flag if definitions diverge.
6. **Recommend**: Produce a verdict — retain, refine (adjust definition), or replace (propose a new north star). Support the recommendation with data from steps 2-5.

## Anti-Patterns

- **Set-and-forget north star**: Treating the north star as permanent avoids the discomfort of admitting it no longer works. *Why*: a stale north star optimizes the team toward a proxy that no longer correlates with business outcomes.
- **Changing the north star every quarter**: Frequent changes prevent longitudinal analysis and erode team alignment. *Why*: meaningful trends require at least two quarters of consistent measurement.
- **Reviewing without data**: Conducting the review as a qualitative discussion without running correlation or actionability analysis produces opinion-based conclusions. *Why*: the entire point of a north star is to ground decisions in data, not consensus.

## Output

**Success:**
- A north star review report containing correlation analysis, actionability assessment, measurability audit, clarity survey results, and a retain/refine/replace recommendation with supporting data.

**Failure:**
- The review produces a recommendation without quantitative backing. Report the data gaps that prevented analysis and the steps required to close them.

## Related Skills

- [`goal-framer-data`](../goal-framer-data/SKILL.md) -- the goal framework descends from the north star; changes here cascade to all analytics goals.
- [`alerting-configurator-data`](../alerting-configurator-data/SKILL.md) -- north star threshold alerts must be recalibrated when the metric definition changes.
- [`north-star-metric-reviewer`](../../vp-product/north-star-metric-reviewer/SKILL.md) -- the VP Product reviews the north star from a strategic perspective; this skill provides the data analysis.
