# Framework: Platform Roadmap Alignment

Reference for aligning the platform engineering roadmap with product engineering needs, business priorities, and technical strategy.

## Platform Roadmap Principles

| Principle | Description | Anti-Pattern |
|-----------|-------------|-------------|
| Demand-driven | Roadmap items must be traceable to engineering team needs | Building platform capabilities nobody has asked for |
| Multiplier focus | Prioritize capabilities that multiply productivity across all teams | Single-team optimizations |
| Graduated rollout | Introduce capabilities to 1 team first, then expand | Big-bang platform launches |
| Outcome-measured | Each item has a measurable outcome target before it enters the roadmap | Roadmap items measured by delivery (not impact) |
| Sustainable pace | Platform team reserves 20–30% capacity for unplanned engineering needs | 100% roadmap utilization leaves no headroom |

## Roadmap Alignment Process

### Quarterly Cycle

| Phase | Activities | Owner | Timing |
|-------|-----------|-------|--------|
| Demand gathering | Survey engineering teams; analyze support tickets; review postmortems | Platform Lead | 6 weeks before quarter start |
| Gap analysis | Run platform-capability-gap-detector; rank by impact and effort | Platform Engineer | 4 weeks before quarter start |
| Roadmap draft | Propose roadmap items; map to engineering team priorities | Platform Lead | 3 weeks before quarter start |
| Alignment review | Review with engineering leads and VP Engineering | Platform Lead + VP Eng | 2 weeks before quarter start |
| Roadmap publish | Announce to all engineering teams; update developer portal | Platform Lead | 1 week before quarter start |
| Mid-quarter check | Validate delivery progress; adjust if demand changes | Platform Lead | Mid-quarter |

### Demand Signal Sources

| Source | Frequency | Signal Type | Weight |
|--------|-----------|------------|--------|
| Quarterly developer survey | Quarterly | Friction points, tool satisfaction | High |
| Support ticket analysis | Monthly | Specific platform gaps | High |
| Postmortem review | After each incident | Platform-related root causes | High |
| Engineering lead interviews | Quarterly | Strategic needs, upcoming projects | Medium |
| Industry benchmarks (DORA, SPACE) | Semi-annually | Capability maturity gaps | Medium |
| Platform team observation | Continuous | Toil, repeated requests | Low-Medium |

## Roadmap Item Classification

Every roadmap item is classified before entering the backlog:

| Classification | Description | Max % of Roadmap |
|---------------|-------------|-----------------|
| Foundation | Enables multiple other capabilities; high leverage | 20–30% |
| Capability | Direct productivity improvement for engineering teams | 40–50% |
| Maintenance | Keeps existing platform healthy; prevents debt | 15–20% |
| Exploratory | Proof of concept for future capability | 5–10% |

## Alignment Decision Framework

When demand exceeds capacity, use this prioritization:

| Factor | Weight | How to Score |
|--------|--------|-------------|
| Number of teams impacted | 30% | 1–5 (1 = 1 team, 5 = all teams) |
| Severity of pain (incidents caused or blocked work) | 30% | 1–5 (1 = minor friction, 5 = production incidents) |
| Strategic alignment (supports OKRs) | 20% | 1–5 |
| Effort to deliver | 20% (inverse) | 5 = small, 1 = very large |

**Priority score** = Weighted sum. Items scoring > 4.0 enter the roadmap; 3.0–4.0 are candidates; < 3.0 are deferred.

## Roadmap Communication Template

For each quarter, communicate to all engineering teams:

```
Platform Engineering Roadmap — Q[N] YYYY

DELIVERING THIS QUARTER:
1. [Capability name] — enables [specific benefit] for [teams] — ships [month]
2. [Capability name] — enables [specific benefit] — ships [month]

NOT DELIVERING (with reasoning):
1. [Requested item] — deferred because [reason: lower priority than X / effort too large / dependency on Y]

FEEDBACK: Reach us at [#platform-eng channel] or file a request at [link]
```

## Cross-Team Dependency Management

Platform capabilities often depend on or affect product engineering teams:

| Dependency Type | Example | Resolution |
|----------------|---------|-----------|
| Platform needs product team changes | Adoption of new secrets API requires teams to update their config | Provide migration guide + 90-day grace period |
| Product team blocked on platform | Teams cannot scale without new infra capability | Escalate to VP Engineering; accelerate roadmap item |
| Shared timeline | Platform capability and product feature must ship together | Joint planning session; shared milestone |

## Success Metrics for Roadmap Alignment

| Metric | Target | How to Measure |
|--------|--------|---------------|
| Roadmap predictability | ≥ 80% of committed items delivered on time | Quarterly retrospective |
| Engineering satisfaction with platform | ≥ 4.0/5.0 | Quarterly developer survey |
| Unplanned platform work | ≤ 20% of capacity | Capacity tracking |
| Time from demand signal to roadmap item | ≤ 1 quarter | Ticket creation date vs. roadmap date |
| Platform capability adoption | ≥ 80% of target teams using within 1 quarter of launch | Adoption tracking |
