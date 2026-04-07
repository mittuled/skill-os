# Framework: First Sales Process Design

## Purpose

Provides the methodology for designing a first repeatable sales process, including stage design principles, qualification frameworks, and handoff standards.

## Deal Audit Method

### Sample Selection

- **Closed-won**: Last 10 deals (or all if fewer than 10). Prioritize recent, representative deals over outliers.
- **Closed-lost**: Last 5 deals. Focus on deals that progressed past discovery (early disqualifications are noise).
- **Interview**: At least 2 reps who closed deals and 1 who lost a deal in the sample.

### Audit Questions Per Deal

| Phase | Questions |
|-------|-----------|
| First touch | How did the prospect enter? What triggered their interest? |
| Discovery | How many discovery sessions? Who attended? What was uncovered? |
| Evaluation | Was there a demo? POC? Technical review? What decided progression? |
| Proposal | What was the proposal format? How long to deliver? What terms? |
| Negotiation | What was negotiated? How many rounds? Who had final authority? |
| Close | What was the final trigger to sign? What nearly killed the deal? |

### Pattern Analysis

Map each deal's actual steps to a timeline. Overlay all deals to identify:
- **Common path**: Steps that appear in 80%+ of deals
- **Divergence points**: Where deals take different routes
- **Stall points**: Where deals spent disproportionate time
- **Skip points**: Steps that successful deals skipped (these may not belong in the process)

## Stage Design Principles

### Buyer-Milestone Alignment

Each stage represents where the buyer is in their journey, not what the seller has done:

| Seller Action (Wrong) | Buyer Milestone (Right) |
|-----------------------|------------------------|
| "Sent intro email" | "Aware of problem and exploring solutions" |
| "Completed demo" | "Evaluating our solution against alternatives" |
| "Sent proposal" | "Building internal business case" |
| "In negotiation" | "Committed to buying, finalizing terms" |

### Stage Count Guidelines

| Motion Type | Recommended Stages | Rationale |
|------------|-------------------|-----------|
| Product-led | 3-4 | Low-touch; too many stages add friction |
| Velocity (SMB) | 4-5 | Fast cycle; each stage must earn its existence |
| Consultative | 5-6 | Multi-stakeholder; need checkpoints for alignment |
| Enterprise | 6-7 | Complex procurement; stages map to buyer's internal process |

### Exit Criteria Requirements

Every stage exit criterion must be:
- **Observable**: Based on something that happened, not something inferred
- **Binary**: Either met or not met (no "partially qualified")
- **Buyer-validated**: Confirmed by the buyer, not assumed by the seller

## Qualification Framework: MEDDIC Implementation

### Element Definitions

| Element | Definition | Discovery Question | Minimum to Advance |
|---------|------------|-------------------|-------------------|
| **M**etrics | Quantified business impact the buyer expects | "What does success look like in numbers?" | Buyer states specific metric and target |
| **E**conomic Buyer | Person with budget authority and veto power | "Who signs the contract?" | Identified by name and title |
| **D**ecision Criteria | Factors the buyer uses to evaluate options | "What are your must-haves vs. nice-to-haves?" | Written list from buyer |
| **D**ecision Process | Steps and timeline to reach a purchase decision | "Walk me through your buying process" | Mapped with dates and approvers |
| **I**dentify Pain | The specific business problem driving the evaluation | "What happens if you don't solve this?" | Buyer articulates pain and consequences |
| **C**hampion | Internal advocate with power and influence | "Who internally is pushing for this?" | Identified, met, and actively engaged |

### Scoring Per Element

- **0**: Not discovered
- **1**: Partially discovered (seller assumption, not buyer-confirmed)
- **2**: Discovered and buyer-confirmed
- **3**: Discovered, confirmed, and validated (evidence supports buyer's claim)

### Minimum Advancement Thresholds

| Stage Transition | Minimum Total Score | Required Elements at 2+ |
|-----------------|--------------------|-----------------------|
| Discovery → Qualification | 6/18 | Identify Pain, Metrics |
| Qualification → Evaluation | 10/18 | Economic Buyer, Decision Criteria |
| Evaluation → Proposal | 14/18 | Decision Process, Champion |
| Proposal → Negotiation | 16/18 | All elements at 2+ |

## Handoff Protocol Standards

### Required Information Per Handoff

| Handoff | Required Fields | Format | SLA |
|---------|----------------|--------|-----|
| SDR → AE | Company, contact, pain summary, MEDDIC initial scores, meeting recording link | CRM record + Slack notification | Within 1 hour of booking |
| AE → SE | MEDDIC scorecard, technical requirements, demo scope, buyer personas attending | CRM record + pre-call briefing doc | 48 hours before SE engagement |
| AE → CS | Contract terms, stakeholder map, success criteria, implementation requirements, risk flags | Handoff document + joint meeting | Within 5 business days of close |

## CRM Configuration Standards

### Required Fields Per Stage

Each stage must have:
- **Stage date**: Auto-set when stage changes
- **Exit criteria fields**: Boolean or picklist fields that enforce exit criteria
- **Required notes**: Free-text field for context (minimum 50 characters)
- **Next step**: Required field capturing the next concrete action with date

### Automation Rules

| Trigger | Action | Purpose |
|---------|--------|---------|
| Deal in stage >2x expected duration | Alert sales manager | Identify stalled deals |
| Stage advanced without required fields | Block advancement | Enforce process compliance |
| Deal closed-lost | Require loss reason from picklist | Enable pattern analysis |
| Handoff triggered | Auto-create task for receiving party | Ensure SLA tracking |
