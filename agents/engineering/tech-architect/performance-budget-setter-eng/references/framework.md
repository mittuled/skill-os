# Framework: performance-budget-setter-eng

Defines the methodology for setting quantitative performance budgets that engineering teams build and test against.

## Budget Category Model

### Latency Budgets
Specify all percentiles — median alone hides tail behavior:

| Percentile | Purpose | Typical Targets |
|-----------|---------|-----------------|
| p50 | Typical user experience | < 50ms (API), < 100ms (page load) |
| p95 | Most-user experience | < 200ms (API), < 500ms (page load) |
| p99 | Edge-case bound | < 1s (API), < 2s (page load) |
| p99.9 | SLA cliff | < 5s (API), define per SLA |

Always set budgets for both **happy path** and **cold start** (first request after scale-up or cache miss).

### Throughput Budgets
| Metric | Definition | How to Set |
|--------|-----------|------------|
| Baseline RPS | Normal operating load | Measure P90 of last 30 days |
| Peak RPS | Expected burst (marketing events, month-end) | Baseline × peak multiplier (typically 3–10×) |
| Target capacity | What infrastructure must handle | Peak RPS × 1.5 safety margin |

### Resource Budgets
| Resource | Budget Metric | Trigger for Review |
|----------|--------------|-------------------|
| Memory | Max RSS per instance (MB) | Exceeds budget by > 10% |
| CPU | Avg CPU % at baseline load | > 60% avg suggests over-utilized |
| Payload size | Max request/response body (KB) | > 100KB for API, > 1MB for file upload endpoint |
| Bundle size | JS bundle (gzip, KB) | > 50KB initial, > 250KB total (web) |
| DB query time | Max allowed per query (ms) | p99 > 100ms triggers slow-query review |

## Baseline Collection Protocol

Before setting any budget, measure current performance:
1. **Identify measurement points**: API gateway logs, APM traces, RUM data, synthetic monitors
2. **Collect for 14+ days**: Capture weekly patterns and weekday/weekend variation
3. **Remove anomalies**: Exclude deploy windows, incidents, and known outlier periods
4. **Record the baseline table**:

| Endpoint / Component | p50 | p95 | p99 | Peak RPS | Error Rate |
|---------------------|-----|-----|-----|----------|------------|
| `GET /api/resource` | — | — | — | — | — |

## Budget Setting Process

### Step 1: Anchor to User Expectations
| User expectation | Latency target |
|-----------------|---------------|
| "Instant" (search, autocomplete) | p99 < 100ms |
| "Fast" (page navigation) | p99 < 500ms |
| "Acceptable" (form submit, save) | p99 < 2s |
| "Background" (export, report) | p99 < 30s; show progress |

### Step 2: Work Backwards from Budget
If the UI target is p99 < 500ms end-to-end:
- Browser render: 50ms
- Network RTT: 50ms
- API gateway overhead: 20ms
- Service budget: **380ms** (where engineering focuses)
- Database budget: 150ms of the service budget

### Step 3: Feasibility Check
Before publishing targets, verify with engineering leads:
- [ ] Can the current architecture achieve the target without a rewrite?
- [ ] Does the database schema support the query patterns at target RPS?
- [ ] Are infrastructure scaling limits documented (max DB connections, instance limits)?
- [ ] Are the targets achievable within the delivery timeline?

## Monitoring and Alerting Mapping

Every budget line must map to an alert:

| Budget | Alert Threshold | Severity | Action |
|--------|----------------|----------|--------|
| p99 latency | > budget × 1.2 | Warning | Notify on-call |
| p99 latency | > budget × 1.5 | Critical | Page on-call |
| Error rate | > 1% | Warning | Notify on-call |
| Error rate | > 5% | Critical | Page + incident |
| Peak RPS | > 80% capacity | Warning | Trigger scale-out |
