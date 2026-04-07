---
name: growth-loop-activator
description: >
  This skill activates growth loops by implementing referral, viral, or content mechanics. Use when asked to build a referral system, implement sharing mechanics, or activate a viral loop. Also consider when the growth model identifies a loop to activate. Suggest when the growth loop optimiser identifies a loop that has not been implemented yet.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: complex
related-skills:
  - growth-loop-optimiser
  - growth-model-designer
  - instrumentation-implementer-growth
  - funnel-analyser-growth
---

# growth-loop-activator

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The growth loop activator implements the technical mechanics of a growth loop — referral programmes, sharing flows, viral invitations, user-generated content distribution, or product-led acquisition triggers — transforming the growth lead's loop design into working product features with full instrumentation.

## When to Use

- When the growth lead approves a loop design and it is ready for engineering implementation.
- When an existing referral or sharing mechanic needs technical overhaul to improve loop throughput.
- When the growth model identifies a new loop type (content, viral, product-led) to activate for the first time.
- When a loop's cycle time needs reduction through technical optimization (faster invite delivery, real-time reward attribution).

## Workflow

1. **Review loop design**: Consume the loop specification from the growth lead — trigger action, distribution mechanic, landing experience, and activation step. Clarify technical requirements and constraints.
2. **Design the technical architecture**: Define the referral code/link system, invite delivery mechanism (email, in-app, deeplink), reward attribution logic, and fraud prevention rules.
3. **Implement the trigger**: Build the UI and backend for the action that initiates the loop (share button, referral prompt, content publish). Ensure the trigger appears at the right moment in the user journey.
4. **Implement the distribution**: Build the invite/share delivery path. Implement deeplinks, attribution tracking, and landing page personalization for referred users.
5. **Implement reward mechanics**: Build the incentive system (both-sides rewards, milestone rewards, or intrinsic rewards). Implement fraud detection to prevent reward gaming.
6. **Instrument the loop**: Add tracking events at every node — trigger impression, trigger action, invite sent, invite opened, referred signup, referred activation, reward granted. These events enable loop throughput measurement.
7. **Test end-to-end**: Execute the full loop cycle in staging — from trigger through distribution, signup, activation, and reward. Verify all events fire correctly and the reward attributes to the right referrer.

## Anti-Patterns

- **No fraud prevention**: Launching a referral system without self-referral detection, duplicate account blocking, and reward caps invites abuse. *Why*: referral fraud can cost thousands in rewards while generating zero genuine new users.
- **Friction at the trigger**: Requiring multiple steps to share or refer (copy link, open email, compose message) reduces trigger conversion. *Why*: every additional step in the sharing flow halves the participation rate.
- **No attribution tracking**: Implementing the loop without tracking which referrer generated which new user makes it impossible to measure loop throughput or attribute rewards. *Why*: without attribution, you cannot compute viral coefficient or optimize the loop.
- **Implementing without instrumentation**: Building the loop mechanics without the events needed to measure each node blinds the team to bottlenecks. *Why*: you cannot optimize what you cannot measure at each node of the loop.

## Output

**Success:**
- A working growth loop implementation with trigger UI, distribution mechanic, reward system, fraud prevention, and full instrumentation at every loop node, deployed to staging with an end-to-end test report.

**Failure:**
- The loop implementation has technical gaps (broken deeplinks, missing attribution, reward mismatch). Report the failure points, the root cause, and the fix required before production deployment.

## Related Skills

- [`growth-loop-optimiser`](../../../data-growth/growth-lead/growth-loop-optimiser/SKILL.md) -- optimizes the loop this skill activates.
- [`growth-model-designer`](../../../data-growth/growth-lead/growth-model-designer/SKILL.md) -- the growth model defines which loops to activate.
- [`instrumentation-implementer-growth`](../instrumentation-implementer-growth/SKILL.md) -- implements the tracking events for the loop.
- [`funnel-analyser-growth`](../funnel-analyser-growth/SKILL.md) -- analyses conversion within the loop's funnel.
