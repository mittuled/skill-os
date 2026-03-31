# Martech Stack Audit — Meridian AI

| Field | Value |
|---|---|
| Company | Meridian AI |
| Total Tools | 7 |
| Total Annual Spend | $74,400 |
| Integration Issues | 2 (HubSpot ↔ Salesforce sync broken) |
| Renewals ≤90 Days | 3 |
| Low Utilisation Tools | 2 |
| Redundant Tools | 2 |
| Coverage Gaps | SEO, Social Media, Events/Webinars, Chat/Conversion, Data Enrichment |
| Skill | martech-stack-manager |

## Full Stack Overview

| Tool | Category | Annual Cost | Utilisation | CRM Integration | Renewal |
|---|---|---|---|---|---|
| LinkedIn Ads | Paid Advertising | $24,000 | GOOD (80%) | Active | Ongoing |
| Salesforce | CRM | $18,000 | LOW (35%) | Broken | 60 days |
| HubSpot | Marketing Automation | $18,000 | MEDIUM (75%) | Broken | 65 days |
| Mixpanel | Analytics | $8,400 | LOW (20%) | Not integrated | 30 days |
| Mailchimp | Email | $3,600 | MEDIUM (50%) | Not integrated | 120 days |
| Webflow | Content | $2,400 | GOOD (85%) | Active | 200 days |
| Google Analytics 4 | Analytics | $0 | GOOD (90%) | Active | Ongoing |

## Critical Issues

### 1. HubSpot ↔ Salesforce Sync Broken (P0)
**Impact:** Leads from HubSpot not flowing to Salesforce. Marketing and sales are operating on different data. MQL handoff is broken.
**Action:** Fix integration this week. Assign HubSpot admin and Salesforce admin to diagnose and repair sync. Check HubSpot-Salesforce connector version and field mapping.

## Redundant Tools

### Mailchimp + HubSpot Email Module
HubSpot's email module covers the Mailchimp use case. Mailchimp ($3,600/year) is redundant.
**Recommendation:** Migrate remaining Mailchimp campaigns to HubSpot email. Cancel Mailchimp at next renewal (120 days).

### Mixpanel + Google Analytics 4
GA4 covers most of Mixpanel's B2B analytics use cases for free. Mixpanel ($8,400/year) has only 20% utilisation.
**Recommendation:** Audit Mixpanel use cases with Head of Growth before 30-day renewal. If product analytics is the primary use case, consider retaining 2-3 seats only or switching to PostHog (better B2B fit).

## Renewal Actions Required ≤90 Days

| Tool | Cost | Days to Renewal | Action |
|---|---|---|---|
| Mixpanel | $8,400 | 30 days | **URGENT:** Do not auto-renew. Evaluate downsize or cancel. |
| Salesforce | $18,000 | 60 days | Downsize from 10 to 3-5 active seats. Fix HubSpot integration first. |
| HubSpot | $18,000 | 65 days | Negotiate flat renewal (not upgrade) until sync is fixed and team audit completed. |

## Coverage Gaps

The current stack is missing coverage in:
1. **SEO Tools** — No keyword tracking, backlink monitoring, or technical SEO tool (consider Ahrefs or Semrush)
2. **Events & Webinars** — No webinar platform despite webinars being a proven pipeline driver (consider Zoom Webinars)
3. **Data Enrichment** — No contact/company enrichment (consider Clearbit or Apollo)
4. **Chat & Conversion** — No live chat or conversational marketing (consider Intercom or Drift)

## Potential Savings

| Action | Annual Savings |
|---|---|
| Cancel Mailchimp | $3,600 |
| Downsize Mixpanel (10→2 seats or cancel) | $6,700–$8,400 |
| Downsize Salesforce (10→4 seats) | ~$10,800 |
| **Total potential savings** | **~$21,100** |
