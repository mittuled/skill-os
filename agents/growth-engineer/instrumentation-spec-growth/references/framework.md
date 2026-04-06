# Framework: Growth Instrumentation Specification

Defines the structure, naming conventions, and completeness requirements for the growth instrumentation spec document.

## Spec Document Architecture

A complete growth instrumentation spec has six event sections and one traceability matrix:

| Section | Events Covered | Purpose |
|---------|---------------|---------|
| 1. Acquisition events | First touch, landing page view, UTM capture, signup started/completed | Channel attribution and signup funnel |
| 2. Activation events | Each onboarding step, activation moment | Onboarding funnel and activation rate |
| 3. Experiment events | experiment_assigned (standard schema), per-experiment goal events | A/B test analysis |
| 4. Loop events | Trigger impression/action, invite sent/opened, referred signup/activation, reward granted | Viral coefficient and loop attribution |
| 5. Retention events | Session start, key engagement actions, re-engagement responses | Retention modelling |
| 6. Revenue events | Trial started, plan selected, payment completed, subscription changed | Revenue funnel |

## Event Schema Standard

For each event, the spec must define:

```yaml
event_name: signup_completed          # snake_case, past tense
section: acquisition
trigger: "User submits signup form and account is created"
firing_side: client                   # client | server | hybrid
properties:
  - name: user_id
    type: string
    required: true
    description: "Stable user identifier assigned at account creation"
  - name: signup_method
    type: enum [email, google_oauth, github_oauth]
    required: true
    description: "Authentication method used"
  - name: utm_source
    type: string
    required: false
    description: "UTM source from first-touch attribution storage"
  - name: experiment_id
    type: string
    required: false
    description: "Populated when signup occurs within an experiment context"
```

## Experiment Event Standard Schema

All experiments use this immutable schema for the assignment event:

| Property | Type | Required | Notes |
|----------|------|----------|-------|
| experiment_id | string | Yes | Unique experiment identifier (e.g., exp_2024_onboarding_v2) |
| variant_id | string | Yes | Variant label (e.g., "control", "treatment_A") |
| user_id | string | Yes | Stable user identifier |
| assignment_timestamp | ISO 8601 | Yes | Time of assignment, not event processing |
| assignment_method | enum | Yes | "client_side" or "server_side" |

**Never deviate from this schema.** Cross-experiment analysis depends on a uniform structure.

## Traceability Matrix

The spec must close with a matrix linking every growth metric to the events required to compute it:

| Growth Metric | Required Events | Computed As |
|--------------|----------------|-------------|
| Activation rate | signup_completed, activation_event | COUNT(activation_event) / COUNT(signup_completed) per cohort |
| Viral coefficient (k) | invite_sent, referred_signup | COUNT(referred_signup) / COUNT(inviting_users) |
| Trial-to-paid conversion | trial_started, subscription_created | COUNT(subscription_created within trial window) / COUNT(trial_started) |
| Channel CAC | signup_completed (with utm_source), ad_spend_by_channel | ad_spend / COUNT(signups) grouped by utm_source |

Any metric in the growth model that cannot be traced to events in the spec is a gap that must be closed before the spec is approved.

## Spec Review Gate

The spec is only complete when:
1. All metrics in the growth model have a traceability entry
2. No event name conflicts with the product instrumentation spec (check against it)
3. Experiment event schema matches the standard exactly
4. Privacy review confirms consent gating for user-level tracking in applicable jurisdictions
