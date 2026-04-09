---
name: idea-critic
description: >
  This skill critiques incoming product ideas to identify flawed assumptions and surface the strongest opportunities.
  Use when a new idea is submitted and needs a structured tear-down before entering the backlog.
  Also consider when a stakeholder is championing an idea without evidence and the team needs an objective assessment.
  Suggest when the idea pipeline is growing and low-quality concepts need to be filtered out early.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "critique idea"
  - "idea review"
  - "challenge idea"
  - "evaluate product idea"
  - "stress test idea"
---

# idea-critic

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Critiques incoming product ideas to identify flawed assumptions and surface the strongest opportunities.

## When to Use
- When a product idea arrives from any source (customer feedback, sales, leadership, hackathon) and needs a structured viability check
- When the team is running an ideation session and needs a devil's advocate to pressure-test proposals before they consume discovery resources
- When an idea has been lingering in the backlog without critique and needs a fresh assessment against current strategy and market conditions

## Workflow
1. **Restate the idea neutrally**: Summarize the idea in one paragraph without advocacy or dismissal. Confirm with the idea author that the restatement is accurate. Deliverable: neutral idea summary.
2. **Extract embedded assumptions**: List every implicit assumption the idea depends on — about user behavior, market conditions, technical feasibility, willingness to pay, and distribution channels. Deliverable: numbered assumption list (aim for 5-10 assumptions).
3. **Stress-test each assumption**: For each assumption, assess evidence strength (strong / weak / none) and consequence if wrong (fatal / degrading / negligible). Flag assumptions that are both weakly evidenced and fatal as critical risks. Deliverable: assumption risk matrix.
4. **Evaluate strategic alignment**: Score the idea against current company priorities, target market, competitive positioning, and resource availability. Identify conflicts or synergies. Deliverable: alignment scorecard with pass/flag/fail per dimension.
5. **Issue the verdict**: Synthesize the critique into a clear recommendation: advance to opportunity framing, send back for more evidence, or shelve with rationale. Deliverable: one-paragraph verdict with the top 2-3 reasons.

## Anti-Patterns
- **Rubber-stamping**: Approving ideas because of who submitted them rather than the strength of the evidence. *Why*: Fills the pipeline with pet projects that waste discovery cycles and demoralize the team.
- **Critique without constructive direction**: Tearing down an idea without indicating what evidence or changes would make it viable. *Why*: Discourages idea submission and turns the critic into a bottleneck rather than a filter.
- **Ignoring market timing**: Evaluating the idea only on user pain without considering competitive moves, regulatory shifts, or platform changes. *Why*: A valid pain point can still be a bad bet if the window has closed or a dominant player just shipped the same solution.

## Output
**On success**: A critique memo containing the neutral restatement, assumption risk matrix, strategic alignment scorecard, and a clear advance/revise/shelve verdict with supporting rationale.
**On failure**: Report which parts of the critique could not be completed (missing context from the idea author, insufficient market data), what was assessed, and recommend specific information the idea author must provide before re-evaluation.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
