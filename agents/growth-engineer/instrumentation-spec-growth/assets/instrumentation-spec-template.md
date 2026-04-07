# Growth Instrumentation Spec

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | instrumentation-spec-growth |
| Product surfaces in scope | [Web / iOS / Android / Server — list all] |
| Reviewed by | [instrumentation-clarity-reviewer — name / date] |

## Executive Summary

[2-3 sentences describing the scope of this spec — how many events, which growth metrics it enables, and any notable gaps or deferred items.
GUIDANCE: Example — "This spec defines 24 growth events across acquisition (7), activation (5), experiment (4), loop (5), and revenue (3) stages. All metrics in the Q1 growth model are traceable to at least one event. Privacy review confirmed consent gating is required for user-level retention events in the EU; consent check is gated on the activation event before retention tracking begins."]

## 1. Acquisition Events

[Define all events that track the path from first touch to signup completion.
GUIDANCE:
- Good: Each event has a full schema table with event_name, trigger condition, firing side, and all properties with types and required flags.
- Bad: "We'll track signup events." — no schema.
- Format: One subsection per event with YAML-style schema]

### 1.1 landing_page_viewed

| Field | Value |
|-------|-------|
| Trigger | User loads any landing page with a UTM parameter present |
| Firing side | Client |

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| anonymous_id | string | Yes | Pre-auth identifier |
| page_path | string | Yes | URL path of the landing page |
| utm_source | string | No | From URL parameter |
| utm_medium | string | No | From URL parameter |
| utm_campaign | string | No | From URL parameter |

### 1.2 signup_completed

[Repeat schema structure for each event]

## 2. Activation Events

[Define events for each onboarding step and the activation moment.
GUIDANCE: The activation event schema must match the activation signal definition exactly (same event name, same properties).]

### 2.1 onboarding_step_completed

| Field | Value |
|-------|-------|
| Trigger | User completes any required onboarding step |
| Firing side | Client |

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| user_id | string | Yes | Stable user identifier (post-auth) |
| step_name | string | Yes | Canonical step identifier |
| step_number | integer | Yes | Ordinal position in onboarding flow |
| time_on_step_seconds | integer | No | Elapsed time on this step |

### 2.2 [activation_event_name]

[Insert the specific activation moment event here — name must match the activation signal definition]

## 3. Experiment Events

[Define the standard assignment event and goal events for each active experiment.
GUIDANCE: The experiment_assigned schema must exactly match the standard schema in the framework. Do not add or remove properties.]

### 3.1 experiment_assigned (standard — do not modify)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| experiment_id | string | Yes | Unique experiment identifier |
| variant_id | string | Yes | Variant label |
| user_id | string | Yes | Stable user identifier |
| assignment_timestamp | ISO 8601 | Yes | Time of assignment |
| assignment_method | enum | Yes | "client_side" or "server_side" |

### 3.2 [Experiment 1 name] — goal event

| Experiment | [experiment_id] |
|-----------|----------------|
| Goal event | [existing semantic event to use as goal] |
| Additional properties | experiment_id, variant_id (attach to existing event) |

## 4. Loop Events

[Define all events for each active growth loop.
GUIDANCE: Every loop must have referrer_id linkage from invite_sent through referred_activation. Without this, viral coefficient is uncomputable.]

### Loop: [Loop Name]

| Node | Event Name | Key Properties |
|------|-----------|---------------|
| Trigger impression | [event] | loop_id, user_id, placement |
| Trigger action | [event] | loop_id, user_id, invite_id |
| Invite sent | invite_sent | loop_id, referrer_id, invite_id, channel |
| Invite opened | invite_opened | loop_id, referrer_id, invite_id |
| Referred signup | signup_completed | loop_id, referrer_id, invite_id |
| Referred activation | [activation_event] | loop_id, referrer_id |
| Reward granted | referral_reward_granted | loop_id, referrer_id, reward_type, amount |

## 5. Retention Events

[Define session and engagement events used for retention modelling.
GUIDANCE: Include consent gate requirement for user-level retention tracking in GDPR jurisdictions.]

### 5.1 session_started

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| user_id | string | Yes | |
| session_id | string | Yes | |
| platform | enum | Yes | web / ios / android |
| days_since_signup | integer | Yes | Used for D1/D7/D30 retention computation |

## 6. Revenue Events

[Define trial and purchase events.
GUIDANCE: subscription_created must include plan, price, and billing_cycle for MRR computation.]

### 6.1 subscription_created

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| user_id | string | Yes | |
| plan | string | Yes | Plan identifier |
| price_usd | float | Yes | Monthly equivalent price |
| billing_cycle | enum | Yes | "monthly" / "annual" |
| trial_converted | boolean | Yes | True if converting from trial |
| experiment_id | string | No | Present if conversion is within experiment |

## 7. Traceability Matrix

[Map every growth metric to the events required to compute it. Every metric in the growth model must appear here.
GUIDANCE: Any metric without a complete event mapping is a spec gap. Add the missing events before approval.]

| Growth Metric | Formula | Required Events |
|--------------|---------|----------------|
| Activation rate | activated_users / signup_users | signup_completed, [activation_event] |
| D7 retention | active_day_7_users / signup_users | signup_completed, session_started |
| Viral coefficient (k) | referred_signups / inviting_users | invite_sent, signup_completed (with referrer_id) |
| Free-to-paid conversion | paid_users / signup_users | signup_completed, subscription_created |
| Trial-to-paid conversion | paid_users / trial_starts | [trial_started], subscription_created |
| [Add all growth model metrics] | | |

## Recommendations

[Document any spec gaps, deferred events, and open decisions requiring stakeholder input.]

| Priority | Item | Owner | Status |
|----------|------|-------|--------|
| P1 | [e.g., Privacy consent gate implementation before retention events] | [Eng] | [Open] |

## Appendices

### A. Methodology

[Growth model used as source of measurement requirements. Product instrumentation spec version checked for event name conflicts. Privacy review date and outcome.]

### B. Supporting Data

[List of events checked against product instrumentation spec for conflicts. Growth model metrics list used to drive traceability matrix.]
