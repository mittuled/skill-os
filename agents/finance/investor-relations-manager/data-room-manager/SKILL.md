---
name: data-room-manager
description: >
  This skill manages the ongoing data room by keeping documents current, controlling
  access, and ensuring completeness for investor diligence. Use when asked to update
  the data room, manage access permissions, or prepare for a diligence process.
  Also consider when documents are stale or a new investor begins diligence.
  Suggest when the user is sharing sensitive documents outside the data room.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../data-room-builder/SKILL.md
  - ../fundraising-process-manager/SKILL.md
  - ../due-diligence-coordinator/SKILL.md
triggers:
  - "manage data room"
  - "update data room"
  - "data room management"
  - "maintain investor data room"
  - "data room upkeep"
---

# data-room-manager

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Manages the ongoing data room by maintaining document currency, controlling investor access, tracking engagement analytics, and ensuring completeness ahead of diligence processes.

## When to Use

- When an investor enters diligence and needs structured access to company documents.
- When quarterly or annual documents are finalized and the data room needs updating.
- When a funding round closes and data room access needs to be revoked or restructured for the next phase.

## Workflow

1. **Document Currency Audit**: Review every data room section against the current state of the business. Flag documents older than their refresh cycle (financials monthly, legal annually, product quarterly). Deliverable: staleness report with update assignments.
2. **Access Management**: Grant, modify, or revoke data room access based on investor status. Apply watermarking and download restrictions per the company's information security policy. Deliverable: access log with current permissions.
3. **Engagement Tracking**: Monitor which documents each investor views, how long they spend, and what they download. Surface engagement patterns to the CEO for meeting preparation. Deliverable: engagement analytics summary.
4. **Completeness Check**: Before each diligence process, run the data room against a standard diligence checklist (corporate docs, financials, IP, contracts, compliance). Identify and fill gaps. Deliverable: completeness checklist with gap resolution status.

## Anti-Patterns

- **Open-access data room**: Granting blanket access to all investors without tiered permissions. *Why*: not all investors should see the same documents at the same stage; unrestricted access leaks sensitive information to parties who have not committed to a process.
- **Set-and-forget documents**: Uploading documents once and never refreshing them. *Why*: stale financials or outdated contracts undermine credibility during diligence and signal poor operational discipline.
- **Ignoring engagement data**: Not tracking which documents investors view. *Why*: engagement data reveals investor intent and interest level, enabling better follow-up timing and meeting preparation.

## Output

**On success**: Produces a current, complete data room with tiered access controls, engagement analytics, and a staleness report. Delivered on an ongoing basis with pre-diligence completeness checks.

**On failure**: Report which documents are missing or stale, which access changes could not be applied, and what steps are needed to restore completeness. Escalate to CFO if sensitive documents are exposed.

## Related Skills

- [`data-room-builder`](../data-room-builder/SKILL.md) -- Builds the initial data room that this skill maintains over time.
- [`fundraising-process-manager`](../fundraising-process-manager/SKILL.md) -- Fundraising triggers diligence processes that require a current data room.
