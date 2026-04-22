# Sales Signal Log

**AE:** [AE NAME]
**Period:** [DATE] — [DATE]
**Total Signals Logged:** [N]
**Pattern Flags Raised:** [N]

---

## How to Use This Log

Log signals within 24 hours of each prospect interaction. Tag each signal by type and map to the relevant MEDDIC criterion. When a signal appears across 3+ deals in a quarter, raise a pattern flag and escalate to the Sales Manager.

**Signal types:** Objection | Competitor | Buying Trigger | Blocker | Decision Process | Budget Indicator | Champion Signal | Timeline Commitment

**MEDDIC criteria:** M (Metrics) | E (Economic Buyer) | D (Decision Criteria) | D (Decision Process) | I (Identify Pain) | C (Champion)

---

## Signal Entries

---

### Signal Entry [S-001]

| Field | Value |
|---|---|
| Signal ID | S-001 |
| Deal / Account | [COMPANY NAME] — [CRM OPPORTUNITY LINK] |
| Signal Type | Objection |
| Date / Source | [DATE] — Discovery Call |
| Signal Summary | Prospect stated: "[VERBATIM OR PARAPHRASED QUOTE]" |
| Context | [What prompted this signal? What was the conversation topic? What happened immediately before and after?] |
| MEDDIC Mapping | I — Identify Pain / D — Decision Criteria / [OTHER] |
| Deal Implication | [What does this mean for deal progression? Does it accelerate, stall, or block?] |
| Recommended Next Step | [What action should be taken in response?] |
| Pattern Flag | Yes — appears in [N] deals this quarter / No |

---

### Signal Entry [S-002]

| Field | Value |
|---|---|
| Signal ID | S-002 |
| Deal / Account | [COMPANY NAME] — [CRM OPPORTUNITY LINK] |
| Signal Type | Competitor |
| Date / Source | [DATE] — Demo Call |
| Signal Summary | Prospect mentioned evaluating [COMPETITOR NAME]. Key stated differentiator: "[WHAT PROSPECT SAID COMPETITOR OFFERS]" |
| Context | [Was this unprompted or in response to a question? How seriously are they considering the competitor?] |
| MEDDIC Mapping | D — Decision Criteria |
| Deal Implication | [Competitive risk level: High / Medium / Low. Any urgency?] |
| Recommended Next Step | [E.g., send competitive battle card, schedule technical differentiation call] |
| Pattern Flag | Yes — [COMPETITOR] mentioned in [N] deals this quarter / No |

---

### Signal Entry [S-003]

| Field | Value |
|---|---|
| Signal ID | S-003 |
| Deal / Account | [COMPANY NAME] — [CRM OPPORTUNITY LINK] |
| Signal Type | Buying Trigger |
| Date / Source | [DATE] — [SOURCE: LinkedIn / Call / Email / News] |
| Signal Summary | [COMPANY NAME] announced [FUNDING ROUND / LEADERSHIP CHANGE / PRODUCT LAUNCH / REGULATORY REQUIREMENT]. This creates urgency for [USE CASE]. |
| Context | [How does this trigger accelerate or create a new buying window?] |
| MEDDIC Mapping | I — Identify Pain / M — Metrics |
| Deal Implication | [Buying timeline likely compressed. Economic buyer likely: [NAME].] |
| Recommended Next Step | [E.g., reach out within 48 hours referencing the trigger event] |
| Pattern Flag | No |

---

### Signal Entry [S-004]

| Field | Value |
|---|---|
| Signal ID | S-004 |
| Deal / Account | [COMPANY NAME] — [CRM OPPORTUNITY LINK] |
| Signal Type | Blocker |
| Date / Source | [DATE] — Negotiation Call |
| Signal Summary | [BLOCKER DESCRIPTION — e.g., "Budget is allocated to [COMPETING INITIATIVE] until Q3. No budget available until [MONTH]."] |
| Context | [Is this a hard blocker or soft resistance? Who confirmed it and how? Any workarounds discussed?] |
| MEDDIC Mapping | E — Economic Buyer / D — Decision Process |
| Deal Implication | [Deal likely to push to Q3. Move to nurture status or negotiate quarterly payment structure?] |
| Recommended Next Step | [E.g., offer quarterly payment aligned to when budget becomes available; mark deal as at-risk; set re-engage date] |
| Pattern Flag | No |

---

### Signal Entry [S-005]

| Field | Value |
|---|---|
| Signal ID | S-005 |
| Deal / Account | [COMPANY NAME] — [CRM OPPORTUNITY LINK] |
| Signal Type | Decision Process |
| Date / Source | [DATE] — Champion 1:1 |
| Signal Summary | Decision requires approval from [LEGAL / SECURITY / FINANCE] in addition to [CHAMPION NAME]. Legal review typically takes [N] weeks. Security questionnaire required before procurement can issue PO. |
| Context | [First time this process detail was surfaced — not mentioned in discovery. Security questionnaire will extend timeline.] |
| MEDDIC Mapping | D — Decision Process |
| Deal Implication | [Timeline at risk — close date may need to move [N] weeks. Send security questionnaire ASAP.] |
| Recommended Next Step | [Send security questionnaire this week; loop in SE for technical review] |
| Pattern Flag | Yes — security review requirement flagged in [N] deals this quarter (see pattern below) |

---

### Signal Entry [S-006]

| Field | Value |
|---|---|
| Signal ID | S-006 |
| Deal / Account | [COMPANY NAME] — [CRM OPPORTUNITY LINK] |
| Signal Type | Budget Indicator |
| Date / Source | [DATE] — Email from [CONTACT NAME] |
| Signal Summary | "We have budget pre-approved for up to $[AMOUNT] for this purchase." |
| Context | [Unsolicited budget disclosure — strong buying signal. Budget covers [TIER/SEATS] at current pricing.] |
| MEDDIC Mapping | E — Economic Buyer (budget confirmed) |
| Deal Implication | [Removes budget uncertainty. Focus on value and timeline. Proposal should be within stated budget.] |
| Recommended Next Step | [Send proposal within 48 hours. Do not exceed stated budget ceiling.] |
| Pattern Flag | No |

---

## Pattern Flag Summary

*(Raise when a signal appears in 3+ deals within a quarter. Escalate to Sales Manager.)*

| Pattern ID | Signal Type | Signal Description | Deal Count | Deals Affected | Escalated To | Date Escalated |
|---|---|---|---|---|---|---|
| PAT-001 | Objection | [RECURRING OBJECTION — e.g., "Your pricing is too high compared to [COMPETITOR]"] | [N] deals | [LIST DEAL IDS] | [SALES MANAGER NAME] | [DATE] |
| PAT-002 | Decision Process | Security questionnaire required before procurement — not surfaced in discovery | [N] deals | [LIST DEAL IDS] | [SALES MANAGER NAME] | [DATE] |
| PAT-003 | Competitor | [COMPETITOR NAME] mentioned as active evaluation in [N] deals this quarter | [N] deals | [LIST DEAL IDS] | [SALES MANAGER NAME] | [DATE] |

---

## CRM Signal Tags Reference

Tag each signal in CRM using these standard tags for aggregate analysis:

`objection:pricing` | `objection:security` | `objection:integration` | `objection:timing` | `objection:trust`
`competitor:[NAME]` | `trigger:funding` | `trigger:leadership-change` | `trigger:regulatory`
`blocker:budget` | `blocker:security` | `blocker:champion-loss` | `blocker:competing-initiative`
`meddic:metrics` | `meddic:economic-buyer` | `meddic:decision-criteria` | `meddic:decision-process` | `meddic:pain` | `meddic:champion`

---

*Signal log maintained by [AE NAME] | Period: [DATE] – [DATE] | Patterns escalated to: [SALES MANAGER NAME]*
