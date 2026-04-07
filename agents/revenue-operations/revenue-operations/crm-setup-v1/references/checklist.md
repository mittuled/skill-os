# CRM Setup Checklist: crm-setup-v1

Use this checklist when configuring a CRM from scratch or setting up a new pipeline for an existing CRM.

## Phase 1 — Pipeline and Stage Configuration

- [ ] Define pipeline stages aligned to the actual sales process (not a generic template)
- [ ] Document entry and exit criteria for each stage:
  - **Lead** → ICP match confirmed, contact information verified
  - **MQL** → Lead score threshold met (define score)
  - **SQL** → Sales-qualified via discovery call; budget, authority, need, timeline confirmed
  - **SQO** → Sales Qualified Opportunity; formal proposal or demo delivered
  - **Negotiation** → Contract/pricing discussion underway
  - **Closed-Won** → Contract signed, payment terms agreed
  - **Closed-Lost** → Lost with reason code recorded
- [ ] Pipeline stages entered in CRM with correct order
- [ ] Stage probability percentages configured for forecasting

## Phase 2 — Custom Fields

Core fields required before go-live:

| Object | Field | Type | Required? |
|--------|-------|------|----------|
| Lead / Contact | Lead Source | Dropdown | Yes |
| Lead / Contact | ICP Score | Number | Yes |
| Account | Industry | Dropdown | Yes |
| Account | Employee Count | Number | Yes |
| Account | ARR | Currency | Yes |
| Opportunity | Deal Size (ARR) | Currency | Yes |
| Opportunity | Product / Tier | Dropdown | Yes |
| Opportunity | Close Date | Date | Yes |
| Opportunity | Lead Source | Lookup | Yes |
| Opportunity | Lost Reason | Dropdown | Yes (on Closed-Lost) |
| Opportunity | Multi-year? | Boolean | Yes |
| Campaign | Channel | Dropdown | Yes |

- [ ] All required fields created and field-level validation rules configured
- [ ] Picklist values defined for all dropdown fields (Industry, Lead Source, Lost Reason, Product)
- [ ] Required fields enforced at stage entry (e.g., Close Date required to advance to SQO)

## Phase 3 — Automation Rules

- [ ] New lead auto-assignment rule configured (round-robin or territory-based)
- [ ] Lead scoring rules configured (minimum: lead source + industry + company size + engagement)
- [ ] MQL threshold triggers task creation for SDR outreach
- [ ] Stage transition triggers task creation (e.g., advance to Negotiation → create contract task)
- [ ] Closed-Won triggers: CS handoff notification, onboarding task, billing setup task
- [ ] Stale deal alert: opportunity in same stage > 14 days → alert to owner and manager
- [ ] Duplicate detection rule enabled for Leads and Contacts

## Phase 4 — Integrations

- [ ] Marketing automation platform connected (HubSpot / Marketo / Pardot)
- [ ] Email sync configured (Gmail/Outlook → CRM activity log)
- [ ] Calendar sync configured (meeting activities logged automatically)
- [ ] Billing/subscription system connected (Stripe / Chargebee / Zuora)
- [ ] Data flow verified: marketing lead → CRM contact → opportunity without manual re-entry

## Phase 5 — Data Migration

- [ ] Source data audit completed (identify duplicates, missing fields, formatting issues)
- [ ] Field mapping document created (source field → CRM field)
- [ ] Test import with 50-record sample; review for errors
- [ ] Full import executed in non-production environment first
- [ ] Duplicate records merged post-import
- [ ] Data quality report generated and reviewed

## Phase 6 — End-to-End Test

- [ ] Create a test lead; verify auto-assignment fires
- [ ] Advance test lead to MQL; verify lead score threshold triggers SDR task
- [ ] Convert to Opportunity; verify stage entry criteria enforced
- [ ] Advance through all stages; verify automations fire at each transition
- [ ] Close as Won; verify CS handoff task created and billing notification sent
- [ ] Close as Lost; verify lost reason field required

## Quality Gate

Before declaring setup complete:

- [ ] All 6 phases completed
- [ ] Test deal processed end-to-end without errors
- [ ] Sales team lead walkthrough completed
- [ ] CRM administrator documented and access granted
