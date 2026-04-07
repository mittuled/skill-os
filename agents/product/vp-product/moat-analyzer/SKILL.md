---
name: moat-analyzer
description: >
  This skill analyses the competitive moat and defensibility of a proposed product or feature,
  identifying which moat types apply and where gaps exist. Use when evaluating a new product
  opportunity and leadership needs a defensibility assessment before committing resources. Also
  consider when a competitor has closed a differentiation gap and the team needs to understand
  remaining defensibility. Suggest when the roadmap prioritizes features without considering
  whether they strengthen or dilute the moat.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills: []
---

# moat-analyzer

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Analyses the competitive moat and defensibility of the proposed product or feature, mapping moat types to product decisions and surfacing vulnerabilities.

## When to Use
- When a new product or major feature is under consideration and leadership needs a defensibility assessment
- When a competitor has replicated a previously differentiating capability and the team needs to evaluate remaining moat strength
- When roadmap prioritization discussions lack a defensibility lens and features are being ranked on user value alone
- When preparing for a board meeting or investor update that requires articulation of competitive advantages

## Workflow
1. **Identify moat categories**: Evaluate the product against standard moat types -- network effects, switching costs, data advantages, economies of scale, brand, regulatory, and technology/IP. Deliverable: moat category checklist with applicability rating per type.
2. **Assess current moat strength**: For each applicable moat type, rate strength (nascent, developing, established, dominant) with supporting evidence. Deliverable: moat strength scorecard with evidence citations.
3. **Map moat to product decisions**: Identify which existing features or architectural choices contribute to each moat type. Trace the causal chain from product decision to defensibility. Deliverable: moat-to-feature mapping.
4. **Identify vulnerabilities**: Pinpoint where the moat is thin or where competitors could erode it. Consider open-source alternatives, API commoditization, data portability regulations, and multi-homing behavior. Deliverable: vulnerability register with severity and likelihood ratings.
5. **Recommend moat-strengthening actions**: Propose roadmap items, architectural decisions, or go-to-market strategies that would deepen the moat. Prioritize by effort-to-defensibility ratio. Deliverable: moat reinforcement roadmap with prioritized recommendations.
6. **Document and share**: Compile findings into a defensibility brief for leadership, product, and strategy teams. Deliverable: moat analysis brief.

## Anti-Patterns
- **Moat by assertion**: Claiming defensibility (e.g., "we have a data moat") without quantifying the data advantage or proving it compounds over time. *Why*: Unsubstantiated moat claims create false strategic confidence and leave the product exposed to commoditization.
- **Feature-as-moat fallacy**: Treating a single feature as a durable moat when it can be replicated in weeks. *Why*: Features are the weakest moat type; competitors with sufficient engineering resources can clone them quickly.
- **Ignoring multi-homing**: Assuming high switching costs when users routinely run competing products side by side. *Why*: Multi-homing eliminates lock-in and turns the competitive landscape into a feature-by-feature comparison.
- **Static moat analysis**: Performing the analysis once and never revisiting as the market evolves. *Why*: Moats erode -- network effects plateau, data advantages get regulated, and technology gets open-sourced.

## Output
**On success**: A moat analysis brief containing moat category ratings, feature-to-moat mapping, vulnerability register, and prioritized reinforcement recommendations ready for roadmap integration and leadership review.
**On failure**: Report which moat categories could not be assessed due to missing data (e.g., no churn cohort data to evaluate switching costs, no competitive usage data), and recommend specific research or instrumentation needed to complete the analysis.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
