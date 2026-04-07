# GA Compliance Review Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | compliance-ga-reviewer-legal |

## Executive Summary

[2-3 sentences summarizing the product/feature reviewed, overall compliance status, and clearance recommendation.
GUIDANCE: Lead with the clearance decision (unconditional / conditional / blocked) and the number of hard blockers remaining.]

## Compliance Checklist

[Compiled regulatory requirements with implementation status.

GUIDANCE:
- Good: Table with Requirement ID, Source (regulation/PRD/contract), Description, Verification Method, Status (Pass/Fail/N-A), Evidence Reference
- Bad: "Checked GDPR compliance"
- Format: Numbered checklist covering privacy, accessibility, data protection, disclosures, sector-specific rules]

## Implementation Verification Results

[Verification of each requirement against actual product implementation.

GUIDANCE:
- Good: "REQ-003 (Cookie Consent): Tested in Chrome, Firefox, Safari. Consent banner appears before tracking cookies set. Reject-all button functional. Evidence: test screenshots in Appendix B, consent management platform logs."
- Bad: "Cookie consent works"
- Format: Table with Requirement ID, Test Performed, Result (Pass/Fail), Evidence Reference, Notes]

## Gap Remediation Tracker

[Identified compliance gaps with severity and remediation status.

GUIDANCE:
- Good: Table with Gap ID, Description, Severity (Hard Blocker/Soft Blocker), Remediation Action, Owner, Target Date, Status
- Bad: "Some things need fixing"
- Format: Tracker with clear hard/soft blocker classification and rationale]

## Compliance Sign-Off Memo

[Formal clearance documentation.

GUIDANCE:
- Good: "Compliance clearance issued conditionally. Conditions: (1) DPA with analytics vendor executed by [date], (2) WCAG 2.1 AA remediation for screen reader navigation completed by [date]. Accepted risks: Cookie consent translation for Japanese locale pending — low risk given <1% Japan traffic."
- Bad: "Approved"
- Format: Clearance type, scope, assumptions, conditions, accepted risks with rationale, post-launch obligations, expiration]

## Recommendations

[Prioritized list of post-clearance actions.
GUIDANCE: Each recommendation should be:
- Specific (not "fix accessibility" but "remediate 3 WCAG 2.1 AA failures identified in screen reader navigation audit")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Requirements sourced from: compliance scanner output, PRD NFR appendix, post-scan regulatory changes. Verification methods: manual testing, automated scans, document review, third-party audit reports.]

### B. Supporting Data

[Test screenshots, accessibility audit reports, DPA execution confirmations, consent management platform configurations, privacy policy review notes.]
