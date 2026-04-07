# Growth Instrumentation Verification Handoff

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Implementer | [Growth Engineer name] |
| Feature / Experiment | [Feature name or experiment name] |
| Spec Reference | [Link to growth instrumentation spec] |
| Branch / PR | [GitHub PR URL] |
| Environment | [Dev / Staging] |
| Skill | instrumentation-implementer-growth |

## Implementation Summary

[1-2 sentences describing what was implemented — number of events, whether this is a new experiment setup, loop instrumentation, or funnel update.

GUIDANCE: Example: "Implemented 8 events for Experiment 23 (onboarding_skip_cta test): 1 variant assignment event, 5 funnel step events, and 2 goal events. Also updated channel attribution to capture utm_content for ad-level attribution."]

## Funnel Event Verification Matrix

| # | Event Name | Trigger Scenario | Channel Attribution Properties | Required Properties | Platform |
|---|-----------|-----------------|------------------------------|--------------------|----|
| 1 | [landing_page_view] | [Page loads] | [utm_source, utm_medium, utm_campaign, referrer] | [page_path, session_id] | [Web] |
| 2 | [signup_started] | [Email field focused or CTA clicked] | [utm_source, utm_medium, utm_campaign] | [signup_method] | [Web] |
| 3 | [signup_completed] | [POST /auth/signup returns 200] | [utm_source, utm_medium (from session)] | [user_id, plan, signup_method] | [Web + Server] |
| 4 | [onboarding_step_N_completed] | [Step N UI action confirmed] | — | [user_id, step_number, step_name] | [Web] |
| 5 | [activation_event] | [Activation action triggered] | — | [user_id, feature_name] | [Web + Server] |

## Experiment Event Verification Matrix

[Complete for each A/B test in scope. Verifier must confirm all rows.]

### Experiment: [Experiment Name / ID]

| # | Event Name | Trigger Scenario | Required Properties | Verify Values |
|---|-----------|-----------------|--------------------|----|
| 1 | experiment_assigned | [User enters experiment — control or variant allocated] | experiment_id=[ID], variant_id=[control\|variant_a], user_id, assignment_timestamp | Verify experiment_id=[EXACT_ID]; variant_id is exactly "control" or "variant_a" |
| 2 | [goal_event_name] | [Primary conversion action for this experiment] | experiment_id=[ID], variant_id, user_id, [additional goal properties] | experiment_id matches; goal fires only once per user per experiment session |

**Experiment ID**: [exact ID string]
**Variants**: [control, variant_a] (or list all)
**Goal event**: [event_name] — confirm this also fires without the experiment context for non-experiment users

## Loop Event Verification Matrix

[Complete only if this implementation includes growth loop instrumentation.]

| # | Event Name | Node | Trigger Scenario | Required Properties |
|---|-----------|------|-----------------|-------------------|
| 1 | [referral_prompt_shown] | Trigger | [Prompt displays to eligible user] | user_id, referral_code, prompt_location |
| 2 | [referral_link_shared] | Distribution | [User copies or sends link] | user_id, referral_code, share_method |
| 3 | [referred_signup_completed] | Signup | [Referred user creates account] | referred_user_id, referrer_user_id, referral_code |

## UTM Attribution Verification

| UTM Parameter | Source | Expected Value in Test | Correctly Captured? |
|--------------|--------|----------------------|---------------------|
| utm_source | URL query string | [e.g., "google"] | [Implementer confirms: Yes / Unknown] |
| utm_medium | URL query string | [e.g., "cpc"] | [Yes / Unknown] |
| utm_campaign | URL query string | [campaign slug] | [Yes / Unknown] |
| utm_content | URL query string | [ad variant ID] | [Yes / Unknown] |
| referrer (HTTP) | Browser API | [organic referrer domain] | [Yes / Unknown] |

Attribution persistence: UTM values are stored in [session storage / localStorage / cookie] and attached to all events in the session.

## Negative Test Cases

| # | Event | Should NOT fire when... |
|---|-------|------------------------|
| 1 | experiment_assigned | User is excluded from experiment (e.g., internal employee, prior test participant) |
| 2 | [goal_event] | Goal action fails (e.g., form validation error) |
| 3 | referral_reward_granted | Self-referral attempted |

## Verifier Instructions

1. Deploy this branch to the staging environment.
2. Clear cookies/localStorage between test scenarios to ensure fresh session state.
3. For attribution testing, append UTM parameters to the URL before triggering events.
4. For experiment testing, enter the experiment by [describe how — feature flag toggle, URL parameter, or random assignment].
5. Confirm experiment_assigned fires immediately on entry with the correct experiment_id and variant_id strings.
6. Complete the goal action and confirm the goal event fires with the experiment_id attached.
7. Return the verification report with pass/fail per event. Include payload JSON snippets for failures.
