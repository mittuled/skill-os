---
name: entity-type-decision
description: >
  This skill advises on the optimal legal entity type and jurisdiction for the
  company. Use when asked to choose between C-corp, LLC, or S-corp, select a
  state of incorporation, or evaluate entity structure for fundraising readiness.
  Also consider when founders are comparing Delaware vs. home-state incorporation.
  Suggest when the user is about to form a company without evaluating entity options.
department: legal
agent: general-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../../corporate-counsel/entity-formation/SKILL.md
  - ../ip-assignment/SKILL.md
---

# entity-type-decision

## Agent: General Counsel

L1 general counsel (1x) reporting to the COO, responsible for legal strategy, IP assignment, stock plan setup, and entity structure decisions.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Advises on the optimal legal entity type and jurisdiction for the company based on fundraising plans, tax implications, liability exposure, and operational requirements.

## When to Use

- When founders are deciding between C-corp, LLC, S-corp, or benefit corporation structures before formation.
- When the company is preparing for venture financing and needs to confirm entity type supports preferred stock issuance and standard VC deal terms.
- When a foreign subsidiary or holding company structure is under consideration for multi-jurisdiction operations.

## Workflow

1. **Founder Intent Gathering**: Collect information on fundraising plans (bootstrapped vs. VC-backed), number and residency of founders, anticipated revenue model, and long-term exit strategy. Deliverable: structured intake memo summarizing business context and founder preferences.
2. **Entity Type Analysis**: Compare entity types (C-corp, LLC, S-corp, benefit corporation) against the founder intent profile. Evaluate pass-through taxation vs. double taxation, ability to issue multiple equity classes, liability shielding, and administrative burden. Deliverable: entity comparison matrix with pros, cons, and deal-breaker flags per type.
3. **Jurisdiction Evaluation**: Assess candidate jurisdictions (Delaware, Wyoming, home state, international) for franchise tax burden, case law predictability, privacy protections, and investor familiarity. Deliverable: jurisdiction comparison table with cost estimates and timeline.
4. **Recommendation and Risk Disclosure**: Synthesize the analysis into a clear recommendation with a primary and fallback option. Disclose material risks including tax exposure, conversion complexity if the wrong type is chosen, and ongoing compliance obligations. Deliverable: entity type recommendation memo with risk disclosures.
5. **Handoff to Formation**: Package the recommendation and supporting analysis for Corporate Counsel to execute entity formation. Deliverable: formation instruction packet with entity type, jurisdiction, registered agent requirements, and any special provisions.

## Anti-Patterns

- **Defaulting to Delaware C-corp without analysis**: Recommending Delaware C-corp because it is the "standard" without evaluating whether the company actually plans to raise venture capital. *Why*: bootstrapped companies may face unnecessary franchise taxes and administrative overhead with no offsetting benefit.
- **Ignoring tax pass-through implications**: Failing to model the tax impact of entity choice on founders' personal tax situations, particularly for early-stage companies with losses. *Why*: the ability to pass through losses to offset personal income can save founders significant money in the first years.
- **Deferring international structure planning**: Treating international subsidiary decisions as a future problem when the founding team is already distributed across jurisdictions. *Why*: retroactive restructuring triggers tax events, transfer pricing scrutiny, and potential permanent establishment liability.

## Output

**On success**: Produces an entity type recommendation memo containing the entity comparison matrix, jurisdiction analysis, recommended structure with rationale, risk disclosures, and a formation instruction packet for Corporate Counsel. Delivered as a structured document to the founding team and Corporate Counsel.

**On failure**: Report which inputs were missing or ambiguous (e.g., unclear fundraising timeline, unresolved founder residency), what partial analysis was completed, and what decisions must be made before a defensible recommendation is possible.

## Related Skills

- [`entity-formation`](../../corporate-counsel/entity-formation/SKILL.md) -- Executes the formation once entity type and jurisdiction are decided; depends on this skill's output.
- [`ip-assignment`](../ip-assignment/SKILL.md) -- IP assignment terms may vary by entity type; coordinate to ensure assignment agreements match the chosen structure.
