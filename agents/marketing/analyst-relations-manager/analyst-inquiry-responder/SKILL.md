---
name: analyst-inquiry-responder
description: >
  Responds to analyst inquiries with strategically framed answers that reinforce the company's positioning in research.
  Use when an analyst firm sends a formal inquiry, requests customer references, or asks for product and financial data for upcoming research.
  Also consider when an analyst is advising a buyer in an active deal and needs information before providing a recommendation.
  Suggest when an evaluation questionnaire arrives or when an analyst inquiry has been pending for more than 24 hours without a response plan.
department: marketing
agent: analyst-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - analyst-briefing-scheduler
  - magic-quadrant-strategy
  - analyst-report-monitor
triggers:
  - "respond to analyst inquiry"
  - "handle analyst RFI"
  - "analyst inquiry response"
  - "draft analyst reply"
  - "answer analyst questions"
---

# analyst-inquiry-responder

## Agent: Analyst Relations Manager

L2 analyst relations manager responsible for analyst briefings, inquiry responses, Magic Quadrant strategy, and peer review platform management.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Responds to analyst inquiries with accurate and strategically framed information, ensuring every interaction reinforces the company's desired positioning and builds analyst confidence.

## When to Use

- An analyst firm sends a formal inquiry requesting data, customer references, or product details for upcoming research.
- An analyst reaches out informally with questions about the company's strategy, market position, or competitive differentiation.
- A client of an analyst firm asks the analyst about the company, and the analyst seeks clarification before advising.
- An evaluation questionnaire arrives that requires coordinated input from multiple internal teams.

## Workflow

1. Triage the inquiry: identify the analyst, their firm, the research context, the deadline, and the inquiry type using the inquiry type table in [`references/framework.md`](references/framework.md). Apply the triage matrix to assign priority level P1/P2/P3.
2. Assess the strategic importance and response SLA: determine whether the inquiry relates to an upcoming evaluation, a published report, or a client advisory that could influence a deal using the triage criteria in [`references/framework.md`](references/framework.md). Activate P1 escalation protocol if deal-linked or evaluation-linked with <48 hours to respond.
3. Gather the required information from internal stakeholders per the content gathering step in [`references/framework.md`](references/framework.md): product, engineering, customer success, or finance depending on the inquiry scope. Route each information category to the correct owner.
4. Draft the response using [`assets/inquiry-response-template.md`](assets/inquiry-response-template.md). Apply the strategic framing principles from [`references/framework.md`](references/framework.md): answer first, then steer; evidence before claims; acknowledge gaps with a remediation timeline.
5. Review the draft with the relevant internal stakeholders per the review table in [`references/framework.md`](references/framework.md). Confirm factual accuracy and strategic alignment. Get legal review for any data-sharing sensitivities or financial metrics.
6. Submit the response within the analyst's stated deadline. If the deadline cannot be met, communicate proactively and negotiate an extension.
7. Log the inquiry and response in the analyst relations tracker using all response tracker fields from [`references/framework.md`](references/framework.md): date, analyst, type, priority, key messages delivered, data shared, and open commitments.
8. Monitor for the resulting publication or advisory to assess whether the response influenced the analyst's framing. Update the tracker with the publication impact when the report is released.

## Anti-Patterns

- **Providing raw data without strategic context.** *Why*: Analysts interpret data through their own frameworks; unframed numbers may be used to support a narrative that hurts the company's positioning.
- **Missing inquiry deadlines without proactive communication.** *Why*: Analysts work on publication schedules; a missed deadline means the company's perspective is absent from the research entirely.
- **Responding to inquiries in a silo without cross-functional input.** *Why*: Inaccurate product claims or misaligned financial data erode analyst trust and create contradictions with other public statements.
- **Treating every inquiry with equal priority.** *Why*: An inquiry feeding into a Magic Quadrant evaluation has orders of magnitude more impact than a routine market update; triage determines resource allocation.

## Output

**Success artifacts:**
- Inquiry response documents with strategically framed answers
- Analyst relations tracker updated with inquiry details and response log
- Internal briefing notes summarising what was communicated to each analyst
- Follow-up action items for any commitments made during the response

**Failure reporting:**
- Flag deadline risks for high-priority inquiries at least 48 hours before the due date
- Escalate inquiries requesting sensitive data or requiring legal review to marketing leadership immediately

## Related Skills

- [`analyst-briefing-scheduler`](../analyst-briefing-scheduler/SKILL.md) — Formal briefings often precede or follow inquiries; use to prepare for the analyst interaction that generated the inquiry.
- [`magic-quadrant-strategy`](../magic-quadrant-strategy/SKILL.md) — Evaluation questionnaires are a specialised form of formal inquiry requiring the full submission strategy managed by this skill.
- [`analyst-report-monitor`](../analyst-report-monitor/SKILL.md) — Monitoring resulting publications confirms whether inquiry responses influenced the analyst's published framing.
