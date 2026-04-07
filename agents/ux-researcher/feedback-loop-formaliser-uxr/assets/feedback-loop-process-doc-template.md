# Feedback Loop Process Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX Researcher] |
| Version | [1.0] |
| Status | [Draft / Approved / Active] |
| Review Date | [Date this document should next be reviewed] |

## Purpose

[State what problem this feedback loop process is designed to solve. GUIDANCE: e.g. "This document formalises the process for ensuring user research findings from all sources are reviewed, synthesised, distributed to decision-makers, and tracked through to action. It replaces the informal ad-hoc approach where findings were surfaced but not systematically acted on."]

## Scope

**In scope**: [What feedback sources and teams this process covers]
**Out of scope**: [What is deliberately excluded]

## Feedback Sources

[Document every active channel that generates user feedback.]

| Source | Type | Volume (approx) | Collection Owner | Review Owner |
|--------|------|----------------|-----------------|-------------|
| [e.g. In-depth user interviews] | Qualitative | [X sessions/quarter] | [UX Research Lead] | [UX Researcher] |
| [e.g. Session recordings (FullStory)] | Behavioural | [X recordings/week available] | [Product] | [Visual Interaction Designer] |
| [e.g. Support tickets (Zendesk)] | Qualitative | [X tickets/week] | [Support Lead] | [UX Researcher (Thursday review)] |
| [e.g. NPS survey (quarterly)] | Quantitative + open text | [X responses/quarter] | [CS team] | [UX Researcher] |
| [e.g. In-app Typeform feedback] | Qualitative | [X responses/week] | [Product] | [UX Researcher (weekly)] |
| [e.g. Sales call notes] | Qualitative | [X calls/week] | [Sales] | [UX Researcher (monthly)] |

## Processing Workflow

### Step 1: Collection
[Describe how raw feedback is gathered and centralised.]

- Support tickets: [Tool] auto-tags UX-related tickets with label "[UX-REVIEW]"
- Session recordings: [Researcher] reviews 5-10 sessions per bi-weekly batch
- Interview findings: [Researcher] completes synthesis within 48h of last session

### Step 2: Tagging
[Describe the tagging taxonomy used to classify findings.]

Every insight is tagged with:
- **Product area**: [e.g. Onboarding / Checkout / Dashboard / Settings / Notifications]
- **User segment**: [e.g. New user / Power user / Admin / Mobile-primary]
- **Insight type**: [Pain point / Delight / Request / Behaviour observation / Confusion]
- **Severity**: [Critical / Major / Minor / Observation]

**Tool used**: [Dovetail / Notion database / Airtable / etc.]

### Step 3: Synthesis
[Describe how individual insights are grouped into patterns.]

- Pattern threshold: [X] independent data points from [X] different sources
- Synthesis format: [Insight brief template / Research report]
- Output owner: [UX Researcher]

### Step 4: Distribution
[Describe how findings reach the teams that need them.]

| Output | Recipient | Channel | Cadence |
|--------|-----------|---------|--------|
| Insight brief (single critical finding) | PM + Head of Design | Slack #design-research | As found |
| Research synthesis report | Design + PM + Engineering leads | Email + Notion | Per study |
| Monthly research digest | All team leads | Email | Monthly (first Monday) |
| Sprint planning research input | PM | Sprint planning meeting | Per sprint |

### Step 5: Action Tracking
[Describe how findings are tracked through to action.]

- All P0 and P1 insights are added to the research backlog within 24h of identification
- PM reviews and assigns priority within [X] days
- Status updated in research repository: [Open / In Progress / Complete / Closed-Not-Actioned]
- Closed-Not-Actioned items include documented reason and revisit date

## RACI

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|------------|-------------|-----------|---------|
| Collect and tag feedback | UX Researcher | UX Research Lead | – | – |
| Synthesise findings | UX Researcher | UX Research Lead | Designer | PM |
| Prioritise insights | PM + UX Research Lead | Head of Design | Engineering | – |
| Action design changes | Designer | Head of Design | UX Researcher | PM |
| Track to completion | UX Researcher | UX Research Lead | PM | Head of Design |

## Health Metrics

[Track these to confirm the feedback loop is functioning.]

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Average days from insight to action assignment | < 5 days | [X days] | [On track / At risk] |
| % of P0/P1 insights actioned within 2 sprints | > 80% | [X%] | [On track / At risk] |
| Open insights > 30 days old | < 20% of total | [X%] | [On track / At risk] |
| Research readout attendance (PM + Design) | 100% | [X%] | [On track / At risk] |

## Review Cadence

This document is reviewed every [quarter / 6 months]. Next review: [Date].
