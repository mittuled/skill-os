# Framework: Onboarding Sequence Designer

Defines the structural framework for designing post-signup email sequences aligned to activation milestones.

## Sequence Architecture

### Trigger Model

| Trigger Type | When to Use | Example |
|-------------|------------|---------|
| Behavioural | User completes or skips a milestone | Send "connect your data source" email when user has signed up but not connected in 24h |
| Time-based | Fallback when behavioural data unavailable | Send day-3 reminder if no milestone events received |
| Negative | User has NOT done something within a window | Send "stuck?" email if no login 48h after signup |

### Milestone Map Template

| Milestone | Action | Prerequisite | Typical Time | Email if Skipped |
|-----------|--------|-------------|-------------|-----------------|
| M0 | Account created | None | 0h | Welcome email (immediate) |
| M1 | First setup step | M0 | 0-2h | Setup nudge (24h after M0) |
| M2 | Core action completed | M1 | 2-48h | Value preview (48h after M0) |
| M3 | Activation moment | M2 | 1-7 days | Stuck-user help (72h after M0) |
| M4 | First value realised | M3 | 3-14 days | Celebration + next step |

### Suppression Rules

1. Skip any email where the user has already completed the relevant milestone
2. Suppress all onboarding emails once the user reaches the activation moment
3. Never send more than 1 onboarding email per 24-hour window
4. Suppress if user has an open support ticket

## Copy Principles

1. **One CTA per email**: each email drives exactly one milestone action
2. **Show, don't tell**: include a screenshot or GIF of the next step
3. **Progress framing**: "You're 2 steps away from [value]" not "Complete your setup"
4. **Personalise by state**: reference what the user has already done, not just their name
