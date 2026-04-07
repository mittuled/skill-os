# Framework: effort-estimator-eng

Guides engineering effort estimation using reference-class forecasting, DORA metrics, and structured uncertainty quantification.

## Estimation Method: Reference-Class Forecasting

1. **Identify the reference class**: Find 3-5 historical analogues — past projects with similar technology, scope, and team composition.
2. **Extract base rates**: For each analogue, record actual duration, team size, and notable deviations from plan.
3. **Adjust for differences**: Apply calibration factors for known differences between the analogue and current project.
4. **Produce estimate range**: Use the analogue distribution to generate optimistic (P25), expected (P50), and pessimistic (P75) estimates.

## Complexity Classification

| Level | Characteristics | Typical Range |
|-------|----------------|---------------|
| Simple | Well-understood domain, existing patterns, no external dependencies | 1-3 person-weeks |
| Medium | Some novelty, one external dependency, moderate integration surface | 3-8 person-weeks |
| Complex | Novel technology, multiple external dependencies, high integration surface, regulatory requirements | 8-20 person-weeks |

## Risk Buffer Multipliers

| Risk Level | Multiplier | When to Apply |
|-----------|-----------|---------------|
| Low (1.2x) | 20% buffer | Team has built similar systems before; no external dependencies; stable requirements |
| Medium (1.5x) | 50% buffer | One or two unknowns; some external dependencies; requirements mostly stable |
| High (2.0x) | 100% buffer | Novel technology; multiple unknowns; external dependencies with unclear timelines; volatile requirements |

## DORA Metrics Integration

Use these metrics from the team's recent history to calibrate estimates:

| Metric | Use in Estimation |
|--------|------------------|
| Lead Time for Changes | Baseline for per-task cycle time; if average lead time is 3 days, a 5-point story takes ~3 days |
| Deployment Frequency | Indicates CI/CD maturity; high frequency = lower deployment overhead per task |
| Change Failure Rate | Factor into testing effort; high CFR = add buffer for rework |
| MTTR | Factor into operational readiness tasks; high MTTR = add buffer for observability setup |

## Confidence Interval Format

Every estimate must include three values:

```
Optimistic (P25): [value] person-weeks
Expected (P50):   [value] person-weeks
Pessimistic (P75): [value] person-weeks
Confidence: [Low/Medium/High] based on analogue availability and unknowns count
```

## Common Estimation Traps

| Trap | Mitigation |
|------|-----------|
| Anchoring to deadline | Estimate scope first, compare to deadline second |
| Component-only thinking | Add 30-40% for integration, testing, deployment overhead |
| Ignoring ramp-up | Add 1-2 weeks if team is new to the technology |
| Forgetting documentation | Include 5-10% of total effort for documentation tasks |
| Optimism bias | Use reference class data, not gut feel |
