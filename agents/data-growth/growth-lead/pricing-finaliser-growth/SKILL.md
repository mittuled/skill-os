---
name: pricing-finaliser-growth
description: >
  This skill reviews final pricing from a growth mechanics perspective before launch. Use when asked to approve pricing for growth impact, assess how pricing affects conversion, or validate freemium/trial mechanics before launch. Also consider when pricing changes are proposed mid-cycle. Suggest when pricing is finalized without growth team input.
department: data-growth
agent: growth-lead
version: 1.0.0
complexity: simple
related-skills:
  - pricing-strategy-growth
  - growth-model-designer
triggers:
  - "finalise growth pricing"
  - "lock pricing growth"
  - "confirm pricing tiers"
  - "finalize pricing model"
  - "pricing sign-off growth"
---

# pricing-finaliser-growth

## Agent: Growth Lead

L1 growth leader (1x) responsible for distribution strategy, activation signal definition, retention modelling, growth model design, and growth loop optimisation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The pricing finaliser reviews the final pricing structure from a growth mechanics perspective, evaluating whether the price points, tier boundaries, and trial/freemium mechanics support acquisition velocity, activation rates, and expansion revenue without creating growth-inhibiting friction.

## When to Use

- When pricing is finalized and ready for launch but has not been reviewed for growth impact.
- When a pricing change is proposed and the growth team needs to assess funnel impact.
- When the freemium or trial conversion rate is below target and pricing structure may be a contributing factor.

## Workflow

1. **Review pricing structure**: Examine price points, tier boundaries, feature gating, trial length, and freemium limits against the growth model's assumptions.
2. **Assess activation friction**: Determine whether the pricing structure (paywalls, credit card requirements, feature gates) creates friction before users reach the activation moment.
3. **Model conversion impact**: Estimate the impact on signup-to-paid conversion rate and trial-to-paid conversion rate. Compare against the growth model's targets.
4. **Check expansion mechanics**: Verify that usage-based or seat-based pricing creates natural expansion triggers that drive net revenue retention above 100%.
5. **Deliver verdict**: Approve, approve-with-conditions, or reject the pricing from a growth perspective. Document specific concerns and recommended adjustments.

## Anti-Patterns

- **Gating before activation**: Requiring payment before users experience the core value moment kills activation rates. *Why*: users who have not experienced value cannot make an informed purchase decision.
- **Reviewing pricing in isolation**: Assessing price points without considering the full funnel (signup, activation, conversion, expansion) misses growth friction. *Why*: a reasonable price can still kill growth if it appears at the wrong funnel step.

## Output

**Success:**
- A growth pricing review with approval status, conversion impact estimate, activation friction assessment, expansion mechanic evaluation, and any conditions for approval.

**Failure:**
- Pricing launches without growth review and activation or conversion rates drop. Report the pricing element causing friction and the recommended adjustment.

## Related Skills

- [`pricing-strategy-growth`](../pricing-strategy-growth/SKILL.md) -- the strategy this skill reviews for final approval.
- [`growth-model-designer`](../growth-model-designer/SKILL.md) -- the growth model's conversion assumptions must align with pricing mechanics.
