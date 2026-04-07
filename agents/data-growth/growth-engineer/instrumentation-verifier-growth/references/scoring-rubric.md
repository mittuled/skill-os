# Scoring Rubric: instrumentation-verifier-growth

Evaluates whether growth tracking events in the development and staging environment match the approved instrumentation spec across funnel events, experiment events, and loop events.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Funnel Event Coverage | 30% | All acquisition-to-activation funnel step events fire with correct names and trigger conditions |
| 2 | Experiment Event Accuracy | 30% | experiment_assigned and goal events fire with correct experiment_id, variant_id, and linkage |
| 3 | Payload Property Compliance | 25% | Event payloads contain all spec-required properties with correct types and values |
| 4 | Loop Event Completeness | 15% | All loop node events fire with referrer_id linkage intact across the full cycle |
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
| A+ | 9.0 – 10.0 | Exceptional | All events pass spec, no missing properties, experiment linkage perfect, loop attribution intact | Approve for production deployment |
| A | 8.0 – 8.9 | Strong | All critical events pass; 1–2 minor property issues on non-critical events | Approve with minor notes for implementer to fix post-deploy |
| B | 7.0 – 7.9 | Good | Critical events pass; experiment events have minor gaps not affecting significance calculation | Approve with conditions; fix flagged issues before experiment launch |
| C | 5.0 – 6.9 | Adequate | Significant payload gaps on 2–3 funnel events; experiment linkage partially broken | Return to implementer; fix and re-verify before deployment |
| D | 3.0 – 4.9 | Weak | Multiple critical events failing; experiment_assigned missing variant_id; loop attribution broken | Do not deploy; full remediation sprint required |
| F | 0.0 – 2.9 | Failing | Core growth events (signup, activation) not firing; no experiment tracking; loop events absent | Block deployment; fundamental instrumentation redesign needed |

## Signal Tables

### Funnel Event Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | All N spec-defined funnel events fire at correct trigger points; event names match spec exactly; duplicate events absent; events fire once per action |
| 7-8 | All critical funnel events (signup_started, signup_completed, activation_event) fire correctly; 1–2 non-critical onboarding steps missing or misnamed |
| 5-6 | Critical events fire but 2–3 onboarding step events missing; 1 event fires at wrong trigger point (e.g., signup_completed fires before email confirmation) |
| 3-4 | 2+ critical funnel events missing or misfiring; activation event does not fire; duplicate events observed on 2+ steps |
| 0-2 | Core funnel events absent (no signup_completed or activation event firing in any test scenario); funnel analysis impossible |

### Experiment Event Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | experiment_assigned fires exactly once per user per experiment with correct experiment_id and variant_id; goal events carry experiment_id and variant_id; no double-assignment |
| 7-8 | experiment_assigned fires correctly; goal events carry experiment_id on ≥95% of conversions; variant_id present but incorrect on 1 edge case |
| 5-6 | experiment_assigned fires but fires twice for some users (double assignment risk); goal events missing experiment_id on 10–20% of conversions |
| 3-4 | experiment_assigned fires but variant_id is null or incorrect; goal events do not carry experiment_id; experiment results cannot be attributed |
| 0-2 | experiment_assigned event does not fire; experiment tracking completely absent; experiment cannot be analyzed |

### Payload Property Compliance

| Score | Evidence |
|-------|----------|
| 9-10 | 100% of tested event payloads contain all spec-required properties; UTM properties populated from first-touch storage (not URL); data types match spec |
| 7-8 | ≥95% of payloads spec-compliant; UTM populated correctly; 1–2 optional enrichment properties missing on minority of events |
| 5-6 | 85–94% compliance; UTM reading from current URL (not first-touch) on some events; 1 required property has wrong type |
| 3-4 | Required properties (user_id, session_id, platform) missing on >10% of events; UTM hardcoded or absent; timestamp format inconsistent |
| 0-2 | Core properties absent or corrupted across majority of events; payloads are incomplete shells; events are unanalyzable |

### Loop Event Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | Full loop cycle tested end-to-end; all N node events fire; referrer_id correctly propagated from invite_sent through referred_signup and referred_activation |
| 7-8 | All loop events fire; referrer_id present on invite_sent and referred_signup; minor gap in reward event properties (non-critical) |
| 5-6 | Loop trigger and distribution events fire; referred_signup missing referrer_id linkage; loop attribution partially broken |
| 3-4 | Only trigger and invite_sent events present; referred_signup and referred_activation events missing; viral coefficient is uncomputable |
| 0-2 | No loop events implemented; loop tracking absent entirely |
