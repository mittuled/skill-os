# Framework: Onboarding Flow Design

Defines the progressive disclosure model, activation journey mapping, and measurement approach for building onboarding flows that maximize activation rates.

## Activation Journey Map

Before building any UI, define the activation journey:

| Step # | Step Name | Type | Goal | Skip Allowed? |
|--------|-----------|------|------|--------------|
| 1 | Welcome / intent capture | Optional | Learn user segment for branching | Yes |
| 2 | [Required setup step] | Required | Enable core functionality | No |
| 3 | [Value delivery step] | Required | User sees the product's core value | No |
| 4 | [Activation moment action] | Required | User completes the activation signal action | No |
| 5 | [Reinforcement step] | Optional | Encourage repeat usage | Yes |

**Rule**: Minimize required steps. Every required step is a potential drop-off point. Defer optional profile and configuration steps to contextual prompts after activation.

## Progressive Disclosure Principles

1. **Show only the next needed step**: Do not display the entire checklist on step 1. Reveal steps as the user completes prior ones.
2. **Maximize time-to-first-value**: Steps 1-3 should take ≤5 minutes for the median user.
3. **Branch by user segment**: If the product serves multiple personas (e.g., individual vs. team), branch the flow at intake to show relevant steps.
4. **Resume capability**: If a user exits mid-onboarding, they must resume at the same step — not restart from the beginning.
5. **Skip paths for power users**: Any user identifying as experienced must be able to reach the product directly. Mandatory walkthroughs kill experienced-user activation.

## Activation Rate Benchmarks

| Product Type | Good Activation Rate | Target Measurement Window |
|-------------|---------------------|--------------------------|
| Consumer mobile | ≥40% | Within 7 days of signup |
| SaaS / B2B tool | ≥25% | Within 14 days of signup |
| Marketplace (demand) | ≥30% | Within 7 days of signup |
| Developer tool | ≥20% | Within 7 days of first code execution |

If current activation rate is below benchmark, the onboarding flow is a priority for redesign.

## Drip Sequence Architecture

Connect onboarding milestones to triggered notification sequences:

| Trigger | Notification | Channel | Timing |
|---------|-------------|---------|--------|
| Signup completed | Welcome email | Email | Immediately |
| No onboarding activity after 24h | Reminder nudge | Email | T+24h after signup |
| Onboarding step N incomplete after 48h | Step-specific prompt | Email / Push | T+48h after step N viewed |
| Activation moment NOT completed at D3 | Activation encouragement | Email | D+3 |
| Activation moment completed | Success email + next step | Email | Immediately after activation |

## Measurement Requirements

Each onboarding step must fire a tracking event. Minimum required metrics:

| Metric | Definition | Dashboard View |
|--------|-----------|---------------|
| Step N completion rate | Users completing step N / users entering step N | Funnel chart per step |
| Time-to-activation | Median hours from signup_completed to activation_event | Distribution histogram |
| Onboarding completion rate | Users reaching activation / users who started onboarding | Summary KPI |
| Drop-off by step | Absolute user loss per step | Ranked drop-off table |
