# Framework: Growth Instrumentation Implementation

Defines the implementation standards for growth tracking events, experiment instrumentation, and attribution pipelines.

## Event Implementation Standard

Every growth event must include these base properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| event_name | string | Yes | Snake_case, past tense (e.g., signup_completed) |
| user_id | string | Yes | Stable identifier; anonymous_id for pre-auth events |
| timestamp | ISO 8601 | Yes | Client-side event time |
| session_id | string | Yes | Session identifier for journey stitching |
| platform | enum | Yes | web / ios / android / server |
| utm_source | string | Conditional | Required for acquisition events; null for post-signup |
| utm_medium | string | Conditional | Same as utm_source |
| utm_campaign | string | Conditional | Same as utm_source |
| experiment_id | string | Conditional | Required when event fires in an experiment context |
| variant_id | string | Conditional | Required alongside experiment_id |

## Experiment Instrumentation Pattern

Every A/B experiment requires exactly two event types:

**1. Assignment event** (fires once per user per experiment):
```
event: experiment_assigned
properties:
  experiment_id: "exp_2024_onboarding_v2"
  variant_id: "control" | "treatment_A" | ...
  user_id: string
  assignment_timestamp: ISO 8601
  assignment_method: "client" | "server"
```

**2. Goal event** (fires when the conversion action occurs):
- Use the existing semantic event (e.g., `onboarding_completed`, `subscription_created`)
- Attach `experiment_id` and `variant_id` as properties on the existing event
- Do NOT create a new goal event — link to the existing semantic event

## Attribution Pipeline Pattern

UTM parameters must persist through the entire signup-to-activation journey:

```
1. First touch: Capture utm_* params from URL → store in localStorage / session cookie
2. Signup: Read stored utm_* → attach to signup_started and signup_completed
3. Onboarding: Carry utm_* on onboarding step events via user profile enrichment
4. Activation: Activation event should include first_touch_source derived from utm_* at signup
```

**Never**: Read UTM from current URL on post-signup pages (URL changes after redirect).

## Growth Loop Event Pattern

For each loop node, fire events in this sequence:

| Node | Event Name | Key Properties |
|------|-----------|---------------|
| Trigger impression | loop_trigger_shown | loop_id, user_id, placement |
| Trigger action | loop_trigger_clicked | loop_id, user_id, placement |
| Distribution | invite_sent | loop_id, referrer_id, channel, invite_id |
| Landing | referral_landing_viewed | loop_id, referrer_id, invite_id |
| Referred signup | signup_completed | loop_id, referrer_id, invite_id (attached to signup) |
| Referred activation | activation_event | loop_id, referrer_id (carried forward) |
| Reward | referral_reward_granted | loop_id, referrer_id, reward_type, amount |

## Implementation Checklist

Before submitting for verification:

- [ ] All events use snake_case past-tense naming
- [ ] user_id present on all post-auth events; anonymous_id on pre-auth
- [ ] UTM properties read from first-touch storage (not current URL)
- [ ] experiment_id and variant_id attached to all events fired within experiment context
- [ ] Loop events include referrer_id linkage at every node
- [ ] No hardcoded UTM values — all read dynamically
- [ ] Duplicate event suppression for idempotent actions (e.g., signup_completed fires once)
