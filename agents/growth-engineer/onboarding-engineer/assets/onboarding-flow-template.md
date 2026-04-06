# Onboarding Flow Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | onboarding-engineer |
| Product surface | [Web / iOS / Android] |
| Target user segment | [e.g., Individual / Team / Enterprise] |

## Executive Summary

[2-3 sentences describing the onboarding flow design, target activation moment, and projected activation rate improvement.
GUIDANCE: Example — "The new onboarding flow reduces required steps from 6 to 3, eliminating mandatory profile setup and deferred team invite from the critical path. The activation moment (first dashboard created) is reachable in ≤3 minutes. Expected activation rate improvement: from 22% to ≥35% within 7 days of signup based on removing the 2 highest drop-off steps."]

## Activation Moment Definition

[State the activation moment this flow is designed to deliver users to.
GUIDANCE: Must match the activation signal definition exactly. This section is the north star for all step design decisions.]

**Activation signal**: A user is activated when they **[event_name]** **[threshold]** time(s) within **[window]** days of signup.

**Current activation rate**: [%] within [N] days
**Target activation rate**: [%] within [N] days (benchmark: [PLG/Consumer/SaaS benchmark])

## Activation Journey Map

[Document every step in the onboarding flow with type (required/optional), goal, and skip behaviour.
GUIDANCE:
- Good: "Step 2 (Required): User connects their data source. Goal: Enable the core analysis feature. Skip: Not allowed — the product cannot deliver value without a data source connected."
- Bad: "We have a few setup steps before the user can start."
- Format: Table with all steps]

| Step # | Step Name | Type | Goal | Skip Allowed? | Estimated Time |
|--------|-----------|------|------|--------------|---------------|
| 1 | [Step name] | [Required / Optional] | [What this step achieves] | [Yes / No] | [~N minutes] |
| 2 | | | | | |
| [Activation step] | [Activation moment action] | Required | User completes activation signal | No | [~N minutes] |

**Total time-to-activation (estimated)**: [N minutes for median user]

## Flow Design: Branching Logic

[Describe any branching in the flow based on user segment or intake response.
GUIDANCE:
- Good: "Users who select 'Team' at step 1 see a team invite step (step 3a) before activation. Users who select 'Individual' skip directly from step 2 to the activation step."
- Bad: "We might add different paths later."
- Format: Decision tree or table]

| Branch Condition | Path |
|-----------------|------|
| Default (no condition) | Steps [1 → 2 → activation] |
| User selects [segment A] | Steps [1 → 2a → activation] |
| User selects [segment B] | Steps [1 → 2 → 3b → activation] |

## Drip Sequence Plan

[Map onboarding milestones to triggered notification sequences.
GUIDANCE: Every required step that users can stall on needs a recovery drip.]

| Trigger | Notification Type | Channel | Timing | Message Goal |
|---------|-----------------|---------|--------|-------------|
| signup_completed | Welcome email | Email | Immediately | Orient user, confirm next step |
| No activity at T+24h | Reminder | Email | T+24h | Return user to onboarding |
| Stuck at step [N] for 48h | Step-specific nudge | Email / Push | T+48h at step N | Remove the specific blocker |
| Activation moment NOT completed at D3 | Activation encouragement | Email | D+3 | Re-engage with value promise |
| Activation completed | Success + next step | Email | Immediately | Celebrate + reinforce usage |

## Instrumentation Plan

[List every tracking event the onboarding flow must fire.
GUIDANCE: Every step must have a corresponding onboarding_step_completed event with step_name.]

| Step | Event | Properties |
|------|-------|-----------|
| Flow start | onboarding_started | user_id, segment, variant (if A/B) |
| Each step | onboarding_step_completed | user_id, step_name, step_number, time_on_step_seconds |
| Skip action | onboarding_step_skipped | user_id, step_name |
| Flow exit | onboarding_abandoned | user_id, last_step_viewed |
| Activation | [activation_event_name] | [per activation signal definition] |

## Baseline Metrics and Targets

[Document current funnel metrics and targets. Required before building to establish what "success" means.
GUIDANCE: If no baseline exists, establish one by monitoring the current experience for 2 weeks before shipping the new flow.]

| Metric | Current Baseline | Target | Timeline |
|--------|-----------------|--------|---------|
| Step [N] completion rate | [%] | [%] | [Date] |
| Activation rate (D7) | [%] | [%] | [Date] |
| Median time-to-activation | [N hours] | [N hours] | [Date] |

## Recommendations

[Prioritized list of implementation decisions.
GUIDANCE: P1 = required for launch; P2 = A/B test to run post-launch; P3 = longer-term iteration]

| Priority | Recommendation | Owner | Timeline |
|----------|---------------|-------|---------|
| P1 | [e.g., Confirm skip path exists for users with existing data] | [Growth Eng] | [Before launch] |
| P2 | [e.g., A/B test step count (3 steps vs. 2 steps)] | [Growth Eng] | [30 days post-launch] |

## Appendices

### A. Methodology

[Activation moment source: activation-signal-definer output. Drop-off analysis source: funnel-analyser-growth report. Drip provider: [SendGrid / Postmark / other].]

### B. Supporting Data

[Current onboarding funnel conversion data by step. User research insights (quote interviews or survey data that informed progressive disclosure decisions).]
