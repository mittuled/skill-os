# Framework: Analyst Inquiry Responder

Defines inquiry types, triage criteria, response SLAs, preparation methodology, and strategic framing principles for responding to analyst inquiries.

## Inquiry Types

| Type | Description | Source | Strategic Importance |
|------|-------------|--------|---------------------|
| Formal Evaluation Questionnaire | Structured questionnaire from a research firm for a Magic Quadrant, Wave, or Market Guide | Analyst firm portal or email | Critical — directly determines evaluation placement |
| Capability / Product Inquiry | Analyst requests information about specific features, integrations, or roadmap to update their knowledge | Direct analyst email | High — shapes ongoing analyst perception and published research |
| Customer Reference Request | Analyst requests names of customers willing to be interviewed for an evaluation or report | Direct analyst email | High — reference quality directly influences evaluation scores |
| Financial / Business Metrics Inquiry | Analyst requests revenue range, growth rate, customer count, or other business performance data | Direct analyst email or questionnaire | High — business metrics influence market presence scores |
| Market Position / Strategy Inquiry | Analyst asks for the company's view on a market trend, competitor action, or industry event | Direct analyst email or phone | Medium — opportunity to shape analyst's published narrative |
| Competitive Intelligence Inquiry | Analyst asks the company to comment on a competitor's capability or announcement | Direct analyst contact | Medium — handle with care; avoid direct attacks |
| Client Advisory Inquiry | An analyst's client (a buyer) asks the analyst about the company; analyst seeks verification | Direct analyst email | High — often tied to an active deal; fast response critical |
| Press / Media Support Inquiry | Analyst reaches out on behalf of a journalist seeking vendor perspective | Forwarded from analyst | Medium — treat as earned media opportunity |

---

## Inquiry Triage Matrix

| Factor | Weight | High Priority (P1) | Medium Priority (P2) | Low Priority (P3) |
|--------|--------|-------------------|---------------------|------------------|
| Evaluation link | 40% | Feeds directly into MQ, Wave, or Market Guide | Related to an evaluation in the next 6 months | Unrelated to any upcoming evaluation |
| Deal influence | 30% | Analyst is advising an active deal in the pipeline | Analyst is known to advise this buyer segment | No known deal connection |
| Deadline | 20% | <48 hours | 3–5 business days | >5 business days |
| Analyst tier | 10% | Tier 1 (primary evaluator) | Tier 2 (category coverage) | Tier 3 (adjacent coverage) |

**P1 (Critical):** Respond within 24 hours; AR Manager escalates to leadership immediately if content cannot be gathered in time.
**P2 (Important):** Respond within 48–72 hours; cross-functional input gathered within 24 hours.
**P3 (Standard):** Respond within the stated deadline; standard internal review process.

---

## Response SLAs

| Inquiry Type | SLA | Escalation Trigger |
|-------------|-----|-------------------|
| Formal Evaluation Questionnaire | Full response by stated deadline; interim acknowledgement within 24 hours | Flag to leadership if deadline is <5 business days away |
| Client Advisory (deal-related) | Same-day acknowledgement; full response within 24 hours | Escalate to sales and leadership immediately |
| Capability / Product Inquiry | 48–72 hours | Flag if requires legal review or involves unannounced features |
| Customer Reference Request | 48 hours for initial list; references briefed within 1 week | Flag if <3 suitable references are available |
| Financial Metrics | 48–72 hours | Requires CFO/finance approval for any revenue or growth data |
| Market Strategy | 72 hours | No escalation unless involves forward-looking statements |

---

## Preparation Methodology

### Step 1: Inquiry Intake (Day 0)

1. Log the inquiry in the AR tracker immediately upon receipt
2. Record: analyst name, firm, inquiry type, deadline, information requested
3. Apply triage matrix to assign priority level (P1/P2/P3)
4. Identify internal stakeholders who own the required information:
   - Product data → CPO or Product Lead
   - Customer references → Customer Success or Sales
   - Financial / business metrics → CFO or Finance
   - Competitive positioning → AR Manager + CEO
5. Send intake brief to relevant stakeholders with information request and deadline

### Step 2: Content Gathering (Day 0–1 for P1; Day 0–2 for P2)

| Information Category | Internal Source | Preparation Notes |
|--------------------|----------------|-------------------|
| Product capabilities | Product team | Current spec sheet; avoid over-claiming; align with public documentation |
| Customer references | CS / Sales | Pre-brief references before sharing names; confirm willingness and availability |
| Business metrics | Finance | Use approved ranges; avoid specific revenue unless explicitly approved |
| Market positioning | AR Manager + CEO | Align with current messaging framework; avoid contradicting other public statements |
| Roadmap | Product Lead | Only share what is on record or behind NDA; flag unannounced items |

### Step 3: Response Drafting

**Strategic Framing Principles:**

| Principle | Application |
|-----------|------------|
| Answer the question — then steer | Directly address what was asked before adding strategic context; evasion triggers analyst skepticism |
| Lead with evidence, not claims | Support every positioning statement with a customer metric, analyst citation, or data point |
| Frame gaps as roadmap progress | If a gap exists, acknowledge it and provide the timeline and plan for closure — never claim a capability that does not exist |
| Maintain consistency | Every response must align with the current positioning framework and previous analyst interactions — contradictions are flagged by analysts across firms |
| Avoid competitive attacks | Compete on strengths; never make unverifiable claims about competitors |

### Step 4: Internal Review

| Reviewer | What They Check | Required For |
|----------|----------------|-------------|
| Product Lead | Accuracy of capability claims | All product-related inquiries |
| Legal | Sensitive data, forward-looking statements, litigation-adjacent content | Any inquiry involving financial data, regulatory matters, or customer PII |
| CEO / Executive | Strategic alignment, tone, message consistency | All P1 inquiries; evaluation questionnaires |
| AR Manager (final) | Strategic framing, completeness, SLA compliance | Every inquiry before submission |

---

## Response Tracker Fields

| Field | Content |
|-------|---------|
| Inquiry date | YYYY-MM-DD received |
| Analyst name + firm | Full name and firm |
| Inquiry type | From inquiry type table |
| Priority | P1 / P2 / P3 |
| Deadline | YYYY-MM-DD |
| Response sent date | YYYY-MM-DD |
| Key messages delivered | 3–5 bullet summary of what was communicated |
| Data shared | List of metrics or materials provided |
| Legal review required | Y/N |
| Open commitments | Any follow-up actions promised |
| Publication impact | Resulting report or advisory (when published) |
