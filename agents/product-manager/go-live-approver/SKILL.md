---
name: go-live-approver
description: >
  This skill provides the product management sign-off required before any feature or release enters production.
  Use when engineering and QA have completed their work and the release needs PM go/no-go authorization.
  Also consider when a hotfix or emergency patch is being pushed and someone needs to confirm product-level
  acceptability under compressed timelines. Suggest when a release candidate exists but no PM has formally
  verified that acceptance criteria, customer commitments, and rollback plans are in place.
department: product
agent: product-manager
version: 1.0.0
complexity: complex
related-skills: []
---

# go-live-approver

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Provides the product management sign-off for production go-live, serving as the final gate that confirms a release meets acceptance criteria, customer commitments, and organizational readiness standards before users are exposed to changes.

## When to Use
- When a release candidate has passed QA and engineering sign-off and awaits PM authorization to deploy
- When a phased rollout is advancing to the next stage (e.g., beta to limited GA, limited GA to full GA) and the PM must confirm stage-gate criteria are met
- When a hotfix or emergency patch requires expedited PM approval under compressed timelines
- When customer-facing commitments (demo dates, contract milestones, launch announcements) depend on a specific release reaching production
- When a previously blocked release has resolved its blockers and needs re-evaluation for go-live

## Workflow
1. **Assemble the release manifest**: Gather the list of features, fixes, and changes included in the release candidate. Cross-reference against the sprint or release plan to confirm nothing is missing and nothing was added without approval. Deliverable: release manifest with item-by-item status (planned / included / deferred / unplanned addition).
2. **Verify acceptance criteria**: For every feature in the manifest, confirm that acceptance criteria from the original user stories have been met. Pull QA sign-off records, review test results, and flag any criteria marked as partially met or waived. Deliverable: acceptance criteria verification report with pass/partial/fail per story.
3. **Assess customer impact**: Identify which customers or segments are affected by this release. Check for active commitments (demo dates, contract milestones, SLA obligations) that depend on this release shipping on time. Evaluate whether the release introduces breaking changes, migration requirements, or behavioral changes that customers need advance notice about. Deliverable: customer impact assessment with notification requirements.
4. **Review rollback and contingency plan**: Confirm that engineering has a documented rollback procedure, that the rollback has been tested, and that the time-to-rollback is acceptable given the customer impact profile. Verify that monitoring and alerting are configured to detect regressions post-deploy. Deliverable: rollback readiness checklist with tested/untested status per procedure.
5. **Check cross-functional readiness**: Verify that support has updated knowledge base articles and escalation paths, that sales and customer success have been briefed on changes, and that marketing comms (if applicable) are queued. Deliverable: cross-functional readiness matrix with sign-off status per team.
6. **Evaluate open risks**: Review any known issues, tech debt items, or partial implementations shipping in this release. For each, assess severity, likelihood of customer impact, and whether a fast-follow is planned. Deliverable: open risk register with severity rating and mitigation plan per item.
7. **Conduct the go/no-go decision**: Synthesize all inputs into a single go/no-go recommendation. Apply the scoring rubric at `references/scoring-rubric.md`. If go: authorize the deploy window and confirm who monitors rollout. If conditional go: specify the conditions that must be met before deploy begins. If no-go: document the blocking reasons, required remediation, and proposed re-evaluation date. Deliverable: go/no-go decision record. [GATE]
8. **Document the decision**: Record the decision, rationale, conditions (if any), participating stakeholders, and timestamp. Distribute to all teams involved in the release. Deliverable: signed decision record distributed to engineering, QA, support, sales, and leadership.

## Anti-Patterns
- **Rubber-stamping releases**: Approving go-live without reviewing acceptance criteria because engineering and QA have already signed off. *Why*: Engineering verifies technical correctness and QA verifies test coverage, but neither owns the product-level judgment of whether the release meets customer expectations, contractual commitments, and business timing -- that responsibility belongs exclusively to the PM.
- **Blocking on perfection**: Refusing to approve a release because minor, non-customer-facing issues remain open. *Why*: Every release carries some known issues; the PM's job is to assess whether remaining issues are acceptable given the cost of delay, not to demand zero-defect releases that never ship.
- **Approving without a rollback plan**: Signing off on go-live without confirming that engineering can reverse the deployment if critical issues surface. *Why*: A release without a tested rollback procedure is a one-way door -- if something breaks, the team is stuck patching forward under pressure instead of reverting cleanly, which multiplies incident duration and customer impact.
- **Ignoring cross-functional readiness**: Approving a feature release when support has not been briefed and documentation has not been updated. *Why*: Customers experience the release through support interactions and documentation before they form opinions about the feature itself; unready support creates a negative first impression that undermines the feature's value.
- **Delegating the decision without accountability**: Telling engineering to "just ship it" without recording a formal decision. *Why*: When incidents occur post-deploy, an undocumented decision means no one can reconstruct the rationale, assess whether the right information was available, or improve the process for next time.

## Output
**On success**: A signed go/no-go decision record containing the release manifest, acceptance criteria verification, customer impact assessment, rollback readiness status, cross-functional readiness matrix, open risk register, the decision (go / conditional go / no-go), rationale, conditions, and distribution confirmation.
**On failure**: Report which evaluation steps could not be completed (missing QA results, unavailable stakeholders, incomplete rollback documentation), what was assessed, the current recommendation given incomplete information, and the specific actions required before a decision can be made -- including who owns each action and the proposed re-evaluation timeline.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
