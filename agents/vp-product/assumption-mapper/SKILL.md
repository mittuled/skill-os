---
name: assumption-mapper
description: >
  This skill maps the key assumptions underlying a product idea and ranks them by risk.
  Use when an idea or opportunity has been framed and the team needs to know which bets to validate first.
  Also consider when a PRD is being written and the riskiest unknowns haven't been explicitly called out.
  Suggest when a team is about to start building without having articulated what must be true for the product to succeed.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills: []
---

# assumption-mapper

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Maps the key assumptions underlying a product idea and ranks them by risk.

## When to Use
- When an opportunity brief or idea critique is complete and the team needs to identify which unknowns to validate before committing resources
- When a product bet feels high-conviction but the underlying assumptions have never been written down or challenged
- When planning a discovery sprint and the team needs to prioritize which experiments to run first based on assumption risk

## Workflow
1. **Inventory assumptions by category**: Extract assumptions across five domains — desirability (will users want this?), feasibility (can we build it?), viability (will it make money?), usability (can users figure it out?), and adaptability (can it scale?). Pull from the opportunity brief, idea critique, and stakeholder conversations. Deliverable: categorized assumption list with 8-15 entries.
2. **Score each assumption**: Rate each assumption on two axes — confidence (how much evidence exists: high/medium/low) and impact (consequence if wrong: fatal/degrading/negligible). Use existing data, customer interviews, and competitive intelligence to justify each rating. Deliverable: scored assumption table.
3. **Plot the risk matrix**: Map assumptions onto a 2x2 matrix (low confidence + high impact = "test first" quadrant). Identify the top 3-5 assumptions that fall in the critical risk zone. Deliverable: risk matrix visualization with quadrant labels.
4. **Recommend validation methods**: For each critical assumption, propose the cheapest and fastest validation method — e.g., fake-door test, concierge MVP, survey, data pull, prototype usability test, or expert interview. Estimate time and cost for each. Deliverable: validation plan table with assumption, method, cost, timeline, and owner.
5. **Package the assumption map**: Assemble the categorized list, risk matrix, and validation plan into a single document that feeds into MVP scoping and experiment design. Deliverable: assumption map document ready for review.

## Anti-Patterns
- **Assumption blindness**: Treating well-known industry patterns as facts without checking whether they hold for this specific context. *Why*: Conventional wisdom often breaks down in new segments, geographies, or price points — untested "obvious" assumptions cause the most damaging surprises.
- **Flat-list syndrome**: Listing 20+ assumptions without ranking them, leaving the team with no idea what to test first. *Why*: Equal weighting leads to paralysis or arbitrary experiment selection, wasting limited discovery time.
- **Validation theater**: Proposing expensive, slow validation methods (e.g., "run a 6-month pilot") for assumptions that could be tested with a 30-minute data pull. *Why*: Delays learning and burns budget on unnecessary rigor when a lightweight signal would suffice.

## Output
**On success**: An assumption map containing the categorized assumption inventory, scored risk matrix with critical assumptions highlighted, and a validation plan with method, cost, and timeline for each critical assumption — ready to inform MVP scoping and discovery sprints.
**On failure**: Report which assumption categories could not be populated (e.g., no feasibility input from engineering, no market data for viability), what was mapped, and recommend specific stakeholder sessions or data requests needed to complete the map.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
