# CRM Configuration Record

**CRM Platform**: `[HubSpot / Salesforce / Pipedrive / Other]`
**Configuration Owner**: `[Revenue Operations]`
**Date**: `YYYY-MM-DD`
**Version**: `v1.0 — Initial Setup`

---

## 1. Pipeline Configuration

### Pipeline: `[Primary Sales Pipeline Name]`

| Stage # | Stage Name | Entry Criteria | Exit Criteria | Probability | Target Duration |
|---------|-----------|---------------|--------------|-------------|----------------|
| 1 | `[e.g., Lead Qualified]` | `[Criteria]` | `[Criteria]` | `10%` | `[# days]` |
| 2 | `[e.g., Discovery Completed]` | `[Criteria]` | `[Criteria]` | `25%` | `[# days]` |
| 3 | `[e.g., Proposal Sent]` | `[Criteria]` | `[Criteria]` | `50%` | `[# days]` |
| 4 | `[e.g., Contract Sent]` | `[Criteria]` | `[Criteria]` | `75%` | `[# days]` |
| 5 | `[e.g., Closed Won]` | `[Criteria]` | `[Criteria]` | `100%` | — |
| — | `[e.g., Closed Lost]` | `[Criteria]` | — | `0%` | — |

---

## 2. Custom Field Schema

### Contact Fields

| Field Name | Type | Values / Format | Required? | Purpose |
|-----------|------|----------------|-----------|---------|
| `Lead Source` | Dropdown | `Organic / Paid / Outbound / Partner / Referral / Event` | Yes | Attribution tracking |
| `ICP Score` | Number | `1–100` | No | Lead quality scoring |
| `[Custom Field]` | `[Type]` | `[Values]` | `Yes / No` | `[Purpose]` |

### Deal Fields

| Field Name | Type | Values / Format | Required? | Purpose |
|-----------|------|----------------|-----------|---------|
| `Deal Source` | Dropdown | `Inbound / Outbound / Partner / Expansion` | Yes | Attribution |
| `Product Line` | Dropdown | `[List product lines]` | Yes | Revenue segmentation |
| `Contract Start Date` | Date | `YYYY-MM-DD` | Yes | Revenue recognition |
| `Contract Term` | Dropdown | `Monthly / Annual / Multi-year` | Yes | Recognition model |
| `ACV` | Currency | `$` | Yes | Annual contract value |
| `TCV` | Currency | `$` | Yes | Total contract value |
| `Close Date` | Date | `YYYY-MM-DD` | Yes | Forecast date |
| `[Custom Field]` | `[Type]` | `[Values]` | `Yes / No` | `[Purpose]` |

---

## 3. Automation Rules

| Automation Name | Trigger | Action | Status |
|----------------|---------|--------|--------|
| `Deal stage notification` | Deal moves to Contract Sent | Notify Account Executive + Manager | `Active / Inactive` |
| `Stale deal alert` | No activity on deal for 14 days | Create task for AE to follow up | `Active / Inactive` |
| `Close date validation` | Deal created without close date | Block save; require close date | `Active / Inactive` |
| `Win notification` | Deal marked Closed Won | Slack notification to #wins + CRM log | `Active / Inactive` |
| `[Automation name]` | `[Trigger condition]` | `[Action performed]` | `Active / Inactive` |

---

## 4. Integration Connections

| Integration | Purpose | Status | Data Flow | Last Tested |
|------------|---------|--------|-----------|------------|
| `[Marketing automation]` | Lead sync from marketing to CRM | `Active / Pending` | `Marketing → CRM` | `YYYY-MM-DD` |
| `[Email / Calendar]` | Activity logging | `Active / Pending` | `Bidirectional` | `YYYY-MM-DD` |
| `[Billing system]` | Contract and revenue data | `Active / Pending` | `CRM → Billing` | `YYYY-MM-DD` |
| `[Slack]` | Deal notifications | `Active / Pending` | `CRM → Slack` | `YYYY-MM-DD` |

---

## 5. User Roles and Permissions

| Role | Access Level | Users Assigned | Capabilities |
|------|-------------|---------------|-------------|
| Admin | Full access | `[Names]` | All settings, reporting, export |
| Manager | Read all + edit assigned | `[Names]` | View all deals, edit team records |
| Rep / AE | Edit own + read team | `[Names]` | Edit own deals and contacts |
| Read-Only | View only | `[Names]` | Reports and dashboards |

---

## 6. Data Import Log

| Dataset | Source | Records | Import Date | Deduplication Method | Quality Issues |
|---------|--------|---------|------------|---------------------|---------------|
| `Contacts` | `[Google Sheets / Old CRM / CSV]` | `##,###` | `YYYY-MM-DD` | `Email address match` | `[e.g., 123 duplicates merged]` |
| `Companies` | `[Source]` | `##,###` | `YYYY-MM-DD` | `Domain match` | `[Notes]` |
| `Deals` | `[Source]` | `##` | `YYYY-MM-DD` | `Manual review` | `[Notes]` |

---

## 7. End-to-End Test Results

| Test Scenario | Steps | Expected Outcome | Actual Outcome | Pass? |
|--------------|-------|-----------------|---------------|-------|
| Create contact → qualify → create deal | `[Steps]` | Deal appears in pipeline | `[Result]` | `[ ] Pass  [ ] Fail` |
| Move deal through all stages | `[Steps]` | Automations fire correctly | `[Result]` | `[ ] Pass  [ ] Fail` |
| Close deal → check integrations | `[Steps]` | Billing notified; Slack fires | `[Result]` | `[ ] Pass  [ ] Fail` |
| Import lead from marketing | `[Steps]` | Lead appears with source field set | `[Result]` | `[ ] Pass  [ ] Fail` |

---

## 8. Known Gaps / Deferred Items

| Item | Reason Deferred | Target Date |
|------|----------------|-------------|
| `[e.g., Billing integration pending API access]` | `[Reason]` | `YYYY-MM-DD` |

---

*Template version 1.0 — Revenue Operations*
