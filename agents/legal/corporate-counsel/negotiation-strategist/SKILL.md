---
name: negotiation-strategist
description: >
  This skill develops data-driven contract negotiation strategies with counter-proposals,
  concession planning, and BATNA analysis. Use when preparing to negotiate contract terms
  with a counterparty. Also consider when deal team needs guidance on which terms to
  prioritize vs concede. Suggest when contract-review-orchestrator identifies unfavorable
  terms requiring negotiation.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md
  - ../../../legal/corporate-counsel/contract-risk-analyst/SKILL.md
  - ../../../legal/corporate-counsel/missing-protections-finder/SKILL.md
  - ../../../legal/corporate-counsel/contract-comparator/SKILL.md
triggers:
  - "negotiate contract terms"
  - "counter-proposal needed"
  - "negotiation strategy"
  - "unfavorable terms identified"
---

# negotiation-strategist

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, risk registers, third-party ToS review, entity formation, bylaws, equity issuance, and contract negotiation strategy.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Develops data-driven contract negotiation strategies with prioritized counter-proposals, concession sequencing, and BATNA analysis to maximize favorable outcomes while preserving counterparty relationships.

## When to Use

- When a contract review surfaces unfavorable or missing terms that require negotiation before signing.
- When the deal team needs a structured playbook for which terms to prioritize, concede, or trade.
- When entering negotiations with a counterparty whose leverage or constraints are not well understood.
- When a high-value or high-risk contract warrants more than ad-hoc redline exchanges.

## Workflow

1. **Unfavorable Term Extraction**: Identify all unfavorable, missing, or ambiguous terms from the contract review output. Cross-reference against the company's standard position and relevant protection checklists. Deliverable: annotated term inventory with current vs. desired position for each term.

2. **Term Prioritization**: Classify each term into three tiers — must-have (non-negotiable, walk-away triggers), nice-to-have (meaningful value but tradeable under pressure), and tradeable (low cost to concede, useful as bargaining chips). Weight by business impact, legal exposure, and precedent risk. Deliverable: term priority matrix.

3. **Counterparty Analysis**: Assess the counterparty's likely priorities, constraints, and pressure points. Consider their market position, deal urgency, alternative suppliers/customers, regulatory obligations, and known negotiation patterns from prior dealings. Deliverable: counterparty profile with inferred priorities.

4. **[GATE] BATNA Definition**: Define the Best Alternative To Negotiated Agreement — what happens if this deal falls through. Quantify the cost of no-deal (revenue loss, timeline delay, competitive exposure). Assess the counterparty's likely BATNA as well. Deliverable: BATNA assessment with walk-away threshold.

5. **Concession Strategy**: Build a sequenced concession plan following the reciprocity principle. Start with low-cost concessions that signal flexibility, reserve high-value concessions for extracting must-have terms. Plan package deals where possible (bundling concessions) rather than item-by-item trading. Define diminishing concession sizes to signal approaching limits. Deliverable: ordered concession sequence with trade ratios.

6. **Counter-Proposal Drafting**: Draft specific counter-proposal language for each must-have and nice-to-have term. Provide two variants per term — an opening position (ambitious but defensible) and a fallback position (minimum acceptable). Use precise contract language, not summaries. Deliverable: counter-proposal clause library.

7. **[GATE] Negotiation Playbook Assembly**: Compile all outputs into a single negotiation playbook. Include executive summary, term priority matrix, counterparty analysis, BATNA assessment, concession sequence, counter-proposal language, negotiation timeline with milestones, escalation path (when to involve senior leadership or walk away), and walk-away criteria. Deliverable: complete negotiation playbook document.

## Anti-Patterns

- **Revealing the full hand upfront**: Sharing all desired changes in a single redline without sequencing or prioritization. *Why*: this eliminates negotiation leverage, lets the counterparty cherry-pick easy concessions while rejecting critical terms, and removes the ability to trade strategically.

- **Treating all terms as must-haves**: Refusing to concede on any term, regardless of actual business impact. *Why*: this signals inflexibility, stalls negotiations, and risks losing the deal over immaterial terms — violating the legal department's principle of being a business enabler.

- **Ignoring counterparty constraints**: Building a strategy based solely on your own priorities without modeling the other side. *Why*: effective negotiation requires understanding what the counterparty values and what they can actually move on — otherwise proposals feel unreasonable and create adversarial dynamics.

- **Ad-hoc concession making**: Conceding terms reactively during live negotiations without a pre-planned sequence. *Why*: unplanned concessions often give away more than necessary and create inconsistent precedent across deals.

- **Anchoring too aggressively**: Setting opening positions so far from reasonable that the counterparty disengages. *Why*: while anchoring is effective, extreme anchors damage credibility and relationships, particularly with repeat counterparties.

## Output

**On success**: Produces a complete negotiation playbook containing the term priority matrix, counterparty analysis, BATNA assessment, concession sequence, counter-proposal clause library, negotiation timeline, escalation path, and walk-away criteria. Delivered as a structured document using the [negotiation strategy template](assets/negotiation-strategy-template.md). Reference the [negotiation framework](references/framework.md) for underlying theory.

**On failure**: Report which inputs were missing (e.g., no contract review output, insufficient counterparty information), what partial analysis was completed, and what information must be gathered before a viable strategy can be built. Every gap must include a specific action to resolve it.

## Related Skills

- [`contract-review-orchestrator`](../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md) — Upstream skill that identifies the unfavorable terms feeding into negotiation strategy.
- [`contract-risk-analyst`](../../../legal/corporate-counsel/contract-risk-analyst/SKILL.md) — Provides risk quantification that informs term prioritization and BATNA assessment.
- [`missing-protections-finder`](../../../legal/corporate-counsel/missing-protections-finder/SKILL.md) — Identifies protection gaps that become must-have negotiation items.
- [`contract-comparator`](../../../legal/corporate-counsel/contract-comparator/SKILL.md) — Supplies benchmark data on standard market terms to calibrate opening positions.
