# Performance Test Report — /api/search

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | QA Test Engineer |
| Endpoint | /api/search |
| Verdict | FAIL |
| Skill | performance-tester |

## Recommendation

**Release blocked** — 1 budget violation: p95_latency_ms: 380ms vs budget 250ms (+52.0%). The p95 tail latency regression must be investigated and resolved before release.

---

## Budget vs. Measured

| Metric | Budget | Measured | Status | Delta |
|---|---|---|---|---|
| P50 Latency | 80ms | 65ms | PASS | -18.8% |
| P95 Latency | 250ms | **380ms** | **FAIL** | +52.0% |
| P99 Latency | 800ms | 750ms | PASS | -6.3% |
| Throughput | 300 rps | 340 rps | PASS | +13.3% |
| Error Rate | 0.5% | 0.2% | PASS | -60% |

---

## Regression Analysis

**P95 latency increased 52% vs previous baseline.** Context: likely due to missing query cache warm-up. Cold-cache requests are hitting the database directly, inflating p95.

**Diagnosis steps:**
1. Compare p95 latency distribution between warm and cold cache scenarios
2. Check if the new index has a pre-warming step configured
3. Review slow query log for p95+ requests — identify the slowest query patterns

**Recommended fix:** Add cache pre-warm step to deployment runbook; configure index warming on startup.

---

## Verdict

**FAIL — Release is blocked.**

The p95 latency violation represents a significant tail latency regression affecting the worst-served 5% of search users. For a 300 rps endpoint, approximately 15 users per second would experience 380ms+ latency vs. the 250ms budget.
