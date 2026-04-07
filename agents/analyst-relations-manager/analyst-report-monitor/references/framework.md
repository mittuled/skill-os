# Framework: Analyst Report Monitor

Defines the monitoring cadence, report evaluation criteria, internal intelligence brief structure, and response protocols for transforming analyst publications into actionable intelligence.

## Monitoring Coverage Model

### Analyst Firm Tiers

| Tier | Firms | Monitoring Priority | Review SLA |
|------|-------|--------------------|-----------| 
| Tier 1 — Market-shaping | Gartner, Forrester | Review every publication mentioning category or competitors within 24 hours | 24 hours |
| Tier 2 — Category coverage | IDC, S&P Global / 451 Research, Omdia | Review all category reports within 48 hours; spot-check others monthly | 48 hours |
| Tier 3 — Adjacent / emerging | HFS Research, Constellation Research, RedMonk | Review quarterly; alert system monitors for company name mentions | 1 week |

### Publication Types to Monitor

| Publication Type | Strategic Value | Alert Threshold |
|-----------------|----------------|-----------------|
| Magic Quadrant / Wave / MarketScape | Critical — defines buyer shortlists | Immediate on publication |
| Market Guide | High — sets category definitions and inclusion criteria | Within 24 hours |
| Hype Cycle | High — signals maturity stage buyers assign to the category | Within 24 hours |
| Research Note | Medium — shapes analyst and client understanding | Within 48 hours if category-relevant |
| Competitive Profile | High — reveals how analyst positions each competitor | Within 24 hours |
| Predicts / Forecast | Medium — market size and growth data used in pitches | Within 1 week |
| Client Inquiry Report | Low visibility — internal to analyst firm; not usually distributed | Not directly monitorable; track via relationship intelligence |

---

## Alert Configuration

### Keyword Sets

| Category | Keywords to Monitor |
|----------|-------------------|
| Company mentions | [Company name], [common abbreviation], [product names], [executive names] |
| Competitor mentions | [Competitor A], [Competitor B], [Competitor C] (at minimum top 3 direct competitors) |
| Category definitions | [Primary category term], [alternative category names], [adjacent categories] |
| Evaluation keywords | "Magic Quadrant [category]", "Forrester Wave [category]", "Market Guide [category]" |

### Alert Channels

| Alert Type | Trigger | Channel | Owner |
|-----------|---------|---------|-------|
| Company mentioned in Tier 1 publication | Any Gartner or Forrester publication | Immediate Slack/email | AR Manager |
| Negative company positioning | Company cited with "caution" / weakness language | Immediate Slack + leadership email | AR Manager + Marketing Lead |
| Competitor positioned above company | Competitor placed Leaders quadrant; company not | Same-day internal brief | AR Manager |
| Category definition change | New sub-category or redefined inclusion criteria | Within 24 hours; product + leadership | AR Manager + CPO |
| New evaluation cycle announced | Firm announces new MQ, Wave, or equivalent | Immediate planning trigger | AR Manager |

---

## Report Evaluation Criteria

When reviewing any relevant publication, extract and assess:

| Criterion | Questions to Answer |
|-----------|-------------------|
| Company positioning | How is the company described? What quadrant, tier, or category segment? What language is used? |
| Strengths cited | What capabilities or attributes does the analyst highlight positively? |
| Cautions / weaknesses cited | What gaps or risks does the analyst identify? Are these addressable? |
| Competitor positioning | How are direct competitors positioned relative to the company? What do they score well on that we do not? |
| Category definition | How does the analyst define the category? Does this definition include or exclude the company's core capabilities? |
| Buyer guidance | What purchasing criteria does the analyst recommend? Which of these favour the company? |
| Market trends | What trends does the analyst identify? Do these align with or challenge the company's positioning? |
| Scoring methodology | For evaluations: what criteria weightings are used? Has the methodology changed since the last cycle? |

---

## Internal Intelligence Brief Structure

Every high-impact publication produces an internal intelligence brief distributed to relevant teams.

| Section | Content | Audience |
|---------|---------|---------|
| Headline | One sentence: what published, who wrote it, what it means for the company | All recipients |
| Company positioning | How the company was described; quadrant, tier, or mention type | Marketing, Sales, Leadership |
| Key strengths cited | Analyst-cited positives — use these in sales and marketing | Sales, Marketing |
| Cautions to address | Analyst-cited gaps — each needs a briefing response or roadmap fix | Product, Leadership |
| Competitive moves | How competitors are positioned; what they are doing better per the analyst | Sales, Product, Leadership |
| Buyer guidance implications | What the analyst tells buyers to look for — does the company meet this bar? | Marketing, Sales |
| Sales talking points | Analyst quotes and findings to use in active deals | Sales (immediate distribution) |
| Recommended actions | Specific next steps with owners and deadlines | All recipients |

---

## Response Protocols by Finding Type

| Finding Type | Response Protocol | Owner | Timing |
|-------------|-----------------|-------|--------|
| Positive company positioning | Amplify: add to sales deck, website, and media materials | Marketing + Sales | Within 1 week |
| Weakness / caution cited | Internal review: is it accurate? Is it addressable? Draft briefing response plan | AR Manager + Product | Within 48 hours |
| Category definition that excludes the company | Executive escalation: assess if the company should be repositioned or if the analyst needs re-briefing | AR Manager + CEO | Within 24 hours |
| Competitor positioned above company | Competitive response brief: what would need to change for the company to close that gap? | AR Manager + Product | Within 48 hours |
| New evaluation cycle announced | Launch magic-quadrant-strategy skill immediately | AR Manager | Immediate |
| Market trend that contradicts company positioning | Strategic review: is the positioning outdated? Schedule narrative update session | AR Manager + CEO | Within 1 week |

---

## Quarterly Analyst Landscape Summary

Compile quarterly from all high-impact publications reviewed in the period.

| Section | Content |
|---------|---------|
| Publications reviewed | Full list with dates and analyst authors |
| Positioning trend | How the company's analyst-cited positioning has shifted over the quarter |
| Competitive shifts | Changes in how analysts rank or describe direct competitors |
| Category evolution | Any definitional shifts, new sub-categories, or inclusion criteria changes |
| Briefing priority recommendations | Which analysts need a proactive briefing in the next 90 days based on coverage trends |
| Action items carried forward | Open items from previous quarter's intelligence briefs |

---

## Competitive Positioning Tracker Schema

| Field | Content |
|-------|---------|
| Analyst firm | Gartner / Forrester / IDC / Other |
| Publication | Report name and type |
| Publication date | YYYY-MM-DD |
| Our positioning | Quadrant / tier / description language |
| Competitor A positioning | Quadrant / tier / description language |
| Competitor B positioning | |
| Key differentiator cited (us) | Analyst-noted strength |
| Key weakness cited (us) | Analyst-noted caution |
| Category definition used | Verbatim or summary |
| Next review cycle expected | YYYY-QX |
