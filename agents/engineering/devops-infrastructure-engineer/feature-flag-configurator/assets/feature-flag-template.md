# Feature Flag Configuration

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | feature-flag-configurator |
| Flag Name | [service-feature-variant] |
| Platform | [LaunchDarkly / Unleash / Flagsmith / GrowthBook / other] |

## Executive Summary

[2-3 sentences describing what this flag controls, why it is needed, and its intended lifecycle.
GUIDANCE: Lead with the feature being gated and the rollout strategy. Example: "This flag gates the Stripe PaymentElement migration for the checkout service. It will roll out from 1% to 100% over 2 weeks, enabling instant rollback to the legacy Charges API if conversion rate degrades."]

## Flag Definition

[Define the flag's core properties.

GUIDANCE:
- Good: "Flag: `checkout-payment-element`. Boolean. Default: false. Kill-switch safe: yes — disabled state falls back to existing Stripe Charges API with no code changes required."
- Bad: "Flag controls the new payment feature."]

| Property | Value |
|----------|-------|
| Flag key | [service-feature-variant] |
| Type | [Boolean / String / Number / JSON] |
| Default (off state) | [Describe what happens when flag is false/off] |
| Default (on state) | [Describe what happens when flag is true/on] |
| Kill-switch safe | [Yes — describe fallback / No — describe risk] |
| Owner | [Team or person responsible for cleanup] |
| Linked ticket | [JIRA/Linear ticket] |
| Cleanup deadline | [YYYY-MM-DD] |

## Targeting Rules

[Define the targeting rules for each environment in order of priority (first match wins).

GUIDANCE:
- Good: "Rule 1: Users with email matching `*@company.com` → ON (internal dog-fooding). Rule 2: User attribute `beta_enrolled = true` → ON (opted-in beta). Rule 3: Percentage rollout: 5% of remaining users by user ID hash → ON."
- Bad: "Roll out to some users first."
- Format: Ordered table — rules are evaluated top-to-bottom; first match wins]

### Production Targeting Rules

| Priority | Rule Name | Condition | Variant | Notes |
|----------|-----------|-----------|---------|-------|
| 1 | Internal users | email contains `@[company].com` | On | Dog-fooding |
| 2 | Beta opt-in | attribute `beta_enrolled = true` | On | Voluntary |
| 3 | Canary percentage | [X]% of users by user ID | On | Sticky hash |
| Default | All others | (no match) | Off | |

### Environment Overrides

| Environment | State | Notes |
|-------------|-------|-------|
| Local dev | On | Developer convenience |
| CI | Both (two test runs) | Validate both code paths |
| Staging | On | QA validation |
| Production | Per targeting rules above | |

## Rollout Plan

[Define the planned progression of the percentage-based rollout.

GUIDANCE:
- Good: "Stage 1: 1% for 24 hours. Success criteria: error rate ≤ baseline + 0.1%, conversion rate ≥ baseline − 1%. Stage 2: 10% for 48 hours. Same criteria. Stage 3: 50% for 48 hours. Stage 4: 100%."
- Bad: "Gradually increase the percentage over time."]

| Stage | Traffic % | Duration | Success Criteria | Gate Decision |
|-------|-----------|----------|-----------------|---------------|
| Canary | 1% | 24 hours | [Specific metrics at thresholds] | [Who approves advance] |
| Expansion 1 | 10% | 48 hours | [Specific metrics at thresholds] | [Who approves advance] |
| Expansion 2 | 50% | 48 hours | [Specific metrics at thresholds] | [Who approves advance] |
| Full rollout | 100% | — | Stable for 72 hours | [Who approves cleanup] |

## Disabled State Validation

[Document what happens when the flag is off, and how it was tested.

GUIDANCE: The disabled state must be as well-tested as the enabled state. It is the rollback path.]

- Disabled behavior: [Exact description of code path when flag is off]
- Tested in CI: [ ] Yes — test suite covers disabled state explicitly
- Tested in staging with flag off: [ ] Yes — QA signed off on [date]
- Known limitations in disabled state: [None / List any]

## Cleanup Plan

[Define the cleanup steps to remove the flag after full rollout is stable.

GUIDANCE: Flag cleanup is a code change, not just a platform delete. Both steps are required.]

1. [ ] Set flag to 100% enabled with no targeting rules (stable for [duration])
2. [ ] Remove all flag evaluation code from source (`if (flagEnabled) { ... }` → inline the enabled path)
3. [ ] Delete the disabled code path
4. [ ] Remove flag from the feature flag platform
5. [ ] Close the cleanup ticket: [ticket link]
6. [ ] Cleanup deadline: [YYYY-MM-DD] — assigned to: [owner]

## Recommendations

- **P1**: Test the disabled (rollback) state in staging before enabling the flag in production
- **P2**: Set up a monitoring dashboard showing the flag's enabled percentage alongside error rate and key business metrics
- **P3**: Configure a Slack alert for when the cleanup deadline passes without the flag being removed

## Appendices

### A. Dependency Map

[Other services or components that depend on the behavior of this flag — especially if the flag controls an API contract change.]

### B. Rollback Decision Criteria

[Specific metric thresholds that should trigger an immediate flag disable (kill switch action).]
