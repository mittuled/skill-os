---
name: data-room-v1-builder
description: >
  This skill builds the first investor data room for the initial fundraising round.
  Use when asked to set up the company's first data room, prepare for seed-stage
  diligence, or organize early-stage company documents for investors. Also consider
  when the company is raising its first priced round and has no data room. Suggest
  when the user is in investor conversations without organized documentation.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: simple
related-skills:
  - ../data-room-builder/SKILL.md
  - ../fundraising-process-manager/SKILL.md
---

# data-room-v1-builder

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Builds the first investor data room for the initial fundraising round, organizing the minimum viable set of documents that early-stage investors expect during diligence.

## When to Use

- When the company is raising its first priced round (seed or Series A) and has no existing data room.
- When angel or pre-seed investors request organized documentation before committing.
- When the company needs to establish a document management foundation that will scale with future rounds.

## Workflow

1. **Document Inventory**: Identify the minimum document set for early-stage diligence: certificate of incorporation, bylaws, cap table, financial statements or projections, material contracts, IP assignments, and founder bios. Check what exists vs. what needs to be created. Deliverable: document inventory with gap analysis.
2. **Document Assembly**: Collect, organize, and name documents using a consistent naming convention. Create any missing documents (e.g., basic financial projections, IP assignment confirmation). Deliverable: assembled document set.
3. **Data Room Setup**: Set up the data room platform (Google Drive, Dropbox, or a purpose-built tool like Notion or Ansarada). Create the folder structure, upload documents, and configure access controls. Deliverable: live data room with organized documents and access controls.

## Anti-Patterns

- **Perfectionism paralysis**: Delaying the data room because not every document is polished or complete. *Why*: early-stage investors expect a work-in-progress company; a good-enough data room that exists beats a perfect one that does not.
- **No access tracking**: Setting up a shared folder without the ability to see who accessed what. *Why*: knowing which documents investors review helps gauge their interest level and anticipate their questions.

## Output

**On success**: Produces a live data room with organized early-stage diligence documents, access controls, and a document index. Delivered before investor outreach begins.

**On failure**: Report which documents are missing, what is available, and what actions are needed to complete the minimum viable data room. Provide a timeline with owners.

## Related Skills

- [`data-room-builder`](../data-room-builder/SKILL.md) -- Evolves this initial data room into a comprehensive diligence resource for later rounds.
- [`fundraising-process-manager`](../fundraising-process-manager/SKILL.md) -- Manages the fundraising process that this data room supports.
