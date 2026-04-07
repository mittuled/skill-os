---
name: prd-nfr-compliance
description: >
  This skill reviews product requirements documents to ensure non-functional
  compliance requirements are captured. Use when asked to review a PRD for legal
  requirements, embed compliance into product specs, or ensure regulatory NFRs
  are documented. Also consider when a PRD covers data handling without privacy
  requirements. Suggest when the user writes a PRD without compliance sections.
department: legal
agent: product-counsel
version: 1.0.0
complexity: simple
related-skills:
  - ../compliance-ga-reviewer-legal/SKILL.md
  - ../../../legal/corporate-counsel/compliance-scanner/SKILL.md
---

# prd-nfr-compliance

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews product requirements documents to ensure non-functional compliance requirements -- data privacy, accessibility, data retention, consent, and regulatory obligations -- are captured as explicit, testable requirements.

## When to Use

- When a new PRD is drafted and needs legal review to embed compliance requirements before engineering begins implementation.
- When a product feature handles personal data, processes payments, or targets a regulated user segment (minors, healthcare consumers, financial services users).
- When a compliance scan has identified regulatory obligations that must be translated into specific product requirements.

## Workflow

1. **PRD Review**: Read the PRD to understand feature scope, data flows, user interactions, and target audience. Identify compliance areas per the coverage criteria in `references/scoring-rubric.md`: privacy, accessibility, security, regulatory disclosures, audit logging, and sector-specific requirements. Deliverable: annotated PRD highlighting compliance-relevant sections.
2. **NFR Injection**: Draft testable NFRs for each area — data privacy (GDPR consent, CCPA opt-out, data minimization, retention, deletion endpoint with 30-day SLA), accessibility (WCAG 2.1 AA), security (AES-256 at rest, TLS 1.2+ in transit, MFA), regulatory disclosures (terms acceptance, cookie consent, age verification), and audit logging. Each NFR must have a concrete acceptance criterion. Deliverable: compliance NFR appendix.
3. **PRD Update and Handoff**: Integrate NFRs into the PRD with traceability to regulatory source. Confirm each requirement is assigned to engineering and acknowledged by PM. Apply scoring rubric at `references/scoring-rubric.md` to evaluate review completeness. Deliverable: updated PRD with embedded compliance requirements and PM acknowledgment.

## Anti-Patterns

- **Vague compliance requirements**: Writing NFRs like "must comply with GDPR" without specifying the concrete product behaviors required (e.g., "must provide a data export endpoint returning user data in machine-readable format within 30 days of request"). *Why*: untestable requirements are unimplementable; engineering needs specific acceptance criteria to build compliance into the product.
- **Reviewing PRDs after implementation starts**: Injecting compliance requirements after engineering has begun building, forcing rework. *Why*: late-stage compliance requirements are expensive to implement and create friction between legal and product teams; early embedding is a force multiplier.

## Output

**On success**: Produces the compliance NFR appendix and an updated PRD with embedded, testable compliance requirements. Delivered to the product manager and engineering lead with legal sign-off.

**On failure**: Report which compliance areas could not be specified (e.g., regulatory framework still under analysis, data flow undocumented), what partial requirements are available, and what must be resolved before the PRD is complete.

## Related Skills

- [`compliance-ga-reviewer-legal`](../compliance-ga-reviewer-legal/SKILL.md) -- The GA reviewer verifies at launch that the compliance NFRs injected by this skill were actually implemented.
- [`compliance-scanner`](../../../legal/corporate-counsel/compliance-scanner/SKILL.md) -- The compliance scanner identifies the regulatory frameworks that inform which NFRs must be injected.
