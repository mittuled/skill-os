# Scope Boundary Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [VP Engineering / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | scope-boundary-setter-eng |

## Executive Summary

[2-3 sentences identifying the delivery, its timeline, and the most important scope boundary being established.
GUIDANCE: Lead with the most contentious or risk-prone boundary. Example: "This document defines scope for the Payments v2 delivery (target: 2026-05-01). The most critical boundary is that multi-currency support is explicitly out of scope for this phase — it will be addressed in Phase 3. Any requests to include currency features must go through the formal change control process defined in Section 4."]

## In-Scope Items

[Explicit list of everything this delivery covers. Ambiguity here invites scope creep.

GUIDANCE:
- Good: Reference specific feature names, ticket IDs, or spec sections; include constraints on depth (e.g., "single-currency only")
- Bad: "The features in the Payments v2 spec"
- Format: Numbered list; for each item, specify the depth of implementation if relevant]

| # | Item | Spec Reference | Implementation Depth | Notes |
|---|------|---------------|---------------------|-------|
| 1 | [Feature name] | [Spec section / Ticket ID] | [Full / MVP / Partial — describe] | [Any constraints] |
| 2 | [Feature name] | [Spec section / Ticket ID] | [Full / MVP / Partial — describe] | |

## Out-of-Scope Items

[Explicit exclusions. Every "no" here prevents a future misunderstanding.

GUIDANCE:
- Good: Name specific features, edge cases, or integrations that people have asked about and explicitly exclude them with rationale
- Bad: "Everything not listed above"
- Format: Numbered list with rationale and planned resolution]

| # | Item | Why Excluded | Planned Resolution |
|---|------|-------------|-------------------|
| 1 | [Feature / capability] | [Too large for this phase / Not yet specified / Dependency on Phase N] | [Phase N+1 / Future roadmap item / Not currently planned] |
| 2 | [Feature / capability] | [Reason] | [Resolution] |

## Boundary Decisions

[Explicit decisions made about items that were debated or are ambiguous.

GUIDANCE:
- Good: Record every boundary call that required a judgment, including who made it and why
- Bad: Omit this section because "everyone agreed"
- Format: Table]

| Item | Decision | Rationale | Decision Owner | Date |
|------|----------|-----------|---------------|------|
| [Item that was debated] | [In scope / Out of scope] | [Why this decision was made] | [Name] | [YYYY-MM-DD] |

## Change Control Process

[How mid-phase scope changes are requested, evaluated, and approved or rejected.

GUIDANCE:
- Good: Specify exactly who can request, who reviews the impact, and who approves or rejects
- Bad: "Discuss with the team"
- Format: Process steps]

### How to Request a Scope Change

1. Requestor submits a scope change ticket with: (a) the item requested, (b) the business justification, (c) the urgency level
2. Tech lead assesses engineering effort and dependency impact within 24 hours
3. VP Engineering reviews the request with the engineering effort assessment and renders a decision: Approve / Defer / Reject
4. Decision logged in the scope change decision log (Section 5)

### Approval Authority

| Change Size | Effort Required | Approval Authority |
|------------|----------------|-------------------|
| Minor (bug fix or copy change) | < 1 day | Tech Lead |
| Small (1–3 days) | 1–3 days | Tech Lead + PM |
| Medium (4–10 days) | 4–10 days | VP Engineering |
| Large (> 10 days) | > 10 days | VP Engineering + CEO/CPO |

## Scope Change Decision Log

[Record of all scope change requests and their outcomes.

GUIDANCE:
- Every request must be logged, even if rejected — rejection rationale is as valuable as approval
- Format: Table updated in real time as requests arrive]

| Date | Requestor | Item Requested | Effort Assessment | Decision | Decision Owner | Rationale |
|------|-----------|---------------|------------------|----------|---------------|-----------|
| [Date] | [Name] | [Description] | [Story points / days] | Approved / Deferred / Rejected | [Name] | [Why] |

## Recommendations

[Prioritized guidance for stakeholders.
GUIDANCE: Include any pre-emptive communications needed to prevent scope requests]

- **P1**: [Communicate out-of-scope items proactively to stakeholders most likely to request them]
- **P2**: [Set a recurring scope review cadence if this is a long-running delivery]
- **P3**: [Document lessons from any previous scope boundary failures on similar deliveries]

## Appendices

### A. Methodology

[Source documents reviewed (spec version, PRD date, phase plan), stakeholders consulted in boundary setting, decision process used (consensus / VP decision / joint product-engineering agreement)]

### B. Supporting Data

[Links to approved spec, phase plan, effort estimates, and any scope change requests from pre-delivery planning]
