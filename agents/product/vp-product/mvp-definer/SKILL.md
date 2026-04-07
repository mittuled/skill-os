---
name: mvp-definer
description: >
  This skill defines the minimum viable product scope that tests the core value hypothesis.
  Use when an opportunity has been validated and the team needs to draw the line between must-have and nice-to-have scope.
  Also consider when scope creep is inflating a v1 beyond what can ship in one development cycle.
  Suggest when engineering asks "what can we cut?" or when a PRD draft contains more than one core bet.
department: product
agent: vp-product
version: 1.0.0
complexity: complex
related-skills: []
triggers:
  - "define the MVP"
  - "what's the minimum we need to ship"
  - "scope the v1"
  - "draw the MVP cut line"
  - "what can we cut from v1"
---

# mvp-definer

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Defines the minimum viable product scope that tests the core value hypothesis.

## When to Use
- When a validated opportunity needs to be scoped into a shippable first release that tests the riskiest assumption
- When a PRD draft has ballooned with features and the team needs a principled cut-line to separate MVP from fast-follow
- When engineering capacity is constrained and leadership needs a scope recommendation that fits within a single sprint cycle or development window

## Workflow
1. **Extract the core value hypothesis**: Distill the opportunity brief into a single testable hypothesis in the format "We believe [user] will [behavior] because [value proposition]." Confirm this is the riskiest assumption — the one that, if wrong, invalidates the entire initiative. Deliverable: one-sentence value hypothesis with risk rationale.
2. **Map the user journey**: Sketch the minimum end-to-end flow a user must complete to experience the core value. Identify each step and mark which are essential versus enhanceable. Use a story map format with backbone (activities) and walking skeleton (minimum tasks). Deliverable: user journey map with essential-path annotations.
3. **Define the scope boundary**: For each step in the journey, decide build vs. fake vs. omit. Apply the "what's the cheapest way to test this assumption?" lens. Catalog each feature as in-MVP, fast-follow, or out-of-scope with explicit rationale. Deliverable: scope table with feature name, category, rationale, and estimated effort (T-shirt size).
4. **Stress-test with the Wizard of Oz check**: For every in-MVP feature, ask "could a human do this manually instead of building it?" If yes, consider whether manual fulfillment is acceptable for the test period. Reclassify features that fail the automation necessity test. Deliverable: revised scope table with manual-override annotations.
5. **Set the success experiment**: Define the metric that validates or invalidates the value hypothesis. Specify the sample size, measurement window, and pass/fail threshold before building begins. Tie this directly to the North Star metric from the goal framework. Deliverable: experiment card with hypothesis, metric, threshold, duration, and sample size.
6. **Negotiate with engineering**: Walk the scope table and experiment card through technical review. Identify hidden complexity, infrastructure prerequisites, and integration risks. Adjust scope to fit the target development window without compromising the core test. Deliverable: engineering-validated scope with revised effort estimates and identified technical risks.
7. **Document the MVP contract**: Assemble the final MVP definition including the value hypothesis, scoped journey, feature table, experiment design, and engineering agreement. This becomes the authoritative input to the PRD. Deliverable: MVP definition document with sign-off from product, engineering, and design leads.

## Anti-Patterns
- **Kitchen-sink MVP**: Including every feature stakeholders request to avoid difficult conversations. *Why*: Delays time-to-learning, increases build cost, and makes it impossible to attribute success or failure to the core hypothesis.
- **Hypothesis-free MVP**: Defining scope without an explicit testable hypothesis. *Why*: Without a hypothesis, there is no experiment — the MVP becomes a mini-product launch with no learning framework, and the team cannot decide what to cut.
- **Perfection bias**: Refusing to ship until edge cases are handled and the UI is polished. *Why*: The purpose of an MVP is to learn, not to delight — over-polishing delays the feedback loop and wastes effort on features that may be discarded.
- **Invisible MVP**: Building backend infrastructure or data pipelines with no user-facing surface to test. *Why*: If no user touches the product, the value hypothesis remains untested regardless of technical progress.
- **Ignoring the fast-follow plan**: Cutting features from MVP without documenting when and how they return. *Why*: Stakeholders lose trust if cuts feel permanent, and the team loses context on deferred scope.

## Output
**On success**: An MVP definition document containing the core value hypothesis, annotated user journey map, feature scope table (in-MVP / fast-follow / out-of-scope with rationale), experiment design with pass/fail criteria, and engineering sign-off — ready to feed directly into PRD assembly.
**On failure**: Report which elements could not be resolved (ambiguous hypothesis, unresolvable scope disagreement, missing effort estimates), what trade-offs were explored, and recommend specific next steps such as a design spike, technical spike, or stakeholder alignment session to unblock the definition.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
