---
name: data-processing-agreement-negotiator
description: >
  This skill negotiates data processing agreements with vendors and customers. Use
  when asked to draft or review a DPA, negotiate data processing terms, or ensure
  vendor data handling meets regulatory requirements. Also consider when onboarding
  a new sub-processor. Suggest when the user is sharing personal data with a vendor
  without a DPA in place.
department: legal
agent: product-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../privacy-impact-assessor/SKILL.md
  - ../../security-compliance-programme-manager/vendor-security-assessor/SKILL.md
---

# data-processing-agreement-negotiator

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Negotiates data processing agreements with vendors and customers by defining processing purposes, security requirements, sub-processor terms, breach notification obligations, and cross-border transfer mechanisms to ensure regulatory compliance.

## When to Use

- When onboarding a new vendor or sub-processor that will process personal data on behalf of the company or its customers.
- When a customer requires a DPA as part of their procurement process and the company's standard DPA needs to be negotiated.
- When regulatory changes (new SCCs, adequacy decisions, sector-specific requirements) require existing DPAs to be updated.

## Workflow

1. **Processing Scope Definition**: Document the personal data categories, data subjects, processing purposes, and retention periods for the relationship. Determine whether the company is controller or processor in the arrangement. Deliverable: processing scope document.
2. **Template Selection and Customization**: Select the appropriate DPA template (company standard, customer-provided, or regulatory model clauses). Customize for the specific processing activities and relationship structure. Deliverable: customized DPA draft.
3. **Security Requirements Alignment**: Define the technical and organizational security measures required. Align with the company's security standards and any regulatory minimums. Review the counterparty's security certifications and audit reports. Deliverable: security schedule with required measures.
4. **Sub-Processor Terms**: Define sub-processor notification and approval rights. Review the counterparty's current sub-processor list. Establish the flow-down obligations from the primary DPA to sub-processors. Deliverable: sub-processor schedule and approval workflow.
5. **Cross-Border Transfer Mechanisms**: Identify cross-border data transfers and implement appropriate transfer mechanisms (SCCs, adequacy decisions, binding corporate rules, or derogations). Conduct transfer impact assessments where required. Deliverable: transfer mechanism documentation.
6. **Negotiation and Execution**: Negotiate contentious terms (liability caps, indemnification, audit rights, breach notification timelines). Document deviations from standard terms with risk acceptance rationale. Execute the final agreement. Deliverable: executed DPA with deviation log.

## Anti-Patterns

- **Template-only approach**: Sending the standard DPA template without customization and refusing to negotiate. *Why*: rigid templates block deals; negotiation flexibility on non-critical terms while holding firm on regulatory requirements closes agreements faster.
- **Ignoring the sub-processor chain**: Executing a DPA without reviewing the counterparty's sub-processors. *Why*: the company's data may flow to sub-processors with inadequate security; the primary DPA is only as strong as its weakest sub-processor link.
- **DPA without enforcement**: Executing DPAs without tracking compliance, exercising audit rights, or monitoring sub-processor changes. *Why*: an unenforced DPA provides paper compliance but no actual data protection; regulators evaluate practice, not paperwork.
- **Treating all data equally**: Applying the same DPA terms to non-sensitive business data and sensitive personal data. *Why*: over-engineering DPAs for low-risk data wastes negotiation cycles; under-engineering for high-risk data creates regulatory exposure.

## Output

**On success**: Produces an executed DPA with processing scope document, security schedule, sub-processor terms, transfer mechanism documentation, and deviation log. Delivered per the vendor onboarding or customer deal timeline.

**On failure**: Report which terms could not be agreed, what the regulatory risk of proceeding without a DPA is, and recommended alternatives (different vendor, data minimization, or escalation to General Counsel for risk acceptance).

## Related Skills

- [`privacy-impact-assessor`](../privacy-impact-assessor/SKILL.md) -- Privacy impact assessments identify processing activities that require DPAs.
- [`vendor-security-assessor`](../../security-compliance-programme-manager/vendor-security-assessor/SKILL.md) -- Vendor security assessments validate the security measures referenced in DPAs.
