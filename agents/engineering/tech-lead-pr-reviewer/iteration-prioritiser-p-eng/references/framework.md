# Framework: iteration-prioritiser-p-eng

Defines the methodology for prioritising post-launch engineering iterations using production signals, business impact, and capacity constraints.

## Signal Aggregation Model

### Signal Sources

| Source | Signal Type | Collection Cadence |
|--------|------------|-------------------|
| APM / Error tracking (e.g., Sentry, Datadog) | Production bugs, p99 latency, error rates | Real-time + weekly digest |
| Support ticket system | User-reported bugs, friction points, feature requests | Weekly triage |
| Customer success escalations | Retention-risk issues, committed feature gaps | As they arise |
| Product analytics (funnels, retention) | Feature adoption, drop-off points, engagement regressions | Weekly |
| On-call incident log | Reliability issues, MTTR, repeat incidents | Per sprint |
| Tech debt register | Compounding slowdowns, architectural risks | Per sprint |

### Signal Classification

| Category | Definition | Priority Tier |
|----------|-----------|--------------|
| **Production Bug** | Functionality deviates from specification or causes data loss/errors in production | P1 by default; downgrade to P2 if < 1% of users affected and workaround exists |
| **Performance Regression** | p95 or p99 latency exceeds the published performance budget post-launch | P1 if SLA breach; P2 if within SLA but trending toward breach |
| **SLA Violation** | Uptime or latency commitments to customers are not being met | P1 — escalate to customer success immediately |
| **Tech Debt** | Accumulated shortcuts slowing engineering velocity or increasing incident risk | P2 — schedule at minimum one tech debt item per iteration |
| **Feature Enhancement** | Improvement to existing functionality based on usage data | P3 — schedule after stability items |

## Production Impact Scoring

### Impact Score (1–10) for Post-Launch Signals

| Score | Definition | Signals |
|-------|-----------|---------|
| 9–10 | Revenue loss, SLA breach, or data integrity risk | Confirmed revenue impact; customer on churn risk; P1 incident recurrence |
| 7–8 | Core workflow degraded for significant user population | > 10% of active users affected; support ticket spike; conversion drop > 5% |
| 5–6 | Secondary workflow affected; workaround available | 2–10% of users affected; occasional user report; < 5% conversion impact |
| 3–4 | Edge case or power user impact | < 2% of users affected; low support volume; no revenue signal |
| 1–2 | Cosmetic or preference-based | No user impact; internal tooling improvement; optional quality-of-life |

### Stability Weight Override

For post-launch prioritisation, apply a stability multiplier before ranking:

| Item Type | Multiplier | Rationale |
|-----------|-----------|-----------|
| P1 Production Bug | × 2.0 | User trust and SLA depend on immediate resolution |
| SLA Violation | × 2.5 | Customer contract obligation |
| P99 Latency Breach | × 1.5 | Compounding impact if unaddressed |
| Tech Debt (compounding) | × 1.2 | Compounding velocity tax if deferred |
| Enhancement | × 0.8 | Deprioritised relative to stability |

**Final Score** = (Impact ÷ Effort) × Multiplier

## Iteration Composition Rules

Every post-launch iteration must include:
1. **At minimum one production stability item** (bug fix or performance improvement) — no exceptions
2. **At minimum one tech debt item** — unless the P1 bug backlog exceeds iteration capacity
3. **No more than 50% of capacity on enhancements** — unless zero stability or tech debt items remain

## DORA Metrics Baseline

Use DORA metrics to contextualize prioritisation decisions:

| Metric | Definition | Elite Benchmark | How It Affects Prioritisation |
|--------|-----------|----------------|-------------------------------|
| Deployment Frequency | How often code deploys to production | Multiple times/day | Low frequency → prioritise CI/CD improvements |
| Lead Time for Changes | Commit to production time | < 1 hour | High lead time → prioritise build/review process improvements |
| Change Failure Rate | % deploys causing incidents | < 5% | High CFR → prioritise test coverage and canary tooling |
| MTTR | Time to restore service after incident | < 1 hour | High MTTR → prioritise runbook and observability improvements |

## Stakeholder Input Integration

Before finalising iteration scope, gather:
1. **Customer success**: Any customers on churn risk requiring specific fixes?
2. **Product**: Any committed roadmap items or public release date dependencies?
3. **Engineering leadership**: Any architectural items that unblock a future quarter's work?

Document all stakeholder inputs and how they were weighted. If a stakeholder request overrides the data-driven ranking, document the exception and rationale.
