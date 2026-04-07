# Accessibility Audit Report: SaaS Onboarding Flow

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-03-15 |
| Author | Head of Design |
| Version | 1.0 |
| Status | Final |
| Skill | accessibility-auditor-design |

## Executive Summary

The onboarding flow **fails WCAG 2.1 AA conformance** with 4 critical issues and 7 major issues across 5 screens. The most severe finding is a keyboard trap in the sign-up form (confirming the 3 reported support tickets) where custom dropdown components intercept Tab key events without providing an escape mechanism. Remediation of critical issues is estimated at 2 design days + 3 engineering days.

## Compliance Scorecard

| Principle | Criteria Tested | Pass | Fail | Compliance % |
|-----------|----------------|------|------|-------------|
| Perceivable | 12 | 9 | 3 | 75% |
| Operable | 10 | 5 | 5 | 50% |
| Understandable | 8 | 7 | 1 | 87.5% |
| Robust | 6 | 4 | 2 | 66.7% |
| **Total** | **36** | **25** | **11** | **69.4%** |

## Critical Findings

| ID | WCAG Criterion | Severity | Component | Description | Remediation |
|----|---------------|----------|-----------|-------------|-------------|
| A-001 | 2.1.2 No Keyboard Trap | Critical | Sign-up form dropdown | Custom role-selector dropdown traps keyboard focus; Escape key does not close it | Replace with design system `Select` component that implements ARIA listbox pattern with Escape-to-close |
| A-002 | 1.4.3 Contrast (Minimum) | Critical | Placeholder text, all forms | Placeholder text (#B0B0B0 on #FFFFFF) has 2.65:1 ratio, below 4.5:1 minimum | Update `--color-text-placeholder` token from #B0B0B0 to #767676 (4.54:1) |
| A-003 | 4.1.2 Name, Role, Value | Critical | Team invite autocomplete | Autocomplete suggestions have no ARIA role or live-region announcement | Add `role="listbox"` to suggestion list, `role="option"` to items, and `aria-live="polite"` region |
| A-004 | 2.4.3 Focus Order | Critical | First-project wizard | Focus jumps from step 3 header to step 1 input on Tab, bypassing visible step 3 fields | Fix tab index ordering to follow visual layout; remove all `tabindex` values > 0 |

## Major Findings

| ID | WCAG Criterion | Severity | Component | Remediation |
|----|---------------|----------|-----------|-------------|
| A-005 | 1.1.1 Non-text Content | Major | Workspace setup illustration | Decorative SVG has no `aria-hidden="true"`; screen readers announce file name |
| A-006 | 1.4.11 Non-text Contrast | Major | Form field borders | Input border (#D4D4D4 on #FFFFFF) at 1.59:1, below 3:1 for UI components |
| A-007 | 2.4.7 Focus Visible | Major | All buttons | Focus ring uses `outline: none` with no replacement; keyboard users cannot see focus |
| A-008 | 3.3.2 Labels or Instructions | Major | Email verification code input | No visible label; relies on placeholder only which disappears on input |
| A-009 | 2.4.1 Bypass Blocks | Major | All screens | No skip-to-content link; keyboard users must tab through header on every screen |
| A-010 | 1.3.1 Info and Relationships | Major | Progress stepper | Visual progress indicator has no ARIA markup; screen readers cannot determine current step |
| A-011 | 3.3.1 Error Identification | Major | Sign-up form | Validation errors appear visually but are not associated with fields via `aria-describedby` |

## Recommendations

- **P1 (this sprint)**: Fix A-001 through A-004. These are task-blocking issues affecting keyboard and screen reader users. Design: update Select component spec, placeholder token, autocomplete ARIA pattern. Engineering: implement fixes. Estimated: 2 design days, 3 eng days.
- **P2 (next sprint)**: Fix A-005 through A-011. These cause significant friction but do not block task completion. Design: update focus ring spec, add visible labels, define ARIA patterns for stepper. Estimated: 1.5 design days, 2 eng days.
- **P3 (backlog)**: Add automated accessibility CI checks (axe-core in pipeline) to prevent regression.
