---
name: ip-assignment
description: >
  This skill ensures all intellectual property is properly assigned to the company
  from founders, employees, and contractors. Use when asked to draft IP assignment
  agreements, audit IP ownership, or prepare for due diligence. Also consider when
  new founders or contractors join without signed assignments. Suggest when the user
  is about to engage contractors without IP transfer provisions.
department: legal
agent: general-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../../corporate-counsel/founder-equity-issuance/SKILL.md
  - ../../corporate-counsel/legal-template-library-builder/SKILL.md
---

# ip-assignment

## Agent: General Counsel

L1 general counsel (1x) reporting to the COO, responsible for legal strategy, IP assignment, stock plan setup, and entity structure decisions.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Ensures all intellectual property created for or on behalf of the company is properly assigned through executed agreements covering founders, employees, and contractors.

## When to Use

- When onboarding founders, employees, or contractors who will create patentable inventions, copyrightable works, or trade secrets for the company.
- When preparing for a fundraising round, acquisition, or due diligence process that will scrutinize IP chain of title.
- When a contributor created work prior to formal engagement and that pre-existing IP needs to be assigned or licensed to the company.

## Workflow

1. **IP Inventory Audit**: Identify all individuals who have contributed or will contribute intellectual property, including founders' pre-incorporation work, employee inventions, and contractor deliverables. Deliverable: IP contributor roster with contribution type, date range, and current assignment status.
2. **Prior Art and Pre-existing IP Assessment**: Determine whether contributors hold pre-existing IP that will be incorporated into company products. Distinguish between IP that must be assigned outright and IP that can be licensed in. Deliverable: pre-existing IP schedule listing each item, its owner, and the proposed treatment (assignment vs. license).
3. **Agreement Drafting**: Draft IP assignment agreements tailored to contributor type. Founder assignments should include present-tense assignment language ("hereby assigns"), work-for-hire declarations where applicable, moral rights waivers, and invention disclosure obligations. Contractor agreements must include work-for-hire clauses with fallback assignment provisions. Deliverable: executed IP assignment agreements per contributor.
4. **Execution and Filing**: Circulate agreements for signature, track execution status, and file any required patent or copyright assignment recordations. Deliverable: signed agreement repository with execution log.
5. **Gap Remediation**: Identify any gaps in the IP chain of title (unsigned agreements, ambiguous scope, state law limitations on work-for-hire) and remediate through supplemental assignments or confirmatory agreements. Deliverable: gap analysis report with remediation actions completed or escalated.

## Anti-Patterns

- **Relying solely on employment agreements**: Assuming that a general employment agreement with an IP clause is sufficient without a standalone IP assignment for pre-existing and prior work. *Why*: employment agreements typically cover only future work created during employment; pre-incorporation contributions require separate assignment.
- **Ignoring state-specific carve-outs**: Failing to account for state laws (e.g., California Labor Code 2870) that limit employer claims on employee inventions created on personal time with personal resources. *Why*: overbroad assignment clauses that violate state law may be unenforceable, creating IP ownership gaps discovered during diligence.
- **Delaying contractor IP assignment until project completion**: Waiting until a contractor engagement ends to address IP ownership. *Why*: contractors who have completed work and been paid have less incentive to sign; leverage is highest at engagement start.

## Output

**On success**: Produces a complete IP assignment package containing the contributor roster, pre-existing IP schedule, executed assignment agreements, execution log, and gap analysis report. Delivered to the company's document management system and flagged for due diligence readiness.

**On failure**: Report which contributors lack executed agreements, what specific gaps exist in the chain of title, and what remediation steps are required with estimated timelines.

## Related Skills

- [`founder-equity-issuance`](../../corporate-counsel/founder-equity-issuance/SKILL.md) -- Founder IP assignment should be executed concurrently with equity issuance to ensure consideration flows both ways.
- [`legal-template-library-builder`](../../corporate-counsel/legal-template-library-builder/SKILL.md) -- IP assignment templates feed into the broader template library for reuse across future engagements.
