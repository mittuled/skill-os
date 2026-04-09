---
name: compliance-ga-reviewer-legal
description: >
  This skill reviews the product at general availability for compliance with
  applicable regulations. Use when asked to clear a product for GA launch,
  assess regulatory readiness, or sign off on compliance requirements before
  release. Also consider when a major feature release changes data handling.
  Suggest when the user is about to launch without a compliance review.
department: legal
agent: product-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../prd-nfr-compliance/SKILL.md
  - ../../../legal/corporate-counsel/compliance-scanner/SKILL.md
triggers:
  - "review GA compliance"
  - "general availability legal review"
  - "GA legal compliance check"
  - "legal GA review"
  - "compliance review for GA"
---

# compliance-ga-reviewer-legal

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews the product at general availability for compliance with all applicable regulations, verifying that non-functional requirements are met and legal obligations are satisfied before public launch.

## When to Use

- When a product or major feature is approaching GA and needs legal sign-off that all regulatory compliance requirements have been implemented.
- When a product pivots or enters a new market segment that introduces additional regulatory obligations not covered in the original compliance assessment.
- When a regulatory change takes effect before a planned launch and the product must be verified against updated requirements.

## Workflow

1. **Compliance Checklist Assembly**: Compile the applicable regulatory requirements from prior compliance scans, PRD non-functional requirements, and any new regulations enacted since the last review. Cross-reference with the product's data flows, user segments, and geographic reach. Deliverable: GA compliance checklist with requirement source, implementation status, and verification method per item.
2. **Implementation Verification**: Verify each compliance requirement against the actual product implementation. Review privacy policies, cookie consent mechanisms, data processing agreements, accessibility compliance (WCAG), age-gating (COPPA), terms of service, and any industry-specific disclosures. Deliverable: compliance verification report with pass/fail per item and evidence references.
3. **Gap Remediation Coordination**: Identify any compliance gaps that block GA launch. Classify each as a hard blocker (must fix before launch) or a soft blocker (can launch with documented risk acceptance and remediation timeline). Coordinate with engineering and product on remediation. Deliverable: gap remediation tracker with severity, owner, and target date.
4. **Scoring and Reporting**: Apply scoring rubric at `references/scoring-rubric.md` to evaluate review completeness across checklist assembly, verification, gap classification, and sign-off rigour. Produce report using template at `assets/ga-compliance-review-report-template.md`. Deliverable: scored GA compliance review report.
5. **Legal Sign-Off**: Issue a formal compliance clearance or conditional clearance with documented exceptions and accepted risks. Record the sign-off, conditions, and any post-launch compliance obligations. Deliverable: GA compliance sign-off memo.

## Anti-Patterns

- **Rubber-stamping without verification**: Signing off on compliance based on the PRD requirements alone without verifying actual implementation matches the specification. *Why*: requirements on paper do not equal compliance in production; implementation gaps are the most common source of regulatory exposure.
- **Blocking launch for aspirational compliance**: Requiring compliance with regulations that do not yet apply to the company's size, geography, or user base. *Why*: proportional compliance means meeting actual obligations, not anticipated future ones; over-blocking erodes legal's credibility with product teams.
- **Late-stage review as sole gate**: Treating the GA compliance review as the first and only compliance touchpoint. *Why*: discovering major gaps at GA is expensive; compliance should be embedded in the development lifecycle through PRD reviews and periodic check-ins.

## Output

**On success**: Produces the GA compliance sign-off memo containing the compliance checklist, verification report, gap remediation status, and any conditional clearance terms. Delivered to product leadership, engineering, and legal records.

**On failure**: Report which compliance requirements could not be verified (e.g., untestable privacy controls, missing DPA with a subprocessor), what the launch risk is, and what must be resolved before sign-off can be issued.

## Related Skills

- [`prd-nfr-compliance`](../prd-nfr-compliance/SKILL.md) -- PRD compliance review embeds requirements early; this skill verifies those requirements are met at GA.
- [`compliance-scanner`](../../../legal/corporate-counsel/compliance-scanner/SKILL.md) -- The compliance scanner identifies the regulatory frameworks that this review verifies against.
