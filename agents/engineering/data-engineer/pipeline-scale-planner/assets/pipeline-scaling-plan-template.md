# Pipeline Scaling Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Approved] |
| Skill | pipeline-scale-planner |
| Pipeline Name | [pipeline-name] |

## Executive Summary

[2-3 sentences stating the projected SLA breach date, the recommended scaling intervention, and the expected cost delta.

GUIDANCE: Lead with the urgency. Example: "At the current 15% MoM growth rate, this pipeline will breach its 2-hour SLA window in approximately 47 days. The recommended intervention is switching from full-reload to CDC-based incremental extraction, which reduces processing volume by ~85% and extends SLA compliance by an estimated 18+ months at a net infrastructure cost reduction of $200/month."]

**SLA breach projection:** [N days / Estimated date]
**Recommended intervention:** [Strategy name]
**Cost delta:** [+/−$X/month]

## Current State Baseline

[Observed pipeline performance metrics.

GUIDANCE:
- Good: Table with measured throughput, resource utilization, and execution duration over the past 30 days.
- Bad: Estimated values without measurement evidence.
- Format: Table with P50/P95 statistics.]

| Metric | P50 | P95 | Max (30d) | Trend | Source |
|--------|-----|-----|-----------|-------|--------|
| Pipeline duration (min) | [N] | [N] | [N] | [+X%/month] | [Orchestrator logs] |
| Rows processed / run | [N] | [N] | [N] | [+X%/month] | [Pipeline metrics] |
| Throughput (rows/sec) | [N] | [N] | [N] | [stable / declining] | [Pipeline metrics] |
| CPU utilization (%) | [N] | [N] | [N] | [trend] | [Infrastructure metrics] |
| Memory utilization (%) | [N] | [N] | [N] | [trend] | [Infrastructure metrics] |

## Growth Forecast

[Projected volume growth and SLA breach timeline.

GUIDANCE:
- Good: Projections with explicit growth rate source (historical trend vs. business plan) and breach date calculation.
- Bad: "Volume will grow as the business grows."
- Format: Table with quarterly projections + breach date.]

**Growth rate assumption:** [X% MoM / X% QoQ] — source: [Historical trend from last N months / Business plan FY2026]

| Period | Projected Daily Volume | Estimated Pipeline Duration | SLA Window | Status |
|--------|----------------------|--------------------------|---------|----|
| Today | [N rows] | [N min] | [N min] | Within SLA |
| +30 days | [N rows] | [N min] | [N min] | [Within / At limit / Breach] |
| +60 days | [N rows] | [N min] | [N min] | [Within / At limit / Breach] |
| +90 days | [N rows] | [N min] | [N min] | [Within / At limit / Breach] |

**Projected SLA breach date:** [YYYY-MM-DD] ± [N days confidence interval]

## Bottleneck Analysis

[Root cause of the scaling limit.

GUIDANCE:
- Good: Flamegraph or execution plan evidence identifying the specific task and step causing the bottleneck.
- Bad: "The pipeline is slow."
- Format: One paragraph per bottleneck with evidence.]

**Primary bottleneck:** [Layer: Extract / Transform / Load] — [Type: I/O / CPU / Memory / SQL]

**Evidence:**
- [Execution plan screenshot / timing breakdown showing where time is spent]
- [Profiler output showing spill-to-disk / GC overhead / rate limiting]

**Root cause:** [Explanation linking the evidence to the bottleneck classification]

## Scaling Strategy Options

[Evaluated interventions with cost-benefit analysis.

GUIDANCE:
- Good: At least 2 options evaluated; each has SLA extension estimate, cost delta, effort, and recommendation rationale.
- Bad: Only one option presented with no alternatives.
- Format: Table + narrative on chosen option.]

| Option | SLA Extension | Cost Delta | Engineering Effort | Reversible? | Debt Risk |
|--------|-------------|-----------|-------------------|------------|---------|
| [Option A] | [+N months] | [+/−$X/mo] | [N days] | [Yes/No] | [Low/Med/High] |
| [Option B] | [+N months] | [+/−$X/mo] | [N days] | [Yes/No] | [Low/Med/High] |
| **Recommended: [Option N]** | [+N months] | [+/−$X/mo] | [N days] | [Yes/No] | [Low/Med/High] |

**Recommendation rationale:** [Why the recommended option has the best SLA extension / cost ratio]

## Implementation Plan

[High-level steps to implement the recommended scaling strategy.

GUIDANCE:
- Good: Numbered steps with owners and sequencing dependencies.
- Bad: "Implement the scaling strategy."
- Format: Numbered list with owners.]

1. [Step 1] — Owner: [name] — Duration: [N days]
2. [Step 2] — Owner: [name] — Duration: [N days]
3. [Step 3 — validation/cutover] — Owner: [name] — Duration: [N days]

## Validation Test Plan

[How to confirm the scaling strategy works before full production cutover.

GUIDANCE:
- Good: Specific test types, pass criteria, and rollback trigger.
- Bad: "We'll test it."
- Format: Table.]

| Test Type | Method | Pass Criteria | Rollback Trigger |
|-----------|--------|--------------|----------------|
| Load test | Run against [N×] volume test dataset | Completes in ≤ [N min] | Duration > [N min] |
| Data quality check | Compare row counts and aggregates vs. old pipeline | Match within 0.1% | Any row count discrepancy > 0.5% |
| Canary deployment | Route [X%] of runs to new pipeline | No quality regressions | Any data quality failure |

## Recommendations

[Prioritized decisions and next steps.

GUIDANCE:
- P1: Approve and begin implementation before [breach date − 30 days].
- P2: Monitoring enhancements to detect the next bottleneck before it becomes urgent.
- P3: Architectural improvements to pipeline design to reduce future scaling frequency.]

## Appendices

### A. Methodology

[Profiling tools used, execution plan sources, growth rate calculation method, and SLA breach projection formula.]

### B. Supporting Data

[Raw execution time trends (30-day chart), profiler output, volume growth data, infrastructure cost breakdown before and after.]
