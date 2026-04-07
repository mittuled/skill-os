# Design Iteration Backlog — Prioritized

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Product Area | Analytics Dashboard |
| Prepared by | Head of Design |
| Items Scored | 4 |
| Status | Ready for stakeholder alignment |
| Skill | iteration-prioritiser-design |

## Executive Summary

Four post-launch iteration items were scored against user impact, business value, design effort, and accessibility severity. The export button discoverability issue ranks highest at 82/100 and is a must-do due to its direct revenue impact. The keyboard navigation WCAG violation is also must-do at 73/100 — a legal compliance blocker. The mobile chart legend overlap is a should-do. The empty state copy fix is a quick-win could-do that can be shipped alongside any of the above items.

## Prioritized Backlog

| Rank | ID | Title | Score | Tier |
|---|---|---|---|---|
| 1 | DX-004 | Export button not discoverable | 82 | must-do |
| 2 | DX-002 | Date range picker no keyboard navigation | 73 | must-do |
| 3 | DX-001 | Chart legend overlaps on mobile | 68 | should-do |
| 4 | DX-003 | Empty state uses developer placeholder text | 60 | should-do |

## Tier Breakdown

### Must-Do (critical issues, address this sprint)

**DX-004 — Export button not discoverable (Score: 82)**
- User Impact: 4/5 | Business Value: 5/5 | Design Effort: 3/5 | Accessibility: 0/5
- Source: 3 support tickets, cited in 2 deal blockers
- Note: Export discoverability is blocking deal cycles where prospects need CSV export for reporting workflows. Highest priority item.

**DX-002 — Date range picker keyboard navigation (Score: 73)**
- User Impact: 3/5 | Business Value: 2/5 | Design Effort: 3/5 | Accessibility: 5/5
- Source: Accessibility audit
- Note: WCAG 2.1 AA keyboard trap — legal compliance requirement, not optional. Must ship before next major customer review.

### Should-Do (high-impact improvements, next sprint cycle)

**DX-001 — Chart legend overlaps on mobile (Score: 68)**
- User Impact: 4/5 | Business Value: 3/5 | Design Effort: 4/5 | Accessibility: 2/5
- Source: Session recordings, 8 support tickets
- Note: Affects ~35% of mobile users. Relatively low effort (design change only, no new component).

**DX-003 — Empty state placeholder text (Score: 60)**
- User Impact: 2/5 | Business Value: 2/5 | Design Effort: 5/5 | Accessibility: 0/5
- Source: NPS verbatims
- Note: XS effort — copy-only change. Recommend shipping as a rider on any related PR this sprint.

## Recommended Next Steps

1. Confirm stakeholder alignment on this prioritization with PM and Engineering Lead by end of week
2. Add DX-004 and DX-002 to the next sprint as must-do items
3. Schedule DX-001 for the following sprint cycle
4. Bundle DX-003 with the next engineering deployment touching the dashboard
5. Re-prioritize this backlog in 3 weeks following the next NPS survey close
