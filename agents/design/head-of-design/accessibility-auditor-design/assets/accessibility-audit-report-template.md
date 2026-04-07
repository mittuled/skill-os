# Accessibility Audit Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Head of Design / auditor name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | accessibility-auditor-design |

## Executive Summary

[2-3 sentences summarizing the audit outcome, overall compliance level, and most critical findings.
GUIDANCE: Lead with the pass/fail verdict and the count of critical issues. State the WCAG conformance target (e.g., 2.1 AA) and whether it was met.]

## Audit Scope

[Define what was audited: product surfaces, user flows, platforms, and devices.

GUIDANCE:
- Good: "Audited 12 screens across the onboarding flow (web, iOS) including sign-up, profile setup, and first-run experience at mobile and desktop breakpoints"
- Bad: "Audited the product"
- Format: Table listing each surface, platform, and flow path included/excluded]

## Compliance Scorecard

[Per-principle compliance summary across WCAG's four principles.

GUIDANCE:
- Good: Table with Perceivable/Operable/Understandable/Robust rows, each with pass count, fail count, and percentage
- Bad: A single "we passed most things" statement
- Format: Table with columns: Principle | Criteria Tested | Pass | Fail | Compliance % ]

## Automated Findings

[Results from automated scanning tools (axe-core, Lighthouse, contrast checkers).

GUIDANCE:
- Good: Each finding with WCAG criterion, element selector, screenshot, and severity
- Bad: "Lighthouse score was 78"
- Format: Table per tool with columns: ID | WCAG Criterion | Element | Severity | Screenshot Ref]

## Manual Testing Results

[Findings from keyboard navigation, screen reader, magnification, and reduced-motion testing.

GUIDANCE:
- Good: "VoiceOver on Safari announces the 'Submit' button as 'button, Submit application' — correct. However, the modal close button is announced as 'button' with no label."
- Bad: "Screen reader testing was done"
- Format: Matrix with rows per flow step, columns per assistive technology, cell contains pass/fail/finding]

## Prioritised Issue Register

[All findings consolidated, deduplicated, and priority-ranked.

GUIDANCE:
- Good: Each issue with ID, WCAG criterion, severity (critical/major/minor), affected component, screenshot, and remediation recommendation
- Bad: Flat list of issues without priority or grouping
- Format: Table sorted by severity with columns: ID | WCAG | Severity | Component | Description | Remediation | Owner | Effort]

## Recommendations

[Prioritised list of remediation actions based on audit findings.
GUIDANCE: Each recommendation should be:
- Specific (not "fix contrast" but "update --color-text-secondary token from #999 to #767676 to achieve 4.52:1 ratio")
- Actionable (assigned to design or engineering with effort estimate)
- Prioritised (P1: critical blockers, P2: major issues, P3: minor improvements)]

## Appendices

### A. Methodology

[How the audit was conducted: tools used, assistive technologies tested, WCAG version and conformance level, testing environment details, session duration]

### B. Supporting Data

[Raw tool output files, full screenshot library, session recordings of assistive technology testing, and colour contrast calculation details]
