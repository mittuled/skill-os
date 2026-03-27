---
name: case-study-extractor-cs
description: >
  This skill identifies and extracts customer case studies from successful CS
  engagements. Use when asked to find case study candidates, draft customer
  stories, or build the reference library. Also consider when marketing or
  sales requests customer proof points. Suggest when successful engagements
  are completing without capturing their stories.
department: customer-success
agent: cs-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# case-study-extractor-cs

## Agent: CS Manager

L2 customer success manager (1x) responsible for CS cohort selection, release readiness, health monitoring, and case study extraction.

Department ethos: [ideal-customer-success.md](../../../departments/customer-success/ideal-customer-success.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Identifies and extracts customer case studies from successful CS engagements for use by marketing, sales, and the customer reference programme.

## When to Use

- When marketing or sales needs customer proof points for campaigns, proposals, or collateral.
- When a customer engagement has achieved notable outcomes that should be captured as a reference.
- When the case study pipeline is empty and successful engagements need to be systematically identified.

## Workflow

1. **Identify Candidates**: Review the customer portfolio for engagements with strong outcomes -- measurable ROI, fast time-to-value, or innovative use cases. Cross-reference with health scores and NPS. Deliverable: case study candidate list with rationale.
2. **Qualify and Secure Permission**: Confirm the customer is willing to participate. Verify no contractual or legal restrictions on public reference. Deliverable: approved candidate list with customer consent.
3. **Extract Story Elements**: Gather the case study components: customer context, challenge, solution approach, implementation details, and quantified outcomes. Source from CS notes, customer interviews, and usage data. Deliverable: raw case study content.
4. **Draft and Review**: Assemble content into a structured case study draft. Review with the customer for accuracy and approval. Deliverable: customer-approved case study.

## Anti-Patterns

- **Extracting without permission**: Drafting case studies using customer data without explicit customer consent. *Why*: publishing unauthorized customer stories violates trust and may breach contractual obligations.
- **Vanity case studies**: Focusing on brand-name logos rather than stories with compelling, quantified outcomes. *Why*: prospects are persuaded by measurable results, not logo walls.
- **One-time extraction**: Capturing case studies only when asked rather than maintaining a continuous pipeline. *Why*: reactive extraction misses time-sensitive stories and creates bottlenecks when marketing needs references urgently.

## Output

**On success**: Produces approved case study documents with customer context, challenge, solution, and quantified outcomes. Delivered to marketing and the customer reference programme.

**On failure**: Report which candidates declined or could not be contacted, what partial content was gathered, and alternative candidates to pursue.

## Related Skills

- [`customer-reference-programme-manager`](../../customer-programs-manager/customer-reference-programme-manager/SKILL.md) -- Case studies feed into the reference programme.
- [`cs-health-monitor`](../cs-health-monitor/SKILL.md) -- Health data helps identify case study candidates.
- [`cs-signal-extractor`](../../customer-success-manager/cs-signal-extractor/SKILL.md) -- Customer signals may surface case study-worthy outcomes.
