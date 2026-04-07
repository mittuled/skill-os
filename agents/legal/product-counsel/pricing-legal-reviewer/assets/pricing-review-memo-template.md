# Pricing Legal Review Memo

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | pricing-legal-reviewer |

## Executive Summary

[2-3 sentences summarizing the pricing model reviewed, compliance verdict, and primary recommendation.
GUIDANCE: Lead with the recommendation (compliant/modify/reject) and the highest-risk area identified.]

## Antitrust Risk Assessment

[Analysis of pricing model for antitrust concerns.

GUIDANCE:
- Good: "Usage-based pricing with volume discounts. Robinson-Patman analysis: volume discounts justified by cost savings (economies of scale in infrastructure). No similarly situated customers receive different pricing without cost justification. Tying: no bundling requirements. Predatory pricing: margins positive at all tiers."
- Bad: "No antitrust issues"
- Format: Analysis by antitrust dimension (predatory pricing, discrimination, tying, price-fixing risk)]

## Consumer Protection Checklist

[Billing practice compliance verification.

GUIDANCE:
- Good: Table with Requirement, Applicable Law, Status (Pass/Fail), Evidence, Remediation Needed
- Bad: "Billing is compliant"
- Format: Checklist covering auto-renewal, disclosures, refund, cancellation, free trials, currency conversion]

## Pricing Review Recommendation

[Formal recommendation with approved pricing terms.

GUIDANCE:
- Good: "Recommendation: MODIFY. Free trial auto-conversion requires explicit consent disclosure per California ARL Section 17602. Current flow shows pricing on signup but no renewal reminder. Required change: send renewal notice 7 days before first charge with clear cancellation instructions."
- Bad: "Pricing is mostly fine"
- Format: Recommendation category, specific changes required, approved pricing terms for implementation]

## Recommendations

[Post-review actions.
GUIDANCE: Each recommendation should be:
- Specific (not "fix billing" but "add pre-renewal email notification 7 days before auto-conversion per CA ARL Section 17602")
- Actionable (assignable to product/engineering)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Laws reviewed: Sherman Act, Robinson-Patman Act, FTC Act Section 5, California ARL, FTC Negative Option Rule, EU Consumer Rights Directive, Australian Consumer Law.]

### B. Supporting Data

[Pricing model documentation, billing flow screenshots, auto-renewal implementation details, competitive pricing data (if relevant to predatory pricing analysis).]
