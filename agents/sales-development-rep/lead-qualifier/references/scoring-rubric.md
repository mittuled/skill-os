# Scoring Rubric: lead-qualifier

Evaluates lead qualification readiness by scoring Budget, Authority, Need, and Timeline dimensions using publicly available signals to produce a composite qualification score and tier assignment.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Budget | 25% | Evidence that the prospect has or can allocate budget for a solution in this category |
| 2 | Authority | 25% | Evidence that the contact has decision-making power or direct access to the economic buyer |
| 3 | Need | 30% | Evidence that the prospect has an active, quantifiable pain point the product addresses |
| 4 | Timeline | 20% | Evidence that the prospect's buying window aligns with the current sales cycle |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score x weight)

**MEDDIC Modifier**: If 4+ MEDDIC elements are Confirmed, multiply composite by 1.1 (cap at 10.0). If 2+ MEDDIC elements are Unknown, multiply by 0.9.

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 - 10.0 | Exceptional | All 4 BANT dimensions score 8+, MEDDIC confirms deal structure, multiple buying signals converge within 30 days | Assign to senior SDR immediately; begin multi-channel outreach within 24 hours; fast-track to AE if discovery call booked within 48 hours |
| A | 8.0 - 8.9 | Strong | 3 of 4 BANT dimensions score 7+, at least 1 MEDDIC element confirmed, clear outreach path to decision-maker | Prioritize for outreach this week; personalize message using confirmed need and authority signals; schedule AE shadow for discovery call |
| B | 7.0 - 7.9 | Good | 2 of 4 BANT dimensions score 7+, remaining dimensions score 5+, partial MEDDIC coverage | Schedule outreach within 5 business days; fill highest-impact data gap before first touch; warm with content relevant to identified need |
| C | 5.0 - 6.9 | Adequate | 1-2 BANT dimensions score 6+, others below 5, limited MEDDIC evidence | Add to warm nurture sequence; monitor for trigger events (funding, hiring, content engagement); re-qualify monthly |
| D | 3.0 - 4.9 | Weak | No BANT dimension scores above 5, no MEDDIC elements confirmed, signals are indirect or stale | Deprioritize to automated nurture; re-qualify only on explicit trigger event (inbound request, pricing page visit, event registration) |
| F | 0.0 - 2.9 | Failing | Minimal or no signals across BANT dimensions, contact may be invalid, company may not match ICP | Disqualify and archive; document reason; set 6-month re-evaluation date if company is within ICP but timing is wrong |

## Signal Tables

### Budget

| Score | Evidence |
|-------|----------|
| 9-10 | Company raised Series B+ in last 6 months with stated investment in the product category; or public budget allocation visible (government RFP, annual report line item); or confirmed spend on competitor product at similar price point |
| 7-8 | Company raised Series A+ in last 12 months; or headcount and revenue indicators suggest budget capacity; or job postings reference tools in the category (implying budget allocated for tooling) |
| 5-6 | Company has funding but round is older than 12 months; or revenue indicators are moderate; or company uses a free/low-tier competitor (suggesting awareness of category but uncertain budget for premium) |
| 3-4 | Bootstrapped company with no visible funding; or in a cost-cutting phase (layoffs, hiring freeze reported); or very early stage (pre-seed/seed) with limited runway indicators |
| 0-2 | No funding data available; company appears to be pre-revenue; or active signs of financial distress (down-round, mass layoffs, bankruptcy filings) |

### Authority

| Score | Evidence |
|-------|----------|
| 9-10 | Contact is C-level or VP with direct budget authority for the category (e.g., CTO for dev tools, VP Sales for sales tools); confirmed by LinkedIn title and company org structure; contact has engaged with content (webinar, whitepaper) |
| 7-8 | Contact is Director-level in the relevant department; or C-level engaged with general content but not category-specific; or contact's LinkedIn shows they report directly to the economic buyer |
| 5-6 | Contact is Manager-level or Senior IC with likely influence but not decision authority; or contact's exact role in purchasing is unclear; or multiple contacts exist but economic buyer not identified |
| 3-4 | Contact is an individual contributor or in a department unrelated to the buying decision; or contact title is generic/unclear (e.g., "Consultant", "Advisor"); or contact may have left the company |
| 0-2 | No contact identified; or contact information is invalid (bounced email, inactive LinkedIn); or contact is clearly not in the buying path (e.g., intern, contractor) |

### Need

| Score | Evidence |
|-------|----------|
| 9-10 | Company has active job postings for roles the product directly serves (3+ postings); visited pricing page and product-specific feature pages multiple times in 30 days; downloaded category-specific content; G2/Gartner research activity in the category confirmed |
| 7-8 | Job posting for 1-2 roles the product serves; or content engagement with problem-space material (not product-specific); or tech stack signals indicate a gap the product fills; or competitor product review suggests evaluation activity |
| 5-6 | General content engagement (blog reads, newsletter subscription) but not category-specific; or job postings suggest adjacent need; or company is in a vertical where the problem is common but no company-specific evidence |
| 3-4 | No direct need signals; company may have recently purchased a competitor (suggesting need is met); or engagement is limited to a single generic touchpoint (e.g., one blog visit 3 months ago) |
| 0-2 | Company has no visible need for the product category; or recently signed a multi-year contract with a competitor; or company's business model does not align with the product's value proposition |

### Timeline

| Score | Evidence |
|-------|----------|
| 9-10 | Active RFP issued in the category; or contract with incumbent expiring within 3 months; or public statement about initiative timeline (e.g., "migrating to new platform in Q2"); or confirmed evaluation in progress (demo requested, trial started) |
| 7-8 | Fiscal year start aligns with outreach window (budget cycle opening); or recent funding round suggests investment deployment within 6 months; or leadership change in last 3 months signals strategic shift |
| 5-6 | Annual planning season approaching but no confirmed initiative; or job postings suggest team build-out that precedes tool purchase by 3-6 months; or industry event attendance indicates early-stage interest |
| 3-4 | No timeline signals; fiscal year recently started (budget likely allocated); or company appears to be in a holding pattern (no hiring, no initiatives, stable state) |
| 0-2 | Negative timing signals: just signed a multi-year contract with competitor; or in a freeze/restructuring mode; or recently completed an initiative in the category (need satisfied for foreseeable future) |
