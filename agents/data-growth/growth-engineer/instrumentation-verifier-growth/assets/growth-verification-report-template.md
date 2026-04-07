# Growth Instrumentation Verification Report (Dev/Staging)

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Verifier | [Growth Engineer name] |
| Feature / Experiment | [Name] |
| Spec Reference | [Link] |
| Handoff Checklist | [Link] |
| Environment | [Dev / Staging] |
| Branch / PR | [GitHub PR URL] |
| Overall Result | [PASS / FAIL — N events failed] |
| Skill | instrumentation-verifier-growth |

## Summary

| Category | Total | Pass | Fail |
|----------|-------|------|------|
| Funnel events | [N] | [N] | [N] |
| Experiment assignment events | [N] | [N] | [N] |
| Experiment goal events | [N] | [N] | [N] |
| Loop events | [N] | [N] | [N] |
| Negative test cases | [N] | [N] | [N] |

## Funnel Event Results

| # | Event | Platform | Trigger Tested | Event Fired | UTM Captured | Properties Correct | Result |
|---|-------|---------|---------------|-------------|-------------|-------------------|--------|
| 1 | [event_name] | [Web] | [Yes] | [Yes] | [Yes] | [Yes] | **PASS** |
| 2 | [event_name] | [Web] | [Yes] | [Yes] | [No — utm_content missing] | [Partial] | **FAIL** |

## Experiment Event Results

### Experiment: [Experiment Name / ID]

| # | Event | Trigger Tested | Fired? | experiment_id Correct? | variant_id Correct? | Other Props Correct? | Result |
|---|-------|---------------|--------|----------------------|--------------------|--------------------|--------|
| 1 | experiment_assigned | [Yes] | [Yes] | [Yes — exact: EXP-001] | [Yes — "control" or "variant_a"] | [Yes] | **PASS** |
| 2 | [goal_event] | [Yes] | [Yes] | [Yes] | [Yes] | [Yes] | **PASS** |

**Experiment Assignment Distribution Check** (if testable in staging):

| Variant | Expected % | Observed % | Balanced? |
|---------|-----------|-----------|-----------|
| control | 50% | [X%] | [Yes / No] |
| variant_a | 50% | [X%] | [Yes / No] |

## Loop Event Results

| # | Event | Node | Trigger Tested | Fired? | referrer_id Correct? | Properties Correct | Result |
|---|-------|------|---------------|--------|---------------------|-------------------|--------|
| 1 | [referral_prompt_shown] | Trigger | [Yes] | [Yes] | [N/A] | [Yes] | **PASS** |
| 2 | [referral_link_shared] | Distribution | [Yes] | [Yes] | [N/A] | [Yes] | **PASS** |
| 3 | [referred_signup_completed] | Signup | [Yes] | [Yes] | [Yes — referrer_user_id: usr_123] | [Yes] | **PASS** |

## Negative Test Case Results

| # | Event | Scenario | Silence Confirmed? | Notes |
|---|-------|---------|-------------------|-------|
| 1 | experiment_assigned | Internal test account (email: @company.com) | [Yes / No] | — |
| 2 | [goal_event] | Form validation fails (400 response) | [Yes / No] | — |
| 3 | referral_reward_granted | Self-referral attempted | [Yes / No] | — |

## Failure Details

### Failure #1: [event_name] — [Short description]

**Severity**: [Critical / High / Medium]
**Event**: [event_name]
**Scenario**: [Describe trigger scenario]

**Expected payload**:
```json
{
  "event": "[event_name]",
  "properties": {
    "utm_content": "ad_variant_b",
    "utm_source": "google",
    "user_id": "usr_456"
  }
}
```

**Actual payload**:
```json
{
  "event": "[event_name]",
  "properties": {
    "utm_source": "google",
    "user_id": "usr_456"
  }
}
```

**Missing**: `utm_content` — the implementation reads only utm_source and utm_medium from the URL. utm_content needs to be added to the attribution capture function in [file:line].

**Remediation**: Update `captureUTMParams()` in [file path] to also capture utm_content and utm_term from the URL query string.

---

## Recommendation

**Verdict**: [APPROVED / BLOCKED — N critical failures must be resolved]

[1-2 sentences. Example: "Experiment instrumentation is correct and the experiment assignment distribution is balanced at 50/50. One failure on utm_content capture is non-blocking (medium severity) but must be resolved before the ad-level attribution analysis is reliable. Recommend conditional GO — merge after implementer resolves Issue #1."]

**Re-verification required?** [Yes — after Issue #1 resolved / No]
