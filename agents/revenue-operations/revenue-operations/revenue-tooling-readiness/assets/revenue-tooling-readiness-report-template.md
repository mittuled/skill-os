# Revenue Tooling Readiness Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [RevOps analyst name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | revenue-tooling-readiness |
| Assessment Scope | [List tools assessed: CRM, billing, CPQ, analytics] |
| Go-Live Date | [YYYY-MM-DD] |
| Assessed By | [Name + role] |

## Verdict

[State the overall go/no-go determination prominently at the top.]

| Verdict | Composite Score | Grade |
|---------|----------------|-------|
| **[GO / CONDITIONAL GO / NO-GO]** | [0–100] | [A+ / A / B / C / D / F] |

## Score Summary

[Per-criterion scores weighted to composite total.

GUIDANCE: Any criterion scoring 1-2 should be listed as a blocker in the Issues section below, regardless of composite score.]

| Criterion | Weight | Raw Score (0–10) | Weighted Score | Status |
|-----------|--------|-----------------|----------------|--------|
| CRM Configuration | 30% | [0–10] | [score × 0.30] | [Pass / Fail / Partial] |
| Billing System Accuracy | 25% | [0–10] | [score × 0.25] | [Pass / Fail / Partial] |
| End-to-End Integration | 25% | [0–10] | [score × 0.25] | [Pass / Fail / Partial] |
| Reporting and Analytics | 10% | [0–10] | [score × 0.10] | [Pass / Fail / Partial] |
| Data Quality | 10% | [0–10] | [score × 0.10] | [Pass / Fail / Partial] |
| **Composite Score** | **100%** | — | **[total]** | **[Grade]** |

## Tool Inventory Assessed

[List every revenue-facing tool included in this assessment.]

| Tool | Role in Deal-to-Cash | Version / Config Date | Tested |
|------|---------------------|-----------------------|--------|
| [CRM name] | Pipeline tracking, lead routing, attribution | [date] | [Yes / No] |
| [Billing system] | Invoice generation, revenue recognition | [date] | [Yes / No] |
| [CPQ tool] | Quote generation, pricing rules | [date] | [Yes / No] |
| [Analytics / BI tool] | Pipeline reporting, attribution reporting | [date] | [Yes / No] |

## End-to-End Test Results

[Document the test transaction run through the full deal-to-cash flow.

GUIDANCE: At minimum, test one full flow: test lead → MQL → SQL → Opportunity → Closed-Won → Invoice → Revenue Recognition entry. Document each step pass/fail.]

| Step | System | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| Lead created | CRM | Lead source captured | [result] | [Pass / Fail] |
| MQL qualification | CRM | Lead score triggers MQL status | [result] | [Pass / Fail] |
| Opportunity created | CRM | Stage, amount, close date populated | [result] | [Pass / Fail] |
| Quote generated | CPQ | Pricing correct per product | [result] | [Pass / Fail] |
| Closed-Won | CRM | Stage updates; billing triggered | [result] | [Pass / Fail] |
| Invoice generated | Billing | Correct amount, payment terms | [result] | [Pass / Fail] |
| Revenue recognised | Billing / ERP | Recognition schedule matches contract | [result] | [Pass / Fail] |
| CRM updated | CRM | Billing status synced back | [result] | [Pass / Fail] |

## Issues and Blockers

[List all issues found, classified by severity.

GUIDANCE: BLOCKER issues must be resolved before go-live. HIGH issues must have a mitigation or owner before go-live. MEDIUM and LOW may be resolved post-launch with tracking.]

### Blockers (Must Resolve Before Go-Live)

| # | Tool | Issue | Resolution Required | Owner | Target Date |
|---|------|-------|--------------------|-|-------------|
| 1 | [Tool] | [Description] | [What must be done] | [Name] | [Date] |

### High (Should Resolve or Mitigate Before Go-Live)

| # | Tool | Issue | Mitigation | Owner | Target Date |
|---|------|-------|-----------|-------|-------------|
| 1 | [Tool] | [Description] | [Mitigation plan] | [Name] | [Date] |

### Medium / Low (Post-Launch Backlog)

| # | Tool | Issue | Owner | Target Date |
|---|------|-------|-------|-------------|
| 1 | [Tool] | [Description] | [Name] | [Date] |

## Recommendations

[Prioritised actions to achieve or maintain readiness.]

| Priority | Action | Owner | Deadline | Impact if Missed |
|----------|--------|-------|----------|-----------------|
| P1 | [Action] | [Team] | [Date] | [Revenue risk or operational impact] |

## Sign-Off

[Required approvals before go-live.]

| Approver | Role | Decision | Date | Notes |
|----------|------|----------|------|-------|
| [Name] | Head of RevOps | [GO / NO-GO] | [Date] | |
| [Name] | Head of Finance | [GO / NO-GO] | [Date] | |
| [Name] | VP Sales | [GO / NO-GO] | [Date] | |

## Appendices

### A. CRM Configuration Detail

[List all pipeline stages, required fields, and automation rules verified during the assessment.]

### B. Billing Configuration Detail

[Document pricing plans, billing intervals, recognition rules, and tax configuration verified.]

### C. Data Quality Report

[Duplicate count, required field completion rates, and data migration validation results.]
