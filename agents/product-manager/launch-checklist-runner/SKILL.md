---
name: launch-checklist-runner
description: >
  This skill runs through the launch checklist to confirm all go-live criteria are met before a release
  reaches production. Use when the team is approaching a launch date and needs a structured pass through
  every prerequisite. Also consider when a launch was previously blocked and the team needs to verify that
  all remediation items are resolved. Suggest when multiple workstreams are converging on a release and
  no one has systematically verified that every dependency is satisfied.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "run the launch checklist"
  - "are we ready to launch"
  - "go through the go-live checklist"
  - "verify launch readiness"
---

# launch-checklist-runner

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Runs through the launch checklist to confirm all go-live criteria are met, systematically verifying every prerequisite across engineering, QA, support, marketing, and operations before authorizing a release.

## When to Use
- When a release date is within one week and the team needs a structured readiness sweep
- When a prior launch attempt was blocked and the PM needs to verify all remediation items are resolved before re-attempting
- When a new launch checklist has been created or updated and the PM needs to validate it against the current release
- When multiple teams are reporting "ready" independently but no one has verified cross-team dependencies

## Workflow
1. **Retrieve the active checklist**: Pull the launch checklist template for this release type (feature launch, hotfix, major version). Confirm the template is current and includes any items added from previous launch retrospectives. Deliverable: versioned checklist with item count and category breakdown.
2. **Walk through each category systematically**: Evaluate every checklist item in sequence, grouped by category (engineering readiness, QA sign-off, documentation, support readiness, marketing and comms, legal and compliance, infrastructure and monitoring). For each item, record status: pass, fail, blocked, or not applicable with justification. Deliverable: completed checklist with status per item.
3. **Identify and escalate blockers**: For every item marked fail or blocked, identify the owner, the specific issue, and the estimated time to resolution. Escalate items where the resolution timeline threatens the launch date. Deliverable: blocker list with owners, issues, ETAs, and escalation status.
4. **Assess overall readiness**: Calculate the percentage of checklist items passing. Determine whether the remaining failures are launch-blocking or acceptable-with-mitigation. Consult with engineering and QA leads on risk tolerance for any items marked acceptable-with-mitigation. Deliverable: readiness summary with go/conditional-go/no-go recommendation.
5. **Document and distribute results**: Record the checklist run results, the readiness recommendation, and any conditions attached to a conditional-go. Distribute to all stakeholders involved in the launch. Deliverable: checklist run report distributed to engineering, QA, support, marketing, and leadership.
6. **Schedule re-run if needed**: If the result is conditional-go or no-go, schedule a follow-up checklist run once blockers are expected to be resolved. Confirm owners commit to resolution dates. Deliverable: re-run calendar entry with prerequisites.

## Anti-Patterns
- **Skipping items because they "always pass"**: Marking recurring checklist items as pass without actually verifying them. *Why*: The item that always passes is the one that fails catastrophically when it finally does, because the team has no muscle memory for handling its failure.
- **Running the checklist too late**: Performing the first checklist run on launch day instead of days before. *Why*: Blockers discovered on launch day force a choice between shipping with known issues or delaying under pressure -- both outcomes are worse than catching the blocker earlier.
- **Checklist without owners**: Running through items without knowing who is responsible for each category. *Why*: Unowned items have no one to escalate to, no one to verify the fix, and no one accountable if the item was incorrectly marked as passing.
- **Treating the checklist as a formality**: Going through the motions without genuine assessment because the team has already decided to launch. *Why*: The checklist exists to surface information that might change the decision; running it performatively eliminates its value as a safety mechanism.

## Output
**On success**: A completed checklist run report containing status per item (pass/fail/blocked/N-A), blocker list with owners and ETAs, overall readiness percentage, go/conditional-go/no-go recommendation with rationale, and distribution confirmation.
**On failure**: Report which checklist categories could not be evaluated (unavailable owners, inaccessible systems, missing documentation), the items that were evaluated with their status, and the specific actions needed to complete the run -- including who must provide what information and by when.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
