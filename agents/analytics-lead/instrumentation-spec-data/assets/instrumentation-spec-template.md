# Instrumentation Spec

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Analytics Lead / name] |
| Version | [1.0] |
| Status | [Draft / In Review / Approved] |
| Skill | instrumentation-spec-data |
| Feature / Initiative | [Name of the product surface being instrumented] |
| Analytics Platform | [Segment / Amplitude / Mixpanel / custom] |

## Executive Summary

[2–3 sentences describing the product surface, the analytics goals this spec enables, and the total number of events defined.
GUIDANCE: Lead with what questions this spec makes answerable. Example: "This spec instruments the onboarding flow for new trial users, enabling computation of step-completion rates, time-to-activation, and drop-off segmentation by acquisition channel. It defines 12 events across web and iOS platforms."]

## Analytics Goals and Coverage

[Table mapping each analytics question to the events and properties that answer it.

GUIDANCE:
- Good: "Trial-to-paid conversion rate — computed from `subscription_started` (plan_type=trial) and `subscription_upgraded` with user_id and timestamp"
- Bad: "Track user upgrades"
- Format: Table with Goal, Required Events, Required Properties, Computed As columns (see framework.md)]

| Analytics Goal | Required Events | Required Properties | Computed As |
|---------------|----------------|---------------------|-------------|
| [Goal 1] | [event_names] | [property_names] | [formula or query description] |
| [Goal 2] | [event_names] | [property_names] | [formula or query description] |

**Coverage gaps**: [List any analytics goals without full event coverage, and the events needed to close each gap.]

## Event Taxonomy

[Full list of events grouped by user journey phase.

GUIDANCE:
- Good: "`checkout_started` — fires when the user clicks "Begin Checkout" on the cart page. Trigger: onClick handler on the checkout CTA. Unique in session? No."
- Bad: "Track checkout events"
- Format: Group by journey phase. One subsection per phase.]

### [Journey Phase 1: e.g., Discovery]

#### `[event_name]`

| Field | Value |
|-------|-------|
| Event ID | [E001] |
| Trigger | [Exact UI action or backend state change that fires this event] |
| Platform | [web / ios / android / server] |
| Frequency | [Estimated events/hour at median DAU] |
| Deduplication Key | [property_a + property_b] |

**Properties**:

| Property | Type | Allowed Values | Nullable | Description |
|---------|------|---------------|----------|-------------|
| [property_name] | [string/number/boolean/enum] | [list or "any"] | [yes/no] | [What this captures] |

### [Journey Phase 2: e.g., Activation]

[Repeat event blocks for each event in this phase]

## Standard Context Properties

All events automatically include these context properties via SDK middleware:

| Property | Type | Description |
|---------|------|-------------|
| `user_id` | string (UUID) | Authenticated user; null when anonymous |
| `anonymous_id` | string (UUID) | Device-level identifier; always present |
| `session_id` | string (UUID) | Current session scope |
| `timestamp` | ISO 8601 | UTC event time |
| `platform` | enum | web / ios / android / server |
| `app_version` | semver | Application version at event time |

## Data Quality Rules

[Per-event quality contracts. List required properties, value constraints, and expected volumes.

GUIDANCE:
- Good: "`checkout_started` — required: [user_id, cart_value, item_count]; cart_value ≥ 0; expected volume: 200–800/hr"
- Bad: "Make sure events are valid"
- Format: Table per event or a consolidated table]

| Event | Required Properties | Value Constraints | Expected Volume (events/hr) | Deduplication Key |
|-------|-------------------|-------------------|----------------------------|-------------------|
| [event_name] | [list] | [constraints] | [low–high] | [key fields] |

## Privacy Classification

[Privacy tier per property. Required for legal review.

GUIDANCE:
- Good: "`email` — PII — requires consent gate; suppress in EU unless consent = true"
- Bad: "Mark sensitive fields"
- Format: Table grouped by privacy tier]

| Property | Tier | Jurisdictions | Treatment Required |
|---------|------|--------------|-------------------|
| `user_id` | Pseudonymous | All | Encrypt at rest; access-controlled |
| [property_name] | [tier] | [jurisdictions] | [treatment] |

## Recommendations

[Prioritized list of gaps or risks identified during spec authoring.

GUIDANCE: Each item should be specific and actionable.
- P1: [Critical gap that blocks metric computation — must resolve before implementation]
- P2: [Quality risk that may cause data issues — resolve before launch]
- P3: [Enhancement for future iteration — log as backlog item]]

## Appendices

### A. Out-of-Scope Events

[Events intentionally excluded from this spec and the reason.]

### B. Migration Notes

[If replacing existing events, document the old event names, the migration period, and the cutover plan.]

### C. Approval Sign-Off

| Reviewer | Role | Status | Date |
|---------|------|--------|------|
| [Name] | Analytics Lead | [Approved / Changes Requested] | [YYYY-MM-DD] |
| [Name] | Instrumentation Clarity Reviewer | [Approved / Changes Requested] | [YYYY-MM-DD] |
