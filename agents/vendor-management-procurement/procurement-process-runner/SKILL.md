---
name: procurement-process-runner
description: >
  This skill runs the procurement process for new vendor selection including RFP, evaluation, and approval.
  Use when asked to source a new vendor, run an RFP, or evaluate vendor proposals.
  Also consider when an existing vendor relationship ends and a replacement is needed.
  Suggest when a team requests a new tool or service that requires formal procurement.
department: technical-operations
agent: vendor-management-procurement
version: 1.0.0
complexity: medium
related-skills: []
---

# procurement-process-runner

## Agent: Vendor Management & Procurement

L1 vendor management and procurement function (1x) reporting to the COO, responsible for vendor contracts, risk assessment, procurement process, and vendor performance reviews.

Department ethos: [ideal-technical-operations.md](../../../departments/technical-operations/ideal-technical-operations.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

The procurement process runner manages the end-to-end vendor procurement process from requirements gathering through RFP issuance, proposal evaluation, and final vendor selection to ensure the organisation selects vendors that meet technical, commercial, and risk requirements.

## When to Use

- When a team requests a new tool, service, or vendor engagement that exceeds the self-service procurement threshold.
- When an existing vendor contract is ending and a competitive evaluation is needed for replacement.
- When a strategic initiative requires sourcing a vendor for a capability the organisation does not have in-house.
- When compliance requirements mandate a formal procurement process for certain spend categories.

## Workflow

1. **Gather requirements**: Work with the requesting team to document functional, technical, security, and budget requirements. Deliverable: procurement requirements document.
2. **Identify candidates**: Research the market and compile a shortlist of vendors that meet baseline requirements. Deliverable: vendor shortlist.
3. **Issue RFP**: Draft and distribute the RFP to shortlisted vendors with clear evaluation criteria and response deadlines. Deliverable: issued RFP.
4. **Evaluate proposals**: Score vendor responses against the evaluation criteria, conduct demos or trials as needed. Deliverable: scored evaluation matrix.
5. **Negotiate terms**: Negotiate pricing, SLA, and contract terms with the top-ranked vendor. Deliverable: negotiated term sheet.
6. **Approve and award**: Present the recommendation to the approval authority, obtain sign-off, and notify the selected vendor. Deliverable: approved vendor selection with signed contract.

## Anti-Patterns

- **Single-vendor evaluation**: Selecting a vendor without competitive comparison. *Why*: without alternatives, there is no leverage on pricing and no validation that the chosen vendor is actually the best fit.
- **Requirements drift during evaluation**: Changing requirements mid-process based on vendor demos. *Why*: shifting criteria undermines fair comparison and delays the selection timeline.
- **Skipping security review**: Evaluating only on features and price without assessing the vendor's security posture. *Why*: a cheap tool with poor security creates risk that far exceeds the cost savings.

## Output

**On success**: A completed procurement process with a signed vendor contract, an evaluation matrix documenting why the vendor was selected, and a handoff to vendor contract management for ongoing oversight.

**On failure**: Report which stage the process stalled at (e.g., no vendors met requirements, budget not approved), what was evaluated, and recommend next steps such as revising requirements or increasing budget.

## Related Skills

- [`vendor-risk-assessor`](../vendor-risk-assessor/SKILL.md) -- risk assessment is a required input to the procurement evaluation.
- [`vendor-contract-manager`](../vendor-contract-manager/SKILL.md) -- contract management takes over once procurement awards the contract.
- [`saas-stack-manager`](../../it-operations-manager/saas-stack-manager/SKILL.md) -- SaaS stack manager identifies when a new procurement is needed for software tools.
