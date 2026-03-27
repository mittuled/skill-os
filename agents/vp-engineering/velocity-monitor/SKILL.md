---
name: velocity-monitor
description: >
  This skill monitors team velocity against plan and flags delivery risks early. Use when asked to
  track engineering throughput, assess sprint performance, or identify delivery slowdowns. Also
  consider when DORA metrics trend negatively. Suggest when a team has missed commitments in
  two consecutive sprints without investigation.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../vp-engineering/inter-phase-retrospective/SKILL.md
  - ../../vp-engineering/team-allocator/SKILL.md
---

# velocity-monitor

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Monitors team velocity against planned commitments and flags delivery risks using DORA metrics, sprint data, and burndown trends.

## When to Use

- When a sprint ends and actual velocity needs to be compared against planned commitments.
- When DORA metrics (lead time, deployment frequency, change failure rate, MTTR) show negative trends.
- When stakeholders request a delivery health assessment mid-phase.

## Workflow

1. **Collect metrics**: Gather sprint velocity (points completed vs. planned), cycle time, lead time, deployment frequency, change failure rate, and MTTR from the project management and CI/CD tools. Deliverable: raw metrics dashboard.
2. **Trend analysis**: Compare current metrics against the rolling average (last 4-6 sprints). Identify statistically significant deviations. Deliverable: trend report with variance flags.
3. **Root cause investigation**: For flagged deviations, investigate contributing factors -- scope changes, dependency blocks, tech debt, team changes, incident load. Deliverable: root cause annotations.
4. **Risk projection**: Project current velocity trends forward to assess impact on milestone and phase deadlines. Identify at-risk deliverables. Deliverable: risk projection with affected milestones.
5. **Recommend interventions**: Propose corrective actions -- reallocation, scope adjustment, tech debt sprint, process change. Deliverable: intervention recommendations with expected impact.

## Anti-Patterns

- **Velocity as a target**: Using velocity as a performance metric that teams are pressured to increase. *Why*: when velocity becomes a target, teams inflate estimates rather than improve throughput, destroying the metric's diagnostic value.
- **Ignoring leading indicators**: Waiting for missed milestones instead of monitoring leading indicators like cycle time and WIP count. *Why*: lagging indicators confirm problems too late for low-cost intervention.
- **Metric without context**: Reporting numbers without investigating why they changed. *Why*: raw metrics without root cause analysis lead to wrong interventions.

## Output

**On success**: Produces a velocity health report containing current metrics, trend analysis, root cause annotations for deviations, risk projections, and intervention recommendations. Delivered to engineering leadership at sprint boundaries.

**On failure**: Report which metrics could not be collected (e.g., missing CI/CD integration, incomplete sprint tracking), the impact on monitoring coverage, and what tooling changes are needed.

## Related Skills

- [`inter-phase-retrospective`](../../vp-engineering/inter-phase-retrospective/SKILL.md) -- velocity data is a key input to retrospective analysis.
- [`team-allocator`](../../vp-engineering/team-allocator/SKILL.md) -- velocity trends may trigger reallocation decisions.
