# Framework: Instrumentation Spec

Defines the methodology for designing event taxonomies, property schemas, and traceability matrices that make every analytics question answerable from captured data.

## Event Taxonomy Design

### Naming Convention

Use `object_action` format — lowercase, underscore-separated:

| Object | Action | Example Event |
|--------|--------|--------------|
| `checkout` | `started` | `checkout_started` |
| `item` | `added` | `item_added` |
| `report` | `exported` | `report_exported` |
| `subscription` | `upgraded` | `subscription_upgraded` |

**Prohibited patterns**: `track_event`, `button_click`, `page_view` (too generic — disambiguate by object).

### Event Classification

| Class | When to Create | Examples |
|-------|---------------|---------|
| **User action** | Direct user interaction | `search_submitted`, `filter_applied` |
| **System event** | Backend state change | `payment_processed`, `email_sent` |
| **Lifecycle event** | Account/session milestone | `user_created`, `session_started` |
| **Error event** | Failure condition | `api_error_encountered`, `validation_failed` |

## Property Schema Standards

### Required Context Properties (Every Event)

| Property | Type | Description |
|---------|------|-------------|
| `user_id` | string (UUID) | Authenticated user identifier; null for anonymous |
| `anonymous_id` | string (UUID) | Device-level identifier; always present |
| `session_id` | string (UUID) | Session scope identifier |
| `timestamp` | ISO 8601 string | UTC event timestamp |
| `platform` | enum: web, ios, android, server | Originating platform |
| `app_version` | semver string | Application version at event time |

### Property Type Enforcement

| Data Holds | Correct Type | Wrong Type | Impact of Error |
|------------|-------------|-----------|----------------|
| Monetary amount | `number` (float) | `string` | SUM/AVG aggregations return null |
| Count | `integer` | `string` | Arithmetic fails |
| Categorical value | `enum` (explicit list) | `string` | Group-by produces unbounded cardinality |
| Boolean flag | `boolean` | `string` ("true"/"false") | Filter queries fail silently |
| Identifier | `string` (UUID format) | `integer` | JOIN failures on type mismatch |

## Traceability Matrix

Link each analytics goal to the events and properties that compute it:

| Analytics Goal | Required Events | Required Properties | Computed As |
|---------------|----------------|---------------------|-------------|
| Activation rate | `onboarding_completed`, `user_created` | `user_id`, `timestamp` | completions / signups in cohort window |
| Trial-to-paid conversion | `subscription_started` (plan_type=trial), `subscription_upgraded` | `user_id`, `plan_type`, `timestamp` | upgrades / trial_starts |
| Feature adoption rate | `feature_used` | `user_id`, `feature_name`, `timestamp` | unique users with ≥ N uses / eligible users |

**Coverage rule**: every analytics goal must map to at least one event. Flag unmapped goals as instrumentation gaps before approving the spec.

## Data Quality Rules Per Event

For each event, define:

1. **Required properties**: list of properties that must be non-null.
2. **Value constraints**: enum allowed values, numeric ranges, string format patterns.
3. **Expected volume**: events-per-hour range based on DAU and typical usage patterns.
4. **Deduplication key**: the combination of properties that uniquely identifies an event (prevents double-counting on retry).

## Privacy Classification Tiers

| Tier | Definition | Examples | Treatment |
|------|-----------|---------|-----------|
| **Anonymous** | Cannot identify an individual | `event_type`, `platform`, `page_path` | No restriction |
| **Pseudonymous** | Linkable to an individual only with key | `user_id`, `session_id` | Encrypt at rest; access-controlled |
| **PII** | Directly identifies an individual | `email`, `full_name`, `ip_address` | Consent gate required; mask in logs |
| **Sensitive PII** | Health, financial, or protected class data | `payment_method`, `diagnosis_code` | Explicit consent + legal review |

**GDPR/CCPA rule**: PII and Sensitive PII properties require consent gating. Suppression in EU/CA jurisdictions must be configured before the spec is approved for implementation.

## Review Checklist Before Approval

- [ ] All events follow `object_action` naming convention
- [ ] Every property has name, type, allowed values, nullability, and description
- [ ] Traceability matrix covers 100% of stated analytics goals
- [ ] Required context properties included in every event
- [ ] Privacy tiers assigned to every property
- [ ] Data quality rules (volume, deduplication key) defined per event
- [ ] Server-side events included where backend actions are critical
- [ ] Clarity reviewer has approved the spec
