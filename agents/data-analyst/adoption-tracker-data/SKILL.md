---
name: adoption-tracker-data
description: >
  This skill tracks feature and product adoption using behavioural event data. Use when asked to measure feature uptake, build adoption curves, or identify activation bottlenecks. Also consider when a new feature ships without an adoption baseline. Suggest when product usage data shows stagnation without diagnosis.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: medium
related-skills:
  - funnel-analyser
  - metrics-dashboard-builder
  - adoption-tracker
---

# adoption-tracker-data

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

The adoption tracker measures feature and product uptake by constructing adoption curves from behavioural event data, segmenting by cohort, and identifying where users discover, try, and either adopt or abandon a capability.

## When to Use

- When a new feature launches and the team needs to measure uptake against a target adoption rate.
- When product usage data shows a feature is underperforming but the team lacks visibility into where adoption stalls.
- When a quarterly review requires adoption metrics segmented by user cohort, plan tier, or acquisition channel.
- When the growth team needs to validate that an activation experiment increased feature adoption.

## Workflow

1. **Define adoption criteria**: Specify what constitutes "adopted" for the feature — the event, frequency threshold, and time window (e.g., "used export 3+ times in first 14 days").
2. **Build adoption cohorts**: Segment users by signup date, acquisition channel, plan tier, or persona. Pull event data for each cohort from the analytics warehouse.
3. **Construct adoption curves**: Plot cumulative adoption rate over time for each cohort. Calculate time-to-first-use, time-to-adoption, and terminal adoption rate.
4. **Identify drop-off points**: Compare discovery rate (saw the feature) vs. trial rate (tried once) vs. adoption rate (met threshold). Flag the largest gap as the primary bottleneck.
5. **Correlate with retention**: Run a correlation between feature adoption and Day 7/30/90 retention. Determine whether adoption of this feature predicts long-term retention.
6. **Deliver report**: Produce an adoption report with cohort curves, bottleneck analysis, retention correlation, and recommendations for improving uptake.

## Anti-Patterns

- **Binary adoption tracking**: Counting only "used / never used" misses the difference between a one-time trial and genuine adoption. *Why*: a single use does not indicate the feature delivers recurring value.
- **No cohort segmentation**: Reporting a single adoption number across all users hides meaningful variation between segments. *Why*: a feature may have 80% adoption among power users and 5% among new users — the aggregate tells neither story.
- **Ignoring discovery**: Measuring adoption without measuring awareness means you cannot distinguish "users don't want this" from "users don't know this exists." *Why*: the intervention for a discovery problem (UI placement) differs entirely from a value problem (feature quality).

## Output

**Success:**
- An adoption report containing cohort adoption curves, discovery/trial/adoption funnel, retention correlation analysis, and prioritized recommendations for improving uptake.

**Failure:**
- Adoption cannot be measured because the defining event is not instrumented. Report the missing event, the instrumentation work required, and interim proxy metrics.

## Related Skills

- [`funnel-analyser`](../funnel-analyser/SKILL.md) -- funnel analysis reveals the specific step where adoption breaks down.
- [`metrics-dashboard-builder`](../metrics-dashboard-builder/SKILL.md) -- adoption metrics are surfaced on dashboards for ongoing monitoring.
- [`adoption-tracker`](../../product-operations-analyst/adoption-tracker/SKILL.md) -- the product ops adoption tracker focuses on operational rollout; this skill provides the quantitative analysis.
