# Checklist: financial-systems-setup

Step-by-step checklist for implementing the financial systems stack from requirements through go-live.

## Requirements Assessment

- [ ] Document transaction volume: invoices per month, payroll headcount, billing transactions, bank feeds
- [ ] Document reporting requirements: GAAP P&L, department-level P&L, investor metrics, board pack
- [ ] Document compliance requirements: ASC 606 revenue recognition, ASC 842 leases, multi-entity consolidation
- [ ] Document integration requirements: billing platform, CRM, bank feeds, payroll system, expense tool
- [ ] Determine current pain points with existing system (spreadsheets or prior tool)
- [ ] Size the company against system tiers:
  - [ ] Under $2M ARR / under 20 employees: QuickBooks Online
  - [ ] $2M–$20M ARR / 20–150 employees: QuickBooks Online Advanced or Xero
  - [ ] Above $20M ARR or multi-entity: NetSuite, Sage Intacct
- [ ] Confirm system selection with CFO before procurement

## Chart of Accounts Design

- [ ] Design the natural account structure aligned to GAAP financial statement line items
- [ ] Create account number ranges by category (1000s = assets, 2000s = liabilities, 3000s = equity, 4000s = revenue, 5000s = COGS, 6000–7000s = OpEx)
- [ ] Design department/class dimension for department-level P&L (Engineering, Sales, Marketing, G&A, Product)
- [ ] Design location or entity dimension for multi-entity consolidation
- [ ] Include accounts required for deferred revenue, prepaid expenses, capitalized software, and lease liabilities
- [ ] Document the chart of accounts with account definitions and examples of transactions posted to each
- [ ] Obtain CFO review and sign-off before loading into the system

## GL System Configuration

- [ ] Set up the chart of accounts per the approved design
- [ ] Configure fiscal year settings and period structure
- [ ] Set up approval workflows aligned to the delegation of authority policy
- [ ] Configure user roles and permissions (view-only, data entry, approver, admin)
- [ ] Implement segregation of duties: AP data entry ≠ AP approver ≠ payment processor
- [ ] Connect bank feeds for all operating accounts and credit cards
- [ ] Test a complete close cycle (journal entry → trial balance → financial statements) before go-live

## Billing System Integration

- [ ] Configure subscription billing plans and invoice templates
- [ ] Set up usage-based billing metering if applicable
- [ ] Configure revenue recognition rules per ASC 606 (ratable vs. milestone vs. usage)
- [ ] Configure the GL integration: map billing product codes to GL revenue accounts
- [ ] Test automated journal entry posting for a full billing cycle
- [ ] Reconcile a billing period: billing system totals should agree to GL revenue and deferred revenue

## Expense Management Setup

- [ ] Deploy expense management tool (Expensify, Ramp, Brex, or equivalent)
- [ ] Configure spend categories with GL mapping for automatic coding
- [ ] Set policy controls: receipt required above $25, manager approval above $100, CFO approval above $500
- [ ] Configure auto-approval for recurring low-risk categories within policy limits
- [ ] Enable corporate card integration for automatic transaction import
- [ ] Test the full expense-to-GL workflow: submission → approval → reimbursement → GL posting

## Historical Data Migration

- [ ] Agree on migration scope: date range, account balances vs. transaction-level detail
- [ ] Export data from the prior system in a clean, structured format
- [ ] Map prior system accounts to new chart of accounts
- [ ] Import opening trial balance as of the migration date
- [ ] Reconcile opening balances against the prior-period financial statements (line by line)
- [ ] Confirm total assets = total liabilities + equity after migration
- [ ] Test that historical reports in the new system agree to prior-period reports

## Testing and Go-Live

- [ ] Test complete AP workflow: vendor setup → invoice entry → approval → payment → GL posting
- [ ] Test complete revenue cycle: invoice → payment → deferred revenue → recognition
- [ ] Test complete expense cycle: submission → approval → reimbursement → GL posting
- [ ] Test monthly close: lock prior period; confirm no postings after lock
- [ ] Test financial statement output: income statement, balance sheet, cash flow
- [ ] Train finance team: GL navigation, journal entry, reconciliation, reporting
- [ ] Document standard operating procedures for each recurring workflow
- [ ] Confirm go-live date with CFO and team; set a parallel run period if volume justifies it
