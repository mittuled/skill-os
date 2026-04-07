# Financial Systems Requirements Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Controller name] |
| Company Stage | [Seed / Series A / Series B / Growth] |
| Current State | [Spreadsheets only / QuickBooks / NetSuite / Other] |
| Target Go-Live | [YYYY-MM-DD] |
| Version | [1.0] |
| Status | [Draft / Finance Review / CFO Approved] |
| Skill | financial-systems-setup |

## Executive Summary

[2-3 sentences: why the current systems are insufficient, what this document specifies, and the expected outcome.

GUIDANCE: Example: "The company has outgrown QuickBooks Online — multi-entity consolidation, revenue recognition automation, and sub-ledger depth are required for Series B reporting. This document specifies requirements for a migration to NetSuite, targeting a go-live of [date] ahead of the Q4 close cycle. A complete system will reduce close time from 20 days to 10 days and support Series C audit readiness."]

## Current State Assessment

| System | Current Tool | Monthly Volume | Pain Points | Replacement? |
|--------|-------------|--------------|------------|-------------|
| GL / ERP | [QuickBooks / Xero / Spreadsheets] | [N journal entries/mo] | [No department-level P&L, manual rev rec] | [Yes / No] |
| Billing | [Stripe / Manual invoicing / Chargebee] | [N invoices/mo] | [No automated dunning, no GL sync] | [Yes / No] |
| Expense management | [Expensify / Credit card statements] | [N reports/mo] | [No policy enforcement, manual GL coding] | [Yes / No] |
| Payroll | [Gusto / ADP / Manual] | [N employees] | [No GL auto-import] | [Yes / No] |
| FP&A / Reporting | [Google Sheets / Excel] | — | [No version control, no drill-down] | [No — augment] |

## Functional Requirements

### General Ledger / ERP

| Requirement | Priority | Detail |
|------------|---------|--------|
| GAAP-compliant double-entry accounting | Must Have | — |
| Chart of accounts with department and class tracking | Must Have | [Departments: Eng, Sales, Marketing, G&A, COGS] |
| Multi-entity consolidation | [Must Have / Nice to Have] | [Current: 1 entity / Future: 2+ entities] |
| Revenue recognition module (ASC 606) | Must Have | Subscription and services revenue |
| Deferred revenue automation | Must Have | Auto-schedule recognition from billing events |
| Audit trail (immutable, user-stamped) | Must Have | — |
| Bank feed integration | Must Have | [Banks: SVB, JPMorgan, Mercury] |
| Approval workflow configuration | Must Have | 3-level approval: submitter, manager, finance |
| User roles and access controls | Must Have | Segregation of duties: AP, AR, GL, Admin |
| API access for data warehouse export | Nice to Have | — |
| Mobile access | Nice to Have | — |

### Billing Platform

| Requirement | Priority | Detail |
|------------|---------|--------|
| Subscription billing (monthly/annual) | Must Have | — |
| Usage-based billing | [Must Have / Nice to Have] | — |
| Automated invoicing and delivery | Must Have | — |
| Dunning management (payment failure retries) | Must Have | — |
| Proration handling | Must Have | Mid-cycle upgrades/downgrades |
| Revenue recognition sync to GL | Must Have | Automatic journal entry creation |
| MRR/ARR reporting | Nice to Have | — |
| CRM integration (Salesforce / HubSpot) | Nice to Have | — |

### Expense Management

| Requirement | Priority | Detail |
|------------|---------|--------|
| Employee expense submission (mobile) | Must Have | — |
| Spend policy enforcement (limits by category) | Must Have | — |
| Corporate card integration | Must Have | — |
| GL coding at submission | Must Have | — |
| AP integration for reimbursements | Must Have | — |
| Receipt capture and OCR | Nice to Have | — |

## Chart of Accounts Design

### Account Structure

Format: `[Natural Account] — [Department] — [Class/Location]`

Example: `6100 — Sales Compensation — SMB`

### Natural Account Ranges

| Range | Category |
|-------|---------|
| 1000-1999 | Assets |
| 2000-2999 | Liabilities |
| 3000-3999 | Equity |
| 4000-4999 | Revenue |
| 5000-5999 | Cost of Revenue (COGS) |
| 6000-6999 | Sales & Marketing Expense |
| 7000-7999 | Research & Development Expense |
| 8000-8999 | General & Administrative Expense |
| 9000-9999 | Non-operating items |

### Key Accounts

| Account | Number | Type | Notes |
|---------|--------|------|-------|
| Cash — Checking | 1010 | Asset | — |
| Accounts Receivable | 1200 | Asset | Sub-ledger by customer |
| Deferred Revenue — Current | 2100 | Liability | Subscription billing |
| Deferred Revenue — Long-term | 2200 | Liability | Annual contracts >12 months |
| Revenue — Subscription | 4100 | Revenue | Per ASC 606 |
| Revenue — Services | 4200 | Revenue | Per ASC 606 |
| Hosting & Infrastructure | 5100 | COGS | Per customer |
| Customer Support | 5200 | COGS | Allocated per headcount |

## Department Codes

| Code | Department | P&L Owner |
|------|-----------|----------|
| ENG | Engineering | VP Engineering |
| SALES | Sales | VP Sales |
| MKT | Marketing | VP Marketing |
| CS | Customer Success | Head of CS |
| GA | General & Administrative | CFO |
| COGS | Cost of Revenue | CFO |

## System Selection Recommendation

| Tool | Vendor | Best For | Estimated Annual Cost | Recommendation |
|------|--------|---------|----------------------|----------------|
| QuickBooks Online Advanced | Intuit | <$10M ARR, simple structure | [$X,XXX/yr] | [Pre-Series A] |
| NetSuite | Oracle | >$10M ARR, multi-entity | [$XX,XXX-$XXX,XXX/yr] | [Series B+] |
| Sage Intacct | Sage | Multi-entity, nonprofit, professional services | [$XX,XXX/yr] | [Alternative to NetSuite] |

**Recommended**: [System name] — [One-sentence rationale based on stage and complexity]

## Implementation Timeline

| Phase | Activities | Owner | Duration |
|-------|-----------|-------|---------|
| Phase 1: Configuration | Chart of accounts, user roles, bank feeds, approval workflows | Controller + Vendor | [N weeks] |
| Phase 2: Integration | Billing → GL, payroll → GL, expense → GL | Controller + IT | [N weeks] |
| Phase 3: Data Migration | Historical transaction import, opening balance validation | Controller | [N weeks] |
| Phase 4: Testing | End-to-end workflow testing, reconciliation | Finance Team | [N weeks] |
| Phase 5: Training and Go-Live | Team training, go-live, hypercare | Controller + Vendor | [N weeks] |

## Go-Live Checklist

- [ ] Chart of accounts configured and validated
- [ ] User roles and permissions set (segregation of duties verified)
- [ ] Bank feeds connected and reconciled
- [ ] Billing integration tested end-to-end
- [ ] Payroll GL import tested
- [ ] Expense management GL coding mapping complete
- [ ] Opening trial balance validates to prior-period financials
- [ ] Finance team training completed
- [ ] Standard operating procedures documented
- [ ] First test close completed in new system
