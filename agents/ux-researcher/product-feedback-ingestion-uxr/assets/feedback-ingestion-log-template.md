# Product Feedback Ingestion Log

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Reviewer | [UX Researcher] |
| Review Period | [From YYYY-MM-DD to YYYY-MM-DD] |
| Sources Reviewed | [List sources checked this cycle] |
| Version | [1.0] |

## Ingestion Summary

[Brief summary of this cycle's review: volume reviewed, number of insights identified, and any urgent findings that need immediate attention.]

**Total feedback items reviewed**: [X]
**New insights identified**: [X]
**Urgent items (P0 — immediate action required)**: [X]

## Raw Feedback Log

[Log every item reviewed, tagged, and classified. One row per feedback item. Add rows as needed.]

| ID | Source | Date Received | Product Area | Segment | Issue Type | Severity | Summary | Action |
|----|--------|--------------|-------------|---------|-----------|---------|---------|--------|
| FB-001 | [Support ticket #1234] | [2024-01-15] | [Checkout] | [New user] | [Pain point] | [Major] | [User unable to find payment method selector on mobile] | [Add to insight register: INS-012] |
| FB-002 | [Session recording SES-045] | [2024-01-16] | [Onboarding] | [Mobile user] | [Confusion] | [Minor] | [User tapped logo expecting navigation — no feedback] | [Note — track for pattern] |
| FB-003 | [NPS open text] | [2024-01-14] | [Dashboard] | [Unknown] | [Request] | [Observation] | ["Would love a way to filter by date range"] | [Add to feature request log] |
| FB-004 | [CS call note] | [2024-01-17] | [Settings] | [Admin] | [Pain point] | [Critical] | [Admin cannot bulk-invite users — inviting one at a time for 200-person team] | [Escalate to PM immediately] |
| FB-005 | | | | | | | | |

**Issue Type**: Pain point / Confusion / Request / Delight / Bug report / Observation
**Severity**: Critical / Major / Minor / Observation

## Pattern Register

[Track patterns across feedback items. A pattern requires 3+ independent items pointing to the same issue.]

| Pattern ID | Issue | Evidence Count | Sources | Severity | Status |
|-----------|-------|---------------|---------|---------|--------|
| PAT-01 | [e.g. Payment method selector not findable on mobile] | [5 items] | [Support ×3, Session ×2] | [Major] | [Escalated to PM] |
| PAT-02 | [e.g. Date range filter missing from dashboard] | [3 items] | [NPS ×2, CS call ×1] | [Minor] | [Added to feature backlog] |

## Urgent Items (P0 — Immediate Action)

[Items requiring action within 24-48 hours — do not wait for weekly synthesis.]

| ID | Issue | Evidence | Action Required | Assigned To | Due |
|----|-------|---------|----------------|------------|-----|
| FB-004 | [Admin bulk-invite blocked] | [CS call — customer managing 200 users] | [PM review + engineering feasibility check] | [PM name] | [Date] |

## Items Added to Insight Register

[Log which feedback items were elevated to the insight register this cycle.]

| Feedback ID | Insight Register ID | Insight Statement |
|------------|--------------------|--------------------|
| [FB-001] | [INS-012] | [Payment method selection fails on mobile — 5 evidence points across 2 sources] |

## Next Cycle Focus

[Based on this cycle's findings, note any areas that warrant deeper review next cycle.]

- [e.g. Mobile checkout flow — 3 independent pain points this week; prioritise in next session analysis batch]
- [e.g. Dashboard filtering — recurring request from NPS; schedule discovery interview to understand depth of need]

## Archive

[Previous ingestion logs are stored in: [link to research repository]]
