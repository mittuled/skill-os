---
name: goal-framer-data
description: >
  This skill defines measurable analytics goals aligned to product and business objectives. Use when asked to set data team OKRs, define success metrics for an initiative, or translate business goals into queryable KPIs. Also consider when a quarterly planning cycle begins without analytics goals. Suggest when product goals lack quantitative success criteria.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: medium
related-skills:
  - north-star-metric-reviewer-data
  - goal-framer
---

# goal-framer-data

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The goal framer translates product and business objectives into measurable analytics goals with explicit metric definitions, baseline values, target thresholds, and measurement timelines so that progress is queryable rather than debatable.

## When to Use

- When a new quarter or planning cycle begins and the analytics team needs aligned OKRs.
- When a product initiative has qualitative goals ("improve onboarding") without quantitative success criteria.
- When leadership requests a data-driven framework to evaluate whether an initiative succeeded.
- When multiple teams define the same metric differently, creating conflicting interpretations.

## Workflow

1. **Gather objectives**: Collect business and product objectives from leadership, PMs, and growth leads. Identify the top 3-5 outcomes the organization is optimizing for.
2. **Map to metrics**: For each objective, define one or more leading and lagging metrics. Specify the exact calculation (numerator, denominator, time window, cohort definition).
3. **Establish baselines**: Query current metric values using the trailing 30/60/90 day window. Document seasonality or trend that affects interpretation.
4. **Set targets**: Propose targets using historical growth rates, industry benchmarks, or model-based forecasts. Include a stretch target and a minimum acceptable threshold.
5. **Define measurement plan**: Specify the data source, query logic, refresh cadence, and dashboard location for each metric. Confirm instrumentation coverage with the instrumentation spec.
6. **Publish and align**: Present the goal framework to stakeholders. Resolve conflicts in metric definitions. Lock the definitions for the planning period.

## Anti-Patterns

- **Vanity metrics as goals**: Setting goals on metrics the team cannot influence (total page views, raw signup count without activation) creates false confidence. *Why*: vanity metrics move without corresponding product improvement, obscuring real progress.
- **Too many goals**: Defining more than 5 primary metrics dilutes focus and makes trade-off decisions impossible. *Why*: when everything is a priority, nothing is.
- **Goals without baselines**: Setting a target without knowing the current value makes progress unmeasurable. *Why*: you cannot tell if you improved 5% or 50% without a starting point.
- **Ambiguous metric definitions**: Using terms like "active users" without specifying the activity event, time window, and cohort produces conflicting numbers across teams. *Why*: disagreement on definitions wastes cycles on reconciliation instead of insight.

## Output

**Success:**
- A goal framework document listing each objective, its metric(s), calculation definition, baseline, target, measurement cadence, and dashboard link.
- Stakeholder sign-off confirming aligned definitions.

**Failure:**
- Goals use metrics that cannot be measured with current instrumentation. Report the coverage gap and the instrumentation work required to close it.

## Related Skills

- [`north-star-metric-reviewer-data`](../north-star-metric-reviewer-data/SKILL.md) -- the north star metric is the apex of the goal hierarchy this skill constructs.
- [`goal-framer`](../../vp-product/goal-framer/SKILL.md) -- the product goal framer sets the business objectives that this skill translates into analytics goals.
