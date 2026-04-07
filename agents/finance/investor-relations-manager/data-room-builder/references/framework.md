# Framework: Investor Data Room Structure

Standard folder structure and content requirements for a Series Seed through Series B data room.

## Data Room Folder Structure

```
[Company Name] Data Room/
├── 00 Index
│   └── data-room-index.pdf
├── 01 Corporate
│   ├── Formation Documents
│   ├── Board Minutes (last 12 months)
│   ├── Shareholder Agreements
│   └── Organizational Chart
├── 02 Financials
│   ├── Financial Statements (audited if available)
│   ├── Management Accounts (last 12 months)
│   ├── Financial Model
│   └── Cap Table
├── 03 Legal
│   ├── Intellectual Property
│   ├── Key Contracts
│   ├── Litigation and Claims
│   └── Regulatory and Compliance
├── 04 Product and Technology
│   ├── Product Roadmap
│   ├── Technical Architecture
│   └── KPIs and Metrics
├── 05 Team
│   ├── Org Chart
│   ├── Key Employee Bios
│   └── Headcount Plan
└── 06 Market and Customers
    ├── Market Analysis
    ├── Customer List and Testimonials
    └── Competitive Analysis
```

## Document Requirements by Stage

### Series Seed Data Room

| Category | Required Documents | Minimum Standard |
|----------|------------------|-----------------|
| Corporate | Certificate of Incorporation, Bylaws, Board resolutions (option grants, SAFE issuances) | Signed originals |
| Financials | 6-12 months management accounts (P&L, balance sheet, cash), financial model | Month-end close quality |
| Legal | IP assignment agreements from founders, key vendor contracts | All signed |
| Cap Table | Fully diluted cap table including all SAFEs | Carta export or equivalent |
| Team | Founder bios, LinkedIn profiles, advisory board list | Professional quality |
| Product | Product demo, key metrics (DAU/MAU, retention), roadmap | Verified data |

### Series A Data Room

All Seed requirements plus:

| Category | Additional Documents |
|----------|---------------------|
| Financials | 18-24 months management accounts, 3-year financial model, unit economics analysis |
| Legal | All material contracts (customer, vendor, partnership), employment agreements for key staff, IP portfolio |
| Corporate | Board meeting minutes (last 18 months), D&O insurance |
| Compliance | Privacy policy, Terms of Service, GDPR documentation if applicable |
| Customers | Customer list with ARR, logo wall, NPS data, reference customer list |
| Market | TAM/SAM/SOM analysis, competitive landscape, analyst reports |

### Series B Data Room

All Series A requirements plus:

| Category | Additional Documents |
|----------|---------------------|
| Financials | Audited financial statements (2 years), tax returns, cohort analysis |
| Legal | All customer contracts, revenue schedule, ASC 606 documentation |
| Corporate | Board committee charters, governance policies |
| People | Compensation benchmarking, key employee retention risk assessment, succession planning |
| Technical | SOC 2 report or security audit, infrastructure architecture, SLA documentation |

## Document Quality Standards

| Dimension | Standard |
|-----------|---------|
| Naming convention | `YYYY-MM-DD_CompanyName_DocumentTitle_vX.X.pdf` |
| Date currency | Financial statements: < 60 days old. Contracts: current versions. Metrics: < 30 days old |
| Redaction | Remove PII from all customer-facing documents. Remove salary data from org charts. |
| Format | PDF preferred for static documents. Excel/Google Sheets for financial models. |
| Index | Maintain a current index.md with document names, last updated dates, and notes |

## Access Control Tiers

| Tier | Investor Status | Documents Accessible |
|------|---------------|---------------------|
| Tier 1 — Initial Review | First meeting completed, verbal interest | Corporate overview, financial summary, cap table (current round) |
| Tier 2 — Active Diligence | Term sheet or letter of intent in discussion | Full Tier 1 + complete financials, key contracts, customer list |
| Tier 3 — Deep Diligence | Term sheet signed, closing diligence | Full Tier 2 + employment agreements, litigation details, all contracts |
| Current Investors | Board directors, major shareholders | All sections updated per board information rights |

## Staleness Thresholds

| Document Type | Refresh Cycle | Alert at |
|--------------|--------------|---------|
| Financial statements | Monthly | 60+ days old |
| Cap table | Per equity event | Any event not reflected within 30 days |
| Board minutes | After each meeting | 60+ days old |
| Metrics dashboard | Monthly | 30+ days old |
| Customer contracts | Upon execution or renewal | Expired contracts not removed |
| Org chart | On headcount change | 30+ days old during growth |

## Sensitive Document Handling

Documents that should only appear in the data room at deep diligence stage (Tier 3):

- Employee compensation schedules (aggregate only in Tier 2)
- Individual employment agreements
- Litigation settlement agreements with confidentiality clauses
- Pending IP applications
- Detailed customer-by-customer churn data (aggregate in Tier 2)
- Technical security documentation (provide summary only in Tier 1-2)
