---
name: data-room-builder
description: >
  This skill builds and maintains the investor data room with organised due diligence
  materials. Use when asked to set up a data room, update diligence materials, or
  prepare for investor due diligence. Also consider when an existing data room has
  stale documents that could undermine credibility. Suggest when the user is entering
  diligence without a current data room.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../data-room-v1-builder/SKILL.md
  - ../fundraising-process-manager/SKILL.md
---

# data-room-builder

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Builds and maintains the investor data room with organised due diligence materials covering financials, legal, product, team, and corporate governance to support fundraising and strategic transactions.

## When to Use

- When a fundraising round is in preparation and the data room needs to be updated with current materials.
- When an investor enters diligence and requests access to organized company documentation.
- When a strategic transaction (M&A, secondary, partnership) requires a comprehensive data room.

## Workflow

1. **Structure Definition**: Define the data room folder structure covering standard diligence categories: corporate (formation docs, bylaws, board minutes), financial (statements, model, cap table), legal (contracts, IP, litigation), product (roadmap, metrics, architecture), and team (org chart, key bios). Deliverable: data room folder structure with index.
2. **Document Collection**: Collect current documents from each department owner. Verify documents are the latest versions, properly named, and appropriately redacted (remove customer PII, employee compensation details). Deliverable: collected and verified document set.
3. **Quality Review**: Review each document for completeness, accuracy, and presentation quality. Flag any gaps (missing contracts, outdated financials, unsigned board resolutions). Deliverable: document quality checklist with gap list.
4. **Access Management**: Configure data room permissions by investor (read-only, watermarked, time-limited). Set up activity tracking to monitor which documents each investor views. Deliverable: configured data room with access controls.
5. **Ongoing Maintenance**: Update materials as new documents are created (monthly financials, new contracts, board minutes). Archive outdated versions. Maintain the index current. Deliverable: maintained data room with version control.

## Anti-Patterns

- **Document dumping**: Uploading documents without organization, naming conventions, or an index. *Why*: disorganized data rooms signal operational sloppiness and waste investor time, creating a negative impression during diligence.
- **Stale materials**: Leaving outdated documents (last quarter's financials, old org chart) in the data room without updating. *Why*: stale materials force investors to ask for updates, slowing the process and signalling that IR is not on top of operations.
- **Over-sharing sensitive data early**: Including highly sensitive materials (detailed customer lists, full compensation data, trade secrets) before an investor has demonstrated serious intent. *Why*: premature sharing creates competitive risk without corresponding commitment from the investor.

## Output

**On success**: Produces a current, organized data room with folder structure, verified documents, access controls, and activity tracking. Delivered as an ongoing maintained resource.

**On failure**: Report which document categories are incomplete, what materials are available, and what actions are needed to fill gaps. Provide a timeline and owners for each missing item.

## Related Skills

- [`data-room-v1-builder`](../data-room-v1-builder/SKILL.md) -- Builds the initial data room for first-time fundraisers; this skill maintains and evolves it.
- [`fundraising-process-manager`](../fundraising-process-manager/SKILL.md) -- Manages the fundraising process that this data room supports.
