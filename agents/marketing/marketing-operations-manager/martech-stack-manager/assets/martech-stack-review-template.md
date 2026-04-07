# Martech Stack Review — [Company Name]

**Version**: 1.0  
**Owner**: Marketing Operations Manager  
**Review Period**: [Quarter / Annual] — YYYY  
**Prepared**: YYYY-MM-DD  

---

## 1. Stack Overview

| Field | Detail |
|-------|--------|
| Total tools in stack | [X] |
| Total annual spend | $[X]K |
| Tools under active use | [X] ([X]%) |
| Tools under-utilized | [X] ([X]%) |
| Tools pending consolidation | [X] |
| Last full audit | [Date] |

---

## 2. Full Stack Inventory

| Category | Tool | Vendor | Annual Cost | Primary Owner | Active Users | Contract Renewal | Usage Status |
|----------|------|--------|-------------|--------------|-------------|-----------------|-------------|
| **Marketing Automation / MAP** | [e.g. HubSpot / Marketo] | [Vendor] | $[X]K | Marketing Ops | [X] | [Date] | Active |
| **CRM** | [e.g. Salesforce] | [Vendor] | $[X]K | Sales Ops | [X] | [Date] | Active |
| **Email Service Provider** | [e.g. Iterable / Klaviyo] | [Vendor] | $[X]K | Lifecycle EM | [X] | [Date] | Active |
| **Paid Media** | [e.g. Google Ads] | Google | $[X]K media | Demand Gen | [X] | Rolling | Active |
| **Paid Social** | [e.g. LinkedIn Campaign Manager] | LinkedIn | $[X]K media | Demand Gen | [X] | Rolling | Active |
| **SEO** | [e.g. Ahrefs / Semrush] | [Vendor] | $[X]K | Content / SEO | [X] | [Date] | Active |
| **Analytics** | [e.g. GA4 / Amplitude] | Google | $0–[X]K | Marketing Ops | [X] | Rolling | Active |
| **Attribution** | [e.g. Rockerbox] | [Vendor] | $[X]K | Marketing Ops | [X] | [Date] | Active |
| **Social Media Management** | [e.g. Sprout Social] | [Vendor] | $[X]K | Social Media | [X] | [Date] | Active |
| **Content Management (CMS)** | [e.g. Webflow / Contentful] | [Vendor] | $[X]K | Web / Content | [X] | [Date] | Active |
| **Webinar / Virtual Events** | [e.g. Goldcast / Zoom Webinars] | [Vendor] | $[X]K | Events | [X] | [Date] | Active |
| **Design** | [e.g. Figma / Canva] | [Vendor] | $[X]K | Design | [X] | [Date] | Active |
| **ABM** | [e.g. 6sense / Demandbase] | [Vendor] | $[X]K | Demand Gen | [X] | [Date] | Under review |
| **Chat / Conversational** | [e.g. Drift / Intercom] | [Vendor] | $[X]K | Marketing Ops | [X] | [Date] | Active |
| **Data Enrichment** | [e.g. Clearbit / ZoomInfo] | [Vendor] | $[X]K | Marketing Ops | [X] | [Date] | Active |

---

## 3. Integration Map

### Critical Integrations (must not break)

| From | To | Data Synced | Sync Frequency | Health |
|------|----|-------------|---------------|--------|
| MAP | CRM | Leads, MQLs, engagement score | Real-time | [ ] Healthy / [ ] Degraded |
| CRM | Attribution | Opportunity data | Daily | [ ] Healthy / [ ] Degraded |
| Email ESP | MAP | Engagement events | Real-time | [ ] Healthy / [ ] Degraded |
| Data enrichment | CRM + MAP | Company + contact data | On create | [ ] Healthy / [ ] Degraded |
| CMS | Analytics | Page view events | Real-time | [ ] Healthy / [ ] Degraded |

---

## 4. Tool Evaluation Scorecard

Rate each tool 1–5 on each dimension (5 = excellent):

| Tool | ROI Delivered | Adoption | Integration Quality | Support Quality | Overall Score | Recommendation |
|------|-------------|----------|--------------------|-----------------|--------------|--------------------|
| [Tool A] | [1–5] | [1–5] | [1–5] | [1–5] | [avg] | Keep / Consolidate / Replace / Evaluate |
| [Tool B] | [1–5] | [1–5] | [1–5] | [1–5] | [avg] | |
| [Tool C] | [1–5] | [1–5] | [1–5] | [1–5] | [avg] | |

---

## 5. Consolidation & Optimization Opportunities

| Opportunity | Tools Involved | Estimated Annual Savings | Risk | Priority | Timeline |
|-------------|---------------|--------------------------|------|----------|---------|
| [e.g. Consolidate MAP + ESP into single platform] | [Tool A] + [Tool B] | $[X]K | Medium | High | Q[X] |
| [e.g. Replace standalone analytics with MAP-native] | [Tool C] | $[X]K | Low | Medium | Q[X] |
| [e.g. Renegotiate data enrichment contract] | [Tool D] | $[X]K | Low | High | [Month] |

---

## 6. Security & Compliance Checklist

- [ ] All tools have completed vendor security questionnaire
- [ ] Data processing agreements (DPAs) signed for GDPR/CCPA-applicable tools
- [ ] PII data mapped — confirmed no unnecessary PII stored in marketing tools
- [ ] SSO / SAML enabled for all enterprise tools
- [ ] Offboarding process confirmed — departing employees removed within 24 hours
- [ ] API keys and credentials stored in secrets manager (not in spreadsheets)

---

## 7. Recommended Actions (Next 90 Days)

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Action 1 — e.g. Evaluate [Tool X] replacement] | [Name] | [Date] | [ ] |
| [Action 2 — e.g. Renegotiate [Tool Y] contract before renewal] | [Name] | [Date] | [ ] |
| [Action 3 — e.g. Fix broken [Integration A] sync] | [Name] | [Date] | [ ] |
| [Action 4 — e.g. Enable SSO for [Tool Z]] | [Name] | [Date] | [ ] |

---

## 8. Stack Roadmap

| Quarter | Initiative | Expected Outcome |
|---------|-----------|-----------------|
| Q[X] | [Add / replace / consolidate tool] | [Benefit] |
| Q[X] | [New integration] | [Benefit] |
| Q[X] | [Renegotiation / renewal] | $[X]K savings |
