# Scoring Rubric: financial-risk-reviewer

Evaluates the severity and management quality of the company's financial risk profile across liquidity, concentration, market, operational, and compliance dimensions.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Liquidity Risk | 30% | Adequacy of runway, burn rate trajectory, and ability to reach the next funding milestone without additional capital |
| 2 | Revenue Concentration Risk | 25% | Exposure to single customer, channel, or geography loss events |
| 3 | Market and Macro Risk | 20% | Exposure to FX movements, interest rate changes, and macroeconomic demand shifts |
| 4 | Operational Risk | 15% | Key-person dependency, vendor concentration, and process failure exposure |
| 5 | Compliance Risk | 10% | Covenant compliance, regulatory exposure, and tax obligation management |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = critical risk requiring immediate action, 5 = manageable risk with identified mitigations, 10 = low residual risk with strong controls

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Low Risk | Runway > 24 months; no customer > 10%; FX exposure hedged; no key-person single points of failure; all covenants in compliance | Maintain current risk management; report quarterly |
| A | 8.0–8.9 | Well Managed | Runway 18–24 months; top customer < 15%; limited FX exposure; single key-person risk with mitigation in progress | Monitor monthly; no immediate action required |
| B | 7.0–7.9 | Manageable | Runway 12–18 months; top customer 15–20%; FX exposure unhedged but <5% of revenue; some vendor concentration | Document mitigation plans for B-rated risks; quarterly review |
| C | 5.0–6.9 | Elevated | Runway 6–12 months; top customer 20–30%; FX exposure impacting margins; covenant headroom < 15% | Activate mitigation plans; brief board; monthly monitoring |
| D | 3.0–4.9 | High Risk | Runway < 6 months; top customer > 30%; covenant breach within 90 days; key-person departure would materially disrupt operations | Immediate CFO and board escalation; risk mitigation sprint required |
| F | 0.0–2.9 | Critical | Runway < 3 months without intervention; covenant breached; single customer > 40%; regulatory action pending | Emergency board session; consider equity raise, debt, or restructuring |

## Signal Tables

### Liquidity Risk

| Score | Evidence |
|-------|----------|
| 9–10 | Runway > 24 months at current burn; burn multiple < 1.0x; company is cash-flow positive or within 6 months of it; no external funding required for core plan |
| 7–8 | Runway 18–24 months; burn multiple 1.0–1.5x; monthly burn is flat or declining as a percentage of revenue |
| 5–6 | Runway 12–18 months; burn multiple 1.5–2.5x; burn is stable but dependent on maintaining current growth rate |
| 3–4 | Runway 6–12 months; burn multiple > 2.5x; each missed month of growth meaningfully shortens runway |
| 0–2 | Runway < 6 months without an immediate capital event; burn accelerating; no realistic path to extending runway through cost actions alone |

### Revenue Concentration Risk

| Score | Evidence |
|-------|----------|
| 9–10 | Top customer < 10% of ARR; top 10 customers < 30%; no single channel > 40%; international concentration < 30% |
| 7–8 | Top customer 10–15%; top 10 customers 30–40%; geographic concentration within manageable limits |
| 5–6 | Top customer 15–25%; top 10 customers 40–55%; one channel (e.g., a single reseller) delivers > 30% of bookings |
| 3–4 | Top customer 25–35%; churn of top customer would reduce ARR by > 20%; single geography > 60% of revenue |
| 0–2 | Top customer > 35% of ARR; active renewal risk on that account; no replacement revenue pipeline exists |

### Market and Macro Risk

| Score | Evidence |
|-------|----------|
| 9–10 | Revenue is USD-denominated with USD cost base; no material FX exposure; product demand is counter-cyclical or acyclical |
| 7–8 | FX exposure < 5% of revenue; hedging policy documented; no pending macro policy changes that directly affect demand |
| 5–6 | FX exposure 5–15% of revenue; unhedged but monitored; macro sensitivity moderate (enterprise discretionary spend category) |
| 3–4 | FX exposure > 15% without hedging; customer demand directly tied to a cyclical macro factor (e.g., housing, consumer spending); margin impact from FX is material in current quarter |
| 0–2 | Revenue in highly volatile currency; macro downturn already visible in pipeline contraction; no mitigation strategy exists |

### Operational Risk

| Score | Evidence |
|-------|----------|
| 9–10 | No single-person dependency for any critical function; all key roles have backups or documented SOPs; no vendor accounts for > 20% of COGS or critical infrastructure |
| 7–8 | One key-person risk identified with succession plan in progress; critical vendor has alternative documented; business continuity plan exists |
| 5–6 | One key-person risk without active mitigation; one critical vendor with no documented alternative; relying on manual processes for > 1 financial control |
| 3–4 | Two or more key-person risks; critical vendor failure would halt operations for > 5 business days; financial controls rely on a single individual for multiple functions |
| 0–2 | CEO or CTO departure would materially impair core operations; critical vendor is in financial distress; no business continuity plan documented |

### Compliance Risk

| Score | Evidence |
|-------|----------|
| 9–10 | All debt covenants met with > 25% headroom; all tax filings current; no pending regulatory inquiries; all nexus jurisdictions registered and filing |
| 7–8 | All covenants met with 15–25% headroom; one minor tax filing extension in progress; no material compliance open items |
| 5–6 | Covenant headroom 5–15% on at least one metric; one state filing overdue or nexus assessment incomplete; no material penalties |
| 3–4 | Covenant headroom < 5% or covenant waiver required within 90 days; tax penalties accruing; known regulatory non-compliance not yet remediated |
| 0–2 | Covenant already breached or breach imminent; material tax liability unrecorded; active regulatory inquiry or litigation affecting financial position |
