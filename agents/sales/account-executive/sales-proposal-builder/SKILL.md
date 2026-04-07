---
name: sales-proposal-builder
description: >
  This skill constructs data-driven sales proposals with 11 sections including
  ROI calculations, competitive differentiation, and implementation timeline.
  Use when asked to build a sales proposal, respond to a pricing request, or
  create a formal evaluation document. Also consider when prospect requests
  pricing or formal evaluation. Suggest when opportunity advances past discovery
  with confirmed budget and timeline.
department: sales
agent: account-executive
version: 1.0.0
complexity: complex
related-skills:
  - ../meeting-prep-builder/SKILL.md
  - ../../../sales/sales-manager/sales-competitive-intel/SKILL.md
  - ../../../sales/vp-sales/company-researcher/SKILL.md
  - ../../sdr/lead-qualifier/SKILL.md
triggers:
  - "build sales proposal"
  - "proposal needed"
  - "pricing request received"
  - "deal at proposal stage"
---

# sales-proposal-builder

## Agent: Account Executive

L3 account executive (Nx) responsible for sales signal synthesis, signal collection, and expansion sales motions.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Constructs data-driven sales proposals with 11 sections including ROI calculations, competitive differentiation, and implementation timeline tailored to the prospect's confirmed pain points, budget, and decision criteria.

## When to Use

- When a deal reaches proposal stage and the prospect has explicitly requested a formal proposal or pricing document.
- When a prospect requests pricing information or a formal evaluation document and there is enough discovery context to build a meaningful proposal.
- When an opportunity advances past discovery with confirmed budget, timeline, and decision criteria — indicating the deal is ready for a structured offer.

## Workflow

1. **Deal Context Gathering**: Gather all deal context from CRM, meeting notes, and discovery outputs: confirmed pain points, technical and business requirements, budget range, decision timeline, evaluation criteria, and competitive alternatives under consideration. Verify that discovery is complete enough to support a credible proposal — if gaps exist, flag them before proceeding. Deliverable: deal context summary with completeness assessment.
2. **Executive Summary Construction**: Build the executive summary tying the value proposition directly to the prospect's stated pain. Lead with the business outcome the prospect will achieve, not the product features. Reference the prospect's own words from discovery where possible to demonstrate listening. Deliverable: executive summary draft (250 words max).
3. **ROI Model Construction**: Construct the ROI model using four components: cost of status quo (what the problem costs today), implementation cost (total investment), projected savings or revenue impact (quantified value delivered), and payback period. Calculate time-to-value and 3-year TCO comparison against status quo and known alternatives. Use conservative assumptions and cite data sources. Deliverable: ROI model with assumptions table and sensitivity analysis. [GATE]
4. **Solution-Requirements Mapping**: Map solution capabilities to each stated requirement with feature-benefit alignment. For each requirement, show: the requirement as stated by the prospect, the specific capability that addresses it, and the business benefit of that capability. Flag any requirements that are partially met or require workarounds. Deliverable: requirements traceability matrix.
5. **Competitive Differentiation Section**: Build the competitive differentiation section addressing three questions: why us (unique advantages), why now (cost of delay), and why not alternatives (specific weaknesses of competitors in this context). Use proof points — customer stories, benchmarks, analyst recognition — not unsubstantiated claims. Deliverable: competitive positioning narrative with proof points.
6. **Implementation Plan Definition**: Define the implementation plan with phases, milestones, resource requirements, and timeline. Include customer-side responsibilities and dependencies. Show the path from signed contract to first value delivered. Deliverable: implementation plan with milestone timeline.
7. **Pricing Structure**: Structure pricing with three options following good/better/best psychology. Anchor high with the best option, make the better option the logical choice, and ensure the good option still solves the core problem. Include volume discounts, multi-year incentives, and payment terms. Clearly state what is included and excluded in each tier. Deliverable: pricing table with three options and terms summary.
8. **Proposal Assembly and Delivery**: Assemble the complete proposal using [sales-proposal-template.md](assets/sales-proposal-template.md). Review for internal consistency (ROI numbers match pricing, timeline matches implementation plan, requirements match solution mapping). Deliverable: final proposal document ready for prospect delivery.

## Anti-Patterns

- **Proposal before discovery**: Sending a proposal before confirming pain points, budget, and decision criteria through discovery. *Why*: a proposal built on assumptions rather than confirmed needs reads as generic and signals the AE prioritizes closing over understanding — prospects see through it immediately.
- **Feature-dump proposals**: Listing every product feature instead of mapping capabilities to the prospect's specific requirements. *Why*: feature lists invite commodity comparison and overwhelm the reader; requirement-mapped proposals demonstrate that you listened and built the solution around their needs.
- **Undefended ROI claims**: Presenting ROI projections without citing assumptions, data sources, or comparable customer results. *Why*: unsubstantiated ROI numbers destroy credibility — if the prospect's finance team cannot validate the assumptions, the entire proposal loses trust.
- **Single-option pricing**: Presenting only one pricing option with no alternatives. *Why*: a single option creates a binary yes/no decision; three options shift the prospect's mental frame from "should I buy" to "which option should I choose" and increase close rates.
- **Ignoring known competitors**: Omitting competitive differentiation when the prospect is evaluating alternatives. *Why*: if you do not address the comparison, the prospect will make the comparison themselves without your input — and competitors will fill the narrative gap.
- **Implementation hand-waving**: Providing a vague "we will work with your team" implementation section instead of a concrete plan. *Why*: enterprise buyers need to staff and budget for implementation internally; vague plans signal risk and invite "we will circle back after we figure out resourcing."

## Output

**On success**: Produces a complete 11-section sales proposal containing cover page, executive summary, current situation analysis, proposed solution with requirements mapping, ROI analysis with assumptions, competitive comparison, implementation plan with timeline, team and support structure, three-tier pricing options, terms, and next steps. Delivered as a structured document for AE review and prospect delivery.

**On failure**: Report what blocked proposal construction (e.g., insufficient discovery data, missing budget confirmation, unknown decision criteria), which sections could not be completed with confidence, and what additional discovery is needed before a credible proposal can be built.

## Related Skills

- [`meeting-prep-builder`](../meeting-prep-builder/SKILL.md) — Provides pre-meeting intelligence that feeds discovery context into the proposal.
- [`sales-competitive-intel`](../../../sales/sales-manager/sales-competitive-intel/SKILL.md) — Provides battle cards and competitive positioning for the differentiation section.
- [`company-researcher`](../../../sales/vp-sales/company-researcher/SKILL.md) — Provides firmographic and company intelligence for the current situation section.
- [`lead-qualifier`](../../sdr/lead-qualifier/SKILL.md) — Provides qualification data (budget, authority, need, timeline) that validates proposal readiness.
