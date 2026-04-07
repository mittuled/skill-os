# Scoring Rubric: sprint-reviewer-data

Evaluates the quality of data deliverables completed in a sprint — instrumentation, dashboards, analyses, and data model changes — against their acceptance criteria and data standards.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Instrumentation Completeness | 30% | Instrumentation tickets include a passing verification report; all spec-defined events confirmed in staging or production |
| 2 | Dashboard Accuracy | 30% | Dashboard metrics match raw SQL queries for the same period; layout matches design spec; metric definitions are documented |
| 3 | Analysis Quality | 25% | Analysis tickets address the stated question; methodology is documented; data sources are verified; conclusions are supported by evidence |
| 4 | Cross-Deliverable Consistency | 15% | Dashboards, analyses, and data models within the sprint reference consistent metric definitions and do not conflict with each other |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0–10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Sprint approved | All deliverables meet acceptance criteria; no rework items; dashboards accurate; analysis rigorous; no cross-deliverable conflicts | Close all tickets; announce at sprint review |
| A | 8.0 – 8.9 | Approved with comments | 1–2 minor rework items; all deliverables functionally complete; no accuracy or consistency blockers | Close with minor fix notes; track follow-up items in next sprint |
| B | 7.0 – 7.9 | Conditionally approved | 1 dashboard with a documented accuracy issue; or 1 analysis with methodology gap; or 1 unverified instrumentation ticket | Fix blocker items before sharing with stakeholders; re-review affected deliverables |
| C | 5.0 – 6.9 | Needs rework | Multiple deliverables with material issues; 1+ instrumentation ticket deployed to production without verification; dashboard values incorrect | Return tickets to "in review"; block sprint retrospective sign-off until fixed |
| D | 3.0 – 4.9 | Significant failures | Majority of deliverables have quality issues; instrumentation shipped to production with known failures; dashboard numbers mislead stakeholders | Immediate retrospective on review process; hotfix plan required |
| F | 0.0 – 2.9 | Sprint failed | No meaningful quality review occurred; deliverables closed without review artifacts; data quality issues already in production | Audit all sprint deliverables; initiate data quality incident process |

## Signal Tables

### Instrumentation Completeness

| Score | Evidence |
|-------|----------|
| 9–10 | Every instrumentation ticket has a verification report attached; all events pass spec validation in staging; production deployment scheduled or confirmed; negative cases tested |
| 7–8 | 90–99% of instrumentation tickets have verification reports; 1 low-criticality event has minor issues documented and tracked; production deployment on schedule |
| 5–6 | 80–89% have verification reports; 1 event failed verification with a fix plan documented; no unverified events in production yet |
| 3–4 | 60–79% have verification reports; 1 high-criticality event deployed to production without verification; no evidence of spec comparison |
| 0–2 | <60% have verification reports; multiple instrumentation tickets closed as "done" with no verification artifact; production data shows unexpected event volumes or missing events |

### Dashboard Accuracy

| Score | Evidence |
|-------|----------|
| 9–10 | All metrics cross-checked against raw SQL for the same period; variance <1%; segment filters tested; date range pickers produce consistent values; metric definitions documented in tooltips |
| 7–8 | All primary metrics validated; 1–2 secondary metrics with minor variance (<3%) documented; segment filters work correctly |
| 5–6 | Primary metrics validated; 1 metric with a known variance issue documented with root cause; metric definitions partially complete |
| 3–4 | Some metrics validated; 1 primary metric has unexplained variance >5% without a fix plan; metric definitions absent |
| 0–2 | No validation performed; metrics not cross-checked; dashboard values differ from raw queries by >10%; data team receives questions from stakeholders because numbers are wrong |

### Analysis Quality

| Score | Evidence |
|-------|----------|
| 9–10 | Analysis addresses exactly the question stated in the ticket; data sources are named and verified; methodology is documented; conclusions follow directly from the data with appropriate caveats |
| 7–8 | Analysis addresses the core question; 1 minor methodological shortcut documented; conclusions are justified |
| 5–6 | Analysis partially addresses the question; methodology not fully documented; 1 assumption not validated |
| 3–4 | Analysis addresses a related but different question than stated; methodology undocumented; conclusions go beyond what the data supports |
| 0–2 | Analysis is incomplete or addresses the wrong question; conclusions not supported by data; no methodology documentation |

### Cross-Deliverable Consistency

| Score | Evidence |
|-------|----------|
| 9–10 | All metrics defined consistently across dashboards and analyses in the sprint; no conflicting definitions; dashboards built on the sprint's data model changes use the new schema correctly |
| 7–8 | 1 minor metric definition difference between deliverables (documented, non-material); all deliverables reference the current data model |
| 5–6 | 1 metric defined differently in two deliverables (e.g., "active user" definition differs); team is aware and will harmonize |
| 3–4 | Multiple conflicting metric definitions across sprint deliverables; 1 dashboard still references a deprecated column from a data model change made in this sprint |
| 0–2 | Sprint deliverables use incompatible metric definitions; dashboards break because they reference columns deprecated by model changes in the same sprint; no cross-deliverable review was performed |
