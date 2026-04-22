---
name: third-party-integrator-review
description: >
  This skill reviews third-party integration plans for risk, compliance, and product fit.
  Use when engineering proposes adding an external service, SDK, or API dependency.
  Also consider when an existing integration is up for renewal and needs a product-fit reassessment.
  Suggest when a vendor dependency is being adopted without documented evaluation criteria.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - market-sizer
  - backlog-populator
  - risk-register-builder
triggers:
  - "review third-party integration"
  - "integration review"
  - "third-party review"
  - "vendor integration review"
  - "integration check"
---

# third-party-integrator-review

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Reviews third-party integration plans for risk, compliance, and product fit.

## When to Use
- When engineering proposes adding a new external service, SDK, or API as a product dependency
- When a third-party vendor contract is up for renewal and the integration needs reassessment against current product needs
- When a compliance or security audit flags an existing integration for review
- When a customer requests an integration and the PM must evaluate whether it aligns with the product roadmap

## Workflow
1. **Assess product fit**: Review the proposed integration against current product goals and roadmap priorities. Determine whether the integration solves a validated user need or is speculative. Deliverable: product-fit assessment with alignment score (strong / moderate / weak) and rationale.
2. **Evaluate technical risk**: Consult engineering on API reliability, data-flow implications, latency impact, and fallback behaviour if the service goes down. Review the vendor's SLA and uptime history. Deliverable: technical risk summary covering availability, performance, and failure-mode analysis.
3. **Review compliance and data handling**: Confirm the vendor's data processing practices meet regulatory requirements (GDPR, SOC 2, HIPAA as applicable). Verify data residency, encryption, and deletion policies. Deliverable: compliance checklist with pass/fail per requirement.
4. **Analyse cost and lock-in**: Review pricing terms, usage-based cost projections, and contractual lock-in clauses. Identify switching costs if the vendor is replaced later. Deliverable: cost analysis with projected spend at current and 3x scale, plus exit-cost estimate.
5. **Render decision**: Synthesise findings into an approve, approve-with-conditions, or reject recommendation. For conditional approvals, specify the mitigations required before proceeding. Deliverable: integration review decision document shared with engineering and stakeholders.

## Anti-Patterns
- **Defaulting to engineering preference**: Approving an integration because the engineering team likes the technology without validating product fit or user need. *Why*: This accumulates vendor dependencies that serve developer convenience rather than customer value.
- **Skipping compliance review**: Assuming the vendor handles data correctly because they are well-known. *Why*: Brand recognition does not guarantee regulatory compliance, and the product team bears liability for data-handling violations.
- **Ignoring switching costs**: Approving a deeply-coupled integration without evaluating what it takes to replace the vendor. *Why*: High switching costs create leverage for the vendor at renewal and limit future product flexibility.

## Output
**On success**: An integration review document containing the product-fit assessment, technical risk summary, compliance checklist, cost analysis, and a clear approve / approve-with-conditions / reject decision — distributed to engineering, legal, and stakeholders.
**On failure**: Report which evaluation areas are incomplete (missing SLA data, pending compliance review, unclear cost projections), what was attempted, and recommend specific follow-ups — such as requesting vendor documentation, scheduling a security review, or running a proof-of-concept.

## Related Skills
- [`market-sizer`](../market-sizer/SKILL.md) — sibling skill under the same agent — combine with market-sizer for end-to-end coverage
- [`backlog-populator`](../backlog-populator/SKILL.md) — sibling skill under the same agent — combine with backlog-populator for end-to-end coverage
- [`risk-register-builder`](../risk-register-builder/SKILL.md) — sibling skill under the same agent — combine with risk-register-builder for end-to-end coverage
