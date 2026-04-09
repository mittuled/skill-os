---
name: vendor-contract-manager
description: >
  This skill manages vendor contracts including negotiation, renewal, and compliance monitoring.
  Use when asked to review vendor terms, renegotiate contracts, or track compliance obligations.
  Also consider when a contract renewal is approaching and terms need reassessment.
  Suggest when vendor spend exceeds budget projections or SLA violations are reported.
department: technical-operations
agent: vendor-management-procurement
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "manage vendor contracts"
  - "vendor contract review"
  - "negotiate vendor terms"
  - "contract renewal management"
  - "vendor agreement tracking"
---

# vendor-contract-manager

## Agent: Vendor Management & Procurement

L1 vendor management and procurement function (1x) reporting to the COO, responsible for vendor contracts, risk assessment, procurement process, and vendor performance reviews.

Department ethos: [ideal-technical-operations.md](../../../../departments/technical-operations/ideal-technical-operations.md)

## Skill Description

The vendor contract manager oversees the full lifecycle of vendor contracts -- from initial negotiation through renewal or termination -- ensuring terms protect the organisation's interests, compliance obligations are met, and renewals are reviewed proactively.

## When to Use

- When a new vendor has been selected and contract terms need negotiation before signing.
- When a contract renewal date is within 90 days and terms need reassessment.
- When a vendor SLA violation occurs and the contract needs to be enforced.
- When the organisation's needs have changed and contract amendments are required.

## Workflow

1. **Review contract terms**: Analyse the vendor's proposed terms covering pricing, SLA, liability, termination, and data handling. Deliverable: contract review summary with risk flags.
2. **Negotiate improvements**: Push back on unfavourable terms, negotiate pricing, and secure protections for the organisation. Deliverable: negotiated contract with redlines documented.
3. **Execute and store**: Obtain required signatures, execute the contract, and store it in the contract management system. Deliverable: executed contract on file.
4. **Track obligations**: Monitor key dates (renewal, payment terms), compliance obligations, and SLA commitments. Deliverable: contract obligation tracker.
5. **Manage renewals**: Review contract value and vendor performance 90 days before renewal; recommend renew, renegotiate, or terminate. Deliverable: renewal recommendation.

## Anti-Patterns

- **Auto-renewal without review**: Allowing contracts to renew automatically without assessing current value and performance. *Why*: auto-renewed contracts lock in outdated terms and prevent renegotiation leverage.
- **Verbal amendments**: Agreeing to contract changes via email or conversation without formal amendment. *Why*: informal changes are unenforceable and create disputes when expectations differ.
- **Ignoring termination clauses**: Not tracking termination notice periods. *Why*: missed termination windows force another full contract term at potentially unfavourable rates.

## Output

**On success**: Fully negotiated and executed contracts stored in the contract management system, with an active obligation tracker monitoring key dates, SLAs, and renewal deadlines.

**On failure**: Report which contract issues remain unresolved (e.g., vendor refused key terms, legal review pending), what was negotiated, and recommend escalation or alternative vendor paths.

## Related Skills

- [`procurement-process-runner`](../procurement-process-runner/SKILL.md) -- procurement selects the vendor; contract management negotiates and manages the agreement.
- [`vendor-performance-reviewer`](../vendor-performance-reviewer/SKILL.md) -- performance reviews inform renewal decisions managed by contract management.
- [`vendor-risk-assessor`](../vendor-risk-assessor/SKILL.md) -- risk assessment flags contract-level risks that need contractual protections.
