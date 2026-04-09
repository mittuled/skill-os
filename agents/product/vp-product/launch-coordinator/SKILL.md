---
name: launch-coordinator
description: >
  This skill coordinates all cross-functional activities required for a successful product launch,
  from go/no-go decision through GA release and hypercare. Use when a feature or product has an
  approved PRD and engineering is approaching code-complete. Also consider when a launch date is
  slipping and the team needs a forcing function to realign dependencies. Suggest when marketing,
  sales enablement, support, and engineering each have launch tasks but no single owner is
  orchestrating the sequence.
department: product
agent: vp-product
version: 1.0.0
complexity: complex
related-skills: []
triggers:
  - "coordinate launch"
  - "launch coordination"
  - "manage launch"
  - "product launch plan"
  - "orchestrate launch"
---

# launch-coordinator

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Coordinates all cross-functional activities required for a successful product launch, orchestrating engineering, marketing, sales, support, and operations into a synchronized go-live sequence.

## When to Use
- When a product or feature has reached code-complete and needs coordinated rollout across teams
- When the launch involves multiple workstreams (documentation, enablement, billing, infrastructure) that must converge on a single date
- When a previously scheduled launch is at risk and dependencies need re-sequencing
- When a phased rollout (beta, limited GA, full GA) requires stage-gate coordination
- When post-launch hypercare responsibilities must be assigned before the release

## Workflow
1. **Confirm launch readiness**: Validate that engineering has met exit criteria, QA has signed off, and staging environment mirrors production. Deliverable: launch readiness checklist with pass/fail status per criterion.
2. **Assemble launch team**: Identify owners from marketing, sales enablement, customer success, support, DevOps, and legal. Assign RACI for every launch task. Deliverable: RACI matrix with named owners and escalation paths.
3. **Build launch timeline**: Create a reverse-planned schedule from the target GA date. Include milestones for beta start, docs freeze, enablement training, press embargo lift, and feature flag activation. Deliverable: launch timeline with dates, owners, and dependency links.
4. **Coordinate marketing and comms**: Confirm messaging, blog posts, changelog entries, email campaigns, and social media are queued and reviewed. Deliverable: comms checklist with publication dates and approval status.
5. **Prepare sales enablement**: Ensure sales decks, demo scripts, pricing updates, and FAQ documents are finalized and distributed. Deliverable: enablement package with distribution confirmation.
6. **Stage support readiness**: Verify knowledge base articles, runbooks, escalation procedures, and support tier routing are updated. Deliverable: support readiness sign-off from CS and support leads.
7. **Execute go/no-go ceremony**: Convene all workstream owners for final go/no-go. Walk through every checklist item, surface blockers, and make the call. Deliverable: go/no-go decision record with blocker resolution plan if conditional. [GATE]
8. **Monitor rollout**: Track feature flag progression, error rates, latency, and user-reported issues during phased rollout. Deliverable: rollout dashboard with real-time metrics and incident log.
9. **Run hypercare**: Staff a dedicated response team for the first 48-72 hours post-launch. Triage incoming issues, escalate P0/P1 bugs, and communicate status to stakeholders. Deliverable: hypercare summary report with issue count, resolution times, and follow-up items.

## Anti-Patterns
- **Big-bang launch without gates**: Skipping phased rollout and pushing to 100% of users simultaneously. *Why*: Eliminates the ability to catch regressions early, turning minor bugs into full-scale incidents that damage user trust.
- **Launch without support readiness**: Going live before support has updated documentation and escalation paths. *Why*: Support tickets spike, resolution times balloon, and customers churn during the most visible moment of the product cycle.
- **Implicit ownership**: Assuming each team knows their launch responsibilities without an explicit RACI. *Why*: Tasks fall through cracks -- nobody owns the changelog, billing config ships late, or legal review blocks at the last minute.
- **Skipping go/no-go**: Treating the launch date as immovable regardless of readiness signals. *Why*: Shipping a broken product to meet an arbitrary date costs more in hotfixes, reputation damage, and team morale than a short delay.
- **No hypercare plan**: Declaring victory at deploy and disbanding the launch team immediately. *Why*: Post-launch issues surface in the first 48 hours; without a dedicated triage team, response times degrade and critical bugs linger.

## Output
**On success**: A completed launch with all workstreams executed on schedule -- GA release live, comms published, sales enabled, support staffed, and hypercare summary delivered with metrics confirming stable rollout.
**On failure**: Report which workstreams are blocked, the current state of each checklist item, recommended date for re-attempt, and specific actions required to unblock (e.g., "enablement training not completed -- reschedule for Tuesday, push GA to Thursday").

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
