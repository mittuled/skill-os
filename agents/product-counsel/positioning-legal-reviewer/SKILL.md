---
name: positioning-legal-reviewer
description: >
  This skill reviews marketing positioning and claims for legal compliance
  including FTC guidelines and comparative advertising rules. Use when asked to
  vet marketing claims, review competitive positioning language, or assess
  testimonial and endorsement compliance. Also consider when launching a campaign
  with performance claims. Suggest when the user publishes claims without legal review.
department: legal
agent: product-counsel
version: 1.0.0
complexity: simple
related-skills:
  - ../pricing-legal-reviewer/SKILL.md
  - ../business-model-legal-reviewer/SKILL.md
---

# positioning-legal-reviewer

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews marketing positioning statements, product claims, and competitive comparisons for compliance with FTC guidelines, Lanham Act requirements, and applicable advertising regulations.

## When to Use

- When the marketing team creates positioning language that includes performance claims, superlatives ("fastest," "most secure"), or competitive comparisons.
- When customer testimonials, case studies, or endorsements will be used in marketing materials and need FTC endorsement guideline compliance.
- When the company enters a regulated industry (healthcare, finance, education) where advertising claims face heightened scrutiny and sector-specific rules.

## Workflow

1. **Claims Inventory**: Catalog all factual claims, performance assertions, comparative statements, and implied representations in the positioning materials. Deliverable: annotated claims inventory categorizing each as factual, opinion, puffery, or comparative.
2. **Substantiation Review**: Verify that each factual claim is supported by competent and reliable evidence. For performance claims, confirm testing methodology and sample sizes. For comparative claims, verify the comparison is accurate, current, and not misleading. Deliverable: substantiation assessment with evidence status per claim.
3. **Compliance Recommendation**: Flag non-substantiated claims, misleading comparisons, missing disclosures (material connections, typical results disclaimers), and FTC/Lanham Act violations. Propose compliant alternative language for each flagged item. Deliverable: positioning review memo with flagged items and approved alternative language.

## Anti-Patterns

- **Approving puffery without analysis**: Waving through subjective claims as "mere puffery" without assessing whether a reasonable consumer would interpret them as factual assertions. *Why*: the line between puffery and an actionable claim is context-dependent; "industry-leading" may be puffery for a consumer product but a substantive claim in a regulated B2B context.
- **Reviewing copy in isolation**: Reviewing positioning language without considering the full context (landing page, adjacent visuals, footnotes, terms) where implied claims arise. *Why*: the FTC evaluates the "net impression" of an advertisement, not individual sentences; a technically accurate claim can be misleading in context.

## Output

**On success**: Produces a positioning review memo containing the claims inventory, substantiation assessment, flagged items, and approved alternative language. Delivered to the marketing team and legal records.

**On failure**: Report which claims could not be substantiated (e.g., missing test data, unavailable competitor information), what alternative language was proposed, and what evidence must be obtained before the claims can be approved.

## Related Skills

- [`pricing-legal-reviewer`](../pricing-legal-reviewer/SKILL.md) -- Pricing claims in positioning materials (e.g., "save 50%") require coordinated review of both positioning and pricing compliance.
- [`business-model-legal-reviewer`](../business-model-legal-reviewer/SKILL.md) -- Business model constraints may affect what positioning claims are legally supportable.
