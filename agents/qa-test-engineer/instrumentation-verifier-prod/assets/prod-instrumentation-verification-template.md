# Production Instrumentation Verification: [Feature / Release Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | QA / Test Engineer |
| Feature | [Feature or release name] |
| Environment | Production |
| Skill | instrumentation-verifier-prod |
| Status | [Pass / Fail / Conditional Pass] |
| Verification Window | [YYYY-MM-DD HH:MM – HH:MM UTC] (24–48 hours post-deploy) |

## Verdict

**Result**: [PASS / FAIL / CONDITIONAL PASS]
**Critical events verified in production**: [N of N]
**Data quality issues found**: [N]

## Production Event Verification

**Method**: Real user traffic sampled during verification window. No synthetic or test events.

| Event | Expected Volume (based on traffic) | Actual Volume | Rate vs. Expected | Status |
|-------|-----------------------------------|--------------|------------------|--------|
| [page_view] | [~X events/hr at current traffic] | [Y events/hr] | [+/-X%] | [Pass/Fail] |
| [cta_clicked] | | | | |
| [form_submitted] | | | | |
| [purchase_completed] | | | | |

**Volume threshold**: Events firing at < 50% or > 200% of expected volume require investigation.

## Data Quality Spot Check

Sample [N random events] from production analytics for each required event:

| Event | Sample Size | Required Properties Present | Type Errors | PII Detected | Pass? |
|-------|------------|---------------------------|------------|-------------|-------|
| [page_view] | [N=50] | [50/50 (100%)] | [0] | [No] | [Pass] |
| [purchase_completed] | [N=20] | [20/20 (100%)] | [0] | [No] | [Pass] |

## Comparison: QA vs. Production

| Metric | QA Environment | Production | Delta | Acceptable? |
|--------|---------------|-----------|-------|------------|
| Event count (24h) | [X] | [Y] | [+/-Z%] | [Yes / No — investigate] |
| Property completeness | [X%] | [Y%] | | |
| Error event rate | [X%] | [Y%] | | |

**Acceptable delta**: ≤ 10% difference in property completeness between QA and production.

## Downstream System Verification

| System | Events Received | Latency | Data Correct | Status |
|--------|----------------|---------|-------------|--------|
| [Data warehouse] | [Yes / Delayed] | [< X min] | [Yes/No] | [Pass/Fail] |
| [Analytics platform] | | | | |
| [Marketing automation] | | | | |

## Issues Found in Production

| # | Event | Issue Type | Description | Impact | Owner | Ticket |
|---|-------|-----------|-------------|--------|-------|--------|
| 1 | [Event name] | [Missing property / Volume anomaly / PII] | [Specific description] | [Low/Med/High] | [Role] | [Link] |

## Sign-off

**Production instrumentation verified**: [Yes / No — outstanding issues listed above]

**QA Sign-off**: [Name] | Date: [YYYY-MM-DD]
