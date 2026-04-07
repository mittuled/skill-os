# Risk Register

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | risk-register-builder |

## Executive Summary

[2-3 sentences summarizing total risk count, high-severity count, and the top risk requiring immediate attention.
GUIDANCE: Lead with the most critical risk and its mitigation status.]

## Scope Statement

[What initiative, release, or milestone this register covers.

GUIDANCE:
- Good: "This register covers the RBAC feature initiative (Q2 2026). Time horizon: discovery through GA launch (10 weeks). Decision context: go/no-go for sprint commitment at Phase 2 gate."
- Bad: "RBAC risks"
- Format: Initiative name, time horizon, decision the register informs]

## Risk Table

[Scored risks across all four categories.

GUIDANCE:
- Good: Table with Risk ID, Category, Description, Likelihood (L/M/H), Impact (L/M/H), Composite (1-9), Source, Mitigation Strategy, Owner, Action Items, Review Date, Trigger Indicator, Trigger Threshold, Escalation Path
- Bad: "There are delivery risks"
- Format: Full markdown table; one row per risk. High-severity risks (composite 6+) highlighted with bold ID.]

## Risk Summary by Category

[Aggregate view of risk distribution.

GUIDANCE:
- Good: Table with Category, Total Risks, High (6-9), Medium (3-5), Low (1-2)
- Bad: "Mostly delivery risks"
- Format: Summary table with counts per severity per category]

## Cascade Analysis

[Risks that compound each other.

GUIDANCE:
- Good: "RK-003 (key engineer departure) amplifies RK-001 (schedule delay) — losing the migration specialist increases schedule risk from Medium to High. RK-005 (API rate limit) triggers RK-007 (adoption shortfall) if users experience timeouts during first use."
- Bad: "Some risks are related"
- Format: Prose paragraph per cascade chain, referencing risk IDs]

## Recommendations

[Actions to reduce overall risk exposure.
GUIDANCE: Each recommendation should be:
- Specific (not "mitigate risks" but "hire contract migration specialist by W3 to reduce single-point-of-failure risk on RK-003")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Risk identification approach (structured brainstorm across 4 categories), scoring model (3x3 likelihood x impact), mitigation strategy taxonomy (avoid/reduce/transfer/accept), review cadence.]

### B. Supporting Data

[Engineering estimates, competitive intelligence, post-mortem references, compliance requirements, historical risk outcomes from analogous projects.]
