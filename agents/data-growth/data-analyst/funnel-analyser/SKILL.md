---
name: funnel-analyser
description: >
  This skill analyses conversion funnels to identify drop-off points and improvement opportunities. Use when asked to diagnose funnel drop-off, measure conversion rates, or identify where users abandon a flow. Also consider when a key metric declines without clear cause. Suggest when a product change ships without funnel impact analysis.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: medium
related-skills:
  - adoption-tracker-data
  - metrics-dashboard-builder
  - funnel-analyser-growth
  - statistical-significance-tracker
---

# funnel-analyser

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The funnel analyser diagnoses conversion funnels by computing step-to-step conversion rates, identifying the highest-impact drop-off points, segmenting by cohort to isolate root causes, and producing prioritized recommendations for improving end-to-end conversion.

## When to Use

- When a conversion metric (signup-to-activation, trial-to-paid, checkout completion) declines and the team needs to locate the drop-off.
- When a new user flow launches and needs baseline funnel measurement.
- When the growth team prioritizes experiments and needs to identify the highest-leverage funnel step to target.
- When a product change ships and the team needs to measure its impact on funnel conversion.

## Workflow

1. **Define funnel steps**: Enumerate each step in the conversion flow with the corresponding event name. Confirm instrumentation coverage for every step.
2. **Pull conversion data**: Query the analytics warehouse for event counts at each step over the analysis window (typically 7-30 days). Compute step-to-step and end-to-end conversion rates.
3. **Identify drop-off points**: Rank steps by absolute drop-off volume and relative conversion rate. Highlight the step with the largest gap between entry and exit.
4. **Segment by cohort**: Break the funnel by user segment (new vs. returning, acquisition channel, device, plan tier). Identify segments with significantly different conversion patterns.
5. **Time-based analysis**: Plot conversion rates over time to detect trends, seasonality, or regressions coinciding with product releases.
6. **Produce recommendations**: For the top 2-3 drop-off points, hypothesize root causes (UX friction, unclear copy, missing trust signals, technical errors) and propose experiments to address each.

## Anti-Patterns

- **Aggregate-only analysis**: Reporting a single conversion rate without segmentation hides that one segment may convert at 80% while another converts at 5%. *Why*: the intervention differs by segment; aggregate data obscures this.
- **Ignoring time-to-convert**: Measuring only whether users convert, not how long it takes, misses latency-driven abandonment. *Why*: a step that takes 3 minutes on mobile but 30 seconds on desktop reveals a platform-specific UX issue.
- **No event verification**: Analysing a funnel without first confirming that every step event fires correctly risks drawing conclusions from broken data. *Why*: a missing event looks like a 100% drop-off, triggering a false alarm.

## Output

**Success:**
- A funnel analysis report containing step-by-step conversion rates, drop-off rankings, cohort segmentation, time-series trends, and prioritized recommendations with hypothesized root causes.

**Failure:**
- One or more funnel steps lack instrumentation, making the analysis incomplete. Report the missing events, the data gap, and the instrumentation work required.

## Related Skills

- [`adoption-tracker-data`](../adoption-tracker-data/SKILL.md) -- adoption tracking uses funnel analysis to identify where feature discovery and trial break down.
- [`metrics-dashboard-builder`](../metrics-dashboard-builder/SKILL.md) -- funnel metrics are surfaced on dashboards for ongoing monitoring.
- [`funnel-analyser-growth`](../../../data-growth/growth-engineer/funnel-analyser-growth/SKILL.md) -- the growth engineer's funnel analyser focuses on acquisition and activation; this skill covers the full product funnel.
- [`statistical-significance-tracker`](../../../data-growth/analytics-lead/statistical-significance-tracker/SKILL.md) -- experiments targeting funnel steps need significance tracking to validate results.
