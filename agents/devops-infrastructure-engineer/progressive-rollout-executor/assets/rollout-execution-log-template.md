# Progressive Rollout Execution Log: [Service / Feature Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Executor | DevOps / Infrastructure Engineer |
| Service | [Service name] |
| Release | [Version / Git SHA] |
| Strategy | [Canary / Blue-Green / Ring-based / Feature flag] |
| Skill | progressive-rollout-executor |
| Status | [In Progress / Complete / Rolled Back] |

## Rollout Plan Summary

| Stage | Traffic % | Bake Time | Promotion | Success Criteria |
|-------|-----------|-----------|-----------|-----------------|
| Stage 1 | 1% | 30 min | Manual | Error rate ≤ 0.1%, p99 ≤ [X ms] |
| Stage 2 | 10% | 30 min | Manual | Same |
| Stage 3 | 25% | 60 min | Manual | Same |
| Stage 4 | 50% | 60 min | Automated | Same |
| Stage 5 | 100% | 30 min (soak) | Automated | Same |

**Rollback trigger**: Error rate > 1% OR p99 > [2×X ms] OR any manual judgment call

## Baseline Metrics (Pre-Rollout)

Captured at [YYYY-MM-DD HH:MM UTC] from production with 100% old version:

| Metric | Baseline Value | Alert Threshold |
|--------|---------------|----------------|
| Error rate | [X%] | > [X+0.5]% |
| p50 latency | [X ms] | > [1.5×X] ms |
| p99 latency | [X ms] | > [2×X] ms |
| Request rate | [X req/sec] | < [0.7×X] req/sec (traffic drop) |
| Business metric (e.g., checkout rate) | [X%] | < [X-2]% |

---

## Execution Log

### Stage 1 — 1% Traffic

**Started**: [YYYY-MM-DD HH:MM UTC]
**Completed**: [YYYY-MM-DD HH:MM UTC]
**Duration**: [X min]

| Metric | During Bake | vs. Baseline | Status |
|--------|------------|-------------|--------|
| Error rate | [X%] | [+/-X%] | [Green/Red] |
| p99 latency | [X ms] | [+/-X ms] | [Green/Red] |
| p50 latency | [X ms] | [+/-X ms] | [Green/Red] |
| Business metric | [X%] | [+/-X%] | [Green/Red] |

**Observations**: [Any notable events, anomalies, or early signals during bake]
**Promotion decision**: [Promoted / Rolled back]
**Decision by**: [Name] at [HH:MM UTC]

---

### Stage 2 — 10% Traffic

**Started**: [YYYY-MM-DD HH:MM UTC]
**Completed**: [YYYY-MM-DD HH:MM UTC]

| Metric | During Bake | vs. Baseline | Status |
|--------|------------|-------------|--------|
| Error rate | | | |
| p99 latency | | | |
| Business metric | | | |

**Observations**:
**Promotion decision**: [Promoted / Rolled back]

---

### Stage 3 — 25% Traffic

[Repeat structure]

---

### Stage 4 — 50% Traffic

[Repeat structure]

---

### Stage 5 — 100% Traffic

[Repeat structure]

---

## Final Status

**Outcome**: [Rollout complete / Rolled back at Stage N]
**Total duration**: [X hours Y minutes]
**100% traffic to new version at**: [YYYY-MM-DD HH:MM UTC]

## Post-Rollout Validation

- [ ] Error rate stable at 100% for 30+ minutes
- [ ] All key metrics within SLO
- [ ] No P1/P2 alerts fired post-rollout
- [ ] Business metrics nominal (conversion rate, order rate, etc.)
- [ ] Old version instances fully drained and removed
- [ ] Feature flag cleanup scheduled (if applicable)

## Rollback Record (if applicable)

**Rollback trigger**: [Metric threshold breached / Manual decision — reason]
**Rollback initiated**: [YYYY-MM-DD HH:MM UTC]
**Rollback complete**: [YYYY-MM-DD HH:MM UTC]
**MTTR**: [X minutes]
**Users affected**: [Estimated N users during partial rollout]
**Incident ticket**: [Link]
**Post-mortem required**: [Yes / No]
