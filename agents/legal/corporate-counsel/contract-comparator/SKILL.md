---
name: contract-comparator
description: >
  This skill performs side-by-side comparison of two contract versions or a
  contract against standard terms, with favorability analysis per clause. Use
  when comparing a counterparty's contract against company standard terms, when
  reviewing redlined contracts, or when comparing competing vendor agreements.
  Suggest when legal receives a counterparty's version alongside an internal
  standard.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../contract-review-orchestrator/SKILL.md
  - ../contract-risk-analyst/SKILL.md
  - ../../../legal/general-counsel/negotiation-strategist/SKILL.md
  - ../../../legal/general-counsel/missing-protections-finder/SKILL.md
triggers:
  - "compare these contracts"
  - "redline analysis"
  - "compare against standard terms"
  - "contract deviation analysis"
---

# contract-comparator

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Performs side-by-side comparison of two contract versions or a contract against standard terms, scoring favorability per clause and calculating the overall favorability shift.

## When to Use

- When a counterparty returns a contract with their proposed changes and the legal team needs to understand every deviation from the company's standard terms.
- When comparing two competing vendor agreements to determine which offers more favorable terms.
- When reviewing a redlined contract to verify that agreed changes were implemented correctly and no unauthorized modifications were introduced.

## Workflow

1. **Parse and Align Clauses**: Parse both documents into discrete clauses. Align clauses by type using the comparison methodology (see [framework.md](references/framework.md)): first by heading match, then by content similarity, then by standard taxonomy position. Flag unmatched clauses as additions or deletions. Deliverable: aligned clause map with match confidence scores.

2. **Identify Differences**: For each aligned clause pair, identify additions (language present only in Version B), deletions (language present only in Version A), and modifications (language changed between versions). Preserve exact wording for both versions. Deliverable: difference inventory with change type tags.

3. **Score Favorability**: Evaluate each difference for favorability to the company's position: Favorable (shifts risk or obligation to counterparty), Neutral (no material change in position), or Unfavorable (shifts risk or obligation to the company). Apply deviation severity classification (Critical, Material, Minor) based on financial and legal impact. Deliverable: favorability-scored difference list.

4. **Calculate Overall Favorability Shift**: Aggregate clause-level favorability into an overall assessment. Count and weight differences by severity: Critical differences weighted 3x, Material weighted 2x, Minor weighted 1x. Calculate net favorability score. Deliverable: overall favorability summary with net score and direction.

5. **Produce Comparison Report**: Assemble the final report using the output template (see [comparison-report-template.md](assets/comparison-report-template.md)). Include executive summary with overall favorability, side-by-side clause table, key deviations, and negotiation priorities. Deliverable: comparison report.

## Anti-Patterns

- **Heading-only alignment**: Matching clauses solely by section headings without verifying content alignment. *Why*: counterparties frequently reorganize clauses under different headings — a clause titled "Limitation of Liability" in Version A may be split across "Remedies" and "Indemnification" in Version B, and heading-only matching misses these structural changes.

- **Treating all differences equally**: Flagging every word change without severity classification. *Why*: a change from "thirty (30) days" to "30 days" is cosmetic, while a change from "not to exceed 12 months of fees" to "not to exceed fees paid in the prior month" is material — weighting all differences equally buries critical changes in noise.

- **Ignoring additions**: Focusing only on modifications to existing clauses while overlooking entirely new clauses added by the counterparty. *Why*: new clauses (e.g., a new audit rights section or a non-compete) can introduce obligations that did not exist in the original terms and often carry the highest risk.

## Output

**On success**: Produces a comparison report containing side-by-side clause analysis, favorability scores per difference, overall favorability shift with net score, key deviations summary, and prioritized negotiation recommendations. Delivered to contract-review-orchestrator or directly to the requesting attorney.

**On failure**: Report which clauses could not be aligned (e.g., entirely restructured sections, clauses referencing external documents not provided), what partial comparison was completed, and recommend manual review for unmatched sections. Include confidence score for the overall alignment.

## Related Skills

- [`contract-review-orchestrator`](../contract-review-orchestrator/SKILL.md) — Dispatches this skill when standard terms are available for comparison; consumes the favorability analysis in the overall contract review.
- [`contract-risk-analyst`](../contract-risk-analyst/SKILL.md) — Provides risk dimension scores that inform whether deviations from standard terms increase risk exposure.
- [`negotiation-strategist`](../../../legal/general-counsel/negotiation-strategist/SKILL.md) — Consumes the key deviations and negotiation priorities to develop counterproposals.
- [`missing-protections-finder`](../../../legal/general-counsel/missing-protections-finder/SKILL.md) — Identifies protections present in standard terms but absent from the counterparty version.
