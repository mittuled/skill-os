# Design Brief — Two-Factor Authentication (2FA)

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Feature | Two-Factor Authentication (2FA) |
| Prepared by | Head of Design |
| Status | Ready for designer walkthrough |
| Phase | Phase 1 — TOTP only |
| Skill | spec-translator-design |

## Problem Statement

Users lack a second layer of security on their accounts. Enterprise customers require 2FA for SOC 2 compliance and are blocking deals due to its absence. 23% of enterprise prospects cited missing 2FA as a deal blocker in Q1 win/loss analysis.

## Target Users

| Persona | Core Need |
|---|---|
| Enterprise admin | Enforce 2FA across all workspace members via org-level policy |
| Individual user | Enroll, manage, and recover 2FA without IT support |

## In-Scope Surfaces

1. Login flow — 2FA verification step
2. Account settings — 2FA enrollment (TOTP only, Phase 1)
3. Account settings — 2FA recovery codes
4. Org settings — enforce 2FA policy (admin only)
5. Login flow — recovery fallback screen

## Design Constraints

- Must use existing OTP input component from design system
- Recovery code display must follow NIST 800-63B formatting guidance
- SMS flow is Phase 2 only — Phase 1 is TOTP only
- No new third-party authentication SDKs in design scope

## Interaction Requirements

- TOTP input must auto-submit on 6th digit entry
- Invalid code must display inline error without page reload
- Recovery code copy button must show confirmation feedback (checkmark + "Copied" label, 2s duration)
- Admin enforcement toggle must require confirmation dialog before enabling — destructive action pattern from design system

## Accessibility Targets

WCAG 2.1 AA minimum. Pay special attention to:
- OTP input keyboard navigation (each digit field must be navigable without mouse)
- Error announcement via ARIA live region so screen readers announce invalid code state
- Focus management after auto-submit (shift focus to success or error state)

## Content Requirements

| Content Item | Owner | Notes |
|---|---|---|
| All 2FA error messages | Content Designer | No developer placeholder text permitted in designs |
| Recovery code security advisory | Legal review required | Before design system update |
| Enrollment success confirmation microcopy | Content Designer | Needed before prototype |

## Resolved Gaps

- PM confirmed Phase 1 is TOTP only — SMS enrollment is deferred to Phase 2

## Open Questions

1. **Does the admin enforcement policy apply retroactively to existing members, or only new logins?**
   - Owner: PM to confirm with engineering
   - Blocks: Admin enforcement screen design (cannot design the confirmation dialog without knowing the enforcement behavior)

## Acceptance Criteria

- [ ] States covered: empty, loading, error (invalid code, expired code), success, edge cases (rate limit, recovery fallback)
- [ ] Responsive breakpoints addressed (desktop, tablet, mobile)
- [ ] Accessibility checks passed (WCAG 2.1 AA) — specifically OTP keyboard nav and error announcement
- [ ] Design system compliance verified — OTP component reused, confirmation dialog pattern followed
- [ ] Content requirements met — all error messages, recovery advisory, and success states have finalized copy
- [ ] Interaction states documented (focus, active, disabled for all interactive elements)
- [ ] Recovery codes generated and displayed only once per enrollment
- [ ] Admin policy enforcement screen accessible only to workspace owner role

## Designer Walkthrough Notes

Schedule a 30-minute walkthrough with the assigned designer to confirm understanding of the TOTP-only scope boundary, the admin enforcement open question, and the content requirements that must arrive before visual design. Designer should not proceed to wireframes until the admin enforcement behavior question is resolved.
