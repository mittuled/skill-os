# Sprint Data Review Summary

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Reviewer | [Data Analyst name] |
| Sprint | [Sprint number / name] |
| Sprint Dates | [YYYY-MM-DD to YYYY-MM-DD] |
| Total Data Tickets | [N] |
| Approved | [N] |
| Needs Rework | [N] |
| Skill | sprint-reviewer-data |

## Deliverable Summary

| Ticket | Type | Title | Status | Reviewed By | Verdict |
|--------|------|-------|--------|-------------|---------|
| [TICKET-123] | [Instrumentation] | [Implement signup events] | [Done] | [Name] | [Approved / Needs Rework] |
| [TICKET-124] | [Dashboard] | [Build activation dashboard] | [Done] | [Name] | [Approved / Needs Rework] |
| [TICKET-125] | [Analysis] | [Q2 funnel analysis] | [Done] | [Name] | [Approved / Needs Rework] |
| [TICKET-126] | [Data Model] | [Add user_plan_tier to events table] | [Done] | [Name] | [Approved / Needs Rework] |

Types: Instrumentation / Dashboard / Analysis / Data Model / Other

## Instrumentation Reviews

### [TICKET-123]: [Ticket Title]

| Check | Status | Notes |
|-------|--------|-------|
| Verification report exists | [Yes / No] | [Link or "missing"] |
| All spec events pass verification | [Yes / No — N failed] | [Link to report] |
| Production deploy scheduled or complete | [Scheduled [date] / Complete / Not yet scheduled] | — |
| Negative test cases verified | [Yes / No] | — |
| Documentation updated in spec | [Yes / No] | — |

**Verdict**: [Approved / Needs Rework]

**Rework Required**: [Describe what must be fixed, or "N/A"]

---

## Dashboard Reviews

### [TICKET-124]: [Ticket Title]

| Check | Status | Notes |
|-------|--------|-------|
| Metric values match raw warehouse queries | [Yes / No] | [Spot-check query: `SELECT ... FROM ...`] |
| Dashboard layout matches design spec | [Yes / No] | [Deviations: describe] |
| All metrics have descriptions / tooltips | [Yes / No] | [Missing: list] |
| Filters and date range selectors work correctly | [Yes / No] | [Issues: describe] |
| Dashboard documentation exists | [Yes / No] | [Link or "missing"] |
| Access permissions set correctly | [Yes / No] | [Who has access?] |

**Verdict**: [Approved / Needs Rework]

**Rework Required**: [Describe, or "N/A"]

---

## Analysis Reviews

### [TICKET-125]: [Ticket Title]

| Check | Status | Notes |
|-------|--------|-------|
| Question posed in ticket is answered | [Yes / Partially / No] | — |
| Data sources are documented and trusted | [Yes / No] | [Source tables: list] |
| Methodology is explained and defensible | [Yes / No] | [Concerns: describe] |
| Statistical tests used correctly (if applicable) | [Yes / No / N/A] | — |
| Conclusions are supported by the data shown | [Yes / No] | — |
| Caveats and limitations are disclosed | [Yes / No] | — |
| Output shared with requestor | [Yes / No] | [Channel/doc link] |

**Verdict**: [Approved / Needs Rework]

**Rework Required**: [Describe, or "N/A"]

---

## Data Model Reviews

### [TICKET-126]: [Ticket Title]

| Check | Status | Notes |
|-------|--------|-------|
| Schema change is backward compatible | [Yes / No — breaking change] | [Describe impact] |
| Downstream dashboards/models updated | [Yes / No — N affected] | [List affected assets] |
| Data dictionary updated | [Yes / No] | — |
| Migration or backfill complete | [Yes / Scheduled / N/A] | — |

**Verdict**: [Approved / Needs Rework]

**Rework Required**: [Describe, or "N/A"]

---

## Cross-Deliverable Dependency Check

[Flag any deliverables that depend on each other and check for integration issues.]

| Dependency | Deliverable A | Deliverable B | Integration Status |
|------------|--------------|--------------|-------------------|
| [Dashboard built on data model that changed] | [TICKET-124] | [TICKET-126] | [Aligned / CONFLICT — dashboard references deprecated column] |

## Sprint Data Quality Scorecard

| Dimension | Score (1-5) | Notes |
|-----------|------------|-------|
| Instrumentation accuracy | [1-5] | [1=many failures, 5=all pass first time] |
| Dashboard accuracy | [1-5] | [1=metric errors, 5=all verified correct] |
| Analysis rigor | [1-5] | [1=methodology unclear, 5=fully documented] |
| Review turnaround (within sprint) | [1-5] | [1=missed, 5=completed day before sprint review] |

**Overall sprint data quality**: [1-5] — [One-sentence summary]

## Action Items for Next Sprint

| Action | Owner | Due Date |
|--------|-------|----------|
| [Rework TICKET-123 verification failures] | [Data Analyst name] | [YYYY-MM-DD] |
| [Add descriptions to TICKET-124 dashboard metrics] | [Data Analyst name] | [YYYY-MM-DD] |
