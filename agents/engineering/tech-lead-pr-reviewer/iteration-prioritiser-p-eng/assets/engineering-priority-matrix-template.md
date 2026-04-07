# Engineering Iteration Priority Matrix: [Sprint / Phase Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Tech Lead |
| Sprint | [Sprint N] |
| Prioritization Method | [Technical risk / Value / Dependencies] |
| Skill | iteration-prioritiser-p-eng |

## Engineering Priority Assessment

### Technical Risk and Value Matrix

| ID | Item | Technical Risk (1–5) | Business Value (1–5) | Dependency Count | Priority Score | Order |
|----|------|--------------------|--------------------|-----------------|---------------|-------|
| [TICKET-001] | [Title] | [4 — novel integration] | [5 — customer blocker] | [0] | [Risk+Value-Dependencies] | [1st] |

**Score** = Technical Risk × 0.4 + Business Value × 0.6 − (Dependency Count × 0.5)

Higher score = tackle first (high-value work with risk removed early)

### Dependency-First Ordering

Items that unlock other items must be scheduled first:

```
TICKET-005 (foundation) → TICKET-010 (depends on 005) → TICKET-015 (depends on 010)
TICKET-007 (independent)
TICKET-020 (independent)
```

### Sprint Sequence Plan

| Day Range | Items to Complete | Rationale |
|-----------|-----------------|-----------|
| Days 1–3 | [TICKET-005] | [Unblocks TICKET-010 and TICKET-015 — critical path] |
| Days 4–7 | [TICKET-010, TICKET-007] | [010 unlocked; 007 independent] |
| Days 8–10 | [TICKET-015, TICKET-020] | [Final items; 015 depends on 010] |

## Tech Debt vs. Feature Balance

| Category | Points | % of Sprint |
|----------|--------|------------|
| Features | [X] | [X%] |
| Tech debt | [X] | [X%] |
| Bug fixes | [X] | [X%] |
| Target balance | — | 70% feature / 20% debt / 10% bugs |

**Current vs. target**: [On target / Tech debt overdue — increase debt allocation]

## Deferred Items

| ID | Item | Reason | Risk of Continued Deferral |
|----|------|--------|---------------------------|
| [TICKET-050] | [Tech debt item] | [Capacity] | [Will block [feature] in Sprint N+2] |
