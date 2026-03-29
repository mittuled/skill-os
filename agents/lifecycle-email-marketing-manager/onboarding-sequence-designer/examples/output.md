# Onboarding Email Sequence Plan: TaskFlow

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-03-29 |
| Author | Lifecycle Email Marketing Manager |
| Version | 1.0 |
| Status | Draft |
| Skill | onboarding-sequence-designer |

## Executive Summary

Six-email onboarding sequence guiding TaskFlow signups from account creation to the activation moment (first project with teammate invited). Targeting 30% signup-to-activation rate, up from 18% baseline, using behaviour-triggered emails focused on the three key drop-off points.

## Activation Moment Definition

**Action**: User creates their first project AND invites at least one teammate.
**Time window**: Within 5 days of signup.
**Retention correlation**: Users who activate within 5 days retain at 4x the rate of non-activators (72% vs 18% 90-day retention).

## Milestone Map

| ID | Action | Prerequisite | Typical Time | Email if Skipped |
|----|--------|-------------|-------------|-----------------|
| M0 | Account created | None | 0h | Welcome email (immediate) |
| M1 | Profile completed | M0 | 0-1h | Profile nudge (24h if skipped) |
| M2 | First project created | M0 | 0-48h | Project creation nudge (48h if skipped) |
| M3 | First task added | M2 | 0-24h | Task nudge (24h after M2) |
| M4 | Teammate invited (ACTIVATION) | M2 | 1-5 days | Invite nudge (48h after M2) |

## Email Sequence

### Email 1: Welcome
- **Trigger**: Account created (immediate)
- **Subject**: Your first project is 60 seconds away
- **Preview**: Here's the fastest path to getting your team organised
- **Body**: Welcome message showing a 3-step visual: create project, add tasks, invite team. One prominent CTA.
- **CTA**: Create your first project
- **Suppression**: None (everyone gets this)

### Email 2: Project Creation Nudge
- **Trigger**: 48 hours after signup, user has NOT created a project
- **Subject**: Most teams start with a simple project
- **Preview**: No templates needed — just name it and go
- **Body**: Screenshot of project creation flow. Address the "I'll set it up properly later" objection by showing a 30-second project creation.
- **CTA**: Create a project now
- **Suppression**: Skip if user has already created a project (M2 complete)

### Email 3: First Task Nudge
- **Trigger**: 24 hours after project creation, user has NOT added a task
- **Subject**: Your project is waiting for its first task
- **Preview**: Start with one task — you can always add more later
- **Body**: Show how a single task in TaskFlow looks. Emphasise that starting small is the right approach.
- **CTA**: Add your first task
- **Suppression**: Skip if user has already added a task (M3 complete)

### Email 4: Teammate Invite Nudge
- **Trigger**: 48 hours after project creation, user has NOT invited anyone
- **Subject**: TaskFlow works best with your team
- **Preview**: Invite one person — it takes 10 seconds
- **Body**: Show the before/after: solo project vs. collaborative project with assignments and comments. Social proof: "Teams that collaborate in TaskFlow ship 2x faster."
- **CTA**: Invite a teammate
- **Suppression**: Skip if user has already invited a teammate (M4 complete / ACTIVATED)

### Email 5: Stuck User Help
- **Trigger**: 96 hours after signup, user has logged in but not reached M2
- **Subject**: Need help getting started?
- **Preview**: Here are three ways teams use TaskFlow in their first week
- **Body**: Three common use cases (sprint planning, client projects, personal tasks) with one-click project templates for each.
- **CTA**: Start with a template
- **Suppression**: Skip if user has reached M2 or beyond

### Email 6: Activation Celebration
- **Trigger**: User reaches activation moment (M4 complete)
- **Subject**: Your team is live on TaskFlow
- **Preview**: Here's what to explore next
- **Body**: Congratulate the achievement. Show three next-step features (views, integrations, automations) to bridge into retention.
- **CTA**: Explore team features
- **Suppression**: Only sent to activated users

## Suppression Rules

| Rule | Condition | Action |
|------|-----------|--------|
| Milestone completed | User has completed the milestone the email targets | Skip that email |
| Already activated | User has reached M4 | Stop all onboarding emails; send celebration |
| Max frequency | User received an onboarding email < 24h ago | Delay next email by 24h |
| Open support ticket | User has an active support conversation | Pause onboarding sends until resolved |
| Unsubscribed | User opts out of onboarding emails | Stop all onboarding sends |

## Recommendations

1. **P1**: Instrument M0-M4 milestone events in the product analytics stack and connect them to the email platform as behavioural triggers before launch.
2. **P1**: Set up A/B test on Email 2 subject line — the project creation drop-off is the biggest leak (40% of users never create a project).
3. **P2**: Create a parallel sequence for users who sign up from a teammate's invite link (they already have social context — skip straight to task creation).
4. **P2**: Add in-app tooltips that reinforce the email CTAs so users arriving from email see consistent guidance.
5. **P3**: After 60 days, analyse activation rates by email engagement pattern to identify which emails drive the most milestone completions.
