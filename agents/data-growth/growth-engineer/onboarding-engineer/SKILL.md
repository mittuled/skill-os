---
name: onboarding-engineer
description: >
  This skill builds user onboarding flows that drive activation. Use when asked
  to create an onboarding experience, improve first-run flow, or increase
  activation rates. Also consider when activation metrics show users dropping
  off before reaching the aha moment. Suggest when the user has sign-up but
  no structured onboarding.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../notification-pipeline-builder/SKILL.md
  - ../funnel-analyser-growth/SKILL.md
  - ../paywall-builder/SKILL.md
triggers:
  - "engineer onboarding flow"
  - "build onboarding experience"
  - "implement onboarding steps"
  - "onboarding UX engineering"
  - "activation flow engineering"
---

# onboarding-engineer

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

Builds user onboarding flows that guide new users from sign-up to activation, implementing progressive disclosure, contextual guidance, and milestone tracking to maximize activation rates.

## When to Use

- When the product needs a structured onboarding experience to guide users from registration to the activation moment.
- When activation funnel analysis shows significant drop-off between sign-up and first value delivery.
- When launching a new product surface (mobile app, new user type, enterprise tier) that requires tailored onboarding.

## Workflow

1. **Activation Definition**: Define the activation moment (the action that correlates with long-term retention). Map the steps from sign-up to activation. Identify required vs. optional steps. Deliverable: activation journey map with step definitions.
2. **Flow Design**: Design the onboarding flow with progressive disclosure: show only what the user needs at each step. Include skip paths for experienced users. Define branching logic for different user segments. Deliverable: onboarding flow specification.
3. **Implementation**: Build the onboarding UI components: welcome screens, setup wizards, checklists, tooltips, and contextual guidance. Implement state management to track user progress and resume where they left off. Deliverable: implemented onboarding flow.
4. **Drip Integration**: Connect onboarding milestones to the notification pipeline for drip sequences: welcome email, incomplete setup reminders, activation encouragement, and post-activation next steps. Deliverable: onboarding drip sequences.
5. **Measurement**: Instrument each onboarding step with tracking events. Build a funnel dashboard showing step-by-step conversion and time-to-activation. Set up alerts for significant conversion drops. Deliverable: onboarding funnel dashboard.

## Anti-Patterns

- **Information overload on first run**: Showing all features and configuration options during initial onboarding. *Why*: cognitive overload causes abandonment; progressive disclosure that reveals features as needed produces higher activation rates.
- **Mandatory onboarding with no skip**: Forcing all users through every onboarding step with no way to skip or defer. *Why*: experienced users and repeat sign-ups are frustrated by mandatory walkthroughs; provide skip paths for users who want to self-serve.
- **Onboarding without measurement**: Building an onboarding flow without step-by-step funnel tracking. *Why*: without measurement, you cannot identify which step has the highest drop-off or whether changes improve activation.

## Output

**On success**: Produces an implemented onboarding flow with drip integration and funnel dashboard showing step-by-step conversion. Delivered to the Growth Lead with baseline activation metrics.

**On failure**: Report which onboarding steps could not be implemented (e.g., missing product features, design assets), what partial flow exists, and what the impact on activation will be. Escalate to Growth Lead.

## Related Skills

- [`notification-pipeline-builder`](../notification-pipeline-builder/SKILL.md) -- Notification pipelines deliver onboarding drip sequences.
- [`funnel-analyser-growth`](../funnel-analyser-growth/SKILL.md) -- Funnel analysis measures onboarding effectiveness and identifies bottlenecks.
