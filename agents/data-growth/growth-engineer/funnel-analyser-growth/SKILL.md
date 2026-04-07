---
name: funnel-analyser-growth
description: >
  This skill analyses the growth funnel to identify the highest-leverage optimisation opportunities. Use when asked to diagnose acquisition or activation drop-off, measure growth funnel conversion, or identify where new users abandon. Also consider when a growth experiment needs baseline funnel data. Suggest when acquisition spend increases but signups do not.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: medium
related-skills:
  - funnel-analyser
  - growth-loop-optimiser
  - activation-moment-validator
  - metrics-dashboard-growth
---

# funnel-analyser-growth

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The growth funnel analyser examines the acquisition-to-activation funnel — from first touch through signup, onboarding, and activation — to identify the step with the largest absolute drop-off, segment by channel and cohort, and recommend experiments that maximize conversion through the growth funnel.

## When to Use

- When acquisition costs rise without corresponding growth in activated users.
- When a growth experiment needs baseline conversion data across funnel steps.
- When a new onboarding flow ships and the team needs to measure its impact on activation rates.
- When the growth lead requests a funnel audit to prioritize the next experiment cycle.

## Workflow

1. **Define growth funnel steps**: Map the funnel from first touch (ad impression, organic visit) through landing page, signup, onboarding, and activation. Confirm each step has a corresponding tracking event.
2. **Pull conversion data**: Query step-to-step conversion rates for the analysis window. Compute both step-to-step and end-to-end conversion rates.
3. **Rank drop-off points**: Identify the step with the largest absolute user loss. Calculate the potential user gain if that step's conversion improved by 10-20%.
4. **Segment by channel**: Break the funnel by acquisition channel (paid search, organic, referral, direct). Identify channels with systematically worse conversion at specific steps.
5. **Segment by device and cohort**: Compare conversion across mobile vs. desktop and by signup cohort (weekly). Flag device-specific UX issues and temporal trends.
6. **Produce recommendations**: For the top 2 drop-off points, hypothesize root causes and propose experiments with expected conversion lift. Prioritize by impact multiplied by confidence.

## Anti-Patterns

- **Optimizing the wrong step**: Targeting the step with the lowest conversion rate rather than the step with the largest absolute drop-off wastes experiment capacity. *Why*: a 50% to 45% drop with 100K users entering is higher-leverage than a 10% to 5% drop with 1K users entering.
- **Channel-blind analysis**: Reporting one funnel for all channels hides that organic users may convert at 3x the rate of paid users. *Why*: the bottleneck step differs by channel; a single funnel view prescribes a generic intervention.
- **No baseline before experiments**: Launching a funnel experiment without a stable baseline makes it impossible to attribute lift. *Why*: if the baseline is noisy, the experiment's signal is indistinguishable from variance.

## Output

**Success:**
- A growth funnel report with step-by-step conversion rates, drop-off rankings, channel and device segmentation, and 2-3 experiment recommendations with projected impact.

**Failure:**
- Growth funnel events are missing or inconsistent, producing gaps in the analysis. Report the missing events and the instrumentation work required before reliable analysis is possible.

## Related Skills

- [`funnel-analyser`](../../../data-growth/data-analyst/funnel-analyser/SKILL.md) -- the data analyst's funnel analyser covers the full product funnel; this skill focuses specifically on acquisition-to-activation.
- [`growth-loop-optimiser`](../../../data-growth/growth-lead/growth-loop-optimiser/SKILL.md) -- funnel analysis within growth loops feeds loop optimisation decisions.
- [`activation-moment-validator`](../../../data-growth/growth-lead/activation-moment-validator/SKILL.md) -- the activation step in the funnel must be validated as a retention predictor.
- [`metrics-dashboard-growth`](../metrics-dashboard-growth/SKILL.md) -- growth funnel metrics are displayed on the growth dashboard.
