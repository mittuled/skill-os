# Risk Register

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | risk-register-maintainer |

## Executive Summary

[2-3 sentences summarizing total risk count, risk level distribution, and key changes since last review.
GUIDANCE: Lead with the number of critical/high risks and any new risks added or escalated since last quarter.]

## Risk Summary Dashboard

[High-level risk posture overview.

GUIDANCE:
- Good: "Total risks: 24. Critical: 2, High: 5, Medium: 11, Low: 6. Changes since Q4: 3 new risks added, 2 risks escalated (Medium to High), 4 risks closed. Top risk category: Third-Party (8 risks)."
- Bad: "We have some risks"
- Format: Summary table with counts by level and category, trend indicators]

## Active Risk Register

[Full register of all open risks.

GUIDANCE:
- Good: Table with Risk ID, Title, Category, Description, Affected Assets, Existing Controls, Inherent Risk (LxI), Residual Risk (LxI), Treatment, Mitigation Plan, Owner, Review Date, Status
- Bad: "Various risks exist"
- Format: Structured table per `references/risk-assessment-framework.md` entry template]

## Risk Mitigation Tracker

[Status of open mitigation actions.

GUIDANCE:
- Good: Table with Risk ID, Mitigation Action, Owner, Deadline, Status (Not Started/In Progress/Complete/Overdue), Evidence of Completion
- Bad: "We are working on mitigations"
- Format: Action tracker with accountability and completion evidence]

## Risk Acceptance Log

[Documented risk acceptance decisions.

GUIDANCE:
- Good: "RISK-2026-003: Legacy API without MFA. Residual risk: Medium (6). Acceptance rationale: API scheduled for deprecation in Q3. Compensating control: IP allowlisting + API key rotation quarterly. Accepted by: CTO on 2026-01-15. Review date: 2026-04-15."
- Bad: "We accept some risks"
- Format: Per-risk acceptance with rationale, compensating controls, approver, and review date]

## Quarterly Review Notes

[Changes and observations from the review cycle.

GUIDANCE:
- Good: "New risks: RISK-2026-012 (vendor X breach notification), RISK-2026-013 (new state privacy law). Escalated: RISK-2025-008 from Medium to High after failed pentest finding. Closed: RISK-2025-003 (MFA rollout complete, verified in access review)."
- Bad: "Review completed"
- Format: New risks, escalated risks, de-escalated risks, closed risks with rationale]

## Recommendations

[Risk management improvement actions.
GUIDANCE: Each recommendation should be:
- Specific (not "reduce risk" but "implement automated vulnerability scanning for the 3 unscanned production APIs by Q2")
- Actionable (assignable to security/engineering)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Risk assessment performed per `references/risk-assessment-framework.md`. Likelihood x Impact scoring on 5x5 matrix. Risk appetite thresholds: Critical (20-25), High (10-16), Medium (5-9), Low (1-4). Aligned with ISO 27005 and NIST SP 800-30.]

### B. Supporting Data

[Vulnerability scan results, incident reports, audit findings, threat intelligence reports, vendor security assessment summaries.]
