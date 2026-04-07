# Scenario: Translate PRD into Design Brief — Two-Factor Authentication

Product has approved a PRD for adding two-factor authentication (2FA) to the product. The Head of Design needs to translate the spec into a design brief before handing it to the UX/UI designer who will begin the flow and wireframe work.

## Input Parameters

```json
{
  "feature_name": "Two-Factor Authentication (2FA)",
  "problem_statement": "Users lack a second layer of security on their accounts. Enterprise customers require 2FA for SOC 2 compliance and are blocking deals due to its absence. 23% of enterprise prospects cited missing 2FA as a deal blocker in Q1 win/loss analysis.",
  "target_users": [
    {"persona": "Enterprise admin", "need": "Enforce 2FA across all workspace members via org-level policy"},
    {"persona": "Individual user", "need": "Enroll, manage, and recover 2FA without IT support"}
  ],
  "in_scope_surfaces": [
    "Login flow — 2FA verification step",
    "Account settings — 2FA enrollment (TOTP and SMS)",
    "Account settings — 2FA recovery codes",
    "Org settings — enforce 2FA policy (admin only)",
    "Login flow — recovery fallback screen"
  ],
  "design_constraints": [
    "Must use existing OTP input component from design system",
    "Recovery code display must follow NIST 800-63B formatting guidance",
    "SMS flow is Phase 2 only — Phase 1 is TOTP only",
    "No new third-party authentication SDKs in design scope"
  ],
  "interaction_requirements": [
    "TOTP input must auto-submit on 6th digit entry",
    "Invalid code must display inline error without page reload",
    "Recovery code copy button must show confirmation feedback",
    "Admin enforcement toggle must require confirmation dialog before enabling"
  ],
  "accessibility_targets": "WCAG 2.1 AA — pay special attention to OTP input keyboard navigation and error announcement",
  "content_requirements": [
    "All 2FA error messages must be drafted by content designer — no developer placeholder text",
    "Recovery code screen requires security advisory copy reviewed by legal",
    "Enrollment success state needs onboarding confirmation microcopy"
  ],
  "gaps_resolved": [
    "PM confirmed Phase 1 is TOTP only — SMS is deferred to Phase 2"
  ],
  "open_questions": [
    "Does the admin enforcement policy apply retroactively to existing members or only new logins?"
  ],
  "custom_acceptance_criteria": [
    "Recovery codes generated and displayed only once per enrollment",
    "Admin policy enforcement screen accessible only to workspace owner role"
  ]
}
```
