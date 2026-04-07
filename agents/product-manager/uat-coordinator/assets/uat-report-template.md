# UAT Summary Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | uat-coordinator |

## Executive Summary

[2-3 sentences summarizing participants, pass/fail decision, and critical findings.
GUIDANCE: Lead with the go/no-go recommendation and the most significant finding.]

## UAT Plan Summary

[Participants, scenarios, and timeline.

GUIDANCE:
- Good: "Participants: 5 design partners (3 enterprise, 2 mid-market). Test period: 2026-04-01 to 2026-04-05. Scenarios: 8 (covering role creation, assignment, enforcement, edge cases). Acceptance threshold: Zero critical issues, max 2 major issues with documented workarounds."
- Bad: "We tested with some customers"
- Format: Labeled fields: Participant Count, Segments, Test Period, Scenario Count, Acceptance Threshold]

## Session Results

[Per-participant findings.

GUIDANCE:
- Good: Per-participant subsection with: Participant (anonymised ID), Segment, Scenarios Completed (X/Y), Issues Found (by severity), Key Quotes, Overall Satisfaction (1-5).
- Bad: "Participants liked it"
- Format: Repeated subsection per participant with structured fields]

## Issue Summary

[Aggregated issues across all participants.

GUIDANCE:
- Good: Table with Issue ID, Severity (Critical/Major/Minor/Cosmetic), Description, Affected Scenarios, Frequency (N of M participants), Status (Open/Resolved/Won't Fix)
- Bad: "A few bugs found"
- Format: Markdown table sorted by severity then frequency]

## Pass/Fail Decision

[Go-live recommendation based on acceptance threshold.

GUIDANCE:
- Good: "Decision: PASS WITH CAVEATS. Critical issues: 0. Major issues: 1 (role inheritance not applied to nested teams — workaround: assign roles at each team level). Minor issues: 3. Acceptance threshold met. Recommendation: Proceed to GA with major issue documented in known issues and hotfix scheduled for 2026-04-22."
- Bad: "Good to go"
- Format: Decision, criteria check (critical count, major count vs. threshold), recommendation with timeline]

## Recommendations

[Post-UAT actions.
GUIDANCE: Each recommendation should be:
- Specific (not "fix bugs" but "file JIRA ticket for role inheritance on nested teams and schedule hotfix for sprint 14")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[UAT coordination approach: participant selection criteria, scenario design, feedback capture method, severity classification, acceptance threshold definition.]

### B. Supporting Data

[Session recordings, raw feedback notes, environment configuration, test data descriptions.]
