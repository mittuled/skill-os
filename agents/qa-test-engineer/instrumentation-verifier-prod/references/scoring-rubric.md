# Scoring Rubric: Instrumentation Verifier (Production)

Evaluates the completeness of post-deployment instrumentation verification in the production environment.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Signal Coverage | 30% | Percentage of expected production signals (logs, metrics, traces) confirmed after deployment |
| 2 | Timeliness | 20% | How quickly verification was performed after deployment |
| 3 | Cross-Pillar Verification | 25% | Coverage across all three observability pillars (logs, metrics, traces) rather than just one |
| 4 | Evidence and Reporting | 25% | Quality of verification report with evidence links and recommendation |
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
| A+ | 9.0 – 10.0 | Exceptional | All signals verified across all pillars within 30 min of deploy; evidence linked; no anomalies | Mark release verified; close deploy ticket |
| A | 8.0 – 8.9 | Strong | All critical signals verified within 1 hour; minor gaps documented; recommendation clear | Mark verified with follow-up items |
| B | 7.0 – 7.9 | Good | Most signals verified; one pillar partially checked; verified within 2 hours | Mark verified with monitoring watch |
| C | 5.0 – 6.9 | Adequate | Logs verified but metrics or traces not confirmed; verified late | Escalate; complete verification urgently |
| D | 3.0 – 4.9 | Weak | Partial verification of one pillar only; delayed significantly | Escalate; consider rollback if signals critical |
| F | 0.0 – 2.9 | Failing | No production verification performed | Immediate escalation; verify or rollback |

## Signal Tables

### Signal Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | 100% of deployment manifest signals confirmed in production observability stack; no missing or malformed signals; duplicates checked |
| 7-8 | 80%+ of signals confirmed; critical signals all verified; minor signals pending |
| 5-6 | Majority of signals checked but some not confirmed due to low traffic or sampling |
| 3-4 | Only a few signals spot-checked |
| 0-2 | No production signal verification |

### Timeliness
| Score | Evidence |
|-------|----------|
| 9-10 | Verification completed within 30 minutes of production deployment |
| 7-8 | Verification completed within 1 hour |
| 5-6 | Verification completed within 2-4 hours |
| 3-4 | Verification completed next business day |
| 0-2 | Verification not performed or performed days later |

### Cross-Pillar Verification
| Score | Evidence |
|-------|----------|
| 9-10 | Logs, metrics, and traces all independently verified; cross-pillar correlation confirmed (trace ID appears in logs and metrics) |
| 7-8 | All three pillars checked; correlation verified for critical paths |
| 5-6 | Two pillars verified; third pillar acknowledged but not confirmed |
| 3-4 | Only one pillar (typically logs) verified |
| 0-2 | No pillar-specific verification |

### Evidence and Reporting
| Score | Evidence |
|-------|----------|
| 9-10 | Structured report with pass/fail per signal; links to specific log entries, metric dashboard queries, and trace IDs; clear recommendation to release owner |
| 7-8 | Report with pass/fail and evidence for critical signals; recommendation provided |
| 5-6 | Report present but evidence links incomplete; recommendation vague |
| 3-4 | Verbal confirmation; no written report |
| 0-2 | No reporting |
