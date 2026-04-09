---
name: product-legal-reviewer
description: >
  This skill reviews product features and changes for legal and regulatory compliance.
  Use when asked to conduct a legal review of a product feature, assess regulatory
  risk of a product change, or clear a feature for launch. Also consider when the
  product enters a regulated domain. Suggest when the user is launching product
  changes without legal review.
department: legal
agent: product-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../ai-risk-assessor/SKILL.md
  - ../privacy-impact-assessor/SKILL.md
  - ../content-moderation-advisor/SKILL.md
  - ../open-source-auditor/SKILL.md
---

# product-legal-reviewer

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews product features and changes for legal and regulatory compliance by evaluating consumer protection, privacy, intellectual property, and sector-specific regulatory requirements before launch.

## When to Use

- When a new product feature is approaching launch and needs legal clearance.
- When an existing feature is being modified in ways that change its legal risk profile (new data collection, new monetization, new user interactions).
- When the product expands into a new market or vertical with different regulatory requirements.

## Workflow

1. **Feature Intake**: Receive the feature specification, user flows, and data practices documentation. Clarify purpose, target users, data handling, monetization, and geographic reach. Deliverable: legal review intake summary.
2. **Regulatory Mapping**: Identify all applicable regulations by jurisdiction — consumer protection, privacy (GDPR, CCPA), accessibility (ADA, WCAG), advertising (FTC), financial services, health (HIPAA), employment (EEOC AI guidance, NYC LL 144), and sector-specific rules. Deliverable: regulatory applicability matrix.
3. **Risk Assessment**: Evaluate each requirement against feature design. Identify compliance gaps with severity classification (blocking/recommended/advisory) and likelihood/severity evaluation. Apply scoring rubric at `references/scoring-rubric.md`. Deliverable: legal risk assessment.
4. **Recommendation and Clearance**: Provide actionable recommendations with compliant alternatives that achieve the product goal. Produce memo using template at `assets/product-legal-review-memo-template.md`. Issue legal clearance when blocking items resolved. Deliverable: legal review memo with clearance status.

## Anti-Patterns

- **Blocking without alternatives**: Flagging legal issues without suggesting compliant alternatives that achieve the product goal. *Why*: product counsel exists to enable the business within legal constraints, not to stop features; alternatives maintain velocity.
- **Review at the end**: Conducting legal review only when the feature is complete and ready to ship. *Why*: late review creates launch delays; early involvement during design prevents expensive rework.
- **Over-indexing on worst case**: Treating every theoretical legal risk as a launch blocker regardless of likelihood or severity. *Why*: risk assessment requires calibration; blocking launches on low-probability risks erodes product trust in legal review.

## Output

**On success**: Produces a legal review memo with regulatory mapping, risk assessment, recommendations, and clearance status. Delivered before feature launch.

**On failure**: Report which aspects of the feature could not be reviewed (insufficient documentation, unclear jurisdictional scope), what risks are identified but unresolved, and what additional information is needed. Escalate to General Counsel for ambiguous high-risk items.

## Related Skills

- [`ai-risk-assessor`](../ai-risk-assessor/SKILL.md) -- AI features require specialized risk assessment as part of product legal review.
- [`privacy-impact-assessor`](../privacy-impact-assessor/SKILL.md) -- Privacy assessments are a key input to the product legal review for data-collecting features.
