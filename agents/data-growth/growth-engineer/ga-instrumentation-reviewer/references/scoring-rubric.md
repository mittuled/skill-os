# Scoring Rubric: ga-instrumentation-reviewer

Evaluates whether growth instrumentation is complete and verified before a product reaches general availability, covering event coverage, dashboard readiness, and A/B test infrastructure.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Critical Event Coverage | 35% | Signup, activation, and revenue events are instrumented, verified, and flowing in staging |
| 2 | Growth Dashboard Readiness | 25% | Every metric on the growth dashboard has a working data source with correct values |
| 3 | Full Funnel Instrumentation | 25% | All acquisition, onboarding, and retention events are instrumented and verified |
| 4 | A/B Test Infrastructure | 15% | Experiment framework is instrumented with standard event schema and variant assignment works |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All events verified, all dashboard metrics live, A/B test infrastructure confirmed end-to-end | Approve GA; no instrumentation blockers |
| A | 8.0 – 8.9 | Strong | All critical events verified; dashboard operational; minor non-critical event gaps | Approve GA with post-launch instrumentation work logged |
| B | 7.0 – 7.9 | Good | Critical events verified; 1–2 non-critical dashboard metrics delayed; A/B test infrastructure ready | Approve GA with conditions; log gaps; fix within 2 weeks post-launch |
| C | 5.0 – 6.9 | Adequate | All critical events present but 1 not yet verified in staging; dashboard incomplete for key AARRR stage | Delay GA 2–3 days to close critical gaps; re-review |
| D | 3.0 – 4.9 | Weak | Critical event (signup or activation) unverified or missing; growth dashboard not functional | Block GA; instrumentation sprint required; re-review after completion |
| F | 0.0 – 2.9 | Failing | Multiple critical events absent; no growth dashboard; A/B test infrastructure not deployed | Block GA; full instrumentation implementation required before re-review |

## Signal Tables

### Critical Event Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | signup_completed, activation_event, and revenue events all verified in staging with correct payloads; data visible in data warehouse; event volumes consistent with test traffic |
| 7-8 | signup_completed and activation_event verified and in DW; revenue event fires correctly; 1 non-critical event (e.g., onboarding step) has minor payload gap |
| 5-6 | signup_completed verified; activation_event fires but missing 1 required property (non-blocking for basic analysis); revenue event not yet verified but business logic tested |
| 3-4 | signup_completed verified; activation_event not yet implemented or failing verification; revenue event has schema errors |
| 0-2 | signup_completed not implemented or failing; activation event absent; revenue tracking missing entirely |

### Growth Dashboard Readiness

| Score | Evidence |
|-------|----------|
| 9-10 | Every metric on the growth dashboard displays non-zero values in staging; values cross-checked against raw queries and match within 1%; dashboard access permissions configured |
| 7-8 | All AARRR metrics display; 1–2 secondary metrics (e.g., loop throughput) show placeholder/zero due to feature not yet at GA; primary KPIs validated |
| 5-6 | Acquisition and activation metrics display correctly; retention and revenue metrics not yet populated (features launching at GA); dashboard partially functional |
| 3-4 | Dashboard exists but fewer than half of metrics are populated; multiple metrics showing zero due to instrumentation gaps rather than feature readiness |
| 0-2 | Growth dashboard not yet built or not connected to production data sources; team reviewing metrics via ad-hoc queries |

### Full Funnel Instrumentation

| Score | Evidence |
|-------|----------|
| 9-10 | All funnel steps (landing → signup → each onboarding step → activation) have verified events; UTM attribution flows correctly through signup; retention events instrumented and consent-gated |
| 7-8 | Landing through activation fully instrumented; 1 non-critical onboarding step event missing; retention events instrumented but consent gating not fully tested |
| 5-6 | Signup and activation instrumented; 2–3 onboarding step events missing; UTM attribution verified for web but not mobile |
| 3-4 | Signup and activation instrumented; onboarding funnel incomplete (multiple step events missing); no retention event instrumentation |
| 0-2 | Only signup_completed present; onboarding, activation, and retention events absent; funnel analysis impossible at GA |

### A/B Test Infrastructure

| Score | Evidence |
|-------|----------|
| 9-10 | experiment_assigned fires with correct schema in staging; goal events carry experiment_id and variant_id; variant allocation verified end-to-end; experiment config management operational |
| 7-8 | experiment_assigned fires correctly; goal event linkage verified for primary goal; secondary goals not yet configured but not required for launch experiments |
| 5-6 | experiment_assigned fires but experiment_id or variant_id value incorrect in 1 test scenario; goal event missing experiment_id on 10–15% of conversions |
| 3-4 | experiment_assigned event exists but has non-standard schema; goal events not linked; experiment analysis would require manual joins |
| 0-2 | No A/B test infrastructure deployed; experiment tracking absent; no experiments can launch at GA |
