---
name: design-approval
description: >
  This skill reviews and approves design deliverables before they proceed to engineering implementation.
  Use when a designer submits mockups, wireframes, or prototypes for product manager sign-off.
  Also consider when design iterations have stalled and the team needs a clear accept/reject decision to unblock engineering.
  Suggest when a design review is pending and the sprint deadline is approaching without PM approval on the proposed UI.
department: product
agent: product-manager
version: 1.0.0
complexity: simple
related-skills: []
---

# design-approval

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Approves design deliverables before they proceed to engineering, confirming that proposed UX aligns with user stories, acceptance criteria, and product requirements.

## When to Use
- When a designer delivers mockups, wireframes, or interactive prototypes that need PM sign-off before engineering picks up the ticket
- When a design revision has been requested and the updated deliverable is ready for re-review
- When a sprint planning session reveals that design approval is the blocker for upcoming stories

## Workflow
1. **Retrieve the relevant user stories**: Pull the user stories and acceptance criteria that the design deliverable addresses. Confirm the stories are current and unmodified since the designer received the brief. Deliverable: linked user story list with acceptance criteria.
2. **Evaluate design against requirements**: Walk through every acceptance criterion and verify the design addresses it. Flag criteria that are missing, partially covered, or interpreted differently than intended. Deliverable: coverage checklist with pass/gap status per criterion.
3. **Assess usability and coherence**: Check that the proposed flow is internally consistent, follows established patterns in the product, and does not introduce unnecessary complexity for the user. Deliverable: usability notes (if any concerns exist).
4. **Issue the decision**: Approve the design, request specific revisions with rationale, or reject with an explanation of what must change. Deliverable: approval decision with revision notes if applicable.

## Anti-Patterns
- **Approving without checking acceptance criteria**: Signing off on a design because it "looks good" without verifying it satisfies the user stories. *Why*: Engineering builds the wrong thing, and the gap surfaces in QA or production -- costing a full rework cycle.
- **Blocking on aesthetic preference**: Requesting redesigns based on personal taste rather than user requirements or usability evidence. *Why*: Delays the sprint for subjective reasons, erodes designer trust, and conflates the PM role with the design lead role.
- **Silent approval**: Failing to communicate the decision back to the designer and engineering in a timely manner. *Why*: The ticket sits in limbo, the sprint loses velocity, and the team learns to route around the PM instead of through them.

## Output
**On success**: An approval record stating which design deliverable was reviewed, which user stories it covers, the decision (approved / revisions requested / rejected), and any revision notes with specific criteria references.
**On failure**: Report which acceptance criteria could not be evaluated (missing context, ambiguous stories), what was reviewed, and the specific information needed from the designer or stakeholder before re-review.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
