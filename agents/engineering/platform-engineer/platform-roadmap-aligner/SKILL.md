---
name: platform-roadmap-aligner
description: >
  This skill aligns the platform roadmap with product and engineering roadmaps. Use
  when asked to prioritize platform work, resolve conflicts between platform and
  product timelines, or ensure platform capabilities arrive before teams need them.
  Also consider when product roadmap changes create new platform requirements.
  Suggest when the user is planning product features without platform readiness review.
department: engineering
agent: platform-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../platform-capability-gap-detector/SKILL.md
  - ../platform-scale-preparation/SKILL.md
triggers:
  - "align platform roadmap"
  - "platform roadmap planning"
  - "platform strategy alignment"
  - "roadmap sync"
  - "platform roadmap review"
---

# platform-roadmap-aligner

## Agent: Platform Engineer

L2 platform engineer (1x) responsible for detecting capability gaps, aligning the platform roadmap, defining golden paths, enabling developer experience, and preparing for platform scale.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Aligns the platform roadmap with product and engineering roadmaps to ensure platform capabilities are delivered ahead of the teams that depend on them.

## When to Use

- When the product roadmap shifts and platform dependencies need to be re-evaluated.
- When platform work is being deprioritized in favour of feature work and the gap between platform needs and platform investment is growing.
- When multiple teams are blocked waiting for platform capabilities that are not on the current roadmap.

## Workflow

1. **Dependency Mapping**: Review the product and engineering roadmaps to identify upcoming features that depend on platform capabilities. Map each dependency to its required delivery date (with lead time for integration). Deliverable: platform dependency map with timelines.
2. **Gap Cross-Reference**: Cross-reference the dependency map against the current platform roadmap and the capability gap inventory. Identify mismatches where product needs arrive before platform readiness. Deliverable: alignment gap analysis.
3. **Prioritization Negotiation**: Meet with product and engineering leadership to negotiate priorities. Present the trade-offs: what ships later if platform work is prioritized, what breaks if it is not. Propose a sequencing that minimizes total delivery risk. Deliverable: agreed priority sequence with trade-off documentation.
4. **Roadmap Update**: Update the platform roadmap to reflect agreed priorities. Set milestones with clear delivery dates and integration windows. Communicate the updated roadmap to all dependent teams. Deliverable: updated platform roadmap.

## Anti-Patterns

- **Reactive platform work**: Only starting platform work after a team is blocked, rather than anticipating needs from the roadmap. *Why*: reactive platform work introduces delays into feature delivery; proactive alignment eliminates waiting.
- **Platform roadmap in isolation**: Planning platform work without reference to product and engineering timelines. *Why*: a platform roadmap that does not serve the product roadmap builds capabilities nobody needs yet while missing capabilities teams need now.
- **Avoiding trade-off conversations**: Accepting all platform requests without discussing what will be delayed. *Why*: platform capacity is finite; accepting everything without trade-offs means nothing ships on time.

## Output

**On success**: Produces an aligned platform roadmap with dependency maps, agreed priorities, and communicated milestones. Delivered quarterly with monthly check-ins.

**On failure**: Report which dependencies could not be resolved, what conflicts remain between platform and product timelines, and recommended escalation to engineering leadership.

## Related Skills

- [`platform-capability-gap-detector`](../platform-capability-gap-detector/SKILL.md) -- Detected gaps are a primary input to roadmap alignment.
- [`platform-scale-preparation`](../platform-scale-preparation/SKILL.md) -- Scale preparation work competes for roadmap slots and must be balanced with feature-enabling work.
