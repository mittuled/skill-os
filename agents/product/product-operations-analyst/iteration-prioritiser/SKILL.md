---
name: iteration-prioritiser
description: >
  This skill prioritises the next iteration backlog based on signal synthesis and business impact.
  Use when the team needs to decide what to build next and multiple competing signals need to be weighed.
  Also consider when the backlog feels stale or when recent data invalidates previous prioritisation decisions.
  Suggest when a sprint or iteration boundary is approaching and the backlog has not been re-ranked with fresh signal.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills:
  - adoption-tracker
  - cohort-selector
  - cs-onboarding-playbook
  - early-adopter-success-builder
  - feedback-loop-formaliser
  - internal-comms-broadcaster
  - objection-handler-updater
  - revenue-impact-monitor
  - rollout-configurator-review
  - signal-synthesiser
  - support-ticket-triage
triggers:
  - "prioritise iterations"
  - "iteration priority"
  - "rank iterations"
  - "prioritise product work"
  - "iteration backlog"
---

# iteration-prioritiser

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Prioritises the next iteration backlog based on signal synthesis and business impact.

## When to Use
- When the team is approaching a sprint or iteration boundary and needs to rank the backlog for the next cycle
- When new signals (support escalations, adoption data, revenue impact, competitive moves) have arrived since the last prioritisation
- When the product manager requests an ops-informed prioritisation recommendation before a planning session
- When the backlog has grown and items lack clear relative ordering

## Workflow
1. **Gather current signals**: Collect the latest data from all relevant sources — adoption metrics, support ticket trends, revenue impact reports, customer feedback summaries, and any competitive intelligence. Deliverable: signal summary document with source, recency, and key findings per signal.
2. **Map signals to backlog items**: For each backlog item, identify which signals support or oppose its priority. Tag items with the signals that affect them. Deliverable: backlog table with signal tags per item.
3. **Score business impact**: Assess each candidate item on business impact dimensions — revenue influence, retention risk, adoption acceleration, support cost reduction, or strategic alignment. Use a consistent scale (e.g., 1-5 or T-shirt sizing). Deliverable: impact scores appended to the backlog table.
4. **Assess effort and risk**: For each high-impact item, estimate relative effort (from engineering input or historical velocity) and implementation risk. Flag items where effort is uncertain and needs spike work. Deliverable: effort and risk estimates per item.
5. **Produce the ranked list**: Combine impact, effort, risk, and signal strength into a prioritised ranking. Apply tiebreakers based on strategic alignment and dependencies. Deliverable: ranked backlog for the next iteration with rationale for the top 5 items.
6. **Present to the product manager**: Walk through the ranked list, highlighting where signals diverge from previous priorities and where new information changed the ordering. Deliverable: prioritisation briefing with the ranked list and change-from-last-cycle annotations.

## Anti-Patterns
- **Prioritising by loudest voice**: Ranking items based on who complained most recently rather than systematic signal analysis. *Why*: Recency and volume bias leads to whiplash prioritisation that undermines team focus and erodes trust in the process.
- **Ignoring effort in the ranking**: Recommending high-impact items without considering that they consume the entire iteration budget. *Why*: A prioritised list that is not feasible within the iteration capacity is not actionable — it forces re-prioritisation during the sprint.
- **Stale signal data**: Using adoption or support data from two cycles ago because refreshing it takes effort. *Why*: Prioritisation based on outdated signal produces decisions that were correct last month but wrong today.
- **Treating all signals as equal**: Weighting a single anecdotal customer complaint the same as a statistically significant adoption drop. *Why*: Signal quality varies — conflating weak and strong signals leads to poor resource allocation.

## Output
**On success**: A ranked iteration backlog containing prioritised items with impact scores, effort estimates, signal justifications, and rationale for the top 5 — ready for the product manager to use in sprint planning.
**On failure**: Report which signals were unavailable (e.g., adoption data delayed, revenue impact not yet calculated), what partial ranking was produced, and recommend which data gaps to close before finalising the prioritisation.

## Related Skills
- [`adoption-tracker`](../adoption-tracker/SKILL.md) — sibling skill under the same agent — combine with adoption-tracker for end-to-end coverage
- [`cohort-selector`](../cohort-selector/SKILL.md) — sibling skill under the same agent — combine with cohort-selector for end-to-end coverage
- [`cs-onboarding-playbook`](../cs-onboarding-playbook/SKILL.md) — sibling skill under the same agent — combine with cs-onboarding-playbook for end-to-end coverage
- [`early-adopter-success-builder`](../early-adopter-success-builder/SKILL.md) — sibling skill under the same agent — combine with early-adopter-success-builder for end-to-end coverage
- [`feedback-loop-formaliser`](../feedback-loop-formaliser/SKILL.md) — sibling skill under the same agent — combine with feedback-loop-formaliser for end-to-end coverage
- [`internal-comms-broadcaster`](../internal-comms-broadcaster/SKILL.md) — sibling skill under the same agent — combine with internal-comms-broadcaster for end-to-end coverage
- [`objection-handler-updater`](../objection-handler-updater/SKILL.md) — sibling skill under the same agent — combine with objection-handler-updater for end-to-end coverage
- [`revenue-impact-monitor`](../revenue-impact-monitor/SKILL.md) — sibling skill under the same agent — combine with revenue-impact-monitor for end-to-end coverage
- [`rollout-configurator-review`](../rollout-configurator-review/SKILL.md) — sibling skill under the same agent — combine with rollout-configurator-review for end-to-end coverage
- [`signal-synthesiser`](../signal-synthesiser/SKILL.md) — sibling skill under the same agent — combine with signal-synthesiser for end-to-end coverage
- [`support-ticket-triage`](../support-ticket-triage/SKILL.md) — sibling skill under the same agent — combine with support-ticket-triage for end-to-end coverage
