# Lead Scoring Model — Meridian AI

| Field | Value |
|---|---|
| Company | Meridian AI |
| ICP | VP/Director Compliance or Risk, fintech/healthcare, 51-500 employees, US-based |
| MQL Threshold | 50 points |
| SQL Threshold | 75 points |
| Dimensions | 4 |
| Sample Leads Scored | 3 |
| Review Cadence | Quarterly, or when MQL-to-SQL rate drops below 30% |
| Skill | lead-scoring-model-builder |

## Scoring Model

### Firmographic Fit (35% weight)

| Signal | Ideal Match | Ideal Points | Acceptable Points |
|---|---|---|---|
| Company Size | 51-500 employees | 15 | 8 |
| Industry | Fintech or healthcare | 12 | 6 |
| Geography | US-based | 8 | 4 |

### Role & Persona Fit (25% weight)

| Signal | Ideal Match | Ideal Points | Acceptable Points |
|---|---|---|---|
| Job Title | VP/Director of Compliance or Risk | 15 | 8 |
| Seniority | Manager+ | 10 | 5 |

### Behavioral Engagement (30% weight)

| Signal | Points | Type |
|---|---|---|
| Free trial started | +30 | Product (custom) |
| Requested a demo | +25 | Standard |
| Integration connected | +20 | Product (custom) |
| Invited a teammate | +15 | Product (custom) |
| Visited pricing page | +15 | Standard |
| Downloaded gated content | +10 | Standard |
| Viewed compliance use case | +8 | Product (custom) |
| Attended a webinar | +8 | Standard |
| Clicked 3+ marketing emails | +6 | Standard |
| Returned to site within 7 days | +5 | Standard |

### Disqualifying Signals (10% weight — negative points)

| Signal | Points |
|---|---|
| Works at known competitor | -30 |
| Student email domain (.edu) | -20 |
| Job title: intern/student/unemployed | -15 |
| Free email provider (gmail, yahoo, etc.) | -10 |

## Sample Lead Scores

| Lead | Score | Status | Key Signals |
|---|---|---|---|
| Rachel Torres | 83 | **SQL** | Ideal firmographic+role fit, free trial started, pricing page, content download, compliance use case viewed |
| Kevin Liu | 16 | **Non-MQL** | Acceptable fit only, free email address (-10), minimal behavioral engagement |
| Sarah Park | 148 | **SQL** | Ideal fit, demo request, trial started, integration connected, teammate invited — highly engaged |

### Rachel Torres — Score Breakdown
- +15 (ideal company size) +15 (ideal role) +30 (free trial) +15 (pricing page) +10 (content download) +8 (compliance use case viewed) = **83 — SQL**

### Kevin Liu — Score Breakdown
- +8 (acceptable company size) +8 (acceptable role) +10 (content download) -10 (free email) = **16 — Non-MQL**

### Sarah Park — Score Breakdown
- +15 (ideal company size) +15 (ideal role) +25 (demo request) +30 (free trial) +20 (integration connected) +15 (pricing page) +15 (invited teammate) +10 (content download) +8 (compliance use case) = **153 — SQL (high intent)**

## Implementation Notes

1. **CRM configuration:** Implement in HubSpot/Salesforce using lead scoring workflows; properties map to each signal above
2. **Sales handoff rule:** Leads reaching 75+ points should trigger immediate SDR outreach within 1 business day
3. **Free trial as leading indicator:** Trial start (30 pts) alone nearly qualifies a lead as MQL — route trial starts to sales notification queue immediately
4. **Recalibration trigger:** If sales rejects >30% of MQLs in any quarter, review closed-won data to identify which signals correlate with conversion and adjust weights
