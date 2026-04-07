# Checklist: dependency-resolver

Ensures every blocked engineering task is diagnosed, escalated, and unblocked through a structured resolution process.

## Phase 1: Diagnose

- [ ] **Identify the exact dependency**: Name the specific API, data, infrastructure component, or task that is blocking progress — not just "blocked by Team X"
- [ ] **Confirm the owner**: Verify the owner of the blocking item (individual, team, vendor) and their current awareness of the block
- [ ] **Determine the root cause**: Is this a timeline slip? A technical conflict? An undocumented interface? A resource constraint?
- [ ] **Quantify the block age**: How many hours or days has this task been blocked? (Blocks older than 24h require escalation path documented)
- [ ] **Document in the blocker log**: Log the blocker with date, task ID, blocking dependency, owner, and root cause category

## Phase 2: Assess Impact

- [ ] **List downstream tasks**: Identify every task that cannot proceed while this block is unresolved
- [ ] **Calculate timeline cost**: Estimate days of delay per downstream task if the block continues for 1 day, 3 days, and 1 week
- [ ] **Assess critical path impact**: Is this block on the critical path? (If yes, every day of block = 1 day of overall schedule slip)
- [ ] **Flag affected sprints or milestones**: Identify which sprint goals or release milestones are at risk

## Phase 3: Generate Options

For every block, generate at least two resolution options before deciding:

- [ ] **Option A — Accelerate the blocking dependency**: Can the blocking team or vendor expedite? What would it require (resources, priority swap)?
- [ ] **Option B — Apply a workaround**: Can a stub, mock, or interface contract let blocked work proceed in parallel? Is the workaround scope-limited with a clear removal plan?
- [ ] **Option C — Resequence work**: Can the team pull non-blocked tasks from the backlog to fill the gap while waiting for resolution? Is the backlog groomed enough to support this?
- [ ] **Document tradeoffs**: Record the cost, risk, and timeline implication of each option before presenting to stakeholders

## Phase 4: Negotiate and Decide

- [ ] **Direct resolution first**: Contact the blocking team directly before escalating. Attempt resolution at peer level.
- [ ] **Set a resolution deadline**: Agree on a specific date by which the block must be resolved or escalated. Default: 48 hours from first contact.
- [ ] **Select resolution path**: Agree on the chosen option with all stakeholders. Document the decision and rationale.
- [ ] **Assign a single owner**: One person is accountable for executing the resolution. No shared ownership.
- [ ] **Record the agreed plan**: Update the blocker log with chosen option, owner, and committed resolution date.

## Phase 5: Execute and Verify

- [ ] **Implement the resolution**: Execute the chosen option (workaround applied, dependency delivered, tasks resequenced)
- [ ] **Confirm the blocked task can proceed**: Verify the previously blocked engineer has what they need to restart
- [ ] **Update the dependency map**: Reflect the resolution in the project's dependency graph
- [ ] **Communicate to affected teams**: Notify all teams whose work was impacted
- [ ] **Document lessons learned**: If the block was foreseeable, note the upstream process change that would prevent recurrence (e.g., add this dependency type to the pre-sprint dependency mapping checklist)

## Escalation Triggers

Escalate to engineering leadership if any of the following are true:
- Block has been unresolved for > 48 hours with no agreed resolution plan
- Resolution requires a priority trade-off that the tech lead cannot make unilaterally
- The blocking party is a third-party vendor with no SLA for resolution
- The block will cause a missed sprint goal or release milestone

## Workaround Documentation Standard

When a workaround is applied, document:
1. **What the workaround does**: Technical description
2. **What it does not handle**: Known gaps vs. the real dependency
3. **Removal criteria**: Exact condition under which the workaround must be removed
4. **Removal owner**: Who is responsible for replacing the workaround when the real dependency arrives
5. **Ticket link**: Link to the tech debt ticket tracking the workaround removal
