# Scoring Rubric: Instrumentation Verifier (QA)

Evaluates the completeness of instrumentation verification in the QA environment before staging promotion.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Signal Coverage | 30% | Percentage of expected instrumentation points (logs, metrics, traces) that were verified |
| 2 | Payload Validation | 25% | Correctness of signal payload shapes, field types, and required attributes |
| 3 | Path Coverage | 25% | Coverage of both happy paths and error paths in instrumentation testing |
| 4 | Documentation Quality | 20% | Completeness of the verification checklist with pass/fail per signal and evidence |
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
| A+ | 9.0 – 10.0 | Exceptional | All signals verified on happy and error paths; payloads validated; no extraneous emissions; comprehensive checklist | Promote to staging |
| A | 8.0 – 8.9 | Strong | All critical signals verified; payloads correct; minor gaps in error path coverage | Promote with follow-up on error path gaps |
| B | 7.0 – 7.9 | Good | Most signals verified; payloads mostly correct; some error paths untested | Promote with caveats; complete error path verification |
| C | 5.0 – 6.9 | Adequate | Happy-path signals verified; error paths not tested; payload validation incomplete | Block promotion; expand test coverage |
| D | 3.0 – 4.9 | Weak | Partial signal verification; payloads not validated; checklist incomplete | Block promotion; restart verification |
| F | 0.0 – 2.9 | Failing | No instrumentation verification performed | Reject; verification required before promotion |

## Signal Tables

### Signal Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | 100% of expected log events, metrics, and trace spans verified in QA observability stack; no missing signals; extraneous signals identified and flagged |
| 7-8 | 80%+ of signals verified; critical signals all confirmed; minor signals pending |
| 5-6 | Logs verified; metrics partially checked; traces not confirmed |
| 3-4 | Only one signal type (logs or metrics) verified |
| 0-2 | No signals verified in QA environment |

### Payload Validation
| Score | Evidence |
|-------|----------|
| 9-10 | All signal payloads validated for correct field names, types, and required attributes; no PII in logs; metric labels match specification; trace attributes complete |
| 7-8 | Critical signal payloads validated; minor signals spot-checked; PII check passed |
| 5-6 | Signals confirmed to fire but payload content not validated |
| 3-4 | Signal presence confirmed; payload shape unknown |
| 0-2 | No payload validation |

### Path Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | Instrumentation tested on happy paths, error paths (4xx, 5xx), timeout scenarios, and edge cases; each path produces expected signals |
| 7-8 | Happy paths and primary error paths tested; timeout scenarios not verified |
| 5-6 | Happy paths tested; error paths not exercised |
| 3-4 | Single flow tested; no variation in scenarios |
| 0-2 | No test execution to trigger instrumentation |

### Documentation Quality
| Score | Evidence |
|-------|----------|
| 9-10 | Structured checklist with pass/fail per signal; evidence links to log entries, metric queries, or trace IDs; recommendation clearly stated |
| 7-8 | Checklist complete with pass/fail; evidence for critical signals; recommendation provided |
| 5-6 | Checklist present but evidence incomplete; recommendation vague |
| 3-4 | Verbal or chat-based report; no structured checklist |
| 0-2 | No documentation |
