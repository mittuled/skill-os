# Velocity Health Report — Platform Team, Sprint 22

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | VP Engineering |
| Version | 1.0 |
| Status | AT RISK — intervention required |
| Skill | velocity-monitor |

## Executive Summary

Platform Team delivered 38/52 story points (73.1% completion) in Sprint 22, a 17.4% variance below the rolling average of 46. DORA metrics are in the "high" tier overall, which is a mitigating factor. The health status is **AT_RISK** — two consecutive misses require root cause investigation. Primary identified causes: external API dependency blocks and unplanned incident load. Interventions recommended before Sprint 23 planning.

---

## Velocity Health Score

**Composite Score: 66.3 / 100** — AT RISK

| Component | Score | Weight | Contribution |
|---|---|---|---|
| Sprint Velocity | 75 | 40% | 30.0 |
| DORA Average | 81.3 | 60% | 48.8 |
| **Total** | | | **66.3** |

---

## Sprint Metrics

| Metric | Value | Assessment |
|---|---|---|
| Completed Points | 38 | Below plan |
| Planned Points | 52 | — |
| Completion Rate | 73.1% | Below 75% threshold |
| Rolling Average | 46 | Baseline |
| Variance from Average | -17.4% | Significant — risk flag triggered |

---

## DORA Metrics

| Metric | Value | Tier | Score |
|---|---|---|---|
| Deployment Frequency | 2.5/week | HIGH | 75 |
| Lead Time to Change | 18 hours | HIGH | 75 |
| Change Failure Rate | 8% | HIGH | 75 |
| MTTR | 3 hours | HIGH | 75 |
| **DORA Average** | | **HIGH** | **75** |

**Positive signal:** DORA metrics are uniformly in the HIGH tier. The deployment pipeline is healthy. Velocity miss is not caused by engineering process dysfunction — it is an upstream dependency and incident load issue.

---

## Risk Flags

1. **Sprint completion rate 73.1%** — below 75% threshold; this is the second consecutive miss. Trend is statistically significant.
2. **Velocity variance 17.4%** — exceeds the 20% risk threshold; pattern indicates a structural issue, not random noise.

---

## Root Cause Analysis

| Cause | Impact | Evidence |
|---|---|---|
| External API team dependency block | 8+ points undeliverable this sprint | 3 tickets blocked on external API contract finalization |
| Unplanned incident load | ~6 points of capacity consumed | 2 P1 incidents in Sprint 22; MTTR 3h each |
| Combined impact | 14 points (~27% of planned) | Accounts for the full velocity shortfall |

**Assessment:** Velocity miss is fully explained by external blockers and incident load. Team throughput is not degraded — the planning process failed to account for dependency risk and incident reserve.

---

## Recommended Interventions

| Intervention | Owner | Sprint |
|---|---|---|
| Add incident reserve buffer (10–15% of capacity) to Sprint 23 plan | VP Engineering | Sprint 23 |
| Escalate external API dependency block to API team leadership | VP Engineering | This week |
| Adjust Sprint 23 scope to reflect remaining external dependency blocks | Tech Lead | Sprint 23 planning |
| Add sprint retrospective to review two-sprint miss pattern | Team | End of Sprint 22 |

**Next skill to activate:** [`team-allocator`](../team-allocator/SKILL.md) if intervention requires capacity rebalancing.
