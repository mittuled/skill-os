---
name: investor-pipeline-manager
description: >
  This skill manages the investor relationship pipeline including tracking, nurturing,
  and prioritization. Use when asked to maintain the investor CRM, prioritize investor
  outreach, or track relationship status. Also consider when preparing for a future
  fundraise and needing to build relationships early. Suggest when the user is
  approaching investors without pipeline tracking.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../fundraising-process-manager/SKILL.md
  - ../investor-comms-drafter/SKILL.md
---

# investor-pipeline-manager

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Manages the investor relationship pipeline by tracking interactions, nurturing relationships between rounds, prioritizing outreach targets, and maintaining a CRM that ensures no high-value investor relationship goes cold.

## When to Use

- When the company is between fundraising rounds and needs to build relationships with potential future investors.
- When inbound investor interest arrives and needs to be tracked, qualified, and prioritized.
- When preparing for a fundraise and needing to identify which nurtured relationships are ready for a formal process.

## Workflow

1. **Pipeline Setup**: Configure the investor CRM with stages (cold, warm, met, engaged, committed, passed), custom fields (thesis fit, check size, portfolio conflicts, warm intro path), and tracking for last contact date. Deliverable: configured investor CRM.
2. **Investor Research**: Research and profile target investors: investment thesis, recent deals, fund size and deployment pace, partner focus areas, and portfolio companies. Deliverable: investor profiles in CRM.
3. **Nurture Cadence**: Establish a touch cadence for each pipeline tier. Warm leads receive monthly updates; engaged investors get quarterly coffee meetings or calls. Track every interaction. Deliverable: nurture schedule with interaction log.
4. **Pipeline Review**: Conduct monthly pipeline reviews with the CEO. Assess which relationships are progressing, which are stale, and which new investors should be added. Deliverable: pipeline review summary with action items.

## Anti-Patterns

- **Fundraise-only outreach**: Only contacting investors when actively raising, ignoring relationship building between rounds. *Why*: cold outreach during a fundraise yields lower conversion than warm relationships built over months of genuine engagement.
- **Quantity over quality**: Building a massive pipeline of hundreds of investors without depth of relationship. *Why*: a fundraise is won by 1-2 lead investors; deep relationships with 20 well-matched investors outperform shallow contact with 200.
- **No CRM discipline**: Tracking investor relationships in email threads and memory rather than a structured system. *Why*: institutional knowledge is lost when team members change, and relationship context cannot be leveraged at scale.

## Output

**On success**: Produces a maintained investor CRM with current profiles, interaction history, nurture schedules, and pipeline review summaries. Delivered on an ongoing basis with monthly pipeline reviews.

**On failure**: Report which investor relationships have gone stale, which CRM data is incomplete, and recommended actions to re-engage lapsed contacts. Include a prioritized list of relationships needing immediate attention.

## Related Skills

- [`fundraising-process-manager`](../fundraising-process-manager/SKILL.md) -- The pipeline feeds qualified investors into the active fundraising process.
- [`investor-comms-drafter`](../investor-comms-drafter/SKILL.md) -- Investor communications are the primary nurture mechanism for pipeline relationships.
