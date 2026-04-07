---
name: jtbd-to-stories
description: >
  This skill translates jobs-to-be-done insights into user stories with clear acceptance criteria ready
  for engineering. Use when customer discovery has produced JTBD statements and the team needs actionable
  backlog items. Also consider when existing stories feel disconnected from real customer needs and need
  to be rewritten with JTBD grounding. Suggest when a PM has interview transcripts or JTBD canvases
  but the backlog contains only feature requests without customer-outcome framing.
department: product
agent: product-manager
version: 1.0.0
complexity: complex
related-skills: []
---

# jtbd-to-stories

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Translates jobs-to-be-done insights into user stories with clear acceptance criteria, ensuring that every backlog item traces back to a real customer outcome rather than an assumed feature need.

## When to Use
- When customer discovery interviews have produced JTBD statements that need to be decomposed into implementable stories
- When the backlog is filled with feature requests that lack customer-outcome framing and need to be rewritten from a JTBD foundation
- When a new product area is being scoped and the team needs to go from raw JTBD canvases to a prioritized story map
- When engineering pushes back on vague stories and the PM needs to strengthen acceptance criteria with outcome-based language
- When multiple JTBD statements overlap and the PM must identify shared underlying jobs to consolidate into fewer, higher-impact stories

## Workflow
1. **Inventory the JTBD inputs**: Collect all JTBD statements, interview transcripts, switch interviews, and outcome-driven innovation data relevant to the scope. Organize by functional job, emotional job, and social job dimensions. Discard statements that are solution descriptions disguised as jobs (e.g., "I want a dashboard" is a solution; "I need to see whether my campaign is on track without asking three people" is a job). Deliverable: curated JTBD inventory organized by job dimension.
2. **Identify the core jobs and outcome expectations**: For each functional job, extract the desired outcome statements using the JTBD outcome format: [direction of improvement] + [outcome metric] + [context]. Group related outcomes under their parent job. Rank outcomes by importance and current satisfaction to identify underserved opportunities. Deliverable: outcome statement list ranked by opportunity score (importance + dissatisfaction).
3. **Decompose jobs into story candidates**: For each high-opportunity outcome, draft one or more user stories in the format: "As a [persona], I want to [action] so that [outcome]." Ensure the "so that" clause maps directly to a JTBD outcome statement -- not to a feature benefit. Keep stories small enough for a single sprint but large enough to deliver a meaningful outcome increment. Deliverable: draft story list with JTBD traceability annotations.
4. **Write acceptance criteria for each story**: Define acceptance criteria that are testable, outcome-oriented, and free of implementation prescription. Each criterion should answer "how will we know this job is done well?" rather than "what should the UI look like?" Include both positive criteria (what must work) and negative criteria (what must not break). Deliverable: acceptance criteria per story with positive and negative test conditions.
5. **Validate story independence and completeness**: Check that stories can be implemented independently (no hidden dependencies between stories in the same batch). Verify that the full set of stories covers all high-priority outcomes from step 2. Identify gaps where an outcome has no corresponding story and stories that serve no identified outcome. Deliverable: dependency map and coverage gap analysis.
6. **Build the story map**: Arrange stories along two axes: the user's journey (horizontal) and priority/depth (vertical). The top row represents the minimum viable journey -- the smallest set of stories that delivers the core job end-to-end. Lower rows add depth, edge cases, and delight. Deliverable: story map with release slicing recommendations.
7. **Review with engineering**: Walk engineering through the story map, acceptance criteria, and JTBD traceability. Collect feasibility feedback, identify stories that need technical spikes, and adjust scope or splitting based on engineering input. Deliverable: reviewed story map with engineering annotations and spike tickets.
8. **Finalize and load into backlog**: Update stories based on the engineering review. Add estimation tags, priority labels, and JTBD traceability links. Load into the backlog management tool in the agreed priority order. Deliverable: backlog loaded with JTBD-traced, acceptance-criteria-bearing stories ready for sprint planning.

## Anti-Patterns
- **Writing stories from feature requests instead of jobs**: Translating "customer asked for X" directly into a story without identifying the underlying job. *Why*: Feature requests describe one possible solution; the underlying job often has better solutions. Stories built on requests lock the team into a specific implementation before understanding what the customer actually needs to accomplish.
- **Acceptance criteria that prescribe implementation**: Writing criteria like "the button should be blue and in the top-right corner" instead of "the user can initiate the export within 2 clicks from any list view." *Why*: Prescriptive criteria prevent engineering and design from finding optimal solutions, create false test failures when the implementation is correct but visually different, and conflate the PM role with the design role.
- **Skipping outcome ranking**: Translating every JTBD statement into stories without prioritizing by opportunity score. *Why*: The team builds stories for well-served outcomes (low opportunity) while neglecting underserved outcomes (high opportunity), spending engineering capacity where it creates the least customer value.
- **Oversized stories**: Creating stories that span multiple sprints because the PM tried to capture an entire job in a single story. *Why*: Large stories resist estimation, hide complexity, delay feedback loops, and make sprint planning a negotiation instead of a commitment.
- **Losing traceability after creation**: Writing JTBD-grounded stories but not tagging them with the source outcome statement. *Why*: When priorities shift or scope is cut, the team cannot assess which customer outcomes are affected because the link between stories and jobs has been severed.

## Output
**On success**: A loaded backlog containing user stories with JTBD traceability links, testable acceptance criteria (positive and negative), a story map with release slicing, and engineering annotations. Every story traces to a ranked outcome statement, and every high-priority outcome has at least one corresponding story.
**On failure**: Report which steps could not be completed (insufficient JTBD data, missing persona definitions, engineering unavailable for review), the stories drafted so far with their current state, the gaps in coverage, and what specific inputs are needed to resume -- including which customer interviews or discovery activities should be conducted to fill the JTBD gaps.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
