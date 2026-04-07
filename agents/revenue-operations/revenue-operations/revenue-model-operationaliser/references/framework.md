# Framework: Revenue Model Operationalisation

Defines how common revenue models map to CRM configuration, pipeline stages, and revenue recognition rules.

## Supported Revenue Model Types

| Model | Description | CRM Stage Pattern | Recognition Rule |
|-------|-------------|-------------------|-----------------|
| Subscription — Annual | Fixed annual fee, billed upfront or monthly | MQL → SQL → SQO → Negotiation → Closed-Won | Recognise ratably over contract term |
| Subscription — Monthly | Month-to-month, cancel anytime | Same as annual; shorter cycle | Recognise monthly on invoice |
| Usage-based | Fee based on consumption (API calls, seats, events) | MQL → SQL → Pilot → Usage Review → Expansion | Recognise on usage event; variable monthly |
| One-time + maintenance | Licence fee + annual maintenance | MQL → SQL → SQO → Professional Services → Go-Live | Licence: point-of-sale; maintenance: ratable |
| Marketplace / transactional | Revenue per transaction or marketplace take rate | MQL → Activation → Active (not traditional pipeline) | Recognise on each transaction |

## Pipeline Stage Configuration by Model

### Subscription (Annual or Monthly)

| Stage | Entry Criteria | Exit Criteria | Probability |
|-------|---------------|---------------|-------------|
| MQL | Lead score ≥ threshold | SAL acceptance | 5% |
| SQL | Discovery call completed; BANT partial | Demo scheduled | 20% |
| SQO | Demo/proposal delivered | Evaluation confirmed | 40% |
| Negotiation | Verbal interest; pricing discussed | Contract sent or POC started | 65% |
| Closed-Won | Contract signed | — | 100% |
| Closed-Lost | Active evaluation ended without purchase | — | 0% |

### Usage-Based / Pilot Model

Add a **Pilot** stage between SQL and Closed-Won:

| Stage | Duration | Success Criteria | Failure Path |
|-------|----------|-----------------|-------------|
| Pilot | 14-30 days | Usage threshold met; stakeholder sign-off | Recycle to Closed-Lost with "Product fit" reason |
| Usage Review | After pilot | Expansion pricing agreed | Close at pilot-tier or disqualify |

## CRM Object Model (Salesforce)

| Object | Purpose | Key Fields |
|--------|---------|-----------|
| Lead | Initial marketing contact before qualification | LeadSource, ICP_Score, Status |
| Contact | Person associated with an Account | Role, Decision_Maker |
| Account | Company-level record | Industry, ARR, Tier, Customer_Since |
| Opportunity | Individual deal | Amount, Close_Date, Stage, Product, Term_Length, ARR, Type (New/Renewal/Expansion) |
| Campaign | Marketing campaign tracking | Channel, Start/End Date, Budget, Actual_Cost, Pipeline_Generated |
| Campaign Member | Lead or Contact linked to Campaign | Status, First_Touch, Last_Touch |

## Revenue Recognition Rules

| Model | Recognition Method | Configuration Point |
|-------|-------------------|---------------------|
| Annual subscription, paid upfront | Ratable: 1/12 of ACV per month | Set in billing system (Stripe/Zuora); sync to CRM |
| Monthly subscription | Fully recognised on invoice date | Billing system + CRM monthly close |
| Usage-based | Recognised on consumption event | Usage data pipeline → billing system → CRM |
| One-time professional services | Percentage-of-completion or milestone | Manual recognition schedule in CRM or ERP |
| Multi-year contract | Each year recognised separately; disclose TCV and ACV | Opportunity fields: TCV, ACV, Term Length |

## Finance Alignment Checklist

Before go-live, confirm with finance:

- [ ] ACV (Annual Contract Value) vs. TCV (Total Contract Value) fields defined consistently
- [ ] MRR / ARR calculation methodology agreed (ACV/12 = MRR, or distinct metric?)
- [ ] Expansion vs. New Business vs. Renewal categorisation defined in CRM Opportunity Type field
- [ ] Churn / Contraction recording method defined (credit note, closed-lost at renewal, separate churn object?)
- [ ] Revenue recognition schedule for multi-year deals confirmed with accounting standards (ASC 606 / IFRS 15)
