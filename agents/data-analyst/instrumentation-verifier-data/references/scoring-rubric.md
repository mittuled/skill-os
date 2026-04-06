# Scoring Rubric: instrumentation-verifier-data

Evaluates the correctness of instrumentation in the development and staging environment, verifying that events match the approved spec before code progresses to production.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Event Presence | 25% | All events defined in the spec fire in the expected user scenarios and do not fire in negative test cases |
| 2 | Property Correctness | 35% | Each event's properties match the spec: correct names, data types, value constraints, and nullability handling |
| 3 | Trigger Accuracy | 25% | Events fire at exactly the right trigger point — not early, not late, not duplicated in a single user action |
| 4 | Negative Case Handling | 15% | Events correctly suppressed for bot traffic, internal test accounts, duplicate submissions, and error states where tracking is not intended |
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
| A+ | 9.0 – 10.0 | Verified | All events present, all properties correct, all triggers accurate, all negative cases handled | Approve for production deployment |
| A | 8.0 – 8.9 | Near-verified | 1–2 minor property issues (wrong nullability, missing optional property); no presence or trigger failures | Approve with minor fix note; recheck property issues in production verification |
| B | 7.0 – 7.9 | Conditionally approved | 1 non-critical property type mismatch or 1 low-severity trigger duplicate; no missing events | Fix required issues; re-verify affected events before production deploy |
| C | 5.0 – 6.9 | Needs rework | 1–3 events missing or misfiring; multiple property type mismatches; negative cases partially handled | Return to implementer; re-verify full spec after fixes |
| D | 3.0 – 4.9 | Significant failures | >3 events missing or misfiring; systematic property type errors; trigger accuracy unreliable | Block production deployment; implementation requires significant rework |
| F | 0.0 – 2.9 | Failed | Majority of events absent or properties unrecognizable from spec; tracking code appears non-functional | Reject; implementer must restart implementation of affected surfaces |

## Signal Tables

### Event Presence

| Score | Evidence |
|-------|----------|
| 9–10 | Every spec-defined event fires in the correct scenario; network inspector or analytics debugger shows all events by name; no expected events are missing from the payload log |
| 7–8 | 95–99% of events present; 1 low-criticality event missing (e.g., an informational event, not a funnel event); confirmed not a test environment artifact |
| 5–6 | 80–94% of events present; 1–2 medium-criticality events missing (e.g., a secondary funnel step); implementer has a plausible explanation |
| 3–4 | 60–79% of events present; 1 high-criticality event missing (e.g., purchase_completed, activation_completed); no explanation from implementer |
| 0–2 | <60% of events present; multiple high-criticality events not firing; tracking code may not have been integrated |

### Property Correctness

| Score | Evidence |
|-------|----------|
| 9–10 | Every property name matches spec (snake_case, no typos); data types match (integer fields send integers, not strings); enum values are from the allowed list; required properties are never null |
| 7–8 | 95–99% of properties correct; 1–2 optional properties missing from some payloads; no required properties null or wrong type |
| 5–6 | 80–94% of properties correct; 1–3 type mismatches (e.g., numeric ID sent as string); some enum values outside allowed list |
| 3–4 | 60–79% of properties correct; required properties null in 10–20% of events; systematic type mismatch on a shared property (e.g., user_id always wrong type) |
| 0–2 | <60% of properties correct; required properties frequently null; property names differ from spec (typos, camelCase vs. snake_case); payload structure unrecognizable from spec |

### Trigger Accuracy

| Score | Evidence |
|-------|----------|
| 9–10 | Every event fires exactly once per the specified user action; no events fire on page load instead of user interaction; no events fire on component unmount without user action |
| 7–8 | 95–99% of events trigger correctly; 1 event fires with a 1–2 second timing offset but at the correct step |
| 5–6 | 80–94% of events trigger correctly; 1 event fires prematurely (before action completes) or with a delay; 1 event duplicates on certain paths (e.g., fires twice on back-navigation) |
| 3–4 | 60–79% of events trigger correctly; 1–2 events fire at wrong steps (e.g., purchase_started fires after purchase_completed); duplicate fires common on retry paths |
| 0–2 | <60% correct trigger timing; events fire on page load, application boot, or other non-user-initiated triggers; systematic duplication across most events |

### Negative Case Handling

| Score | Evidence |
|-------|----------|
| 9–10 | Events confirmed absent for: internal test user accounts, bot traffic simulation (Puppeteer), duplicate form submissions (double-click), and error states where tracking should not fire |
| 7–8 | Test account suppression works; bot filter in place; 1 edge case (e.g., double-click on slow network) not fully handled but documented |
| 5–6 | Test account suppression works; bot filtering not tested; duplicate submission case untested |
| 3–4 | Test account suppression not implemented; events fire for internal accounts; no bot filtering; duplicates possible |
| 0–2 | No negative cases tested; internal account tracking confirmed; no suppression logic present; every bot or automated test will pollute production data |
