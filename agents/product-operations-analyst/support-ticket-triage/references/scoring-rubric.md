# Scoring Rubric: support-ticket-triage

Triages incoming support tickets to identify product bugs and urgent issues requiring product team attention.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Bug Identification Accuracy | 30% | Correct classification of tickets as product bugs vs usage questions vs configuration issues |
| 2 | Severity Assignment Accuracy | 30% | Bug severity matches actual user impact and blast radius |
| 3 | Pattern Detection | 25% | Identification of clusters (same bug reported by multiple users) and cross-ticket correlation |
| 4 | Routing Timeliness | 15% | Product-relevant tickets routed to PM within defined SLA |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: Not present / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Score | Label | Recommended Action |
|-------|-------|-------|-------------------|
| A+ | 9.0–10.0 | Exceptional | Triage complete — escalate flagged items to PM |
| A | 8.0–8.9 | Strong | Proceed — minor classification improvements needed |
| B | 7.0–7.9 | Good | Address misclassified tickets before routing |
| C | 5.0–6.9 | Adequate | Re-review flagged tickets; request second opinion for ambiguous cases |
| D/F | < 5.0 | Inadequate | Restart triage with structured classification checklist |

## Severity Classification Table

Apply this rubric to every ticket classified as a product bug:

| Severity | Criteria | SLA |
|----------|---------|-----|
| P0 – Critical | Data loss, security breach, complete feature failure affecting production users | Route to PM + Engineering immediately (< 1 hour) |
| P1 – High | Core workflow blocked for significant user segment; no workaround | Route to PM within 4 hours |
| P2 – Medium | Feature degraded but workaround exists; affects limited users | Route to PM within 24 hours |
| P3 – Low | Minor UX issue, cosmetic bug, edge case | Add to product bug backlog; weekly review |

## Signal Tables

### Bug Identification Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | All tickets correctly classified as bug/usage/config; misclassification rate < 5% when spot-checked |
| 7-8 | Classification mostly correct; 1-2 ambiguous cases handled with reasonable judgment |
| 5-6 | 10-20% of tickets misclassified; usage questions mixed with bugs |
| 3-4 | Classification inconsistent; no clear methodology applied |
| 0-2 | No classification applied; all tickets treated as undifferentiated queue |

### Severity Assignment Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Severity matches actual impact for all tickets; P0/P1 assignments verified against blast radius |
| 7-8 | Severity mostly accurate; one severity level off on 1-2 edge cases |
| 5-6 | Over- or under-severity on 20%+ of tickets |
| 3-4 | Severity assigned but criteria not applied consistently |
| 0-2 | No severity assignment |

### Pattern Detection

| Score | Evidence |
|-------|----------|
| 9-10 | Cross-ticket clusters identified; duplicate reports merged; root-cause hypothesis documented for clusters |
| 7-8 | Major clusters identified; some duplicates still separate |
| 5-6 | One cluster identified; others missed |
| 3-4 | Tickets reviewed individually; no cross-ticket analysis |
| 0-2 | No pattern detection attempted |

### Routing Timeliness

| Score | Evidence |
|-------|----------|
| 9-10 | All P0/P1 tickets routed within SLA; P2/P3 routed within 24 hours |
| 7-8 | P0/P1 within SLA; P2/P3 routing slightly delayed |
| 5-6 | P1 routed on time; P0 delayed or escalation path not followed |
| 3-4 | Routing occurs but SLAs not tracked or consistently missed |
| 0-2 | No structured routing; tickets unactioned |
