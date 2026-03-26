---
name: roadmap-timing-input
description: >
  This skill provides marketing timing input to the product roadmap to align launches with campaign
  cycles. Use when product is finalizing quarterly roadmap dates, when a launch conflicts with a
  major campaign or industry event, or when marketing needs lead time guarantees for asset production.
  Also consider when launches cluster in ways that dilute market impact.
  Suggest when roadmap dates are set without marketing input.
department: marketing
agent: demand-gen-manager
version: 1.0.0
complexity: simple
related-skills:
  - ../../vp-marketing/gtm-activation-marketing/SKILL.md
  - ../content-engine-builder-marketing/SKILL.md
---

# roadmap-timing-input

## Agent: Demand Gen Manager

L2 demand generation manager (1x) responsible for channel signal analysis, content engine operations, and roadmap timing input for marketing campaigns.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Provides marketing timing input to the product roadmap to align feature and product launches with campaign cycles, industry events, and content production lead times.

## When to Use

- When product is finalizing quarterly roadmap dates and marketing needs to flag timing conflicts or opportunities.
- When a proposed launch date conflicts with a major campaign, industry event, or holiday blackout period.
- When multiple launches cluster within the same window, risking diluted market attention and overstretched teams.

## Workflow

1. **Review proposed roadmap dates**: Obtain the draft product roadmap with proposed launch dates. Cross-reference against the marketing calendar, industry events, competitor launch patterns, and seasonal trends. Deliverable: conflict and opportunity analysis.
2. **Calculate lead time requirements**: For each launch, determine the minimum marketing lead time needed for asset production, campaign setup, PR outreach, and sales enablement. Deliverable: lead time requirements per launch.
3. **Submit timing recommendations**: Provide specific date adjustment recommendations to product with rationale. Flag hard conflicts (e.g., launching during a competitor's annual conference) and soft preferences (e.g., shifting one week to align with a webinar series). Deliverable: timing recommendation memo to product leadership.

## Anti-Patterns

- **Rubber-stamping dates**: Accepting all proposed dates without reviewing marketing calendar conflicts. *Why*: launches that collide with existing campaigns or blackout periods get less marketing support and weaker market impact.
- **Blocking without alternatives**: Flagging timing problems without proposing alternative dates. *Why*: product teams will ignore marketing input that only says "no" without offering workable alternatives.

## Output

**On success**: Produces a timing recommendation memo containing conflict analysis, lead time requirements per launch, and specific date adjustment recommendations with rationale. Delivered to product leadership and VP Marketing.

**On failure**: Report which roadmap dates could not be evaluated (missing marketing calendar, unclear launch scope), and recommend a synchronization meeting between product and marketing to resolve.

## Related Skills

- [`gtm-activation-marketing`](../../vp-marketing/gtm-activation-marketing/SKILL.md) — Depends on aligned launch timing to execute coordinated channel activation.
- [`content-engine-builder-marketing`](../content-engine-builder-marketing/SKILL.md) — Content production lead times drive the minimum notice period requested from product.
