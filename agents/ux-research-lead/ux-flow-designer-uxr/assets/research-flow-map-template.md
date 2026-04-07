# Research-Informed User Flow Map

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX Research Lead] |
| Feature | [Feature name] |
| Research Inputs | [JTBD map, interview findings, session analysis — list sources] |
| Figma Flow | [Link to flow diagram] |
| Version | [1.0] |
| Status | [Draft / Research-validated / Design-approved] |

## Research Foundation

[State the research basis for this flow. Which studies and findings informed it?]

| Research Source | Key Insight Used | Confidence |
|----------------|-----------------|-----------|
| [e.g. JTBD map v1.2 — Checkout initiative] | [e.g. Core job has 4 stages: locate, evaluate, commit, confirm] | [High] |
| [e.g. Discovery interviews — 12 sessions] | [e.g. Users check delivery date before payment — sequence critical] | [High] |
| [e.g. Session analysis — 20 post-launch sessions] | [e.g. 7/20 users back out at payment to check delivery — add early in flow] | [Medium] |

## User Flow Overview

**User**: [User segment / persona this flow is designed for]
**Starting context**: [Where the user is and what triggered the need — grounded in research]
**End goal**: [The outcome the user is trying to achieve — stated in user language from interviews]
**Entry points**: [All realistic starting points, not just the primary one]

## Flow Steps with Research Annotations

| Step | Screen / State | User Action | Research Basis | Design Note |
|------|---------------|-------------|---------------|-------------|
| 1 | [e.g. Product detail page] | [Reviews delivery date and stock status before continuing] | [RES: 10/12 interview participants checked delivery first — P02: "I won't add to cart until I know it arrives in time"] | [Show delivery estimate prominently at top of page] |
| 2 | [e.g. Add to cart confirmation] | [Taps "Add to cart"] | [SEQ: Natural next step after delivery validated] | [Micro-confirmation: cart count updates immediately] |
| 3 | [Decision: Continue shopping or checkout?] | [80% proceed to checkout; 20% continue shopping] | [ANALYTICS: funnel data] | [Two equal-weight CTAs; design for both paths] |
| 4 | [e.g. Cart review] | [Checks order summary; may adjust quantity] | [RES: 6/12 participants adjusted quantity in cart — this is a reconsideration moment, not a commitment step] | [Make editing frictionless; do not over-confirm minor adjustments] |
| 5 | [e.g. Checkout: Delivery] | [Confirms delivery address] | [RES: Mobile users re-enter address 40% more often — saved addresses reduce drop-off (P08)] | [Surface saved address prominently; make edit easy] |
| 6 | [e.g. Checkout: Payment] | [Selects payment method; places order] | [ANXIETY: P04, P07: "I always double-check the total before I click pay"] | [Full order summary visible at payment step; total prominent] |
| 7 | [e.g. Order confirmation] | [Views confirmation] | [SOCIAL JOB: "I need to forward this to my team" — P01, P06] | [Include sharable order reference; easy copy to clipboard] |

## Branch Decisions with Research Rationale

### Branch 1: [Branch Point Name]

| Condition | Path | Research Basis |
|-----------|------|---------------|
| [User has saved address] | [Pre-fill address; confirm or edit] | [8/12 participants have saved address; pre-fill reduces time by 45s avg] |
| [User has no saved address] | [Address entry form] | [New users and guest checkout path] |
| [User is on mobile] | [Same flow; condensed layout] | [Session data: mobile users less likely to edit address once entered] |

### Branch 2: [Branch Point Name]

| Condition | Path | Research Basis |
|-----------|------|---------------|
| [Condition] | [Path] | [Research basis] |

## Entry Point Map

[Document all realistic starting points for this flow, grounded in analytics and research.]

| Entry Point | % of Users | Research Source | Design Consideration |
|------------|-----------|----------------|---------------------|
| [Product detail page] | [60%] | [Analytics] | [Primary path — design for this first] |
| [Cart abandonment email] | [25%] | [Email analytics] | [User returns mid-flow; cart state preserved?] |
| [Shared product link] | [10%] | [Referral data] | [User may be on unfamiliar device; can't assume saved preferences] |
| [Push notification — low stock] | [5%] | [Push analytics] | [High urgency; minimise steps to checkout] |

## Terminology Map

[Words used in the flow, matched to participant language from research.]

| Product / System Term | User Language (from interviews) | Decision |
|----------------------|-------------------------------|---------|
| [e.g. "Checkout"] | [e.g. Participants: "buy it" / "buy now" / "checkout"] | [Use "Checkout" — industry standard; participants familiar] |
| [e.g. "Add to wishlist"] | [e.g. Participants: "save for later" / "save it"] | [Change to "Save for later" — matches participant vocabulary] |
| [e.g. "Order summary"] | [e.g. Participants: "what I'm buying"] | [Retain "Order summary" — participants understood it; changing creates inconsistency] |

## Validation Checklist

Before the flow is approved for wireframing:

- [ ] Every major step traces to a research finding or validated user behaviour
- [ ] Entry points cover all realistic user starting contexts
- [ ] User language used in step labels
- [ ] Branch conditions cover all significant user states identified in research
- [ ] Error and recovery paths address observed failure modes
- [ ] Confirmation state communicates user outcome, not system outcome
- [ ] Flow reviewed against JTBD job stage map
