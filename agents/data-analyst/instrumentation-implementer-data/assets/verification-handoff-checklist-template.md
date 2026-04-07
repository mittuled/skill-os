# Instrumentation Verification Handoff Checklist

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Implementer | [Data Analyst name] |
| Feature / Surface | [Feature name or product surface] |
| Spec Reference | [Link to approved instrumentation spec] |
| Branch / PR | [GitHub PR URL] |
| Environment | [Dev / Staging] |
| Skill | instrumentation-implementer-data |

## Implementation Summary

[1-2 sentences describing what was implemented — number of events, platforms, and any notable implementation decisions.

GUIDANCE: Example: "Implemented 12 events across Web and Server for the onboarding redesign. Server-side mirroring was added for the signup_completed and payment_initiated events to protect against client-side ad-blocker loss."]

## Event Verification Matrix

[Complete this table for every event in the spec. The verifier will use this as the test script.]

| # | Event Name | Platform | Trigger Scenario | Required Properties | Test Account / User |
|---|-----------|----------|-----------------|--------------------|--------------------|
| 1 | [event_name] | [Web] | [Describe the exact UI action or API call that should trigger this event] | [prop1 (string), prop2 (integer), prop3 (enum: a\|b\|c)] | [test user email or ID] |
| 2 | [event_name] | [iOS] | [Tap "Get Started" button on Step 2 of onboarding] | [user_id (string), step_name (string), step_number (integer)] | [test device ID] |
| 3 | [event_name] | [Server] | [POST /api/v2/signup returns 200] | [user_id (string), plan (enum: free\|pro), referral_source (string\|null)] | [API test fixture] |

## Negative Test Cases

[List scenarios where events should NOT fire. Verifier must confirm silence in these cases.]

| # | Event Name | Scenario Where It Must NOT Fire | Reason |
|---|-----------|-------------------------------|--------|
| 1 | [event_name] | [When the user is an internal test account (email contains @yourcompany.com)] | [Prevent internal traffic from polluting metrics] |
| 2 | [event_name] | [When the form submission returns a 4XX error] | [Do not track failed attempts as conversions] |
| 3 | [event_name] | [On duplicate submission (re-click within 500ms)] | [Deduplication logic should suppress repeat fires] |

## Context Properties

[Confirm standard context is attached to all events by the SDK middleware.]

| Context Property | Expected Value Source | Status |
|-----------------|----------------------|--------|
| user_id | Auth session — authenticated users only; null for anonymous | [Implemented / Pending] |
| session_id | SDK auto-generated per session | [Implemented / Pending] |
| timestamp | SDK server timestamp (ISO 8601) | [Implemented / Pending] |
| platform | Static: "web" / "ios" / "android" / "server" | [Implemented / Pending] |
| app_version | Build constant injected at deploy | [Implemented / Pending] |
| anonymous_id | SDK auto-generated; persisted in localStorage | [Implemented / Pending] |

## Edge Case Handling

[Document how each edge case is handled when required properties may not be available.]

| Edge Case | Property Affected | Handling Implementation |
|-----------|-----------------|------------------------|
| User not authenticated | user_id | Send null; do not drop event |
| Referral source absent | referral_source | Send null; do not fall back to "direct" |
| Plan tier API timeout | plan | Send null; log warning server-side |
| Property value exceeds max length | [any string > 256 chars] | Truncate to 256 chars; append "_truncated" flag |

## Implementation Notes

[Free-form notes for the verifier — unusual trigger logic, SDK quirks, known limitations.]

1. [Note 1: e.g., "The payment_initiated event is fired server-side because the client-side Stripe listener is unreliable on slow connections."]
2. [Note 2: e.g., "feature_discovered fires on a 500ms debounce — rapid scrolling past the feature card will not generate repeated events."]
3. [Note 3: e.g., "Events on Android are not yet implemented per Phase 1 scope — Android is Phase 2."]

## Verifier Instructions

1. Deploy this branch to the staging environment.
2. Use the analytics SDK debugger (or Charles Proxy for mobile) to inspect outgoing event payloads in real time.
3. Work through each row of the Event Verification Matrix, executing the trigger scenario exactly as described.
4. For each event, confirm: event name matches spec, all required properties are present with correct types, context properties are attached.
5. Execute all Negative Test Cases and confirm silence.
6. Return the completed Verification Report with pass/fail per event. Failures should include the expected vs. actual payload as a screenshot or JSON snippet.
