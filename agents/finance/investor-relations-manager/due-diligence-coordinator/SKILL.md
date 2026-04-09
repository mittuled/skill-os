---
name: due-diligence-coordinator
description: >
  This skill coordinates the due diligence process for fundraising rounds and M&A
  inquiries. Use when asked to manage a diligence request list, coordinate responses
  across departments, or track diligence completion. Also consider when an investor
  sends an initial diligence checklist. Suggest when the user is responding to
  diligence requests ad hoc without a tracking system.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../data-room-manager/SKILL.md
  - ../fundraising-process-manager/SKILL.md
triggers:
  - "coordinate due diligence"
  - "manage DD process"
  - "due diligence coordination"
  - "run investor diligence"
  - "due diligence"
---

# due-diligence-coordinator

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Coordinates the end-to-end due diligence process by triaging investor requests, assigning response owners across departments, tracking completion, and ensuring no request goes unanswered beyond the agreed SLA.

## When to Use

- When an investor or acquirer sends a formal diligence request list and the company needs to coordinate responses.
- When multiple diligence processes are running in parallel across different investors and need centralized tracking.
- When a diligence process is stalling because responses are scattered across departments without clear ownership.

## Workflow

1. **Request Intake**: Receive the diligence request list from the investor. Normalize the format, categorize each item by department (finance, legal, product, engineering, HR), and assign priority based on typical investor decision patterns. Deliverable: categorized request list with priority assignments.
2. **Owner Assignment**: Assign each request item to a specific person with a clear deadline. Brief each owner on context (who the investor is, what stage of the process, sensitivity level). Deliverable: assignment matrix with owners, deadlines, and escalation paths.
3. **Response Coordination**: Track responses daily. Chase overdue items. Review each response for completeness and accuracy before sending to the investor. Redact sensitive information per company policy. Deliverable: reviewed response package per batch.
4. **Q&A Management**: When the investor asks follow-up questions, route them to the original owner, provide context from the initial response, and track the follow-up to closure. Deliverable: Q&A log with response tracking.
5. **Red Flag Triage**: Identify items that could surface legal, financial, or operational concerns during diligence. Brief the CEO and counsel before the investor discovers them organically. Prepare explanations and mitigation narratives. Deliverable: red flag briefing with prepared responses.
6. **Process Close-Out**: When diligence concludes (successfully or not), archive all materials, document lessons learned, and update the standard diligence readiness checklist for future rounds. Deliverable: diligence archive and process retrospective.

## Anti-Patterns

- **Uncoordinated responses**: Allowing multiple people to respond directly to the investor without central review. *Why*: inconsistent or contradictory responses undermine credibility and can surface issues the company intended to address proactively.
- **Missing SLA tracking**: Not tracking response times against the agreed timeline. *Why*: slow responses signal disorganization and reduce investor confidence; investors compare your responsiveness against other companies they are evaluating.
- **Hiding red flags**: Avoiding or delaying responses to sensitive items hoping the investor will not notice. *Why*: investors always find material issues; proactive disclosure with context builds trust while discovery erodes it.
- **No post-mortem**: Completing diligence without documenting what was difficult to produce, what questions recurred, and what gaps exist. *Why*: every future round requires diligence; failing to learn from each process means repeating the same scramble.

## Output

**On success**: Produces a complete diligence response package with all items answered, Q&A log, red flag briefing, and process retrospective. Delivered per the agreed diligence timeline.

**On failure**: Report which items remain unanswered, which departments are blocking, what the investor has flagged as overdue, and recommended escalation actions. Include a revised timeline and risk assessment for the deal.

## Related Skills

- [`data-room-manager`](../data-room-manager/SKILL.md) -- The data room is the primary delivery mechanism for diligence materials.
- [`fundraising-process-manager`](../fundraising-process-manager/SKILL.md) -- Diligence is a phase within the broader fundraising process this skill supports.
