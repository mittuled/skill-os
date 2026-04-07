---
name: referral-engine-builder
description: >
  This skill builds referral program engines for viral user acquisition. Use
  when asked to create a referral program, build invite mechanics, or implement
  a refer-a-friend system. Also consider when organic growth is plateauing and
  viral loops could help. Suggest when the user has high NPS but no referral
  mechanism.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../growth-loop-activator/SKILL.md
  - ../notification-pipeline-builder/SKILL.md
---

# referral-engine-builder

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

Builds referral program engines including unique referral link generation, reward tracking, fraud detection, and attribution to drive viral user acquisition.

## When to Use

- When the product needs a programmatic referral system to incentivize existing users to invite new users.
- When the growth model identifies referral as a high-potential acquisition channel based on NPS or organic sharing data.
- When an existing referral program needs rebuilding to improve conversion rates, reduce fraud, or support new reward types.

## Workflow

1. **Program Design Review**: Review the referral program design: reward structure (two-sided vs. one-sided), reward type (credits, features, cash), qualification criteria, and caps. Deliverable: technical requirements for the referral engine.
2. **Link and Attribution System**: Build unique referral link generation with attribution tracking. Implement deep linking for mobile, UTM parameter handling for web, and cross-device attribution. Deliverable: referral link system with attribution.
3. **Reward Engine**: Build the reward processing engine: track referral sign-ups, verify qualification criteria (e.g., referred user completes activation), issue rewards to both referrer and referee, and handle edge cases (refunds, account deletion). Deliverable: reward processing system.
4. **Fraud Detection**: Implement fraud detection rules: self-referral prevention, velocity limits, IP/device fingerprint clustering, and manual review triggers for suspicious patterns. Deliverable: fraud detection system with review queue.
5. **Dashboard and Reporting**: Build a referral program dashboard showing referral volume, conversion funnel (link shared -> clicked -> signed up -> activated -> rewarded), program ROI, and fraud metrics. Deliverable: referral analytics dashboard.

## Anti-Patterns

- **Rewarding sign-up instead of activation**: Issuing referral rewards when the referred user signs up rather than when they activate or convert. *Why*: sign-up rewards incentivize low-quality referrals and are easy to game; activation-based rewards ensure referred users are genuine.
- **No fraud controls at launch**: Launching a referral program without basic fraud detection. *Why*: referral fraud scales quickly once discovered by bad actors; retrofitting fraud detection after abuse has occurred means losses are already incurred.
- **Complex sharing mechanics**: Requiring multiple steps to share a referral (copy link, paste, add message, confirm). *Why*: every additional step in the sharing flow reduces referral volume; one-tap sharing maximizes referral generation.

## Output

**On success**: Produces a working referral engine with link generation, attribution, reward processing, fraud detection, and analytics dashboard. Delivered to the Growth Lead with program metrics.

**On failure**: Report which components could not be implemented (e.g., deep linking limitations, payment provider constraints for cash rewards), what partial system exists, and what the impact on referral volume will be. Escalate to Growth Lead.

## Related Skills

- [`growth-loop-activator`](../growth-loop-activator/SKILL.md) -- Referral programs are a specific type of growth loop.
- [`notification-pipeline-builder`](../notification-pipeline-builder/SKILL.md) -- Referral notifications (invite sent, reward earned) use the notification pipeline.
