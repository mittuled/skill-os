---
name: content-moderation-advisor
description: >
  This skill advises on content moderation policies and their legal implications.
  Use when asked to draft moderation policies, evaluate moderation decisions for
  legal risk, or assess Section 230 exposure. Also consider when user-generated
  content features are being built. Suggest when the user is launching UGC features
  without a moderation framework.
department: legal
agent: product-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../terms-of-service-drafter/SKILL.md
  - ../product-legal-reviewer/SKILL.md
---

# content-moderation-advisor

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Advises on content moderation policies, enforcement procedures, and appeal mechanisms to ensure the company manages user-generated content within legal requirements while preserving platform integrity.

## When to Use

- When the product introduces or modifies features that allow user-generated content (posts, reviews, uploads, comments).
- When a content moderation decision is challenged or escalated and needs legal review.
- When new regulations (DSA, state social media laws, CSAM requirements) change content moderation obligations.

## Workflow

1. **Policy Framework Review**: Review existing content moderation policies against applicable laws using the legal framework at `references/content-moderation-framework.md` — Section 230, EU Digital Services Act, NetzDG, Online Safety Act, CSAM reporting obligations, and state social media laws. Identify gaps between legal requirements and current policy coverage. Deliverable: policy gap analysis.
2. **Enforcement Procedure Design**: Design or review the moderation enforcement workflow: detection methods (automated hash-matching, ML classifiers, human review), escalation criteria, response timeframes per DSA requirements, and appeal mechanisms per DSA Article 20. Produce policy using template at `assets/content-moderation-policy-template.md`. Deliverable: moderation procedure specification.
3. **Decision Review**: When high-risk moderation decisions arise (government requests, public figure content, legally ambiguous speech), provide legal analysis applying the Section 230 analysis framework from `references/content-moderation-framework.md`. Deliverable: legal analysis memo.
4. **Compliance Monitoring**: Track regulatory developments affecting content moderation. Advise on DSA transparency reports (Article 15/24/42), government disclosure requirements, and cross-border content obligations. Deliverable: compliance update with required actions.

## Anti-Patterns

- **Over-moderation as safety**: Removing all borderline content to avoid legal risk. *Why*: excessive moderation suppresses legitimate expression, drives user attrition, and in some jurisdictions triggers editorial liability by demonstrating content control.
- **No appeal process**: Enforcing moderation decisions without providing users a mechanism to contest. *Why*: many regulations require appeal processes; even where not legally required, appeals catch false positives and build user trust.
- **Ignoring jurisdiction**: Applying a single moderation policy globally without accounting for jurisdictional differences. *Why*: content that is legal in one jurisdiction may be illegal in another; a one-size-fits-all approach creates either over-moderation or legal exposure.

## Output

**On success**: Produces content moderation policy framework, enforcement procedures, legal analysis memos, and compliance monitoring reports. Delivered as policies are drafted and updated per regulatory changes.

**On failure**: Report which policy areas lack legal coverage, what regulatory requirements are unmet, and recommended remediation timeline. Escalate to General Counsel if the company faces active enforcement risk.

## Related Skills

- [`terms-of-service-drafter`](../terms-of-service-drafter/SKILL.md) -- Terms of service establish the legal foundation for content moderation policies.
- [`product-legal-reviewer`](../product-legal-reviewer/SKILL.md) -- Content moderation is a key dimension of legal review for UGC features.
