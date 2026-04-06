# Scoring Rubric: instrumentation-clarity-reviewer

Evaluates the quality of an instrumentation spec across naming conventions, property completeness, journey coverage, measurability, and privacy compliance.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Event Naming Consistency | 20% | Adherence to the object_action naming convention; uniqueness of event names; absence of ambiguous or duplicate events |
| 2 | Property Completeness | 25% | Every event has all required properties defined with data type, allowed values, and nullability documented |
| 3 | Journey Coverage | 25% | All user journey steps have at least one event; no blind spots in critical flows; no redundant events at a single step |
| 4 | Measurability | 20% | Each analytics goal stated in the spec can be answered by querying the proposed events and properties |
| 5 | Privacy Compliance | 10% | No PII captured in event properties unless explicitly scoped, consented, and documented |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0–10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All events follow naming convention; all properties typed and defined; full journey coverage; every goal traceable to a query path; zero PII flags | Approve for implementation immediately |
| A | 8.0 – 8.9 | Strong | 1–2 minor naming deviations; 95%+ properties defined; one journey gap that is low-criticality; all goals measurable | Approve with minor comments; no implementation blocker |
| B | 7.0 – 7.9 | Good | Naming inconsistencies in <10% of events; some optional properties undefined; one medium-criticality journey gap | Approve with required fixes; implementation can begin on approved events |
| C | 5.0 – 6.9 | Adequate | Multiple naming violations or ambiguous duplicates; 15–25% of properties missing type or nullability; 1–2 journey gaps blocking key analytics goals | Needs revision before implementation; return to spec author |
| D | 3.0 – 4.9 | Weak | No naming convention followed; >25% of properties undefined; major journey steps uncovered; most goals not traceable to events | Major revision required; implementation blocked |
| F | 0.0 – 2.9 | Failing | No naming convention; properties absent or all untyped; journey coverage <50%; analytics goals not connected to proposed events | Reject spec; requires complete rewrite |

## Signal Tables

### Event Naming Consistency

| Score | Evidence |
|-------|----------|
| 9–10 | 100% of events follow object_action format (e.g., `checkout_completed`, `file_exported`); no duplicate event names; no vague names ("user_action", "button_clicked"); all system events distinguished from user events |
| 7–8 | 90–99% of events follow convention; 1–3 events use non-standard format but intent is clear; no duplicates |
| 5–6 | 70–89% adherence; 3–5 events with naming violations; 1–2 ambiguous names that could be confused; minor duplicates possible |
| 3–4 | 50–69% adherence; mixed naming styles (camelCase, snake_case, free text) in same spec; multiple ambiguous events; 1+ duplicate event names |
| 0–2 | <50% adherence; no discernible naming convention; free-form event names that are not self-describing; duplicate names that refer to different actions |

### Property Completeness

| Score | Evidence |
|-------|----------|
| 9–10 | Every property has: name (snake_case), data type (string/integer/boolean/enum), allowed values for enums, nullability (required vs. optional), and a description. No "TBD" entries. |
| 7–8 | 95–99% of properties fully defined; 1–3 optional properties missing description; no required properties undefined |
| 5–6 | 80–94% of properties fully defined; some enum values not exhaustively listed; nullability missing for 5–15% of properties |
| 3–4 | 60–79% of properties defined; data types missing for >15% of properties; multiple required properties documented as "TBD" |
| 0–2 | <60% of properties defined; data types absent across most events; properties listed as names only without any schema detail |

### Journey Coverage

| Score | Evidence |
|-------|----------|
| 9–10 | Every step in the documented user journey has at least one event; no journey step is a blind spot; events are 1:1 with meaningful user actions (no redundancy); coverage map drawn and verified |
| 7–8 | 95%+ of journey steps covered; 1 low-criticality step lacks an event; no redundant events that create double-counting risk |
| 5–6 | 80–94% of journey steps covered; 1–2 medium-criticality gaps; 1–2 redundant events at the same step that could cause double-counting |
| 3–4 | 60–79% of steps covered; 1 high-criticality journey segment (e.g., checkout, activation) entirely missing events; multiple redundant events |
| 0–2 | <60% of journey steps covered; critical flows (onboarding, core action, upgrade) lack events; spec covers isolated actions without journey context |

### Measurability

| Score | Evidence |
|-------|----------|
| 9–10 | For every analytics goal in the spec, a complete query path can be traced through the proposed events and properties; no goal requires an event or property not in the spec |
| 7–8 | 90–95% of goals are directly measurable; 1–2 goals require minor property additions (low-complexity fix) |
| 5–6 | 75–89% of goals measurable; 2–3 goals are partially measurable (can approximate but not compute precisely); fixes require event additions |
| 3–4 | 50–74% of goals measurable; multiple goals blocked by missing events or properties; some goals were not traced at all during spec authoring |
| 0–2 | <50% of goals measurable from the proposed spec; analytics goals were stated as aspirations without event design to support them |

### Privacy Compliance

| Score | Evidence |
|-------|----------|
| 9–10 | Zero PII in event properties; user identification uses hashed or anonymized IDs only; spec includes explicit statement confirming no PII capture |
| 7–8 | No direct PII; 1–2 properties that are indirect identifiers (e.g., company name) are noted with a justification and data handling note |
| 5–6 | 1–3 indirect identifier properties without data handling documentation; no explicit PII review performed |
| 3–4 | 1 direct PII field (email, name, phone) captured in an event property without documented consent or scope; review required before implementation |
| 0–2 | Multiple PII fields in event properties; no consent documentation; spec was authored without a privacy review; implementation is blocked until resolved |
