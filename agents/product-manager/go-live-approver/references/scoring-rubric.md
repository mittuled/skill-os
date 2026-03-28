# Scoring Rubric: Go-Live Approver

Evaluates release readiness across acceptance verification, customer impact, rollback preparedness, cross-functional alignment, and open risk documentation.

## Criteria

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Acceptance Criteria Verification | 25% | 0-10 | Completeness of acceptance criteria validation across all features in the release |
| Customer Impact Assessment | 20% | 0-10 | Thoroughness of customer/segment impact analysis including breaking changes and notification |
| Rollback Readiness | 20% | 0-10 | Quality of rollback plan: documented, tested, time-to-rollback acceptable |
| Cross-Functional Readiness | 20% | 0-10 | Preparedness of support, sales, CS, and marketing for the release |
| Open Risk Register | 15% | 0-10 | Quality of risk documentation: known issues catalogued, severity assessed, mitigations planned |
| **Total** | **100%** | | |

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All acceptance criteria verified, rollback tested, cross-functional teams signed off, risk register clean | Approve go-live immediately |
| A | 8.0 – 8.9 | Strong | Acceptance criteria met with minor gaps; rollback documented; cross-functional teams briefed | Approve go-live with minor items tracked as fast-follows |
| B | 7.0 – 7.9 | Good | Most criteria verified but rollback untested or one cross-functional team not fully prepared | Approve with conditions; resolve gaps before deploy window |
| C | 5.0 – 6.9 | Adequate | Notable gaps in acceptance verification or customer impact assessment; rollback plan exists but untested | Delay go-live; close critical gaps and re-evaluate |
| D | 3.0 – 4.9 | Weak | Multiple unverified acceptance criteria; no rollback plan; customer-facing teams unaware of release | Block go-live; escalate to product and engineering leadership |
| F | 0.0 – 2.9 | Failing | Release contents unknown; no readiness checks performed; risk is unquantified | Reject release; return to planning phase |

## Signal Tables

### Acceptance Criteria Verification
| Score | Evidence |
|-------|----------|
| 9-10 | Every story's acceptance criteria verified with QA sign-off; zero criteria waived; test evidence linked for each criterion |
| 7-8 | All critical stories verified; minor stories have acceptance criteria confirmed; 1-2 non-critical criteria partially met with documented justification |
| 5-6 | Most stories verified but some acceptance criteria marked "partial" without clear justification; QA sign-off exists but gaps noted |
| 3-4 | Several stories have unverified acceptance criteria; QA sign-off is incomplete; criteria waived without risk assessment |
| 1-2 | Acceptance criteria not systematically checked; release contents do not map to original user stories |

### Customer Impact Assessment
| Score | Evidence |
|-------|----------|
| 9-10 | All affected customers/segments identified; breaking changes documented with migration guides; notification plan executed; SLA and contractual obligations verified |
| 7-8 | Affected customers identified; breaking changes documented; notification plan exists; most contractual obligations checked |
| 5-6 | Customer impact assessed at segment level but not individual accounts; breaking changes known but migration guidance incomplete |
| 3-4 | Customer impact assessment is superficial; breaking changes may exist but are not fully catalogued; no notification plan |
| 1-2 | No customer impact assessment performed; unknown whether release introduces breaking changes |

### Rollback Readiness
| Score | Evidence |
|-------|----------|
| 9-10 | Rollback procedure documented and tested in staging; time-to-rollback under 15 minutes; monitoring and alerting configured to detect regressions; rollback owners identified |
| 7-8 | Rollback procedure documented and reviewed; time-to-rollback under 1 hour; monitoring configured; rollback tested for critical paths |
| 5-6 | Rollback procedure documented but not tested; monitoring exists but regression detection not specifically configured |
| 3-4 | Rollback procedure exists informally; untested; monitoring is generic; time-to-rollback unknown |
| 1-2 | No rollback procedure; deployment is a one-way door; no regression monitoring |

### Cross-Functional Readiness
| Score | Evidence |
|-------|----------|
| 9-10 | Support has updated KB articles and escalation paths; sales and CS briefed; marketing comms queued; all teams have signed off on readiness |
| 7-8 | Support briefed with documentation updates in progress; sales and CS informed; marketing aligned; most sign-offs obtained |
| 5-6 | Support aware but documentation not updated; sales/CS received email brief; marketing not involved; no formal sign-off |
| 3-4 | Only engineering and QA aware of the release; support, sales, and CS will discover changes post-deploy |
| 1-2 | No cross-functional communication; customer-facing teams unaware the release is happening |

### Open Risk Register
| Score | Evidence |
|-------|----------|
| 9-10 | All known issues catalogued with severity, likelihood, customer impact, and mitigation plan; fast-follows scheduled for deferred items; risk register reviewed by stakeholders |
| 7-8 | Known issues documented with severity ratings; most have mitigation plans; fast-follows identified for significant items |
| 5-6 | Known issues listed but not consistently rated; some mitigation plans exist; fast-follows not formally scheduled |
| 3-4 | Issues acknowledged informally but not documented; no severity assessment; no mitigation planning |
| 1-2 | No risk documentation; unknown whether the release ships with known issues |
