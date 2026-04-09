---
name: platform-capability-gap-detector
description: >
  This skill identifies missing platform capabilities that block engineering
  productivity or product delivery. Use when asked to audit platform coverage,
  identify what teams are building themselves, or assess platform completeness.
  Also consider when multiple teams report similar blockers. Suggest when the
  user is building a custom solution for a problem the platform should solve.
department: engineering
agent: platform-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../platform-roadmap-aligner/SKILL.md
  - ../golden-path-definer/SKILL.md
  - ../developer-experience-enabler/SKILL.md
triggers:
  - "detect platform gaps"
  - "platform gap analysis"
  - "platform capability audit"
  - "identify platform gaps"
  - "platform capability gaps"
---

# platform-capability-gap-detector

## Agent: Platform Engineer

L2 platform engineer (1x) responsible for detecting capability gaps, aligning the platform roadmap, defining golden paths, enabling developer experience, and preparing for platform scale.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Identifies missing platform capabilities that are blocking engineering productivity or product delivery by analyzing team workarounds, support requests, and infrastructure patterns.

## When to Use

- When multiple engineering teams independently build similar solutions for problems the platform does not address.
- When developer support tickets reveal recurring requests for capabilities that do not exist.
- When product delivery timelines are extended because teams must build infrastructure before features.

## Workflow

1. **Signal Collection**: Gather gap signals from multiple sources: developer surveys, support tickets, architecture reviews, team retrospectives, and infrastructure audit logs. Look for patterns of custom-built solutions and recurring blockers. Deliverable: raw gap signal inventory.
2. **Gap Classification**: Categorize each gap by type (missing capability, insufficient capability, discoverability problem), severity (blocking, slowing, inconvenient), and breadth (one team, multiple teams, all teams). Deliverable: classified gap inventory.
3. **Impact Assessment**: For each gap, estimate the engineering time wasted on workarounds, the number of teams affected, and the risk of the current workaround approach. Prioritize gaps by total impact. Deliverable: prioritized gap list with impact estimates.
4. **Recommendation**: For each high-priority gap, recommend whether the platform team should build the capability, adopt a third-party tool, or document an approved workaround pattern. Deliverable: gap resolution recommendations.

## Anti-Patterns

- **Only listening to the loudest team**: Prioritizing gaps based on which team complains most rather than systematic impact analysis. *Why*: the loudest team may have a niche problem; systematic analysis ensures platform investment helps the most engineers.
- **Treating all workarounds as gaps**: Classifying every team-built solution as a platform gap. *Why*: some solutions are legitimately team-specific; the platform should only absorb capabilities that benefit multiple teams.
- **Gap detection without follow-through**: Identifying gaps and publishing a report without connecting findings to roadmap decisions. *Why*: detection without action erodes trust; teams stop reporting issues if nothing changes.

## Output

**On success**: Produces a prioritized gap inventory with impact estimates and resolution recommendations. Delivered quarterly or triggered by pattern detection.

**On failure**: Report which signal sources could not be accessed, what partial gaps were identified, and recommended alternative data collection methods.

## Related Skills

- [`platform-roadmap-aligner`](../platform-roadmap-aligner/SKILL.md) -- Detected gaps feed directly into platform roadmap prioritization.
- [`golden-path-definer`](../golden-path-definer/SKILL.md) -- Missing golden paths are a common type of capability gap.
