# Accessibility Check Report — Checkout Flow v2

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Artifact | Checkout Flow v2 — Figma file rev 14 |
| Reviewer | Head of Design |
| Status | CONDITIONAL PASS |
| Skill | accessibility-checker-design |

## Executive Summary

The Checkout Flow v2 design passes 6 of 9 WCAG 2.1 AA criteria, achieving a weighted score of 65/100. Three issues were identified that must be resolved before dev handoff: form error states rely on color alone, focus states are missing on primary CTA buttons, and icon ARIA labels are absent from the payment screen spec. The design is conditionally approved pending resolution of all three findings.

## Criteria Results

| Criterion | WCAG | Weight | Status |
|---|---|---|---|
| Contrast ratio ≥ 4.5:1 for normal text | 1.4.3 AA | 20 | ✅ PASS |
| Contrast ratio ≥ 3:1 for large text | 1.4.3 AA | 10 | ✅ PASS |
| Touch targets ≥ 44×44pt | 2.5.5 / mobile | 10 | ✅ PASS |
| Color not sole indicator of state | 1.4.1 AA | 10 | ❌ FAIL |
| Focus states documented | 2.4.7 AA | 15 | ❌ FAIL |
| Focus order logical | 2.4.3 AA | 10 | ✅ PASS |
| Alt text specified | 1.1.1 AA | 10 | ✅ PASS |
| ARIA labels documented | 4.1.2 AA | 10 | ❌ FAIL |
| Error messages descriptive | 3.3.1 AA | 5 | ✅ PASS |

**Weighted Score: 65/100 | Verdict: CONDITIONAL PASS**

## Findings — Blocking Issues

### Finding 1: Error States Use Color Only (WCAG 1.4.1 AA)

**Affected screens:** Address Entry, Payment Entry (all form fields with validation)

**Issue:** Error states on form fields use a red border as the sole visual indicator. Users with red-green color blindness (~8% of male users) cannot distinguish the error state from the default field state.

**Required fix:** Add an error icon (⚠ or ✕) inside or adjacent to the field, plus an inline error label below the field in the existing error message style. Color may remain but cannot be the only signal.

**Acceptance criteria:** Error state distinguishable from default state without color perception.

---

### Finding 2: Focus States Missing on Primary CTAs (WCAG 2.4.7 AA)

**Affected screens:** All 6 screens — "Continue," "Place Order," and "Try Again" buttons

**Issue:** Focus ring styling is not documented in the Figma spec for primary CTA buttons. Engineering will render the browser default (or none) without explicit design specification.

**Required fix:** Add a focus state variant to each CTA button component showing a 2px solid focus ring in the brand's focus color token (#0057B7 or equivalent), offset 2px from the button border.

**Acceptance criteria:** Focus state variant present in every primary button component in the Figma library.

---

### Finding 3: Icon ARIA Labels Missing (WCAG 4.1.2 AA)

**Affected screens:** Payment Entry screen

**Issue:** The credit card icon and the "secure payment" lock icon have no ARIA label annotations in the spec. Screen readers will skip or announce these as unlabelled graphics.

**Required fix:** Add ARIA label annotations to the Figma spec: credit card icon → `aria-label="Credit card"`, lock icon → `aria-label="Secure payment"`. Mark both as `role="img"`.

**Acceptance criteria:** ARIA annotations present on all non-decorative icons in the payment screen layer.

## Verdict and Next Steps

| Step | Owner | Due |
|---|---|---|
| Add error icon + inline label to all error states | Visual Interaction Designer | Before next design review |
| Add focus state variants to all primary CTA buttons | Visual Interaction Designer | Before next design review |
| Add ARIA label annotations to payment screen icons | Visual Interaction Designer | Before next design review |
| Re-run accessibility check on updated Figma file | Head of Design | After fixes applied |

**Handoff is blocked until all three findings are resolved.** Once fixed, the file may proceed to dev-ready status without a full re-review — spot check of the three affected areas is sufficient.
