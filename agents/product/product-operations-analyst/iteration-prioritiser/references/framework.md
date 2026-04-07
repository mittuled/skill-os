# Framework: Iteration Prioritisation

## Core Model

Iteration prioritisation ranks the next set of product changes by weighing multi-source signal against business impact, using a structured scoring model that prevents any single stakeholder's voice from dominating the backlog.

## Signal Sources to Synthesise

Before scoring, collect signal from:
1. **Usage data**: Feature-level engagement, funnel drop-off, session replays
2. **Support tickets**: Volume-weighted issues from the past 2 sprints
3. **Customer feedback**: NPS verbatims, CS check-in themes, beta programme findings
4. **Sales signals**: Objections raised, lost deal reasons, feature gap mentions
5. **Revenue data**: Upgrade/downgrade events correlated with feature usage
6. **Technical debt signals**: Engineering-raised performance or stability issues

Signal is only actionable when at least 2 independent sources point to the same issue.

## Scoring Model (ICE-S)

Score each candidate item on four dimensions (1-10 each):

| Dimension | Question | Scoring Guide |
|-----------|---------|--------------|
| **Impact** | How much will fixing/building this move the primary metric? | 10 = direct primary metric impact; 1 = cosmetic or edge-case only |
| **Confidence** | How certain are we that this will have the stated impact? | 10 = data-confirmed; 5 = strong hypothesis; 1 = gut feel |
| **Effort** | How much engineering effort is required? | 10 = trivial (<1 day); 1 = multi-sprint epic |
| **Signal Strength** | How many independent sources point to this item? | 10 = 5+ sources; 7 = 3-4 sources; 4 = 2 sources; 1 = single source |

**ICE-S Score** = (Impact × Confidence × Effort × Signal Strength) / 1000

## Priority Tiers

| Tier | ICE-S Range | Decision |
|------|------------|---------|
| P0 – Must do this sprint | > 5.0 | Commit immediately |
| P1 – Should do this sprint | 3.0–5.0 | Include if capacity allows |
| P2 – Next sprint candidate | 1.5–3.0 | Groom and size; schedule next cycle |
| P3 – Backlog | < 1.5 | Document; revisit at quarterly planning |

## Tie-breaking Rules

When two items score within 0.5 points of each other, prefer:
1. The item with higher **customer severity** (blocking > friction > nice-to-have)
2. The item that unblocks another high-priority item
3. The item requested by a higher-risk customer segment (enterprise churn risk > SMB feature request)

## Constraints to Apply Before Finalising

- Capacity constraint: Total P0 + P1 items must fit within 80% of sprint capacity
- Dependency constraint: Sequence items so prerequisites are scheduled before dependents
- Balance constraint: No more than 60% of the sprint on any single theme (e.g., not all bug fixes)

## Exclusion Rules

Exclude items from the scored list if:
- They lack a clear acceptance criterion (cannot score Impact reliably)
- They are already in progress and not at risk of deprioritisation
- They require external dependencies that are not yet resolved
