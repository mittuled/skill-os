---
name: cohort-selector-sales
description: >
  This skill selects the outbound prospecting cohort based on ICP criteria,
  intent signals, and pipeline needs. Use when asked to build a prospect list,
  define outbound targeting, or prioritize accounts for a campaign. Also consider
  when pipeline coverage drops below target.
  Suggest when SDRs are prospecting without a defined target list.
department: sales
agent: sales-development-rep
version: 1.0.0
complexity: simple
related-skills:
  - ../../../sales/sales-manager/gtm-activation-sales/SKILL.md
  - ../../../sales/account-executive/sales-signal-collector/SKILL.md
---

# cohort-selector-sales

## Agent: Sales Development Rep

L3 sales development representative (Nx) responsible for outbound prospecting and cohort-based targeting.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Selects the outbound prospecting cohort based on ICP criteria, intent signals, and pipeline needs to maximize meeting conversion rates from outbound activity.

## When to Use

- When launching a new outbound campaign and the target account list needs to be defined.
- When pipeline coverage falls below the required ratio and additional outbound volume is needed against the highest-converting segments.
- When intent data or trigger events (funding rounds, leadership changes, tech stack signals) indicate a subset of ICP accounts are in-market.

## Workflow

1. **ICP Filter Application**: Apply ICP filters to the total addressable market: firmographics (industry, size, geography), technographics (tech stack signals), and behavioral indicators (website visits, content engagement). Exclude accounts already in active pipeline or recently closed-lost within the cooling-off period. Deliverable: filtered account list with ICP match scores.
2. **Intent Signal Overlay**: Layer intent signals (third-party intent data, job postings, funding events, product reviews) onto the filtered list. Rank accounts by combined ICP fit and intent score. Deliverable: ranked prospect list with intent signal annotations.
3. **Cohort Sizing and Assignment**: Size the cohort to match SDR capacity and campaign duration. Assign accounts to individual SDRs based on territory, vertical expertise, or round-robin. Deliverable: assigned cohort roster with per-SDR targets.

## Anti-Patterns

- **Spray-and-pray targeting**: Building the largest possible list without filtering for fit or intent. *Why*: high-volume, low-fit outbound burns through the addressable market, produces low reply rates, and damages domain reputation.
- **Ignoring cooling-off periods**: Re-targeting accounts that were recently contacted or closed-lost without sufficient time gap. *Why*: premature re-engagement annoys prospects and signals desperation; a 90-day cooling-off period allows circumstances to change.

## Output

**On success**: Produces a ranked, assigned prospect cohort with ICP match scores, intent signal annotations, and per-SDR account targets. Delivered to the SDR team for outreach execution.

**On failure**: Report what prevented cohort selection (e.g., ICP criteria too narrow yielding insufficient volume, intent data unavailable), what was attempted, and recommended ICP relaxation or data source additions.

## Related Skills

- [`gtm-activation-sales`](../../../sales/sales-manager/gtm-activation-sales/SKILL.md) -- Provides the GTM context and pipeline targets the cohort selection serves.
- [`sales-signal-collector`](../../../sales/account-executive/sales-signal-collector/SKILL.md) -- Supplies signal data that can inform intent scoring and account prioritization.
