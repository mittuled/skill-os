---
name: sprint-reviewer
description: >
  This skill reviews sprint output against acceptance criteria and decides what is shippable.
  Use when a sprint ends and completed work needs formal acceptance before release.
  Also consider when stories were marked done but lack demo evidence or QA sign-off.
  Suggest when engineering closes a sprint and the PM has not yet verified delivered scope.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - market-sizer
  - backlog-populator
  - risk-register-builder
triggers:
  - "review the sprint output"
  - "what shipped this sprint"
  - "check acceptance criteria for delivered stories"
  - "is this sprint work shippable"
---

# sprint-reviewer

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Reviews sprint output against acceptance criteria and decides what is shippable.

## When to Use
- When a sprint reaches its end date and delivered stories need acceptance verification before release
- When engineering marks stories as complete but the PM has not confirmed they meet the original acceptance criteria
- When a release candidate exists and someone must decide which items ship and which roll back to the backlog
- When stakeholders request a sprint health check to understand delivery velocity against commitments

## Workflow
1. **Gather sprint artifacts**: Collect the sprint backlog, acceptance criteria for each committed story, and any demo recordings or QA reports produced during the sprint. Deliverable: checklist of committed stories with their acceptance criteria and current status.
2. **Review each story against criteria**: Walk through every committed story. Compare the delivered implementation against each acceptance criterion line by line. Flag criteria that are fully met, partially met, or unmet. Deliverable: annotated story list with pass/partial/fail per criterion.
3. **Verify edge cases and non-functional requirements**: Confirm that performance, accessibility, and error-handling requirements specified in the stories have been addressed. Check QA reports for regression issues. Deliverable: non-functional compliance notes appended to each story.
4. **Classify shippability**: Sort stories into three buckets — ship (all criteria met), ship-with-caveat (minor gaps documented and accepted), and reject (criteria materially unmet). For rejected stories, document the specific gaps. Deliverable: shippability matrix with bucket assignment and rationale.
5. **Communicate results**: Share the shippability matrix with engineering, design, and stakeholders. For rejected stories, create follow-up tickets with clear remediation steps and re-review dates. Deliverable: sprint review summary distributed to the team and follow-up tickets filed.

## Anti-Patterns
- **Rubber-stamping without verification**: Approving all stories as shipped without reviewing acceptance criteria. *Why*: This erodes quality standards over time and pushes defects downstream to customers.
- **Scope creep during review**: Adding new requirements during the review that were not in the original acceptance criteria. *Why*: This punishes the team for delivering what was agreed and destroys trust in the planning process.
- **Blocking the entire release for one story**: Holding back all shippable work because a single story failed review. *Why*: This delays value delivery to customers and conflates independent items unnecessarily.

## Output
**On success**: A sprint review summary containing the shippability matrix (ship / ship-with-caveat / reject per story), annotated acceptance-criteria results, and follow-up tickets for any rejected or caveated items — ready for release coordination.
**On failure**: Report which stories could not be reviewed (missing demos, absent QA reports, unclear criteria), what was attempted, and recommend specific actions to unblock — such as scheduling a live demo, re-running test suites, or clarifying ambiguous criteria with the story author.

## Related Skills
- [`market-sizer`](../market-sizer/SKILL.md) — sibling skill under the same agent — combine with market-sizer for end-to-end coverage
- [`backlog-populator`](../backlog-populator/SKILL.md) — sibling skill under the same agent — combine with backlog-populator for end-to-end coverage
- [`risk-register-builder`](../risk-register-builder/SKILL.md) — sibling skill under the same agent — combine with risk-register-builder for end-to-end coverage
