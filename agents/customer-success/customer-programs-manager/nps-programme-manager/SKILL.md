---
name: nps-programme-manager
description: >
  This skill manages the NPS programme including survey timing, response
  analysis, and closed-loop follow-up. Use when asked to run NPS surveys,
  analyze NPS results, or design a closed-loop follow-up process. Also consider
  when customer sentiment is unknown. Suggest when the user relies on anecdotal
  feedback without systematic NPS measurement.
department: customer-success
agent: customer-programs-manager
version: 1.0.0
complexity: medium
related-skills:
  - user-feedback-synthesiser-cs
  - cs-health-monitor
  - customer-reference-programme-manager
triggers:
  - "run NPS programme"
  - "manage NPS survey"
  - "NPS program"
  - "net promoter score"
  - "analyze NPS results"
---

# nps-programme-manager

## Agent: Customer Programs Manager

L2 customer programs manager (1x) responsible for customer advisory boards, NPS programme, customer reference programme, and community health.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Manages the NPS programme including survey timing, distribution, response analysis, and closed-loop follow-up to drive continuous improvement.

## When to Use

- When the organization needs a systematic measurement of customer loyalty and satisfaction.
- When an NPS survey cycle is due and needs planning and execution.
- When NPS results require analysis and follow-up actions to close the loop with respondents.

## Workflow

1. **Design Survey Programme**: Define survey timing (transactional vs. relationship NPS), frequency, audience selection, and survey instrument. Avoid survey fatigue by setting minimum intervals between surveys per customer. Deliverable: NPS programme design document.
2. **Execute Survey**: Distribute the NPS survey to the target audience. Monitor response rates and send reminders if needed. Deliverable: collected NPS responses.
3. **Analyze Results**: Calculate overall NPS, segment scores (by tier, cohort, use case), and trend analysis. Analyze verbatim comments for themes. Deliverable: NPS analysis report with segmented scores and verbatim themes.
4. **Close the Loop**: Follow up with detractors to understand and address concerns. Thank promoters and explore advocacy opportunities. Engage passives with improvement commitments. Deliverable: closed-loop follow-up log.
5. **Drive Action**: Route NPS insights to product, CS, and leadership. Track whether actions taken in response to NPS feedback improve scores in subsequent cycles. Deliverable: NPS action tracker with outcome measurement.

## Anti-Patterns

- **Survey without follow-up**: Collecting NPS scores without contacting detractors or acting on feedback. *Why*: customers who give feedback and see no response become more dissatisfied than if they had never been asked.
- **Over-surveying**: Sending NPS surveys too frequently, causing survey fatigue and declining response rates. *Why*: fatigued respondents either stop responding (selection bias) or give low-effort answers (data quality loss).
- **NPS as vanity metric**: Tracking the headline NPS number without analyzing segments, trends, or verbatims. *Why*: a single number masks critical variations; segment-level analysis reveals where the real problems and opportunities are.

## Output

**On success**: Produces an NPS cycle report containing scores, segmented analysis, verbatim themes, closed-loop follow-up log, and action recommendations. Delivered to leadership, product, and CS.

**On failure**: Report which programme components failed (low response rate, incomplete follow-up), what partial analysis was achieved, and what process improvements are needed for the next cycle.

## Related Skills

- [`user-feedback-synthesiser-cs`](../../../customer-success/customer-success-manager/user-feedback-synthesiser-cs/SKILL.md) -- NPS verbatims are a key input for feedback synthesis.
- [`cs-health-monitor`](../../../customer-success/cs-manager/cs-health-monitor/SKILL.md) -- NPS scores feed into customer health scoring.
- [`customer-reference-programme-manager`](../customer-reference-programme-manager/SKILL.md) -- Promoters identified through NPS are reference recruitment candidates.
