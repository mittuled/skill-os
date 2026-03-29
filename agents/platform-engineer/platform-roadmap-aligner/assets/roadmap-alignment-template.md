# Platform Roadmap Alignment

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Agent role / human name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | platform-roadmap-aligner |

## Executive Summary

[2-3 sentences summarizing alignment status: number of dependencies mapped, mismatches found, and agreed priority changes.
GUIDANCE: Lead with the most critical timing mismatch. State whether the platform roadmap is ahead or behind product needs.]

## Dependency Map

[Map product features to their platform dependencies with required delivery dates.

GUIDANCE:
- Good: "Feature: Real-time notifications (Product Q2). Platform dep: WebSocket infrastructure (not on roadmap). Required by: 2024-04-01 (4-week integration lead time). Current status: not started. Risk: feature delayed 6+ weeks if platform work not prioritized."
- Bad: "Notifications need WebSockets."
- Format: Table with feature, platform dependency, required date, current status, and risk level]

| Feature | Platform Dependency | Required By | Platform Status | Risk |
|---------|-------------------|-------------|----------------|------|
| [Name] | [Capability] | [Date] | [Not started / In progress / Complete] | [High/Medium/Low] |

## Alignment Gap Analysis

[Cross-reference dependency map against current platform roadmap.

GUIDANCE:
- Good: "Gap 1: WebSocket infra needed Q2 but not on platform roadmap. Gap 2: Search indexing on platform roadmap for Q3 but product needs it Q2. Gap 3: Auth service upgrade on both roadmaps, timing aligned."
- Bad: "Some things don't line up."
- Format: Table with gap, product timeline, platform timeline, and delta]

## Priority Negotiation

[Document trade-offs discussed and agreed priorities.

GUIDANCE:
- Good: "Trade-off: Prioritizing WebSocket infra delays database sharding by 4 weeks. Decision: Accept sharding delay because notifications feature has $200K ARR commitment. Approved by: VP Engineering, 2024-01-15."
- Bad: "We agreed on priorities."
- Format: Table with trade-off, what gains, what loses, decision, and approver]

## Recommendations

[Prioritized roadmap changes.
GUIDANCE: Each recommendation should be:
- Specific (not "align roadmaps" but "add WebSocket infrastructure to Q2 platform sprint, displacing sharding work to Q3")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Product roadmap version reviewed, platform roadmap version, stakeholders consulted, meeting dates]

### B. Supporting Data

[Product roadmap extract, platform roadmap current state, dependency analysis spreadsheet]
