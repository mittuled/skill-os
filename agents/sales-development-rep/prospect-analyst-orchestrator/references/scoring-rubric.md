# Scoring Rubric: prospect-analyst-orchestrator

Evaluates overall prospect quality and readiness for SDR outreach by aggregating research completeness, firmographic alignment, intent evidence, buying committee accessibility, and timing indicators.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Data Completeness | 20% | Coverage across all 8 firmographic dimensions with verified, recent sources |
| 2 | Firmographic Fit | 25% | Alignment of company attributes to the defined ICP parameters |
| 3 | Intent Signals | 20% | Strength and recency of observable buying intent indicators |
| 4 | Buying Committee Access | 20% | Identifiability and reachability of key decision-makers in the org |
| 5 | Timing Alignment | 15% | Evidence that the prospect's buying window aligns with the sales cycle |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score x weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 - 10.0 | Exceptional | All 8 dimensions verified within 90 days, ICP match on every parameter, multiple active intent signals, full buying committee mapped with direct contact info, and confirmed active evaluation timeline | Assign to top SDR immediately; begin multi-threaded outreach within 48 hours |
| A | 8.0 - 8.9 | Strong | 6+ dimensions verified recently, strong ICP fit with 1-2 minor gaps, at least 2 intent signals, economic buyer identified with contact path, timing indicators positive | Prioritize for outreach this week; pre-build personalized sequence |
| B | 7.0 - 7.9 | Good | 5+ dimensions verified, solid ICP fit with known gaps, at least 1 intent signal, some buying committee members identified, general timing favorable | Schedule outreach this sprint; fill data gaps before first touch |
| C | 5.0 - 6.9 | Adequate | 4+ dimensions with mixed recency, partial ICP fit, weak or indirect intent signals, limited buying committee visibility, timing unclear | Add to nurture queue; re-evaluate after additional research or trigger event |
| D | 3.0 - 4.9 | Weak | Fewer than 4 dimensions verified, marginal ICP fit, no clear intent signals, buying committee unknown, no timing indicators | Deprioritize; revisit only if new intent signal surfaces |
| F | 0.0 - 2.9 | Failing | Minimal data available, poor ICP fit, no intent evidence, no contact paths, no timing alignment | Disqualify from current campaign; archive for future ICP revision review |

## Signal Tables

### Data Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | All 8 firmographic dimensions populated with data verified within the last 90 days from 2+ independent sources; no flags for staleness or conflicts |
| 7-8 | 6-7 dimensions populated with data from the last 6 months; 1-2 dimensions rely on a single source; no critical dimensions missing |
| 5-6 | 5 dimensions populated but some data older than 6 months; 2-3 dimensions from single unverified sources; headcount or revenue figures estimated |
| 3-4 | 3-4 dimensions populated; multiple data points older than 12 months; key fields (revenue, tech stack) missing or estimated with low confidence |
| 0-2 | Fewer than 3 dimensions populated; most data older than 12 months or sourced from unreliable directories; company may have pivoted or been acquired |

### Firmographic Fit

| Score | Evidence |
|-------|----------|
| 9-10 | Company matches ICP on all parameters: industry vertical, employee range, revenue band, geography, tech stack, and growth stage; no disqualifying attributes |
| 7-8 | Matches on 4-5 of 6 ICP parameters; 1 parameter is borderline (e.g., employee count 10% outside range); no hard disqualifiers |
| 5-6 | Matches on 3-4 parameters; 1-2 parameters outside range but adjacent (e.g., adjacent industry vertical, slightly below revenue threshold) |
| 3-4 | Matches on 2-3 parameters; company is in a tangential industry or significantly outside size/revenue range; product relevance is speculative |
| 0-2 | Matches on 0-1 parameters; company is clearly outside ICP on multiple dimensions; pursuing would violate the qualify-ruthlessly principle |

### Intent Signals

| Score | Evidence |
|-------|----------|
| 9-10 | 3+ active intent signals within 30 days: job postings for roles the product serves, G2/Gartner research in the category, direct website visits to pricing page, RFP issued in the space |
| 7-8 | 2 intent signals within 60 days: relevant job postings or technology evaluation activity combined with content engagement (whitepaper downloads, webinar attendance) |
| 5-6 | 1 clear intent signal within 90 days (e.g., job posting for relevant role) or 2+ weak signals (social media mentions of the problem space, general industry content consumption) |
| 3-4 | Indirect signals only: company is in a growing segment, competitors have adopted similar solutions, but no company-specific buying behavior observed |
| 0-2 | No observable intent signals; company shows no public evidence of evaluating solutions in the category; last known activity in the space is older than 12 months |

### Buying Committee Access

| Score | Evidence |
|-------|----------|
| 9-10 | Economic buyer, champion, and technical evaluator identified by name with verified contact information; at least one existing warm connection (shared connection, event attendance, content engagement) |
| 7-8 | Economic buyer and 1 additional committee member identified with contact info; no warm connection but clear outreach path (active on LinkedIn, speaks at events, publishes content) |
| 5-6 | Economic buyer identified by role/title but not confirmed by name; or named contact is a potential champion but economic buyer role is unclear; contact info partially available |
| 3-4 | General department identified (e.g., "VP Engineering probably owns this") but no specific individuals confirmed; no direct contact paths; org chart is opaque |
| 0-2 | No buying committee members identifiable; company has no public org information; LinkedIn profiles are sparse or absent; no conference or content trail |

### Timing Alignment

| Score | Evidence |
|-------|----------|
| 9-10 | Confirmed active evaluation: RFP issued, budget cycle aligns with current quarter, contract with incumbent expiring within 6 months, or public statement about initiative timeline |
| 7-8 | Strong timing indicators: recent funding round (Series B+ in last 6 months), fiscal year start aligns with outreach window, job postings suggest team build-out for a new initiative |
| 5-6 | Moderate timing signals: annual planning season approaching, company in growth phase but no specific initiative timeline visible, industry peers making moves in the space |
| 3-4 | Weak timing signals: no budget cycle alignment, company recently completed a similar purchase (likely locked in for 12-24 months), general growth but no urgency indicators |
| 0-2 | Negative timing: company in hiring freeze or layoffs, recent down-round or cost-cutting, just signed a multi-year contract with a competitor, or fiscal year just started with budget already allocated |
