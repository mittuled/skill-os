# Revenue Model Configuration Record

**Prepared By**: `[Revenue Operations]`
**Date**: `YYYY-MM-DD`
**Version**: `[v1.0 Initial / v#.# Update: reason]`
**Finance Sign-Off**: `[ ] Pending  [ ] Approved — Date: YYYY-MM-DD`

---

## 1. Revenue Model Summary

| Revenue Model Type | Active? | Notes |
|-------------------|---------|-------|
| `[ ]` Subscription (recurring) | — | Monthly / Annual billing |
| `[ ]` Usage-based | — | Per seat / per event / per GB |
| `[ ]` One-time (professional services) | — | Project-based |
| `[ ]` Marketplace / transactional | — | % of GMV |
| `[ ]` Hybrid | — | Combination of above |

**Primary Model**: `[Model Name]`
**Pricing Structure**:
```
[Describe pricing tiers, plans, or usage thresholds here.
Example: "Starter $49/mo (up to 5 seats), Growth $199/mo (up to 25 seats), Enterprise custom"]
```

---

## 2. Pipeline Stage Mapping

| Stage # | CRM Stage Name | Revenue Model Meaning | Probability | Entry Criteria | Exit Criteria |
|---------|--------------|----------------------|-------------|---------------|--------------|
| 1 | `[Stage Name]` | `[What this stage means in the revenue model]` | `##%` | `[Entry criteria]` | `[Exit criteria]` |
| 2 | `[Stage Name]` | `[Meaning]` | `##%` | `[Entry criteria]` | `[Exit criteria]` |
| 3 | `[Stage Name]` | `[Meaning]` | `##%` | `[Entry criteria]` | `[Exit criteria]` |
| 4 | `[Stage Name]` | `[Meaning]` | `##%` | `[Entry criteria]` | `[Exit criteria]` |
| 5 | `Closed Won` | Deal executed; billing initiated | `100%` | Signed agreement | — |
| — | `Closed Lost` | Opportunity will not progress | `0%` | Loss confirmed | — |

---

## 3. Deal Field Schema

| Field | Type | Purpose | Revenue Recognition Link |
|-------|------|---------|------------------------|
| `ACV` | Currency | Annual contract value | Core forecast metric |
| `TCV` | Currency | Total contract value over term | Long-term pipeline view |
| `MRR Impact` | Currency | Monthly recurring revenue delta | ARR tracking |
| `Contract Start Date` | Date | When billing begins | Recognition start |
| `Contract End Date` | Date | When billing ends | Recognition end |
| `Billing Frequency` | Dropdown: Monthly / Annual | Payment cadence | Cash flow modelling |
| `Revenue Type` | Dropdown: New / Expansion / Renewal | Revenue motion | Segmentation |
| `[Custom Field]` | `[Type]` | `[Purpose]` | `[Link]` |

---

## 4. Revenue Recognition Rules

| Revenue Type | Recognition Method | Trigger | Accounting Standard |
|-------------|-------------------|---------|-------------------|
| Annual subscription (prepaid) | Ratably over contract term | Contract start date | ASC 606 / IFRS 15 |
| Monthly subscription | In the billing period | Invoice date | ASC 606 / IFRS 15 |
| Usage-based | At point of usage | Usage event | ASC 606 |
| Professional services (milestone) | At milestone completion | Milestone sign-off | ASC 606 |
| Professional services (time & materials) | As incurred | Timesheet or delivery | ASC 606 |

**Recognition Rules Configuration in CRM/Billing System**:
```
[Describe how recognition rules are configured: fields used, automations, or billing system settings
that implement the above rules. Reference specific system settings if applicable.]
```

---

## 5. Forecast Configuration

| Forecast Category | Stage(s) Included | Probability Range | Weighting |
|------------------|------------------|------------------|----------|
| Commit | `[Stage names]` | `75–100%` | `1.0x` |
| Best Case | `[Stage names]` | `50–74%` | `0.75x` |
| Pipeline | `[Stage names]` | `25–49%` | `0.5x` |
| Early Stage | `[Stage names]` | `<25%` | `0.0x` |

---

## 6. Finance Validation Test Cases

| Test Case | Deal Setup | Expected CRM Outcome | Expected Finance Outcome | Validated? |
|-----------|-----------|---------------------|------------------------|-----------|
| Annual subscription, $24,000 ACV | Contract start Jan 1; annual billing | ACV: $24,000; TCV: $24,000 | $2,000 MRR recognised monthly | `[ ] Yes  [ ] No` |
| Multi-year, $60,000 TCV | 3-year; $20,000 ACV | ACV: $20,000; TCV: $60,000 | $1,667 MRR recognised monthly | `[ ] Yes  [ ] No` |
| Expansion mid-year | Upgrade from $12k to $24k ACV | MRR Impact: +$1,000/month | Pro-rated recognised from upgrade date | `[ ] Yes  [ ] No` |
| `[Custom test case]` | `[Setup]` | `[Expected CRM]` | `[Expected Finance]` | `[ ] Yes  [ ] No` |

---

## 7. Open Gaps

| Gap | Impact | Workaround | Owner | Target Resolution |
|-----|--------|-----------|-------|------------------|
| `[e.g., Billing system cannot handle usage-based mid-cycle changes]` | `[Impact on recognition]` | `[Manual process in place]` | `[Owner]` | `YYYY-MM-DD` |

---

## 8. Approval

| Approver | Role | Date | Approved? |
|---------|------|------|----------|
| `[Name]` | Head of Sales | `YYYY-MM-DD` | `[ ] Yes  [ ] No` |
| `[Name]` | Head of Finance | `YYYY-MM-DD` | `[ ] Yes  [ ] No` |
| `[Name]` | Revenue Operations | `YYYY-MM-DD` | `[ ] Yes  [ ] No` |

---

*Template version 1.0 — Revenue Operations*
