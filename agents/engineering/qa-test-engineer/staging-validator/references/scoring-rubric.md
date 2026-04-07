# Scoring Rubric: Staging Validator

Evaluates staging environment readiness across environment parity, test coverage, integration validation, observability, and infrastructure smoke tests.

## Criteria

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Environment Parity | 20% | 0-10 | How closely staging mirrors production: configuration, infrastructure, data |
| Test Coverage | 25% | 0-10 | Breadth and depth of end-to-end test execution across critical user journeys |
| Integration Validation | 20% | 0-10 | Verification of cross-service integrations, async workflows, and background jobs |
| Observability Readiness | 15% | 0-10 | Functioning of logs, metrics, traces, and alerting in the staging environment |
| Infrastructure Smoke Tests | 20% | 0-10 | Validation of DNS, load balancers, certificates, and infrastructure changes |
| **Total** | **100%** | | |

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Staging mirrors production exactly; all critical journeys pass; integrations verified; observability confirmed; infrastructure smoke-tested | Clear for production deployment |
| A | 8.0 – 8.9 | Strong | High environment parity; critical paths tested; most integrations verified; observability working with minor trace gaps | Clear for deployment with monitoring watch during rollout |
| B | 7.0 – 7.9 | Good | Staging mostly matches production; core test coverage present but some integration or observability gaps | Deploy with caution; address integration gaps in parallel |
| C | 5.0 – 6.9 | Adequate | Known configuration drift from production; partial test coverage; async workflows unverified; observability incomplete | Block deployment until parity and integration gaps resolved |
| D | 3.0 – 4.9 | Weak | Staging significantly diverges from production; minimal test execution; no integration or observability validation | Halt deployment; rebuild staging environment to match production |
| F | 0.0 – 2.9 | Failing | Staging bears no resemblance to production; no tests run; infrastructure unverified | Reject release; staging validation must be performed from scratch |

## Signal Tables

### Environment Parity
| Score | Evidence |
|-------|----------|
| 9-10 | Staging matches production in version, configuration, and infrastructure; data is representative in schema, volume, and edge cases; feature flags match production state |
| 7-8 | Staging matches production in version and core configuration; data is representative in schema; minor volume or edge-case gaps documented |
| 5-6 | Staging is close to production but has known configuration drift; data schema matches but volume is significantly reduced |
| 3-4 | Staging has different infrastructure or configuration from production; data is synthetic and may not represent real usage patterns |
| 1-2 | Staging bears little resemblance to production; different versions, configurations, or infrastructure; no representative data |

### Test Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | All critical user journeys tested end-to-end; happy paths and key error paths covered; all tests passing |
| 7-8 | Critical user journeys tested; most error paths covered; all tests passing with known non-critical skips documented |
| 5-6 | Most critical journeys tested but some gaps; a few tests skipped without clear justification |
| 3-4 | Only partial journey coverage; significant critical paths untested; test failures present but not investigated |
| 1-2 | Minimal or no test execution; coverage unknown; tests are broken or not maintained |

### Integration Validation
| Score | Evidence |
|-------|----------|
| 9-10 | All cross-service APIs verified; async workflows (queues, webhooks, scheduled jobs) confirmed working; data flows validated end-to-end across services |
| 7-8 | Major integrations verified; most async workflows confirmed; minor integration paths untested with low risk |
| 5-6 | Key integrations tested but async workflows only partially verified; some service boundaries untested |
| 3-4 | Only primary API integrations tested; background jobs and async flows not verified; known integration gaps |
| 1-2 | No integration testing performed; services tested in isolation only |

### Observability Readiness
| Score | Evidence |
|-------|----------|
| 9-10 | Structured logs flowing to aggregator; metrics emitting with correct labels; distributed traces connected across services; alerts configured and verified |
| 7-8 | Logs and metrics confirmed working; traces mostly connected; alerting configured but not fully verified |
| 5-6 | Logs flowing but metrics partially working; traces not verified; alerting configuration exists but untested |
| 3-4 | Logs present but unstructured; metrics missing or misconfigured; no tracing; no alerting |
| 1-2 | No observability verification performed; unknown whether logging, metrics, or tracing function |

### Infrastructure Smoke Tests
| Score | Evidence |
|-------|----------|
| 9-10 | DNS resolves correctly; load balancers routing properly; TLS certificates valid and not expiring soon; all infrastructure changes smoke-tested |
| 7-8 | Core infrastructure verified (DNS, TLS, load balancing); minor infrastructure changes smoke-tested |
| 5-6 | DNS and TLS verified; load balancer and other infrastructure changes not explicitly tested |
| 3-4 | Only basic connectivity confirmed; infrastructure changes assumed to work based on configuration review |
| 1-2 | No infrastructure validation performed; changes deployed without verification |
