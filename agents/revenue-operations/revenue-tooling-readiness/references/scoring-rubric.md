# Scoring Rubric: Revenue Tooling Readiness

## Rubric Metadata

| Field | Value |
|-------|-------|
| Version | 1.0.0 |
| Skill | revenue-tooling-readiness |
| Agent | Revenue Operations |
| Purpose | Assess whether all revenue-facing tools are correctly configured, integrated, and validated before go-live |

## Criteria and Weights

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| CRM Configuration | 30% | CRM is the system of record; misconfiguration breaks pipeline tracking, attribution, and reporting |
| Billing System Accuracy | 25% | Billing errors cause revenue leakage that may not be detected for weeks |
| End-to-End Integration | 25% | Individual tools can work in isolation while the deal-to-cash flow fails at integration points |
| Reporting and Analytics | 10% | Broken reports hide revenue issues and disable executive decision-making at launch |
| Data Quality | 10% | Dirty data entering at go-live compounds exponentially; clean data is foundational |

## Scoring Scale

| Score | Label | Description |
|-------|-------|-------------|
| 9–10 | Excellent | Fully configured, tested end-to-end, no issues found |
| 7–8 | Good | Minor gaps found and resolved; all critical paths validated |
| 5–6 | Adequate | Some issues remain; go-live possible with mitigations documented |
| 3–4 | Poor | Multiple failures; go-live should be delayed until resolved |
| 1–2 | Critical | Major configuration missing or end-to-end test failed; block go-live |
| 0 | Not assessed | Criterion not evaluated in this review |

## Grade Bands

| Grade | Score Range | Go / No-Go |
|-------|-------------|------------|
| A+ | 93–100 | GO |
| A | 85–92 | GO |
| B | 75–84 | GO with monitoring |
| C | 60–74 | CONDITIONAL GO — mitigations required |
| D | 45–59 | NO-GO — remediation required |
| F | 0–44 | NO-GO — significant rework required |

## Criterion Detail

### 1. CRM Configuration (30%)

| Score Range | Signal |
|-------------|--------|
| 9–10 | All pipeline stages, fields, and automation rules configured; lead routing tested; attribution tracking verified |
| 7–8 | Pipeline stages correct; 1-2 minor field gaps; automation rules fire correctly on test records |
| 5–6 | Core stages configured; some required fields missing; automation rules partially tested |
| 3–4 | Missing key stages or fields; automation rules not tested; attribution tracking incomplete |
| 1–2 | CRM not configured for the new model; multiple critical fields or stages absent |

### 2. Billing System Accuracy (25%)

| Score Range | Signal |
|-------------|--------|
| 9–10 | Test transactions processed successfully; invoices generated correctly; revenue recognition schedules accurate |
| 7–8 | Test transaction succeeded; minor invoice format issue (non-blocking); recognition rules validated |
| 5–6 | Test transaction completed; one revenue recognition edge case unvalidated; billing team aware |
| 3–4 | Test transaction partially successful; invoice amounts off; recognition configuration incomplete |
| 1–2 | Test transaction failed; billing system not configured for the new pricing model |

### 3. End-to-End Integration (25%)

| Score Range | Signal |
|-------------|--------|
| 9–10 | Full deal-to-cash flow tested: CRM → CPQ → billing → revenue recognition; all data syncs correctly |
| 7–8 | End-to-end test passed; 1 minor data sync delay (< 15 min); no data loss |
| 5–6 | End-to-end test mostly passed; one integration field mapping incorrect; workaround documented |
| 3–4 | Integration test failed at one stage (e.g., CRM → billing sync broken); manual workaround in place |
| 1–2 | Integration not configured; deal-to-cash flow not testable end-to-end |

### 4. Reporting and Analytics (10%)

| Score Range | Signal |
|-------------|--------|
| 9–10 | All key reports load correctly; data refreshes on schedule; attribution reports show correct first/last touch |
| 7–8 | Core pipeline and revenue reports work; 1 secondary report has a minor data issue |
| 5–6 | Main pipeline report functional; attribution report incomplete; revenue dashboard pending |
| 3–4 | Key reports broken or returning incorrect data; manual exports required at launch |
| 1–2 | Reporting not configured; no visibility into pipeline or revenue at go-live |

### 5. Data Quality (10%)

| Score Range | Signal |
|-------------|--------|
| 9–10 | < 2% duplicate records; all required fields populated; no orphan records; deduplication rule active |
| 7–8 | < 5% duplicate rate; required field completion > 95%; minor orphan records cleaned |
| 5–6 | 5–10% duplicate rate; required fields > 85% complete; deduplication scheduled |
| 3–4 | > 10% duplicate rate; missing required fields on > 15% of records; data migration quality issues |
| 1–2 | Data migration not validated; high duplicate rate; corrupted or incomplete records present |
