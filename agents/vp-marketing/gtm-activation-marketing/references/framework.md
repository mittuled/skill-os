# Framework: gtm-activation-marketing

Defines the activation timeline, asset readiness standards, channel sequencing model, and war room protocol for executing a synchronized GTM launch.

## Activation Planning Timeline

| Weeks Before Launch | Activity | Owner | Gate |
|--------------------|----------|-------|------|
| 6 weeks | Activation kickoff: lock timeline, assign channel owners | VP Marketing | GTM plan approved |
| 5 weeks | Asset brief distributed to all owners | VP Marketing | — |
| 4 weeks | First asset drafts due (landing pages, ad creatives, email) | Channel owners | — |
| 3 weeks | Asset review round 1: messaging consistency check | VP Marketing | — |
| 2 weeks | Assets approved; campaigns loaded into platforms (paused) | Channel owners | — |
| 1 week | Final QA: tracking, targeting, UTMs, pixel fires | Marketing Ops | QA checklist passed |
| Launch - 2 days | Pre-launch briefing: all channel owners confirm ready | VP Marketing | Green-light call |
| Launch day | Staged activation sequence executed | VP Marketing | Per channel sequence |
| +48 hours | War room wrap: launch snapshot delivered | VP Marketing | — |
| +1 week | Launch retrospective | VP Marketing + All leads | — |

## Asset Readiness Checklist Categories

Every launch asset must clear the following checks before approval:

| Category | Required Checks |
|----------|----------------|
| Landing pages | Copy approved, form working, thank-you page configured, UTM parameters live, meta description set, mobile rendering verified |
| Ad creatives | All sizes produced, copy approved, brand-compliant, destination URL correct, UTM tagged |
| Email sequences | Subject lines approved, sender name/address set, unsubscribe link present, preview text set, mobile rendering verified, links UTM-tagged |
| Paid search | Keywords reviewed, negatives loaded, ad copy approved, extensions configured, budget set, tracking template live |
| Social copy | Platform-specific sizing, copy approved, hashtags aligned, scheduling set |
| Press release | Approved by legal and comms, wire service loaded, embargo date set |
| Sales enablement | One-pager ready, battle card updated, discovery deck updated, objection guide current |

## Channel Activation Sequence

Activate in this order to build momentum and avoid message overlap:

| Sequence | Channel | Activation Timing | Rationale |
|----------|---------|-------------------|-----------|
| 1 | PR / Earned media | T-0 or embargo lift | Sets the narrative before paid amplification |
| 2 | Email (own list) | T-0 | Highest conversion; no media dependency |
| 3 | Paid search (branded) | T-0 | Capture demand the PR generates |
| 4 | Paid social | T+2 hours | Retargeting and lookalike after initial press |
| 5 | Content / SEO | T+0 (publish) | Organic amplification of the narrative |
| 6 | Partner channels | T+1 day | Coordinate with partners after initial press coverage |
| 7 | Paid search (non-branded) | T+1 day | Broad demand capture after initial wave |
| 8 | Sales outreach | T+0 (parallel) | ABM accounts notified on launch day |

## UTM Naming Convention

| Parameter | Format | Example |
|-----------|--------|---------|
| utm_source | Platform name, lowercase | linkedin, google, email |
| utm_medium | Channel type | paid-social, cpc, email-blast |
| utm_campaign | [launch-name]-[quarter] | product-launch-q2-2025 |
| utm_content | Creative variant identifier | hero-v1, cta-demo |
| utm_term | Keyword (paid search only) | marketing-automation |

## War Room Protocol (First 48 Hours)

### Monitoring Cadence
| Timeframe | Check Frequency | Escalation Threshold |
|-----------|----------------|---------------------|
| Hour 1–4 | Every 30 minutes | Any campaign not delivering; tracking failures; broken links |
| Hour 4–24 | Every 2 hours | CTR < 50% of benchmark; form conversion rate < 1% |
| Hour 24–48 | Every 4 hours | CPL > 2× benchmark; MQL volume < 40% of 48-hour target |

### Decision Authority During War Room
| Issue | Decision Authority | Response Time |
|-------|-------------------|---------------|
| Tracking failure | Marketing Ops | < 30 minutes |
| Budget reallocation (< 20%) | Demand Gen Manager | < 1 hour |
| Message change (minor) | VP Marketing | < 2 hours |
| Campaign pause | VP Marketing | < 30 minutes |
| Full launch rollback | CBO + VP Marketing | [GATE] — requires explicit approval |

## Launch Retrospective Template

Conduct within 7 days post-launch. Cover:

1. **What launched on time vs. delayed** — list each asset/channel with status and root cause if delayed
2. **48-hour performance vs. targets** — impressions, clicks, MQLs against plan
3. **Execution issues** — tracking failures, broken assets, messaging inconsistencies
4. **What worked well** — positive surprises, overperforming channels
5. **Process improvements** — specific changes to the next activation checklist
