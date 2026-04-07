# CRM Setup v1 Readiness — HubSpot CRM

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | Revenue Operations |
| Platform | HubSpot CRM |
| Overall Completeness | 79% |
| Verdict | INCOMPLETE |
| Skill | crm-setup-v1 |

## Recommendation

**INCOMPLETE** — 3 components missing and end-to-end test not yet passed. Do not onboard the sales team until all missing items are configured and end-to-end test completes successfully.

---

## Component Completeness

| Component | Completeness | Missing Items |
|---|---|---|
| Pipeline Stages | 100% | None |
| Deal Fields | 83% | `contract_term` |
| Automations | 75% | `closed_won_handoff_trigger` |
| Integrations | 67% | `billing_system` |

---

## Missing Components

### Deal Fields: `contract_term`

Contract term (monthly/annual/multi-year) is required for revenue recognition and churn prediction. Add as a dropdown field with values: monthly, annual, 2-year, multi-year.

---

### Automation: `closed_won_handoff_trigger`

No automation exists to notify customer success or onboarding when a deal is marked Closed Won. This is the highest-risk gap — without it, new customers will fall through the cracks during the first week post-sale.

**Configure:** When deal stage = Closed Won → create onboarding task, notify CS rep assigned to territory, send internal Slack notification to #wins channel.

---

### Integration: `billing_system`

The billing system (Stripe/Chargebee) is not connected. Without this integration, closed deals will require manual invoice creation — a scaling bottleneck and source of billing errors.

**Action:** Request API keys from finance team; configure HubSpot → Stripe integration using HubSpot Payments or Zapier connector.

---

## End-to-End Test Status: NOT PASSED

A test deal has not been processed through the full pipeline. This must be completed before go-live — even a fully configured CRM can have silent integration failures that only appear when a real deal flows through.

**Test checklist:**
1. Create a test contact and company in HubSpot
2. Create a deal and advance it through all 7 stages
3. Confirm stage transition notifications fire at each step
4. Confirm overdue alert fires when close date passes
5. Confirm closed-won handoff trigger fires (after adding it)
6. Confirm deal data flows to billing system (after connecting it)

---

## Data Migration Status: In Progress

Current Google Sheet data has not been fully migrated. Complete migration and run deduplication before onboarding the sales team to prevent duplicate contacts and deal records.

---

## Next Steps

| Priority | Action | ETA |
|---|---|---|
| 1 | Add `contract_term` field | Today |
| 2 | Configure `closed_won_handoff_trigger` automation | Today |
| 3 | Connect billing system integration | 2 days |
| 4 | Complete data migration + dedup | 3 days |
| 5 | Run end-to-end test deal | After #3-4 complete |
| 6 | Sales team onboarding | After all above complete |
