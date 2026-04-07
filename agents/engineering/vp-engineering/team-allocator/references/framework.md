# Framework: team-allocator

Defines the methodology for matching engineering capacity to delivery requirements across projects and phases.

## Capacity Model

### Effective Capacity Calculation

Raw headcount is not engineering capacity. Use the effective capacity model:

```
Effective capacity (days) = Working days × (1 - overhead rate)
```

| Overhead Component | Typical Rate | Notes |
|-------------------|-------------|-------|
| Meetings, standups, planning | 10–15% | Higher for leads and managers |
| Code review and PR feedback | 5–10% | Higher for senior engineers on larger teams |
| Unplanned work (bugs, incidents, support) | 10–15% | Higher post-launch; lower for greenfield work |
| Onboarding and context switching | 0–20% | 20% for first 2 weeks on a new project |
| **Total overhead** | **25–35%** | Target allocation at 65–75% of working days |

**Target utilization**: 70% of effective capacity. Allocating > 80% creates fragility.

### Utilization Bands

| Utilization | Status | Implication |
|-------------|--------|------------|
| < 50% | Under-utilized | Capacity available for new work or investment in tech debt/tests |
| 50–70% | Healthy | Team has capacity for unplanned work and cross-training |
| 70–80% | Target | Optimal balance of output and resilience |
| 80–90% | Stretched | Vulnerable to schedule slip on any interruption |
| > 90% | Over-committed | Guaranteed to miss commitments when anything goes wrong |

## Skill Profile Taxonomy

Categorize engineers along three dimensions for accurate matching:

### Technical Stack
- Backend (languages: Go / Python / Java / Ruby / etc.)
- Frontend (frameworks: React / Vue / Angular / etc.)
- Full-stack
- Infrastructure / DevOps (cloud: GCP / AWS / Azure; tooling: Terraform / K8s)
- Data / ML engineering
- Mobile (iOS / Android / Flutter)

### Domain Knowledge
- Business domain expertise (payments, auth, search, etc.) — takes months to build
- System familiarity (knows the codebase, APIs, data models) — takes weeks to build
- New to domain/system — requires onboarding overhead (20% capacity reduction for 2 weeks)

### Seniority Level
- Junior (L1): requires pairing or close review; estimate × 1.5 for effort
- Mid (L2): self-sufficient on known tasks; estimate × 1.0
- Senior (L3): accelerates adjacent work; provides review and design input; estimate × 0.8 for well-scoped tasks

## Key-Person Risk Assessment

A workstream has key-person risk when:
- One engineer owns > 60% of the work in that area
- No other engineer can review their code for correctness
- Their absence would stall the workstream with no available backup

### Mitigation Strategies by Urgency

| Timeframe | Mitigation |
|-----------|-----------|
| Immediate (< 1 week) | Pair the key person with a backup; require dual-engineer review for critical path code |
| Near-term (1–4 weeks) | Schedule knowledge transfer sessions; create written documentation of critical system knowledge |
| Medium-term (1–3 months) | Cross-train a backup engineer on the domain; rotate code ownership |
| Long-term | Hire or develop a second expert; architect the system to reduce single-engineer ownership surface |

## Rebalancing Triggers

Reassess allocations immediately when:
- An engineer leaves or goes on extended leave
- Velocity data shows a team is > 30% over or under its planned output for 2+ sprints
- A new high-priority project requires resource from an existing allocation
- An integration dependency shifts the critical path to a different workstream
- An engineer's utilization exceeds 85% for more than one sprint

## Allocation Review Cadence

| Review | Frequency | Scope |
|--------|----------|-------|
| Sprint planning review | Every sprint | Confirm allocations match sprint tasks; catch capacity drift |
| Phase kickoff review | Start of each phase | Full reallocation review against phase effort estimates |
| Quarterly capacity review | Every quarter | Team headcount, skill gaps, hiring plan alignment |
| Ad-hoc rebalance | As triggered | Triggered by rebalancing conditions above |
