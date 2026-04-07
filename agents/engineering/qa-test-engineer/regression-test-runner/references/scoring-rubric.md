# Scoring Rubric: regression-test-runner

Evaluates the quality of a regression test suite across feature coverage completeness, suite freshness, failure triage accuracy, environmental stability, and release recommendation quality.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Feature Coverage Completeness | 30% | Percentage of shipped features represented in the regression suite |
| 2 | Suite Freshness | 25% | How up-to-date the suite is relative to recently shipped functionality |
| 3 | Failure Triage Accuracy | 20% | Proportion of failures correctly categorized as genuine regression vs. flaky vs. environment |
| 4 | Environmental Stability | 15% | Test environment matches the production configuration and data state closely enough to produce reliable signals |
| 5 | Release Recommendation Quality | 10% | Regression report provides a clear, evidence-based go/no-go recommendation |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely absent or non-functional, 5 = present with significant gaps, 10 = best-in-class, no gaps.

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | 95%+ features covered, suite updated within 1 sprint of each release, < 2% flaky rate, environment mirrors production, recommendations are unambiguous | Use as release gate without augmentation |
| A | 8.0–8.9 | Strong | 85%+ features covered, suite 1–2 sprints behind, flaky rate < 5%, minor environment gaps, clear recommendations | Schedule suite update; reliable as release gate |
| B | 7.0–7.9 | Good | 75–84% features covered, suite up to 1 quarter behind, 5–10% flaky, some environment drift, recommendations include caveats | Plan coverage catch-up sprint; usable as release gate with caveats |
| C | 5.0–6.9 | Adequate | 50–74% features covered, significant portions of recent features untested, > 10% flaky, environment frequently wrong, recommendations hedge heavily | Regression suite improvement required before next major release |
| D | 3.0–4.9 | Weak | 25–49% features covered, many recent features completely untested, > 20% flaky, environment unreliable, recommendations unreliable | Suite cannot function as release gate; rebuild required |
| F | 0.0–2.9 | Failing | < 25% features covered, suite unchanged for > 6 months, flaky rate > 30%, environment wrong, no clear recommendations | Regression suite provides false confidence; retire and rebuild |

## Signal Tables

### Feature Coverage Completeness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Feature-to-test traceability matrix exists and is current; 95%+ features have at least 1 regression test; all critical user flows covered by at least 3 test cases (happy path, boundary, error) |
| 7–8 | 85–94% features have regression tests; traceability matrix partially maintained; most critical flows covered; minor edge cases of 1–2 features uncovered |
| 5–6 | 60–84% features have regression tests; no formal traceability; several features added in the last 2 quarters with no regression coverage |
| 3–4 | 30–59% features covered; features added in the last year frequently lack regression tests; critical user flows missing test cases |
| 0–2 | < 30% features have regression tests; suite reflects the state of the product from > 1 year ago; most recent functionality completely uncovered |

### Suite Freshness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | New regression tests added for every feature within 1 sprint of shipping; tests updated within the same PR as feature changes; suite version matches the last release version |
| 7–8 | Regression tests added within 1–2 sprints of feature ship; occasional feature ships without test update (caught in next sprint); suite is 1 minor version behind |
| 5–6 | Test additions lag 1–2 quarters behind feature development; some features shipped without regression tests and never caught up; team aware of gaps but backlog is growing |
| 3–4 | Suite has not been substantially updated in 3–6 months; 1+ quarterly releases shipped without regression suite expansion; test backlog exceeds 20 items |
| 0–2 | Suite has not been updated in > 6 months; tests reference UI elements, APIs, or flows that no longer exist; team treats regression failures as expected background noise |

### Failure Triage Accuracy

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Each failure correctly categorized in < 5 minutes; genuine regressions have defect tickets within 30 minutes; flaky tests are quarantined immediately and fixed within 2 sprints |
| 7–8 | 90%+ failures correctly categorized; occasional misclassification requiring second opinion; flaky test quarantine process exists and is followed |
| 5–6 | 70–89% of failures correctly categorized; some genuine regressions initially dismissed as flaky; flaky test backlog growing but occasionally addressed |
| 3–4 | < 70% of failures correctly categorized; team defaults to "rerun until it passes" for all failures; no formal flaky test process; genuine regressions regularly missed |
| 0–2 | No formal triage; all failures retried 3 times and dismissed if they pass on retry; genuine regressions reach production regularly |

### Environmental Stability

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Test environment provisioned fresh for each regression run; data state reset to known baseline before each run; environment version matches production exactly |
| 7–8 | Environment mostly stable; data state reset for 90%+ of runs; minor version drift (< 1 minor version); environment failures < 2% of runs |
| 5–6 | Shared environment with occasional data contamination; version drift of 1–2 minor versions; environment failures cause 5–10% of test run cancellations |
| 3–4 | Environment shared and frequently in unknown state; data from previous runs affects current runs; version drift causes false failures for 10–20% of tests |
| 0–2 | No environment management; tests run against production-like shared environments with live data; environment state unknown at test start; environment failures > 30% of runs |

### Release Recommendation Quality

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Report contains: explicit go/no-go verdict, list of blocking defects with severity, specific conditions that must be met before release, and verification steps |
| 7–8 | Report contains explicit go/no-go verdict with supporting evidence; 1–2 recommendations lack specific remediation steps; conditions for conditional approval are clear |
| 5–6 | Report has a verdict but it is hedged ("generally looks OK, a few things to watch"); blocking issues listed without severity; no explicit conditions for release |
| 3–4 | Report lists failures without a verdict; team must interpret whether to release; no prioritization of findings |
| 0–2 | Report is a raw pass/fail count with no analysis; team makes release decisions without using the regression report |
