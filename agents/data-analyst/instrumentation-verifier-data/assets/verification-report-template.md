# Instrumentation Verification Report (Dev/Staging)

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Verifier | [Data Analyst name] |
| Feature / Surface | [Feature name] |
| Spec Reference | [Link to approved instrumentation spec] |
| Handoff Checklist | [Link to implementer's handoff checklist] |
| Environment | [Dev / Staging] |
| Branch / PR | [GitHub PR URL] |
| Overall Result | [PASS / FAIL — N events failed] |
| Skill | instrumentation-verifier-data |

## Summary

| Category | Count |
|----------|-------|
| Total events in spec | [N] |
| Events verified (pass) | [N] |
| Events failed | [N] |
| Events not tested (scope exclusion) | [N] |
| Negative test cases tested | [N] |
| Negative test cases passed | [N] |

## Event Verification Results

| # | Event Name | Platform | Trigger Tested? | Event Fired? | Properties Correct? | Result | Failure Detail |
|---|-----------|----------|----------------|-------------|---------------------|--------|----------------|
| 1 | [event_name] | [Web] | [Yes] | [Yes] | [Yes] | **PASS** | — |
| 2 | [event_name] | [iOS] | [Yes] | [Yes] | [No — missing prop2] | **FAIL** | See Issue #1 below |
| 3 | [event_name] | [Server] | [Yes] | [No — did not fire] | [N/A] | **FAIL** | See Issue #2 below |

## Failure Details

### Issue #1: [event_name] — Missing property on iOS

**Severity**: High (required property)

**Event**: [event_name]
**Platform**: iOS
**Trigger**: [Describe trigger scenario]

**Expected payload**:
```json
{
  "event": "[event_name]",
  "properties": {
    "prop1": "value_a",
    "prop2": 3,
    "user_id": "usr_123"
  }
}
```

**Actual payload**:
```json
{
  "event": "[event_name]",
  "properties": {
    "prop1": "value_a",
    "user_id": "usr_123"
  }
}
```

**Missing**: `prop2` (integer) is absent. Property should be populated from [application state location].

**Remediation**: Implementer must source `prop2` from [describe where it lives in app state] and pass it to the tracking call in [file:line].

---

### Issue #2: [event_name] — Event did not fire on Server

**Severity**: Critical (funnel step missing)

**Event**: [event_name]
**Platform**: Server
**Trigger**: POST /api/v2/[endpoint] with 200 response

**Expected**: Event fires immediately after successful 200 response from the endpoint.
**Actual**: No event observed in the event pipeline debugger after triggering the endpoint 5 times.

**Likely cause**: The tracking call may be conditional on a flag that is disabled in the staging environment. Check the feature flag configuration in [config file/location].

**Remediation**: Confirm tracking is not gated by the feature flag, or enable the flag in staging for verification purposes.

---

## Negative Test Case Results

| # | Event | Scenario | Silence Confirmed? | Notes |
|---|-------|---------|-------------------|-------|
| 1 | [event_name] | Internal test account (email: @company.com) | [Yes / No] | [notes] |
| 2 | [event_name] | Form submission with 400 error | [Yes / No] | [notes] |

## Context Property Check

| Context Property | Present on All Events? | Correctly Sourced? | Notes |
|-----------------|----------------------|-------------------|-------|
| user_id | [Yes / No] | [Yes / No] | [notes] |
| session_id | [Yes / No] | [Yes / No] | [notes] |
| timestamp | [Yes / No] | [Yes / No] | [notes] |
| platform | [Yes / No] | [Yes / No] | [notes] |
| app_version | [Yes / No] | [Yes / No] | [notes] |

## Recommendation

**Verdict**: [APPROVED for production / BLOCKED — N critical failures must be resolved before production deploy]

[1-2 sentences of overall recommendation. Example: "Two failures block production release: the missing prop2 on iOS and the server-side event not firing. Once the implementer addresses Issues #1 and #2 and resubmits, a re-verification pass is required before this branch can merge."]

**Re-verification required?** [Yes — after Issues #1 and #2 are resolved / No — minor issues are non-blocking]
