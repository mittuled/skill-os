# Framework: documentation-requirements-extractor

Defines the source analysis protocol, requirement categorization taxonomy, priority scoring model, and task template for extracting documentation requirements from engineering specs and developer feedback.

## Source Analysis Protocol

| Source Type | Extraction Focus | Key Questions to Ask | Priority |
|------------|-----------------|---------------------|---------|
| Engineering spec / PRD | New endpoints, changed parameters, deprecated features, new concepts | What is new? What changed? What is removed? What is confusing without context? | High |
| API changelog | Every change that requires documentation update | Is this a breaking change needing migration guide? Does this change a code sample? | High |
| Developer support tickets | Repeated confusion, missing docs, incorrect procedures | What did developers search for that they couldn't find? What question appears 3+ times? | High |
| Developer feedback synthesis | Documented gaps from signal extraction | Which gaps are blocking integration? Which are generating support cost? | High |
| Documentation accuracy audit | Inaccuracies found, broken samples, stale content | What must be updated before it misleads the next developer? | High |
| Analytics (page-level) | High-traffic pages, high-exit pages, zero-result searches | What are developers looking for that we're not answering? | Medium |
| User interviews | Unarticulated needs, mental model gaps | What did the developer assume was documented that wasn't? | Medium |
| Feature request backlog | Upcoming features not yet released | What documentation can be written in advance to accelerate launch? | Medium |

## Requirement Categorization Taxonomy

Every extracted requirement must be categorized before it becomes a task.

| Category | Definition | Documentation Type (Divio) | Example |
|----------|-----------|--------------------------|---------|
| New Content | Net-new page or section needed | Tutorial, How-to, Reference, or Explanation | "Create quickstart for webhooks" |
| Update | Existing page needs changes | Any | "Update POST /payments params for v3" |
| Deprecation Notice | Feature being removed needs warning | Reference + Explanation | "Add deprecation notice to legacy auth endpoint" |
| Migration Guide | Breaking change requires upgrade path | How-to | "Write v1→v2 migration guide for auth redesign" |
| Code Sample | Sample needed, broken, or outdated | Reference | "Add Ruby code sample to all endpoint refs" |
| Error Reference | Error code or message undocumented | Reference | "Document all 4xx errors for /orders endpoint" |
| Concept Explanation | Domain concept missing from docs | Explanation | "Write explanation of webhook signature verification" |
| Accuracy Fix | Specific inaccuracy must be corrected | Any | "Fix wrong parameter type for quantity field" |

## Priority Scoring Model

Score each requirement on two dimensions. Multiply to get priority score.

### Developer Impact (1–5)

| Score | Criteria |
|-------|---------|
| 5 | Blocks integration for any developer; causes support tickets or churn; tied to a release |
| 4 | Affects a common developer path; causes multiple questions per week |
| 3 | Affects occasional workflow; developer can work around with community help |
| 2 | Edge case; affects < 5% of developers; workaround is obvious |
| 1 | Nice-to-have; no developer has complained; improvement to existing clear content |

### Release Urgency (1–5)

| Score | Criteria |
|-------|---------|
| 5 | Tied to a release shipping in < 1 week |
| 4 | Tied to a release shipping in 1–2 weeks |
| 3 | Tied to a release shipping in 2–4 weeks |
| 2 | Backlog item — no release dependency |
| 1 | Long-term improvement — no urgency |

**Priority Score** = Developer Impact × Release Urgency

| Score Range | Priority Tier | SLA |
|-------------|--------------|-----|
| 20–25 | P1 — Urgent | Must be published at or before release |
| 12–19 | P2 — High | Should be published within the sprint |
| 6–11 | P3 — Medium | Scheduled in next sprint or backlog grooming |
| 1–5 | P4 — Low | Backlog; address when bandwidth allows |

## Documentation Task Template

Each task must contain all fields before assignment.

| Field | Description | Example |
|-------|-------------|---------|
| Task ID | Unique reference | DOC-042 |
| Title | What is being written or updated | "Write quickstart for Python SDK v2" |
| Category | From taxonomy | New Content |
| Documentation Type | Divio type | Tutorial |
| Source | What triggered this task | Engineering spec #PR-391 |
| Developer Impact | Score 1–5 | 5 |
| Release Urgency | Score 1–5 | 4 |
| Priority Score | Impact × Urgency | 20 (P1) |
| Scope | Specific pages, sections, or samples affected | quickstart.md + /docs/reference/python-sdk |
| Owner | Assigned writer | [name] |
| Deadline | Hard date or relative to release | 2026-04-14 or "Day of release" |
| Acceptance Criteria | What "done" looks like | "All Python code samples tested; page reviewed by engineering" |
| Dependencies | What must exist before writing can start | "PR-391 merged; Python SDK published to PyPI" |
