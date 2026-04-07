---
name: business-agreement-generator
description: >
  This skill generates business agreements across 10 common types with a
  standardized 15-section structure adaptable to each agreement's specific
  requirements. Use when business needs a new agreement drafted (partnership,
  licensing, services, reseller, JV, etc.). Also consider when adapting a
  standard agreement for a non-standard arrangement. Suggest when deal team
  needs draft agreement language before legal review.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../contract-review-orchestrator/SKILL.md
  - ../negotiation-strategist/SKILL.md
triggers:
  - "draft business agreement"
  - "partnership agreement needed"
  - "services agreement template"
  - "licensing agreement"
---

# business-agreement-generator

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Generates business agreements across 10 common types with a standardized 15-section structure adaptable to each agreement's specific requirements, producing review-ready drafts with plain-English annotations.

## When to Use

- When the business needs a new agreement drafted for a partnership, licensing deal, services engagement, reseller arrangement, joint venture, or other commercial relationship.
- When adapting a standard agreement template for a non-standard arrangement that requires type-specific clause modifications.
- When a deal team needs draft agreement language before formal legal review to accelerate negotiation timelines.

## Workflow

1. **Determine Agreement Type**: Identify the agreement type from the 10 supported types in the framework (see [framework.md](references/framework.md)): Services, SaaS License, Reseller/Channel, Strategic Partnership, Joint Venture, Distribution, Consulting, Referral, OEM/White-Label, or Franchise. If the arrangement does not fit a supported type, identify the closest match and document deviations. Deliverable: agreement type classification with rationale.

2. **Gather Key Terms**: Collect all key commercial terms from the deal team: parties and their legal entities, scope of services or rights, term and renewal provisions, compensation structure, territory and exclusivity, performance obligations, and any non-standard requirements. Deliverable: term sheet summarizing all key commercial inputs.

3. **Select Applicable Clause Set**: Using the agreement type and key terms, select the applicable clause set from the 15-section standard structure. Activate type-specific conditional sections and suppress sections that do not apply to the agreement type. Deliverable: clause selection matrix showing which of the 15 sections are active and which type-specific blocks apply.

4. **[GATE] Generate 15-Section Agreement**: Generate the full agreement using the template (see [business-agreement-template.md](assets/business-agreement-template.md)) with all standard and type-specific clauses populated from the key terms. Insert [CUSTOMIZE] markers at every point requiring deal-specific input and [REVIEW] markers at provisions requiring legal judgment. Deliverable: draft agreement with all 15 sections populated.

5. **Flag Customization Points**: Review the draft for completeness. Ensure every [CUSTOMIZE] marker has guidance on what information is needed. Ensure every [REVIEW] marker explains the legal consideration requiring judgment. Count and categorize all markers by urgency. Deliverable: customization summary listing all markers with category and guidance.

6. **Add Plain-English Annotations**: For each complex clause (indemnification, limitation of liability, IP assignment, termination), add a plain-English annotation explaining what the clause means in business terms. Annotations appear as inline comments, not as part of the agreement text. Deliverable: annotated agreement draft.

7. **Produce Agreement Document**: Assemble the final output containing the annotated agreement draft, customization summary, and type-specific negotiation notes from the framework. Deliver to the requesting attorney or deal team lead for review and customization. Deliverable: complete agreement package ready for legal review.

## Anti-Patterns

- **One-size-fits-all drafting**: Using the same clause language for all agreement types without activating type-specific provisions. *Why*: a SaaS license requires different IP, SLA, and data provisions than a consulting agreement; generic clauses create gaps in protection and confuse counterparties.

- **Skipping the term sheet**: Generating the agreement before collecting key commercial terms from the deal team. *Why*: agreements drafted without confirmed terms require multiple revision cycles and may embed assumptions that conflict with the actual deal structure.

- **Over-lawyering standard deals**: Inserting aggressive protective clauses (unlimited indemnity, broad non-compete, one-sided termination) into routine low-value agreements. *Why*: disproportionate terms slow negotiation, damage business relationships, and signal legal inexperience to sophisticated counterparties.

- **Unmarked assumptions**: Filling in assumed values (e.g., default territory, standard payment terms) without marking them for review. *Why*: deal teams may not notice unmarked assumptions, leading to signed agreements with unintended terms that do not reflect the actual commercial arrangement.

## Output

**On success**: Produces a complete agreement package containing the 15-section agreement draft with type-specific clauses, [CUSTOMIZE] and [REVIEW] markers with guidance, plain-English annotations for complex clauses, customization summary, and negotiation notes. Delivered to the requesting attorney or deal team lead.

**On failure**: Report which agreement sections could not be completed (e.g., missing key terms, unsupported agreement type), what assumptions were made, and what information the deal team must provide to complete the draft. Include the partial draft with all gaps explicitly marked.

## Related Skills

- [`contract-review-orchestrator`](../contract-review-orchestrator/SKILL.md) -- Generated agreements should be reviewed through the contract review process before sending to counterparties.
- [`negotiation-strategist`](../negotiation-strategist/SKILL.md) -- Negotiation strategy informs which clauses to draft aggressively vs. which to leave at market standard as negotiation leverage.
