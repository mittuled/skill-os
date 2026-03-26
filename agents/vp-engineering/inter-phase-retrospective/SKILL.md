---
name: inter-phase-retrospective
description: >
  This skill facilitates retrospectives between delivery phases to capture learnings and improve
  processes. Use when asked to run a retro, conduct a post-phase review, or identify process
  improvements after a milestone. Also consider when velocity has degraded or incident count
  has increased between phases. Suggest when a phase ends without a structured review.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../vp-engineering/velocity-monitor/SKILL.md
  - ../../tech-lead-pr-reviewer/inter-phase-reviewer-eng/SKILL.md
---

# inter-phase-retrospective

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Facilitates retrospectives between delivery phases to capture learnings, surface systemic issues, and produce actionable process improvements.

## When to Use

- When a delivery phase completes and the team transitions to the next phase.
- When DORA metrics (lead time, deployment frequency, change failure rate, MTTR) show degradation between phases.
- When a significant incident or scope change occurred during the phase that warrants structured reflection.

## Workflow

1. **Gather phase data**: Collect velocity metrics, incident reports, scope change log, and DORA metrics for the completed phase. Deliverable: phase data summary.
2. **Solicit input**: Collect feedback from engineering, product, and design stakeholders using a structured format (what went well, what didn't, what to change). Deliverable: aggregated feedback document.
3. **Identify patterns**: Analyze feedback and data for recurring themes. Distinguish between one-off issues and systemic problems. Deliverable: categorized findings with frequency and impact ratings.
4. **Define action items**: Convert the top findings into specific, assignable, time-bound action items. Each action item must have an owner and a definition of done. Deliverable: action item register.
5. **Document and distribute**: Write the retrospective summary and publish to the team. Track action items in the project management tool. Deliverable: retrospective document with linked action items.

## Anti-Patterns

- **Blame-oriented framing**: Focusing on who caused problems rather than what systemic factors enabled them. *Why*: blame suppresses honest feedback and prevents identification of root causes.
- **Action-item graveyard**: Capturing action items that are never tracked or completed. *Why*: unactioned retros erode team trust in the process and guarantee the same issues recur.
- **Recency bias**: Discussing only the last week of the phase rather than the full duration. *Why*: early-phase issues that were normalized get overlooked, perpetuating hidden inefficiencies.

## Output

**On success**: Produces a retrospective document containing phase metrics summary, categorized findings, and a prioritized action item register with owners and deadlines. Delivered to all phase participants and linked in the project repository.

**On failure**: Report which data or feedback could not be collected, what limited the retrospective scope, and a plan to gather missing input asynchronously.

## Related Skills

- [`velocity-monitor`](../../vp-engineering/velocity-monitor/SKILL.md) -- velocity data feeds into retrospective analysis.
- [`inter-phase-reviewer-eng`](../../tech-lead-pr-reviewer/inter-phase-reviewer-eng/SKILL.md) -- tech lead phase review complements this leadership-level retrospective.
