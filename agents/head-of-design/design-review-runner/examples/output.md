# Design Review — Billing Settings Redesign

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Deliverable | Billing Settings Redesign — Figma file v3 |
| Review Type | Pre-Handoff |
| Reviewer | Head of Design |
| Score | 53/100 |
| Verdict | REQUIRES RE-REVIEW |
| Skill | design-review-runner |

## Executive Summary

The Billing Settings Redesign pre-handoff review found one blocking issue and two advisory items. The payment method card fails WCAG 2.1 AA contrast requirements for the active badge — this is a compliance blocker that prevents dev handoff. Two advisory items are recorded: a missing downgrade cancel state and incomplete table column annotations. The design cannot proceed to dev-ready until the contrast issue is resolved and the re-review passes.

## Criteria Results

| Criterion | Weight | Status | Notes |
|---|---|---|---|
| Design System Compliance | 20 | ✅ PASS | |
| Accessibility Compliance | 20 | 🔴 BLOCKING | Active badge fails 3:1 contrast on dark background |
| Interaction Completeness | 20 | 🟡 ADVISORY | Downgrade dialog missing cancel state |
| Content Quality | 15 | ✅ PASS | |
| Product Alignment | 15 | ✅ PASS | |
| Handoff Readiness | 10 | 🟡 ADVISORY | Table column annotations missing |

**Score: 53/100 | Verdict: REQUIRES RE-REVIEW**

## Blocking Issues

### 1. Accessibility Compliance — Active Badge Contrast (WCAG 1.4.3 AA)

**Finding:** The "active" badge on the payment method card does not meet the 3:1 contrast requirement for large/bold text against the dark card background. Current ratio: approximately 2.1:1.

**Required fix:** Update the badge background or text color to achieve ≥ 3:1 contrast. Recommend using the existing `badge-success-dark` token from the design system which has been pre-validated for this context.

**Definition of done:** Badge color updated, contrast ratio confirmed ≥ 3:1 via Figma plugin or manual check.

**Owner:** Visual Interaction Designer | **Blocks:** Dev handoff

## Advisory Findings

### 1. Interaction Completeness — Downgrade Cancel State Missing

**Finding:** The downgrade confirmation dialog only documents the "confirm downgrade" path. The "cancel" / "dismiss" path is not shown. Engineering will have to guess at the cancel behavior (return to billing page, close dialog, restore previous state?).

**Recommendation:** Add the cancel interaction path to the downgrade dialog spec. Should be a quick addition — 1 additional screen showing the closed dialog state and return to billing.

**Owner:** Visual Interaction Designer | **Priority:** Before next handoff attempt

### 2. Handoff Readiness — Invoice Table Column Annotations Incomplete

**Finding:** The invoice history table has unlabeled columns in the Figma spec. Engineering cannot determine data types, alignment, or truncation behavior without annotations.

**Recommendation:** Add annotations to all table columns: column name, data type (string/date/currency), alignment, max character length, and truncation behavior.

**Owner:** Visual Interaction Designer | **Priority:** Before handoff

## Additional Feedback

| Theme | Feedback | Severity | Owner |
|---|---|---|---|
| Visual consistency | Invoice table rows use different spacing token — should align to space-4 | Advisory | Visual Interaction Designer |

## Verdict: REQUIRES RE-REVIEW

**Dev handoff is blocked.** Address the blocking accessibility issue and both advisory items, then re-submit for a focused re-review. The re-review will spot-check the three areas above only — no full re-review required.

**Re-review target:** Within 2 business days of fixes applied.
