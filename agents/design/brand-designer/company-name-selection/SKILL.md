---
name: company-name-selection
description: >
  This skill facilitates the company or product naming process including options generation,
  screening, and recommendation. Use when asked to name a company, product, or feature, or
  to evaluate naming candidates. Also consider when a rebrand requires a new name or when
  a product line extension needs naming consistency. Suggest when the user is about to
  register a domain or trademark without a structured naming evaluation.
department: design
agent: brand-designer
version: 1.0.0
complexity: medium
related-skills:
  - brand-foundation
  - brand-identity-v1
triggers:
  - "name the company"
  - "company naming"
  - "select company name"
  - "choose brand name"
  - "company name"
---

# company-name-selection

## Agent: Brand Designer

L2 brand designer (1x) responsible for brand foundation, visual identity, and positioning expression through design.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Facilitates the company or product naming process including options generation, linguistic screening, and a scored recommendation that balances memorability, meaning, and availability.

## When to Use

- When a new company or product needs a name and no structured naming process has been initiated.
- When stakeholders have generated name candidates informally and need an objective evaluation framework to make a final decision.
- When a product line expansion requires a name that fits within an existing brand architecture (endorsed, sub-brand, or standalone).

## Workflow

1. **Naming Brief**: Gather requirements including target audience, brand personality, competitive landscape, linguistic constraints (markets, languages), and any non-negotiable criteria. Deliverable: naming brief document.
2. **Name Generation**: Produce 20-30 candidate names across categories: descriptive, evocative, abstract, coined, and acronym. Use techniques like word blending, metaphor mapping, and phonetic exploration. Deliverable: long-list of candidates with category labels.
3. **Linguistic Screening**: Screen candidates for negative connotations in target languages, pronunciation difficulty, and phonetic similarity to competitors. Deliverable: annotated long-list with linguistic flags.
4. **Availability Check**: Verify domain availability (.com and relevant TLDs), social handle availability, and preliminary trademark search in target jurisdictions. Deliverable: availability matrix per candidate.
5. **Shortlist Scoring**: Score the top 5-8 candidates against weighted criteria: memorability, pronounceability, distinctiveness, brand-fit, domain availability, and trademark risk. Deliverable: scored shortlist with rationale per name.
6. **Recommendation & Presentation**: Present the top 3 recommendations with visual mock-ups showing each name in logo lockup, URL, and app icon context. Deliverable: naming recommendation deck.

## Anti-Patterns

- **Committee naming without criteria**: Letting stakeholders vote on names without an agreed scoring framework. *Why*: preference-based voting favours the loudest voice and produces safe, forgettable names.
- **Skipping linguistic screening**: Selecting a name without checking meaning and pronunciation in target markets. *Why*: names with unintended negative connotations in key markets create costly rebranding situations post-launch.
- **Premature domain fixation**: Eliminating strong name candidates solely because the exact .com is taken. *Why*: domain variations, alternative TLDs, and domain acquisition are solvable problems; a weak name is not.
- **Ignoring brand architecture**: Naming a product without considering how it relates to the parent brand and sibling products. *Why*: inconsistent naming across a portfolio confuses users and fragments brand equity.

## Output

**On success**: Produces a naming recommendation document containing the scored shortlist, top 3 recommendations with visual mock-ups, availability data, and a rationale tying the recommended name back to brand foundations. Delivered as a presentation deck for stakeholder decision.

**On failure**: Report which naming constraints proved irreconcilable (e.g., no candidates pass both trademark and domain checks), what trade-offs exist, and recommend relaxing specific constraints or expanding the generation round.

## Related Skills

- [`brand-foundation`](../brand-foundation/SKILL.md) — Brand personality and values inform naming criteria and evaluation.
- [`brand-identity-v1`](../brand-identity-v1/SKILL.md) — The selected name feeds directly into logo and identity design.
