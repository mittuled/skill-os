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

1. **Processing Scope Definition**: Document the personal data categories, data subjects, processing purposes, and retention periods. Determine controller/processor designation per GDPR Article 28. Apply risk tiering from `references/dpa-negotiation-framework.md` to set assessment depth. Deliverable: processing scope document.
2. **Template Selection and Customization**: Select the appropriate DPA template and customize per the GDPR Article 28 mandatory clauses checklist in `references/dpa-negotiation-framework.md`. Deliverable: customized DPA draft.
3. **Security Requirements Alignment**: Define technical and organizational security measures required per GDPR Article 32. Align with the company's security standards. Review counterparty SOC 2/ISO 27001 certifications. Deliverable: security schedule.
4. **Sub-Processor Terms**: Define sub-processor notification and approval rights per the negotiation positions in `references/dpa-negotiation-framework.md`. Review the counterparty's sub-processor list. Establish flow-down obligations. Deliverable: sub-processor schedule.
5. **Cross-Border Transfer Mechanisms**: Identify cross-border transfers and implement mechanisms per the transfer decision tree in `references/dpa-negotiation-framework.md` — SCCs, adequacy decisions, BCRs, or derogations. Conduct Transfer Impact Assessments. Deliverable: transfer mechanism documentation.
6. **Negotiation and Execution**: Negotiate per the key positions in `references/dpa-negotiation-framework.md`. Document deviations with risk acceptance rationale. Produce DPA using template at `assets/dpa-template.md`. Execute the final agreement. Deliverable: executed DPA with deviation log.

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
