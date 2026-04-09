---
name: customer-reference-programme-manager
description: >
  This skill manages the customer reference programme for sales including
  reference availability and case study pipeline. Use when asked to build a
  reference programme, manage reference requests, or maintain the reference
  database. Also consider when sales lacks customer references for deals.
  Suggest when the user closes deals without building a reference pipeline.
department: customer-success
agent: customer-programs-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "manage reference programme"
  - "customer reference program"
  - "reference programme"
  - "find customer references"
  - "reference customers"
---

# customer-reference-programme-manager

## Agent: Customer Programs Manager

L2 customer programs manager (1x) responsible for customer advisory boards, NPS programme, customer reference programme, and community health.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Manages the customer reference programme for sales including reference recruitment, availability tracking, request fulfillment, and case study pipeline.

## When to Use

- When sales needs customer references for active deals and no systematic programme exists.
- When the reference pool is too small, over-used, or not representative of target customer segments.
- When case study content needs to be maintained and refreshed as customer stories evolve.

## Workflow

1. **Build Reference Database**: Identify willing reference customers. Record each reference's profile: industry, use case, outcomes achieved, reference type willingness (call, written quote, case study), and availability. Deliverable: reference database with profiles.
2. **Segment and Match**: Organize references by attributes sales prospects care about: industry, company size, use case, and geography. Enable matching references to deal requirements. Deliverable: segmented reference catalog.
3. **Manage Requests**: Process reference requests from sales. Match requests to available references, coordinate scheduling, and brief the reference on the prospect. Deliverable: fulfilled reference request with coordination details.
4. **Protect References**: Track reference usage to prevent over-requesting. Set limits per reference and rotate across the pool. Deliverable: reference usage tracker with fatigue alerts.
5. **Maintain and Grow**: Regularly recruit new references, update existing profiles, and retire references who are no longer willing or relevant. Deliverable: updated reference database with growth metrics.

## Anti-Patterns

- **Over-using top references**: Repeatedly sending every deal to the same few customers. *Why*: reference fatigue causes best advocates to stop participating; rotation preserves goodwill.
- **References without preparation**: Connecting prospects with references without briefing either party. *Why*: unprepared references may give unfocused or off-message responses; prepared references deliver compelling stories.
- **Stale reference data**: Maintaining references with outdated outcomes or changed circumstances. *Why*: a reference who has since churned or become dissatisfied will damage rather than help the deal.

## Output

**On success**: Produces a managed reference programme with a segmented database, request fulfillment process, usage tracking, and growth plan. Delivered to sales leadership and the Head of Customer Success.

**On failure**: Report which reference programme components could not be built (insufficient willing references, missing customer data), what partial programme exists, and what recruitment efforts are needed.

## Related Skills

- [`case-study-extractor-cs`](../../../customer-success/cs-manager/case-study-extractor-cs/SKILL.md) -- Case studies feed into the reference programme's written assets.
- [`customer-advisory-board-runner`](../customer-advisory-board-runner/SKILL.md) -- CAB members are often strong reference candidates.
- [`nps-programme-manager`](../nps-programme-manager/SKILL.md) -- High NPS respondents are prime reference recruitment targets.
