---
name: onboarding-sequence-designer
description: Designs post-signup email sequences that drive users to the activation moment and reduce time-to-value. Use when asked to onboarding sequence designer. Suggest when relevant.
department: marketing
agent: lifecycle-email-marketing-manager
version: 1.0.0
complexity: medium
related-skills:
  - email-performance-optimiser
  - nurture-campaign-builder
  - retention-email-designer
  - transactional-email-designer
triggers:
  - "design onboarding email sequence"
  - "build user onboarding emails"
  - "new user email flow"
  - "activation email sequence"
  - "onboarding drip design"
---

# onboarding-sequence-designer

## Agent: Social Media Manager

L2 lifecycle and email marketing manager responsible for onboarding sequences, nurture campaigns, retention emails, re-engagement, and transactional email design.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Designs the post-signup email sequence aligned to the activation moment, guiding new users through setup and first-value milestones to maximise conversion from signup to active customer.

## When to Use

- A new product or feature launches with a self-serve signup flow that needs guided onboarding.
- Activation rates are below target and data shows users dropping off before reaching the first-value milestone.
- The product team redefines the activation moment and the existing onboarding sequence no longer maps to the right milestones.
- A new user segment with different use cases requires a tailored onboarding path.

## Workflow

1. Confirm the activation moment with the product team: the specific user action that correlates with long-term retention.
2. Map the steps between signup and activation: required setup tasks, optional configuration, and the first-value experience.
3. Design the email sequence: welcome email, milestone-triggered nudges, stuck-user reminders, and an activation celebration. Define cadence and send conditions.
4. Write email copy that is action-oriented: each email has one clear CTA that moves the user toward the next milestone.
5. Configure behavioural triggers in the email platform: send emails based on what the user has and has not done, not just time elapsed.
6. Build suppression rules to skip emails when the user has already completed the relevant milestone.
7. Launch to new signups. Monitor open rates, click rates, and milestone completion rates per email in the sequence.
8. Report weekly on onboarding funnel metrics: signup-to-activation rate, median time-to-activation, and drop-off points. Recommend copy or sequence adjustments.

## Anti-Patterns

- **Using time-based sends instead of behaviour-based triggers.** *Why*: Sending email 3 on day 5 regardless of user progress delivers irrelevant content to users who are ahead or behind.
- **Including multiple CTAs in a single onboarding email.** *Why*: Competing actions create decision paralysis; each email should drive exactly one next step.
- **Designing the sequence without product team input on the activation moment.** *Why*: If the emails guide users toward the wrong milestone, activation rates will not improve regardless of email quality.
- **Stopping the sequence at activation without a handoff to retention.** *Why*: Users who activate but receive no follow-up are at risk of churning before forming a habit.

## Output

**Success artifacts:**
- Onboarding sequence map with triggers, milestones, and email content
- Configured automation with behavioural triggers and suppression rules
- Weekly onboarding funnel report with drop-off analysis
- Activation rate trend dashboard segmented by cohort

**Failure reporting:**
- Flag activation rate drops exceeding 10% week-over-week within 48 hours
- Escalate email deliverability or trigger misconfiguration issues to the marketing lead immediately

## Related Skills

*No related skills defined yet.*
- [`email-performance-optimiser`](../email-performance-optimiser/SKILL.md) — sibling skill under the same agent — combine with email-performance-optimiser for end-to-end coverage
- [`nurture-campaign-builder`](../nurture-campaign-builder/SKILL.md) — sibling skill under the same agent — combine with nurture-campaign-builder for end-to-end coverage
- [`retention-email-designer`](../retention-email-designer/SKILL.md) — sibling skill under the same agent — combine with retention-email-designer for end-to-end coverage
- [`transactional-email-designer`](../transactional-email-designer/SKILL.md) — sibling skill under the same agent — combine with transactional-email-designer for end-to-end coverage
