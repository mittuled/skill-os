# Legal Risk Memo

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | General Counsel |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | legal-idea-reviewer |

## Executive Summary

[2-3 sentences stating the go/conditional-go/no-go recommendation and the primary legal risks driving it.
GUIDANCE: Lead with the recommendation. Example: "Conditional Go. The proposed fintech lending product is legally viable in 48 states but requires state-by-state lending license analysis and a TILA-compliant disclosure flow before launch. Two material risks require mitigation before development proceeds."]

## Concept Overview

[Brief summary of the business idea being reviewed.

GUIDANCE:
- Good: "Mobile app enabling peer-to-peer lending between verified users, targeting US market. Revenue model: transaction fees on originated loans. Data collected: SSN, bank account, credit score. Key technology: ML-based credit scoring."
- Bad: "Lending app."
- Format: Structured table with target market, revenue model, data flows, and technology components]

| Aspect | Detail |
|--------|--------|
| Product/Service | [Description] |
| Target Market | [Geography, customer segment] |
| Revenue Model | [How money is made] |
| Data Collected | [Types of data, sources] |
| Key Technology | [Notable technology choices with legal implications] |

## Risk Assessment Matrix

[Color-coded risk assessment across five legal dimensions.

GUIDANCE:
- Good: Each dimension scored with specific regulatory citations and evidence. "Regulatory: RED - Requires state lending licenses in each operating state per state usury laws; TILA and ECOA compliance mandatory for credit decisions."
- Bad: "Regulatory: Yellow - some risk."
- Format: Table with dimension, rating (Green/Yellow/Red), score (0-10), key findings, and specific regulations]

| Dimension | Rating | Score | Key Findings | Applicable Regulations |
|-----------|--------|-------|--------------|----------------------|
| Regulatory Compliance | [Green/Yellow/Red] | [0-10] | [Findings] | [Specific laws/regulations] |
| IP / Freedom to Operate | [Green/Yellow/Red] | [0-10] | [Findings] | [Patents, trademarks at issue] |
| Data Privacy & Security | [Green/Yellow/Red] | [0-10] | [Findings] | [GDPR, CCPA, HIPAA, etc.] |
| Liability Exposure | [Green/Yellow/Red] | [0-10] | [Findings] | [Liability theories, insurance] |
| Contractual Constraints | [Green/Yellow/Red] | [0-10] | [Findings] | [Specific contracts at issue] |

## Detailed Analysis

### Regulatory Compliance
[Detailed analysis of applicable regulations, licensing requirements, and compliance pathway.

GUIDANCE: Cite specific statutes and regulations. Distinguish between requirements that shape the product (must-have) and best practices (should-have).]

### IP and Freedom to Operate
[Prior art considerations, trademark conflicts, trade secret risks.

GUIDANCE: Note whether a formal freedom-to-operate search is needed and the cost/timeline for one.]

### Data Privacy and Security
[Data flow analysis against applicable privacy frameworks.

GUIDANCE: Map each data type to its applicable privacy regime and identify required consent mechanisms.]

### Liability Exposure
[Product liability, professional responsibility, content liability analysis.

GUIDANCE: Identify whether insurance is available and at what cost for identified liability vectors.]

### Contractual Constraints
[Review of existing obligations that may conflict with the concept.

GUIDANCE: List each relevant contract and the specific clause that creates the constraint.]

## Recommendations

[Prioritized list of actions required to proceed.

GUIDANCE: Each recommendation should be:
- Specific: "Obtain state lending licenses in CA, NY, TX before launch" not "Get licenses"
- Actionable: Assignable to a person or team with estimated cost and timeline
- Prioritized: P1 (must resolve before development), P2 (must resolve before launch), P3 (should resolve within 6 months of launch)]

| Priority | Action | Owner | Timeline | Est. Cost |
|----------|--------|-------|----------|-----------|
| P1 | [Action] | [Owner] | [Timeline] | [Cost] |

## Appendices

### A. Methodology

[Frameworks applied (risk assessment matrix per scoring rubric at `references/scoring-rubric.md`), regulations researched, databases consulted, scope limitations]

### B. Regulatory Reference List

[Full citations for all regulations mentioned in the analysis, organized by dimension]
