---
name: paywall-builder
description: >
  This skill builds paywall and monetization gates for freemium conversion. Use
  when asked to implement a paywall, build upgrade prompts, or gate features
  behind paid plans. Also consider when the product has no monetization
  touchpoints. Suggest when the user has a freemium model but no paywall
  implementation.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../onboarding-engineer/SKILL.md
  - ../funnel-analyser-growth/SKILL.md
---

# paywall-builder

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

Builds paywall and monetization gate implementations that convert free users to paid plans, including feature gating, upgrade prompts, and payment flow integration.

## When to Use

- When the product needs paywall implementation to gate premium features behind paid plans.
- When A/B testing different paywall strategies (hard paywall, metered, feature-gated) to optimize conversion.
- When adding new premium features that require integration with the existing paywall and entitlement system.

## Workflow

1. **Entitlement Mapping**: Map product features to plan tiers (free, pro, enterprise). Define which features are gated, which are metered (usage limits), and which are fully open. Deliverable: entitlement matrix by plan tier.
2. **Gate Implementation**: Build feature gates that check user entitlements and display appropriate upgrade prompts when users hit limits. Implement both hard gates (feature blocked) and soft gates (usage warnings). Deliverable: feature gating system.
3. **Upgrade Flow**: Build the upgrade flow: plan comparison, pricing display, payment form integration (Stripe, RevenueCat), and confirmation. Optimize for minimal friction (pre-filled forms, one-click upgrade). Deliverable: working upgrade flow.
4. **Instrumentation**: Track paywall impressions, upgrade clicks, payment starts, payment completions, and plan changes. Build a paywall performance dashboard showing conversion by feature gate, plan, and user segment. Deliverable: paywall analytics dashboard.
5. **Optimization Setup**: Implement A/B test infrastructure for paywall variants (copy, timing, placement, pricing). Define the experiment framework and success metrics. Deliverable: A/B test framework for paywall optimization.

## Anti-Patterns

- **Paywalling before activation**: Showing upgrade prompts before users have experienced the product's core value. *Why*: users who have not reached the aha moment have no motivation to pay; premature paywalls increase churn rather than revenue.
- **Hard paywall on discovery features**: Blocking features that help users discover the product's value behind a hard paywall. *Why*: users cannot evaluate what they are paying for, reducing conversion and increasing refund rates.
- **No free tier value**: Gating so aggressively that the free tier provides no meaningful value. *Why*: an empty free tier produces no word-of-mouth growth and no upgrade pipeline; free users must get enough value to want more.

## Output

**On success**: Produces a working paywall system with entitlement mapping, feature gates, upgrade flow, and analytics dashboard. Delivered to the Growth Lead with baseline conversion metrics.

**On failure**: Report which paywall components could not be implemented (e.g., payment provider integration issues, entitlement system limitations), what partial gating exists, and what the revenue impact is. Escalate to Growth Lead.

## Related Skills

- [`onboarding-engineer`](../onboarding-engineer/SKILL.md) -- Onboarding flows should demonstrate premium value before paywall exposure.
- [`funnel-analyser-growth`](../funnel-analyser-growth/SKILL.md) -- Funnel analysis measures paywall conversion and identifies optimization opportunities.
