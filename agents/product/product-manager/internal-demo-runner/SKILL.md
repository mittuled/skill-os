---
name: internal-demo-runner
description: >
  This skill runs internal product demos to align stakeholders on feature behavior before external release.
  Use when a feature is nearing completion and leadership, sales, or support needs to see it in action.
  Also consider when stakeholder misalignment is emerging and a live walkthrough would resolve conflicting assumptions.
  Suggest when a release is approaching and cross-functional teams have not yet seen the working product.
department: product
agent: product-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# internal-demo-runner

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Runs internal product demos to align stakeholders on feature behavior, surface last-mile concerns, and build organizational confidence before external release.

## When to Use
- When a feature has reached a demonstrable state and internal teams need a walkthrough before launch
- When leadership or sales has questions about an upcoming release that are best answered by a live demo
- When conflicting assumptions across teams need resolution through a shared view of the actual product

## Workflow
1. **Define demo scope and audience**: Identify which features to demonstrate and which stakeholders must attend. Tailor the demo narrative to audience concerns -- leadership cares about strategic fit, sales cares about customer-facing value, support cares about edge cases. Deliverable: demo agenda with feature list, audience roster, and narrative angle.
2. **Prepare the demo environment**: Confirm the staging or preview environment is stable, loaded with realistic data, and accessible to all attendees. Run through the demo flow once to catch broken states or missing data. Deliverable: verified demo environment with backup plan if the environment fails.
3. **Run the demo**: Walk through each feature in the planned sequence. Narrate the user's perspective -- what problem they have, what they do, what happens. Pause after each feature for questions. Capture feedback, objections, and action items in real time. Deliverable: recorded feedback log with attribution.
4. **Distribute findings**: Summarize feedback into categories (must-fix before launch, fast-follow, nice-to-have, out of scope). Share with engineering, design, and leadership within 24 hours. Deliverable: demo summary with categorized feedback and assigned owners.

## Anti-Patterns
- **Demoing on an unstable environment**: Running the demo on a broken or outdated staging environment. *Why*: Crashes during the demo destroy stakeholder confidence in the release and shift the conversation from features to reliability concerns.
- **Demoing without a narrative**: Walking through screens without explaining the user problem or context. *Why*: Stakeholders evaluate features differently when shown raw UI versus a story -- without narrative, feedback skews toward cosmetic opinions rather than functional alignment.
- **Collecting feedback without follow-through**: Capturing stakeholder concerns during the demo but never distributing or acting on them. *Why*: Stakeholders stop attending demos when their input disappears, and the PM loses the alignment mechanism the demo was meant to provide.

## Output
**On success**: A demo summary containing the features demonstrated, attendee list, categorized feedback (must-fix / fast-follow / nice-to-have / out of scope), assigned owners for action items, and a timeline for resolution.
**On failure**: Report what prevented the demo from completing (environment failure, missing features, key stakeholders absent), what was demonstrated, and the proposed reschedule plan with prerequisites.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
