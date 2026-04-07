# Lead Scoring Model — [Company Name]

**Version**: 1.0  
**Owner**: Marketing Operations Manager  
**Approved by**: VP Marketing + VP Sales  
**Effective Date**: YYYY-MM-DD  
**Review Cadence**: Quarterly  

---

## 1. Model Overview

| Field | Detail |
|-------|--------|
| CRM / MAP Platform | [Salesforce / HubSpot / Marketo / other] |
| Score Range | 0 – 100 |
| MQL Threshold | [X] points |
| SAL Threshold | [X] points (Sales Accepted Lead) |
| Score Decay | Yes — inactive leads decay [X] points/week after [X] days |
| Negative Scoring | Enabled (disqualifying signals subtract points) |

---

## 2. Scoring Dimensions

### Dimension 1: Demographic / Firmographic Fit (max 40 pts)

| Attribute | Value | Points |
|-----------|-------|--------|
| **Job Title** | C-level (CEO, CTO, CFO, CPO) | 15 |
| | VP / SVP / EVP | 12 |
| | Director | 10 |
| | Manager | 5 |
| | Individual Contributor | 2 |
| | Unknown / Other | 0 |
| **Company Size** | 201–2,000 employees | 15 |
| | 2,001–10,000 employees | 12 |
| | 10,001+ employees | 10 |
| | 51–200 employees | 5 |
| | 1–50 employees | 2 |
| **Industry** | [Primary target industry] | 10 |
| | [Secondary target industry] | 7 |
| | [Tertiary target industry] | 4 |
| | Other / Unknown | 0 |

### Dimension 2: Behavioural Engagement (max 40 pts)

| Activity | Points | Time Window |
|----------|--------|-------------|
| Requested a demo | 25 | Any |
| Viewed pricing page (2+ times) | 20 | Last 30 days |
| Downloaded high-intent content (e.g. ROI calculator, comparison guide) | 15 | Last 60 days |
| Attended live webinar | 12 | Last 60 days |
| Opened + clicked 3+ emails in sequence | 10 | Last 30 days |
| Downloaded mid-funnel content (eBook, guide) | 8 | Last 60 days |
| Attended virtual event / conference | 8 | Last 90 days |
| Viewed product page (3+ times) | 7 | Last 30 days |
| Opened email (single open, no click) | 2 | Last 30 days |
| Visited blog only (no product pages) | 1 | Last 30 days |

### Dimension 3: Negative / Disqualifying Signals (subtracted)

| Signal | Points |
|--------|--------|
| Competitor domain email | –25 |
| Free email provider (gmail, yahoo, etc.) if company email expected | –15 |
| Student / academic email | –15 |
| Unsubscribed from email | –20 |
| Marked email as spam | –30 |
| Job title = intern / student | –10 |
| Company size < 10 employees (if SMB is not ICP) | –10 |

---

## 3. Score Thresholds & Routing

| Score Range | Classification | Action |
|-------------|---------------|--------|
| 0 – 29 | Cold Lead | Nurture sequence only; no SDR outreach |
| 30 – 49 | Warm Lead | Add to targeted nurture track; monitor activity |
| 50 – 69 | Marketing Qualified Lead (MQL) | Alert SDR; SDR outreach within 1 business day |
| 70 – 84 | Hot MQL | Priority SDR outreach same business day |
| 85 – 100 | Sales Ready / SAL | Direct-to-AE routing; immediate outreach |

---

## 4. Score Decay Rules

| Condition | Decay Rate |
|-----------|-----------|
| No email engagement for 30 days | –3 pts/week |
| No website activity for 45 days | –5 pts/week |
| No activity of any kind for 60 days | –8 pts/week |
| Score floor | 0 (never goes negative) |
| Score reset | Manual by SDR/AE; or 6 months of no activity |

---

## 5. Model Validation Metrics

Review quarterly against these benchmarks:

| Metric | Healthy Range | Current | Status |
|--------|--------------|---------|--------|
| MQL-to-SAL conversion rate | 40–65% | [X]% | [ ] |
| SAL-to-Opportunity conversion rate | 50–70% | [X]% | [ ] |
| MQL-to-Closed-Won rate | 8–15% | [X]% | [ ] |
| Average days from MQL to first contact | ≤ 1 business day | [X] days | [ ] |
| False positive rate (MQLs rejected by sales) | < 25% | [X]% | [ ] |
| Score distribution: % of leads as MQL | 5–15% of all leads | [X]% | [ ] |

---

## 6. Change Log

| Version | Date | Change Description | Owner | Approved By |
|---------|------|-------------------|-------|-------------|
| 1.0 | [Date] | Initial model launch | [Name] | [Name] |
| [Next] | | | | |

---

## 7. Implementation Checklist

- [ ] Scoring fields mapped in CRM / MAP
- [ ] Negative scoring rules active
- [ ] Score decay automation built and tested
- [ ] MQL threshold triggers SDR alert / task
- [ ] SAL threshold triggers direct-to-AE routing
- [ ] Sales team briefed on scoring logic and thresholds
- [ ] Baseline metrics captured pre-launch
- [ ] Quarterly review meeting scheduled
