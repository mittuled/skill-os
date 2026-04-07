# Scope Boundary Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | scope-boundary-setter |

## Executive Summary

[2-3 sentences summarizing the sprint/release, total scope, capacity utilisation, and lock status.
GUIDANCE: Lead with the scope lock decision and utilisation percentage.]

## Scope Inventory

[All committed items with estimates and owners.

GUIDANCE:
- Good: Table with Item ID, Title, Estimate (SP), Owner, Status (Ready/In Progress/Blocked), Dependencies
- Bad: "Sprint backlog items"
- Format: Markdown table, one row per item, total estimate at bottom]

## In Scope

[Items committed for delivery.

GUIDANCE:
- Good: "8 stories totalling 21 SP. Capacity utilisation: 78% of 27 SP available. All items have estimates, acceptance criteria, and assigned owners."
- Bad: "The sprint backlog"
- Format: List of item IDs and titles with total SP and utilisation percentage]

## Out of Scope

[Items explicitly excluded with rationale.

GUIDANCE:
- Good: Table with Item ID, Title, Exclusion Reason, Future Destination (backlog/next sprint/cancelled)
- Bad: "Other stuff"
- Format: Markdown table with documented reason per exclusion]

## Conditional Items

[Items that may be promoted to In if specific triggers fire.

GUIDANCE:
- Good: Table with Item ID, Title, Trigger Condition, Deadline for Trigger, Estimate
- Bad: "Maybe items"
- Format: Markdown table with explicit trigger per item]

## Change Protocol

[Rules for scope changes after lock.

GUIDANCE:
- Good: "Any scope change request must include: (1) item description with estimate, (2) proposed trade-off (item to remove), (3) impact on sprint goal. Requests submitted to PM via Slack #sprint-changes. Approval authority: PM for items <3 SP, PM + Eng Lead for items >=3 SP. Response SLA: 4 hours during business hours."
- Bad: "Ask the PM"
- Format: Structured paragraph with request format, submission channel, approval authority, and SLA]

## Recommendations

[Actions to maintain scope integrity.
GUIDANCE: Each recommendation should be:
- Specific (not "protect the scope" but "schedule mid-sprint scope check on Wednesday to review conditional item triggers")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scope classification criteria, capacity calculation method, buffer allocation rationale.]

### B. Supporting Data

[Team capacity breakdown per person, historical sprint completion rates, backlog priority rankings.]
