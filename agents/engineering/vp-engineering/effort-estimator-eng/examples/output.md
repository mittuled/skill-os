# Effort Estimate — Multi-Tenant Architecture

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Risk Level | High (2x buffer) |
| Expected Sprints | 6.9 |
| Confidence Interval | 3.4–9.7 sprints |
| Skill | effort-estimator-eng |

## Summary

Total base estimate: 84 story points. With high-risk 2x buffer: 168 points. At 35 points/sprint velocity, expected delivery is 6.9 sprints (~14 weeks). High confidence interval (3.4–9.7 sprints) reflects external Stripe dependency uncertainty.

## Work Stream Breakdown

| Work Stream | Complexity | Base Points | Adjusted Points | Notes |
|---|---|---|---|---|
| Tenant isolation in data layer | Complex | 20 | 50 | Schema partitioning, row-level security |
| Billing per-tenant integration | Complex | 15 | 38 | Depends on Stripe billing API |
| Tenant-scoped authentication | Medium | 10 | 15 | |
| Tenant admin UI | Medium | 8 | 12 | |
| **Total** | | **53** | **115** | |

## Estimate Summary

| Metric | Value |
|---|---|
| Base Points | 115 |
| Risk Buffer | 2x (high) |
| Buffered Points | 168 |
| Sprints Expected | 6.9 |
| Confidence Interval | 3.4–9.7 sprints |

## Recommendation

Do not commit to a fixed 14-week deadline. Communicate to stakeholders as "12–20 week range, targeting 14 weeks." The external Stripe integration is the primary uncertainty driver — consider running a technical spike in Sprint 1 to reduce estimate variance before committing to a delivery date.
