# Scoring Rubric: uat-coordinator

Evaluates the quality of user acceptance testing coordination including participant selection, test execution, result synthesis, and follow-through.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Participant Selection and Planning | 20% | Quality of participant matching to target persona and test scenario design |
| 2 | Test Environment Preparation | 15% | Readiness of staging environment with realistic data and access |
| 3 | Session Execution and Feedback Capture | 30% | Thoroughness of guided testing and quality of captured feedback |
| 4 | Result Synthesis and Decision | 20% | Quality of aggregated findings and pass/fail determination |
| 5 | Follow-Through and Closure | 15% | Completeness of ticket filing, participant communication, and go-live recommendation |

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
| A+ | 9.0 – 10.0 | Exceptional | Representative participants, structured scenarios, complete feedback capture, clear pass/fail with evidence, all issues ticketed and communicated | Proceed to release with confidence |
| A | 8.0 – 8.9 | Strong | Good participant match, scenarios covered, findings aggregated, decision documented | Release with documented caveats |
| B | 7.0 – 7.9 | Good | Adequate participants and scenarios, most feedback captured, decision present | Address minor gaps before GA |
| C | 5.0 – 6.9 | Adequate | Some real users tested, feedback partially structured, decision made with limited evidence | Expand UAT coverage before GA decision |
| D | 3.0 – 4.9 | Weak | Internal-only testing, unstructured feedback, no clear pass/fail | Re-run UAT with external participants |
| F | 0.0 – 2.9 | Failing | No meaningful UAT conducted | Block release until UAT completes |

## Signal Tables

### Participant Selection and Planning

| Score | Evidence |
|-------|----------|
| 9-10 | 5+ external participants matching target persona. Test scenarios defined with expected outcomes. Schedule confirmed. Screening questionnaire used. Mix of experience levels included. |
| 7-8 | 3-4 external participants, scenarios defined, schedule set |
| 5-6 | 1-2 external participants or participants partially match target persona |
| 3-4 | Internal team members only used as participants |
| 0-2 | No participant selection or planning performed |

### Test Environment Preparation

| Score | Evidence |
|-------|----------|
| 9-10 | Staging environment provisioned with realistic data. Feature enabled and verified. Access credentials distributed. Known environment limitations documented. |
| 7-8 | Environment ready with feature enabled, access distributed |
| 5-6 | Environment available but data unrealistic or feature partially configured |
| 3-4 | Participants directed to production with no controlled setup |
| 0-2 | No test environment prepared |

### Session Execution and Feedback Capture

| Score | Evidence |
|-------|----------|
| 9-10 | Each participant guided through all scenarios. Feedback captured per scenario with severity ratings. Verbatim quotes recorded. Deviations from expected outcomes documented. Session recordings available. |
| 7-8 | All scenarios covered, feedback captured with severity, most deviations noted |
| 5-6 | Some scenarios covered, feedback captured but not per-scenario or missing severity |
| 3-4 | Participants asked to explore freely with minimal guidance; anecdotal feedback only |
| 0-2 | No structured session execution |

### Result Synthesis and Decision

| Score | Evidence |
|-------|----------|
| 9-10 | Findings aggregated across all participants. Issues categorised by severity (critical/major/minor/cosmetic). Clear pass/fail determination against acceptance threshold. Statistical summary provided. |
| 7-8 | Findings aggregated, severity assigned, pass/fail decision documented |
| 5-6 | Findings listed but not aggregated or severity-ranked; pass/fail implied but not stated |
| 3-4 | Individual session notes exist but no synthesis performed |
| 0-2 | No result synthesis |

### Follow-Through and Closure

| Score | Evidence |
|-------|----------|
| 9-10 | Tickets filed for every issue with reproduction steps and severity. Participants notified of outcome and timeline. Go-live recommendation issued to stakeholders. |
| 7-8 | Tickets filed for major issues, participants thanked, recommendation issued |
| 5-6 | Some tickets filed, participant communication incomplete |
| 3-4 | Issues noted but not ticketed; no communication to participants |
| 0-2 | No follow-through actions |
