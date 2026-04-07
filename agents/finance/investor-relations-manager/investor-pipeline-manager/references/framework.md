# Framework: investor-pipeline-manager

Defines the CRM structure, stage definitions, nurture cadences, and pipeline review process for managing investor relationships between fundraising rounds.

## Pipeline Stage Definitions

| Stage | Definition | Entry Criteria | Exit Criteria |
|-------|-----------|----------------|---------------|
| Research | Firm identified as a potential fit; no contact made | Added to target list | Contact made or removed as not relevant |
| Cold | Introductory outreach sent or made; no response | Outreach sent | Response received (→ Warm) or 3 non-responses (→ Archived) |
| Warm | Two-way communication established; relationship developing | Response to outreach | Meeting scheduled (→ Met) or no contact in 60 days (→ Cold) |
| Met | At least one substantive meeting has occurred | Meeting completed | Regular cadence established (→ Engaged) or no follow-up in 90 days (→ Warm) |
| Engaged | Ongoing relationship; investor is receiving regular updates | Investor proactively engages with updates or shares content | Formal process begins (→ In Process) or relationship cools (→ Met) |
| In Process | Formal fundraising process underway | Term sheet received or investor confirms entering diligence | Round closes (→ Committed) or investor passes (→ Passed — archive reason) |
| Committed | Investment complete | Wired and cap table updated | N/A — maintain as LP relationship post-investment |
| Passed | Investor declined; capture reason | Formal or informal pass received | Re-engage if significant company development changes their view |

## CRM Required Fields

Every investor record must contain these fields:

| Field | Description | Update Frequency |
|-------|-------------|-----------------|
| Firm name | Full legal name of the fund | On creation |
| Partner name | Primary contact at the firm | On creation; update if partner changes |
| Fund stage focus | Pre-seed / Seed / Series A / B / C+ | On creation |
| Check size range | Minimum and maximum typical investment | On creation |
| Thesis fit score | 1-5 internal rating on thesis alignment | On creation; revisit quarterly |
| Warm intro path | Name of mutual connection who can make the introduction | On creation or when identified |
| Portfolio conflicts | List of direct portfolio competitors | On creation; update after new fund closes |
| Last contact date | Date of most recent meaningful interaction | After every interaction |
| Next action | Specific next step with owner and due date | After every interaction |
| Stage | Current pipeline stage (see above) | After every stage change |
| Notes | Summary of key conversations, preferences, and signals | After every interaction |

## Nurture Cadence by Tier

### Tier 1 — Priority targets (top 10-15 firms, highest thesis fit)

| Touchpoint | Frequency | Format | Owner |
|-----------|-----------|--------|-------|
| Monthly investor update | Monthly | Email — same as all-investor update | IR Manager |
| Milestone-specific note | Per milestone | Personal email, 2-3 sentences | CEO |
| Quarterly coffee or call | Quarterly | 30-minute call or in-person | CEO + IR Manager |
| Annual in-person meeting | Annual | Office visit or conference overlap | CEO |

### Tier 2 — Watch list (20-30 firms, moderate thesis fit or unclear)

| Touchpoint | Frequency | Format | Owner |
|-----------|-----------|--------|-------|
| Monthly investor update | Monthly | Email — same as all-investor update | IR Manager |
| Milestone note | Per major milestone | BCC on team email announcing milestone | IR Manager |
| Semi-annual check-in | Semi-annual | Brief email or LinkedIn message | IR Manager |

### Tier 3 — Long tail (all other tracked firms)

| Touchpoint | Frequency | Format | Owner |
|-----------|-----------|--------|-------|
| Quarterly digest | Quarterly | Brief email with key metrics snapshot | IR Manager |

## Monthly Pipeline Review Agenda

Conduct monthly with CEO (30 minutes):

1. **Stage movement review** (10 min): Which investors moved stages? Forward or backward? What triggered the movement?
2. **Staleness audit** (5 min): Which relationships have not been touched in >60 days? Assign re-engagement actions.
3. **New targets** (5 min): Which new firms should be added to the pipeline based on recent fund announcements, portfolio signals, or network referrals?
4. **Fundraise readiness** (5 min): Based on current pipeline depth and stage distribution, what is the estimated timeline and confidence level to close the next round within 90 days of starting a formal process?
5. **Action items** (5 min): Assign specific next steps with owners and due dates.

## Fundraise Readiness Assessment

Use this heuristic to assess pipeline health before starting a formal process:

| Stage | Minimum Count | Rationale |
|-------|-------------|-----------|
| Engaged | 8–12 investors | The best-qualified pool to enter a formal process |
| Met | 15–20 investors | Second-tier candidates to activate if engaged tier thins out |
| Warm | 20–30 investors | Backstop pipeline; move select warm leads to met before process |

If pipeline counts fall below these minimums, invest 60-90 days building the pipeline before starting a formal process — a thin pipeline destroys competitive tension.
