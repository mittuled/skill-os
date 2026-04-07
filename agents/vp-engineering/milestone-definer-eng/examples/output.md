# Milestone Register — iOS App Rebuild v3

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Total Milestones | 3 |
| Skill | milestone-definer-eng |

## Milestone Register

| ID | Milestone | Target Date | Type | Criteria | Dependencies |
|---|---|---|---|---|---|
| M01 | Core Navigation Shell | 2026-04-18 | Delivery | 3 outcome-based | None |
| M02 | Authentication Flow | 2026-05-02 | Delivery | 3 outcome-based | M01 |
| M03 | Beta TestFlight Release | 2026-05-23 | Gate | 3 outcome-based | M02 |

---

## Milestone Detail

### M01 — Core Navigation Shell (2026-04-18)

**Type:** Delivery | **Team:** Mobile Team

**Success Criteria (all must be met for milestone to pass):**
1. Tab bar navigation renders correctly on iOS 16+ with all 5 tabs
2. Deep link routing resolves to correct screen for all 12 defined routes
3. App launches to main screen in <2 seconds on iPhone 12

**Validation method:** Automated UI test suite + manual QA on physical device

---

### M02 — Authentication Flow (2026-05-02)

**Type:** Delivery | **Team:** Mobile Team | **Depends on:** M01

**Success Criteria:**
1. Email/password login returns authenticated session token
2. Biometric login (Face ID / Touch ID) passes on supported devices
3. Session refresh works without prompting re-login for 30-day sessions

**Validation method:** Integration tests against staging auth service + device lab test run

---

### M03 — Beta TestFlight Release (2026-05-23)

**Type:** Gate — all criteria must pass before M03 is marked complete | **Team:** Mobile Team | **Depends on:** M02

**Success Criteria:**
1. App passes Apple TestFlight review (Apple review approval required)
2. Zero P0 crash bugs in first 48h of internal testing
3. All core user flows (login, browse, checkout) functional end-to-end

**Gate note:** This is a release gate — M03 cannot be marked complete until TestFlight approval is received from Apple. Allow 3–5 business days for Apple review in the timeline.

---

## No warnings — all milestone criteria are outcome-based.
