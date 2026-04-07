# Framework: data-room-v1-builder

Defines the minimum viable document set, folder structure, and access controls for a first investor data room at the early-stage (pre-seed or seed).

## Minimum Viable Document Set

For a first-time data room, the following documents are required before investor outreach begins:

### Tier 1 — Must-Have (Cannot Send Data Room Without These)

| Document | Description | Owner | Common Gap |
|----------|-------------|-------|------------|
| Certificate of Incorporation | Delaware C-Corp formation document | Legal / Founder | Missing for LLC or foreign entities |
| Bylaws | Corporate governance rules | Legal / Founder | Often unsigned or using template without review |
| Cap table | Fully-diluted ownership summary | IR Manager / FP&A | Often a spreadsheet rather than Carta/Pulley |
| Financial projections | 2-3 year P&L and cash flow model | FP&A | Rarely exists at pre-seed; create a simple model |
| Pitch deck | Current investor presentation | CEO | Usually exists; may need data room version without notes |
| Founder bios / LinkedIn | Summary of each founder's background | Founders | Often omitted — always include |

### Tier 2 — Should-Have (Include If They Exist)

| Document | Description |
|----------|-------------|
| Most recent financial statements | P&L, balance sheet, and cash flow — even if unaudited |
| Material contracts | Any customer contracts, partnership agreements, or LOIs over $10K ACV |
| IP assignment agreements | Confirm IP is owned by the company, not individuals |
| Employee offer letters (templates) | Shows compensation structure and equity policy |
| Product screenshots or demo video | Tangible evidence of product progress |
| Customer references or NPS data | Early evidence of product-market fit |

### Tier 3 — Nice-to-Have (Add as Available)

| Document | Description |
|----------|-------------|
| Board minutes | If a formal board exists |
| Technology architecture overview | 1-page summary of the tech stack and scalability |
| Market sizing analysis | TAM/SAM/SOM with methodology |
| Competitive landscape | Feature comparison or positioning map |

## Folder Structure

```
📁 Data Room — [Company Name]
├── 📁 01 - Overview
│   ├── Pitch Deck — [Company] — [Date].pdf
│   └── Executive Summary — 1 Page.pdf
├── 📁 02 - Corporate
│   ├── Certificate of Incorporation.pdf
│   ├── Bylaws.pdf
│   └── Board Resolutions — Summary.pdf
├── 📁 03 - Cap Table
│   ├── Cap Table — Fully Diluted — [Date].pdf
│   └── SAFE Register — [Date].pdf (if applicable)
├── 📁 04 - Financials
│   ├── Financial Projections — [FY] — [Date].xlsx
│   ├── Financial Statements — [Most Recent Period].pdf
│   └── Key Metrics Dashboard — [Date].pdf
├── 📁 05 - Legal
│   ├── IP Assignment Agreements — Summary.pdf
│   └── Material Contracts — [Redacted].pdf
├── 📁 06 - Team
│   ├── Founder Bios.pdf
│   └── Org Chart — [Date].pdf
└── 📁 07 - Product
    ├── Product Screenshots — [Date].pdf
    └── Demo Video Link.txt (link to Loom or similar)
```

## Document Naming Convention

Every file must follow: `[Category] — [Description] — [Date YYYY-MM-DD].[ext]`

Examples:
- `Cap Table — Fully Diluted — 2026-04-01.pdf`
- `Financial Projections — FY2027 — 2026-04-01.xlsx`
- `Certificate of Incorporation — 2024-01-15.pdf`

Never use: `Final`, `v2`, `copy`, `new` in filenames — use the date for versioning.

## Access Control Levels

| Access Level | Who Gets It | Permissions |
|-------------|------------|------------|
| Full access | Lead investor in active diligence | View all folders, download Tier 1 and 2 only |
| Standard access | Investors in first meeting stage | View Overview + Financials + Team; no download |
| Request-only | Cold or warm pipeline | No access until meeting completed |

Configure access in the data room platform (Docsend, Caplinked, Notion with permissions, or a dedicated data room tool). Every access grant must be logged with the investor name, date, and access level.

## Access Tracking Use

Monitor document engagement to infer investor interest:
- Investor who spends >5 minutes on the cap table = evaluating ownership deeply (likely serious)
- Investor who skips financials = may be earlier stage or thesis-driven (not financially focused)
- Investor who downloads the pitch deck = saving for internal review (positive signal)

Share engagement summary with CEO before each follow-up conversation.
