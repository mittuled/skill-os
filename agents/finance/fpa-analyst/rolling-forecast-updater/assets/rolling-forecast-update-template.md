# Rolling Forecast Update

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [FP&A Analyst name] |
| Forecast As Of | [Month YYYY] |
| Close Reference | [Link to monthly variance analysis for actuals period] |
| Budget Reference | [Link to annual budget] |
| Prior Forecast Version | [Link to prior forecast] |
| Version | [1.0] |
| Status | [Draft / CFO Review / Approved] |
| Skill | rolling-forecast-updater |

## Executive Summary

[3-4 sentences: actuals vs. prior forecast for the just-closed month, key assumption changes, updated full-year outlook vs. budget, and runway impact.

GUIDANCE: Example: "April actuals came in at $580K revenue (+6% vs. prior forecast of $548K) driven by a large enterprise deal that closed early. Expense was $12K over forecast due to unplanned vendor spend. Full-year forecast updated to $8.2M ARR (+2% vs. budget), with cash runway extended by 1.4 months to 18.2 months. Key risk is the Q3 hiring plan — 3 open roles create $240K downside if backfilled at senior level."]

## Actuals Integration

| Month | Revenue (Actual) | Revenue (Prior Forecast) | Variance | Expense (Actual) | Expense (Prior Forecast) | Variance |
|-------|-----------------|-------------------------|---------|-----------------|-------------------------|---------|
| [Month N] (now closed) | [$XXX,XXX] | [$XXX,XXX] | [+$X,XXX (+X%)] | [$XXX,XXX] | [$XXX,XXX] | [+$X,XXX (+X%)] |

Year-to-date actual vs. prior forecast:

| Metric | YTD Actual | YTD Prior Forecast | YTD Variance |
|--------|-----------|-------------------|--------------|
| Revenue | [$X,XXX,XXX] | [$X,XXX,XXX] | [+/- $X,XXX (+/- X%)] |
| Gross Profit | [$X,XXX,XXX] | [$X,XXX,XXX] | [+/- $X,XXX] |
| Operating Expense | [$X,XXX,XXX] | [$X,XXX,XXX] | [+/- $X,XXX] |
| Net Burn / EBITDA | [-$XXX,XXX] | [-$XXX,XXX] | [+/- $X,XXX] |

## Revenue Reforecast

### Updated Revenue Model

| Driver | Prior Forecast Assumption | Updated Assumption | Change | Rationale |
|--------|--------------------------|-------------------|--------|-----------|
| ARR as of [month] | [$X,XXX,XXX] | [$X,XXX,XXX] | [+/-$X,XXX] | [Actual bookings vs. forecast] |
| Monthly new MRR | [$XX,XXX/mo] | [$XX,XXX/mo] | [+/-$X,XXX] | [Pipeline update from sales] |
| Monthly churn MRR | [-$X,XXX/mo] | [-$X,XXX/mo] | [+/-$X,XXX] | [Churn actuals from CS] |
| Monthly expansion MRR | [$X,XXX/mo] | [$X,XXX/mo] | [+/-$X,XXX] | [Expansion pipeline update] |
| Net MRR growth/month | [$X,XXX] | [$X,XXX] | [+/-$X,XXX] | — |

### Pipeline Support for Revenue Forecast

| Stage | Count | Avg Deal Size | Close Rate | Weighted Value | Notes |
|-------|-------|--------------|-----------|---------------|-------|
| Qualified / Stage 2 | [N deals] | [$X,XXX] | [20%] | [$X,XXX] | — |
| Proposed / Stage 3 | [N deals] | [$X,XXX] | [45%] | [$X,XXX] | — |
| Verbal / Stage 4 | [N deals] | [$X,XXX] | [75%] | [$X,XXX] | — |
| Commit | [N deals] | [$X,XXX] | [90%] | [$X,XXX] | — |
| **Total weighted pipeline** | — | — | — | **[$X,XXX]** | — |

Sales team bottom-up commit: [$X,XXX] in next 60 days. Alignment with weighted pipeline: [Within X% / Gap of $X,XXX — explain].

## Expense Reforecast

| Department | Prior Forecast | Updated Forecast | Change | Driver |
|------------|---------------|-----------------|--------|--------|
| Engineering | [$XX,XXX/mo] | [$XX,XXX/mo] | [+/-$X,XXX] | [Hiring pace: N hires vs. N planned] |
| Sales | [$XX,XXX/mo] | [$XX,XXX/mo] | [+/-$X,XXX] | [Commission actuals + quota attainment] |
| Marketing | [$XX,XXX/mo] | [$XX,XXX/mo] | [+/-$X,XXX] | [Campaign spend reallocation] |
| G&A | [$XX,XXX/mo] | [$XX,XXX/mo] | [+/-$X,XXX] | [Vendor spend changes] |
| **Total Opex** | **[$XXX,XXX/mo]** | **[$XXX,XXX/mo]** | **[+/-$X,XXX/mo]** | — |

## Cash Flow and Runway Update

| Metric | Prior Forecast | Updated Forecast | Change |
|--------|---------------|-----------------|--------|
| Cash balance today | [$X,XXX,XXX] | [$X,XXX,XXX] | — |
| Monthly net burn (updated) | [-$XXX,XXX/mo] | [-$XXX,XXX/mo] | [+/-$X,XXX] |
| Cash runway | [N months] | [N months] | [+/- N months] |
| Projected zero-cash date | [YYYY-MM] | [YYYY-MM] | [+/- N months] |

**Runway threshold alert**: [Green — >18 months / Yellow — 12-18 months / Red — <12 months]

## Forecast vs. Budget Reconciliation

| Metric | Annual Budget | Updated Full-Year Forecast | Variance vs. Budget | Explanation |
|--------|--------------|--------------------------|--------------------|----|
| Revenue | [$X,XXX,XXX] | [$X,XXX,XXX] | [+/-$X,XXX (+/-X%)] | [Key drivers of budget gap] |
| Gross Margin % | [X%] | [X%] | [+/- X pp] | — |
| Total Opex | [$X,XXX,XXX] | [$X,XXX,XXX] | [+/-$X,XXX] | — |
| EBITDA / Net Burn | [-$X,XXX,XXX] | [-$X,XXX,XXX] | [+/-$X,XXX] | — |

**Budget reallocation needed?** [Yes — $X,XXX reallocated from [dept] to [dept] / No]

## Scenario Analysis

| Scenario | Revenue (Full Year) | Net Burn | Runway | Key Assumption |
|----------|--------------------|-----------|----|---------------|
| Bear | [$X,XXX,XXX (-X% vs. forecast)] | [-$X,XXX,XXX] | [N months] | [Churn +X pp, pipeline converts at -20%] |
| **Base (this forecast)** | **[$X,XXX,XXX]** | **[-$X,XXX,XXX]** | **[N months]** | **[Current assumptions]** |
| Bull | [$X,XXX,XXX (+X% vs. forecast)] | [-$X,XXX,XXX] | [N months] | [Pipeline converts at +20%, 2 enterprise deals close] |

## Risks and Open Items

| Risk | Probability | Revenue Impact | Expense Impact | Mitigation |
|------|------------|---------------|----------------|------------|
| [Senior engineering hire backfill at $200K vs. $160K budgeted] | [High] | [None] | [+$40K/yr] | [Update forecast if hire confirmed] |
| [Key account renewal at risk (ARR = $X,XXX)] | [Medium] | [-$X,XXX ARR] | [None] | [CS escalation plan in progress] |
| [New pricing tier delayed by 1 quarter] | [Medium] | [-$XX,XXX in H2] | [None] | [Reflected in bear scenario] |

## Approvals

| Role | Name | Status | Date |
|------|------|--------|------|
| FP&A Analyst | [Name] | [Draft] | [YYYY-MM-DD] |
| CFO | [Name] | [Pending] | — |
