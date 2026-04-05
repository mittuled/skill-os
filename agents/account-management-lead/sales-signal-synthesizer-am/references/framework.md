# Framework: Account Signal Synthesis

Defines the methodology for aggregating account-level signals into portfolio-level intelligence for expansion, churn risk, and relationship health.

## Signal Classification Taxonomy

| Signal Type | Examples | CRM Tag | Priority |
|------------|---------|---------|---------|
| Expansion Opportunity | Usage > 80% capacity, new team formed, budget increase mentioned | `signal:expansion` | High |
| Churn Risk | Usage declining, sponsor departed, budget cut mentioned | `signal:churn-risk` | Critical |
| Competitive Threat | Competitor mentioned in conversation, RFP issued | `signal:competitive` | High |
| Relationship Health | Exec engagement frequency, QBR attendance, NPS delta | `signal:relationship` | Medium |
| Product Feedback | Feature requests, bugs reported, UX complaints | `signal:product-feedback` | Low-Medium |

## Confidence Rating Scale

| Rating | Definition | Example |
|--------|-----------|---------|
| Confirmed | Direct statement from the customer, documented | "CFO said they are cutting software budget by 20%" |
| Inferred | Behavioural evidence strongly implies the signal | Usage dropped 35% with no explanation |
| Speculative | Indirect indicator; could have other explanations | LinkedIn shows key champion interviewing elsewhere |

## Portfolio Synthesis Process

### Step 1: Signal Aggregation

Aggregate signals from four primary sources:

| Source | Data | Cadence |
|--------|------|---------|
| AM Reports | CRM signal entries, call notes | Weekly |
| Usage Analytics | Feature adoption, capacity utilisation, login frequency | Real-time |
| Support System | Ticket volume, P1/P2 count, CSAT per account | Weekly |
| NPS/CSAT Survey | Scores and verbatim comments | Monthly/Quarterly |

### Step 2: Pattern Detection

Identify patterns across the portfolio using these analytical frames:

**Churn Risk Concentration**: What % of ARR is in Amber/Red health accounts?
- Healthy: < 10% ARR in Red accounts
- Warning: 10–20% ARR in Red accounts
- Critical: > 20% ARR in Red accounts

**Expansion Pipeline Coverage**: What is the ratio of identified expansion opportunities to quota?
- Minimum: 3x coverage of expansion quota
- Good: 4–5x coverage
- Exceptional: > 5x coverage

**Segment-level patterns**: Cluster signals by industry, size tier, or product tier to isolate whether risk/opportunity is systemic or isolated.

### Step 3: Prioritisation Matrix

| Urgency | Revenue Impact | Priority |
|---------|---------------|---------|
| This month | > $50K ARR | P1 — Immediate AM + AML action |
| This quarter | $10K–$50K ARR | P2 — AM action in current cycle |
| Next quarter | < $10K ARR | P3 — Monitor; log for next QBR |

## Cross-Functional Distribution

| Stakeholder | What They Need | Format |
|------------|---------------|--------|
| AM Leadership | Portfolio health, churn risk ARR, expansion pipeline | Executive summary + dashboard |
| Product Team | Recurring product feedback themes, feature gaps driving churn | Categorised feedback report |
| Customer Success | At-risk accounts needing intervention | Account list with health scores and notes |
| Finance | Revenue forecast confidence based on renewal risk | ARR at risk summary |
