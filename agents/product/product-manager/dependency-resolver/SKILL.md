---
name: dependency-resolver
description: >
  This skill resolves cross-team and cross-system dependency conflicts that are actively blocking or threatening product delivery. Use when a dependency flagged by the dependency mapper has no clear resolution path and requires negotiation, re-sequencing, or escalation. Also consider when two teams deadlock on priority ordering for a shared resource. Suggest when a blocking dependency has persisted for more than half a sprint without progress.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - dependency-mapper-review
  - sprint-planner
  - scope-boundary-setter
  - phase-scope-adjuster
triggers:
  - "resolve dependencies"
  - "fix dependencies"
  - "dependency resolution"
  - "unblock dependencies"
  - "clear blockers"
---

# dependency-resolver

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
The dependency resolver takes blocking or at-risk dependencies surfaced by the dependency mapper and drives them to resolution through negotiation with owning teams, scope adjustment, workaround design, or escalation. It converts an identified risk into a concrete action plan with committed dates, fallback options, and clear accountability so that delivery timelines are protected.

## When to Use
- A blocking dependency identified in the dependency map has no committed delivery date from the owning team.
- Two or more teams are deadlocked on priority ordering for a shared service, API, or infrastructure component.
- A third-party vendor dependency has slipped and the original delivery plan is at risk.
- A blocking dependency has persisted for more than half a sprint without visible progress or a named owner driving resolution.
- Sprint planning cannot proceed because a critical-path item depends on unresolved external work.
- A circular dependency is detected in the dependency map and requires architectural or sequencing intervention to break.

## Workflow
1. Review the dependency map and risk register; identify all dependencies classified as blocking or at-risk that lack a committed resolution date.
2. For each unresolved dependency, contact the owning team's PM or tech lead to understand their current priority, capacity, and earliest feasible delivery date.
3. Assess resolution options for each dependency:
   - **Direct resolution:** the owning team commits to delivering by the needed date within their existing sprint plan.
   - **Re-sequencing:** adjust the dependent team's sprint order so the blocked work moves to a later sprint while non-blocked work pulls forward.
   - **Scope reduction:** negotiate a minimal viable version of the dependency (e.g., a read-only API endpoint instead of full CRUD) that unblocks the critical path.
   - **Workaround:** design a temporary solution (mock, feature flag, hardcoded config) that lets the dependent team proceed while the full dependency is delivered later.
   - **Escalation:** if the owning team cannot or will not commit, escalate to the shared manager or product lead with a clear impact statement.
4. For each dependency, select the resolution path and document: the action, the owner, the committed date, and the fallback if the commitment slips.
5. Update the dependency map to reflect the resolution status and any new dependencies introduced by workarounds.
6. Communicate the resolution plan to both the dependent and owning teams; confirm mutual understanding of commitments.
7. Set a follow-up checkpoint at the midpoint between now and the committed date to verify progress; re-escalate if off track.
8. Close the dependency item in the risk register once the deliverable is confirmed complete and integrated.

## Anti-Patterns
- **Resolving by assumption.** Marking a dependency as "resolved" because the owning team said they would "try to get to it" without a committed date. *Why: uncommitted timelines are not resolutions; they are hopes that create false confidence in the delivery plan.*
- **Always escalating first.** Jumping to management escalation before attempting direct negotiation burns political capital and slows resolution. *Why: most dependency conflicts stem from information asymmetry, not ill intent; a direct conversation often surfaces a simple fix.*
- **Ignoring workaround debt.** Implementing temporary workarounds without tracking the follow-up to remove them creates long-lived technical debt. *Why: workarounds that persist beyond one sprint become permanent architecture that no one planned for.*
- **Resolving scope without the dependent team's input.** Negotiating a reduced scope with the owning team without confirming the reduction still unblocks the dependent team. *Why: a minimal API that omits a critical field does not actually resolve the dependency; it just moves the blocker downstream.*

## Output

**Success:**
- A resolution plan for every blocking or at-risk dependency, with a named owner, committed date, chosen resolution path, and documented fallback.
- Updated dependency map and risk register reflecting current resolution status.
- Follow-up checkpoints scheduled for each open resolution.

**Failure:**
- Dependencies are marked resolved without committed dates, leaving the sprint plan exposed to slippage.
- Workarounds are deployed without follow-up tracking, embedding unplanned technical debt.

## Related Skills
- `dependency-mapper-review` -- surfaces the dependencies this skill resolves.
- `sprint-planner` -- adjusts sprint scope based on resolution outcomes and re-sequencing decisions.
- `scope-boundary-setter` -- collaborates when scope reduction is the chosen resolution path.
- `phase-scope-adjuster` -- recalibrates phase plans when dependency resolution shifts delivery timelines.
