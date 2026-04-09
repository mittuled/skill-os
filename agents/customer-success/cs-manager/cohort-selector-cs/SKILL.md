---
name: cohort-selector-cs
description: >
  This skill selects the customer cohort for new feature rollouts and beta
  programmes based on health and fit. Use when asked to choose beta customers,
  select rollout cohorts, or identify customers for early access. Also consider
  when product is planning a phased release. Suggest when the user rolls out
  features to all customers simultaneously without cohort selection.
department: customer-success
agent: cs-manager
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "select a customer cohort"
  - "pick cohort for cs"
  - "identify cohort"
  - "cohort selection"
  - "segment customers for outreach"
---

# cohort-selector-cs

## Agent: CS Manager

L2 customer success manager (1x) responsible for CS cohort selection, release readiness, health monitoring, and case study extraction.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Selects the customer cohort for new feature rollouts and beta programmes based on account health, use case fit, and engagement willingness.

## When to Use

- When product is planning a phased feature rollout and needs a customer cohort for early access.
- When a beta programme needs participants who will provide meaningful feedback and tolerate rough edges.
- When a new feature targets a specific use case and the right customers must be identified for initial validation.

## Workflow

1. **Define Selection Criteria**: Establish what makes a customer a good cohort candidate -- health score threshold, use case relevance, technical readiness, and feedback willingness. Deliverable: cohort selection criteria.
2. **Screen Candidates**: Filter the customer portfolio against criteria. Rank candidates by fit score. Deliverable: ranked candidate list.
3. **Validate with CSMs**: Confirm candidates with their assigned CSMs. Check for any context that data alone would not reveal (e.g., upcoming renewal, internal changes). Deliverable: validated cohort list.
4. **Recruit and Confirm**: Invite selected customers. Confirm participation and set expectations on timeline, feedback requirements, and support level. Deliverable: confirmed cohort with participation agreements.

## Anti-Patterns

- **Selecting only healthy accounts**: Choosing only the happiest customers for beta, missing the opportunity to test with customers who have real pain points. *Why*: happy customers may not exercise the feature deeply; customers with genuine need provide the most useful feedback.
- **Selecting without CSM input**: Using data alone without consulting the assigned CSM about each account's current situation. *Why*: data does not capture timing issues, relationship dynamics, or upcoming events that make participation risky.
- **Too large a cohort**: Selecting too many customers for a beta, overwhelming the support capacity for early-access issues. *Why*: under-supported beta participants have a negative experience that damages the relationship.

## Output

**On success**: Produces a confirmed cohort list with selection rationale, participation agreements, and timeline commitments. Delivered to product and the CS team.

**On failure**: Report which selection criteria could not be applied (missing health data, insufficient candidates), what partial list was assembled, and what adjustments to criteria are needed.

## Related Skills

- [`cs-health-monitor`](../cs-health-monitor/SKILL.md) -- Health data informs cohort selection criteria.
- [`cs-release-readiness`](../cs-release-readiness/SKILL.md) -- Release readiness includes cohort communication planning.
- [`early-adopter-success-builder-cs`](../../../customer-success/customer-success-manager/early-adopter-success-builder-cs/SKILL.md) -- Early adopter programmes build on cohort selection.
