# Integration Review Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | third-party-integrator-review |

## Executive Summary

[2-3 sentences summarizing the vendor, the integration purpose, and the decision (approve/conditional/reject).
GUIDANCE: Lead with the decision and the most significant finding.]

## Product Fit Assessment

[Alignment analysis between the integration and product goals.

GUIDANCE:
- Good: "Vendor: Stripe Connect. Purpose: Enable marketplace payouts to sellers. User Need: Validated in 6 seller interviews — manual payout processing takes 4 hours/week per operations staff. Alignment Score: Strong. Roadmap Priority: Q2 marketplace expansion initiative. Alternatives Considered: PayPal Commerce Platform (rejected: higher per-transaction fees, weaker API documentation), custom build (rejected: 6-month effort, compliance burden)."
- Bad: "Good fit for our product"
- Format: Vendor name, purpose, validated user need with evidence, alignment score (Strong/Moderate/Weak), roadmap link, alternatives evaluated]

## Technical Risk Summary

[API reliability, performance impact, and failure modes.

GUIDANCE:
- Good: "SLA: 99.99% uptime (historical: 99.98% over 12 months). Latency: P50 120ms, P99 450ms (within our 500ms budget). Failure mode: If Stripe is unreachable, payouts queue locally and retry with exponential backoff. Data flow: Seller bank details stored in Stripe (PCI-compliant vault), only Stripe account IDs stored in our database."
- Bad: "Stripe is reliable"
- Format: Labeled fields: SLA, Latency, Failure Mode, Data Flow, Rate Limits]

## Compliance Checklist

[Regulatory and data handling assessment.

GUIDANCE:
- Good: Table with Requirement, Status (Pass/Fail/N/A), Evidence. Covering: GDPR, SOC 2, PCI DSS, Data Residency, Encryption (rest/transit), Data Deletion, Sub-processors.
- Bad: "They have SOC 2"
- Format: Markdown table, one row per compliance requirement]

## Cost Analysis

[Pricing, scale projections, and lock-in.

GUIDANCE:
- Good: "Current usage projection: 500 payouts/month x $0.25 = $125/month. At 3x scale: $375/month. Contract: Pay-as-you-go, no minimum commitment. Switching costs: Moderate — seller bank details stored in Stripe vault require re-collection if switching providers. Exit estimate: 2 weeks engineering + seller re-onboarding."
- Bad: "Affordable"
- Format: Current cost, 3x scale cost, contract terms, switching cost estimate with engineering effort]

## Recommendations

[Post-decision actions.
GUIDANCE: Each recommendation should be:
- Specific (not "proceed with integration" but "execute DPA with Stripe legal by 2026-04-01 and configure webhook for payout failure notifications")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Evaluation framework: product fit scoring, technical risk assessment, compliance checklist, cost modelling approach.]

### B. Supporting Data

[Vendor SLA reports, pricing documentation, compliance certifications, competitive vendor comparison matrix.]
