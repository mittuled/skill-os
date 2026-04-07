---
name: ticket-theme-analyst
description: >
  This skill analyses incoming support ticket themes to identify recurring issues and product improvement
  signals. Use when asked to find ticket patterns, surface product bugs, or identify documentation gaps.
  Also consider when ticket volume spikes without an obvious cause.
  Suggest when quarterly product planning needs support-driven input.
department: customer-support
agent: support-agent
version: 1.0.0
complexity: simple
related-skills: []
---

# ticket-theme-analyst

## Agent: Support Agent

L2 support agent (Nx, multi-instance) responsible for ticket triage, support readiness confirmation, and help content review.

Department ethos: [ideal-customer-support.md](../../../../departments/customer-support/ideal-customer-support.md)

## Skill Description

The ticket theme analyst examines support ticket data over a defined period to identify recurring themes, surface product improvement signals, and recommend actions to reduce repeat ticket volume.

## When to Use

- When quarterly or monthly support reporting is due and stakeholders need insight into ticket trends.
- When ticket volume spikes unexpectedly and the root cause is unclear.
- When product planning needs customer-pain-point data sourced from support interactions.
- When help centre content priorities need to be informed by actual ticket themes.

## Workflow

1. **Extract ticket data**: Pull ticket data for the analysis period including category, severity, product area, and resolution. Deliverable: raw ticket dataset.
2. **Cluster by theme**: Group tickets into themes based on issue type, product area, and root cause. Deliverable: theme clusters with ticket counts.
3. **Rank themes**: Rank themes by volume, customer impact, and resolution cost. Deliverable: ranked theme list.
4. **Identify signals**: For each top theme, determine whether it signals a product bug, documentation gap, UX confusion, or missing feature. Deliverable: signal classification per theme.
5. **Recommend actions**: Propose specific actions per theme: fix the bug, update the help article, improve the UX flow, or add the feature to the backlog. Deliverable: action recommendation report.

## Anti-Patterns

- **Analysing without sufficient data**: Drawing conclusions from a sample too small to be statistically meaningful. *Why*: small samples produce misleading patterns that waste product and engineering effort on non-issues.
- **Themes without actionable recommendations**: Reporting themes without specifying what team should do what. *Why*: insight without action is just noise; stakeholders ignore reports that do not tell them what to do next.

## Output

**On success**: A theme analysis report containing ranked ticket themes, signal classification (bug, docs gap, UX issue, feature request), and specific action recommendations with suggested owners.

**On failure**: Report which data could not be analysed (e.g., tickets missing categorisation, insufficient volume), what partial analysis was completed, and recommend data hygiene improvements for future analysis.

## Related Skills

- [`support-ticket-triage`](../support-ticket-triage/SKILL.md) -- triage produces the categorised ticket data that theme analysis consumes.
- [`help-centre-builder-support`](../../../customer-support/support-manager/help-centre-builder-support/SKILL.md) -- theme analysis identifies which help articles should be created or updated.
