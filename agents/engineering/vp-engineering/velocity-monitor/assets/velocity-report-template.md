# Velocity Report: [Team Name] — [Sprint / Quarter]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | VP Engineering |
| Period | [Sprint N / Q1–Q4 YYYY] |
| Team | [Team name and size] |
| Skill | velocity-monitor |
| Status | [Draft / Final] |

## Executive Summary

[2–3 sentences covering trend direction, key blocker if any, and the single most important action.
GUIDANCE: Lead with the number — "Team delivered 34 points this sprint, 12% above the 4-sprint rolling average of 30.4. No velocity blockers remain active. Recommended action: increase next sprint commitment to 36 points."]

## Velocity Metrics

### Sprint Velocity (Last 6 Sprints)

| Sprint | Committed | Delivered | Delta | Carry-Over |
|--------|-----------|-----------|-------|------------|
| [N-5] | [pts] | [pts] | [+/-] | [pts] |
| [N-4] | [pts] | [pts] | [+/-] | [pts] |
| [N-3] | [pts] | [pts] | [+/-] | [pts] |
| [N-2] | [pts] | [pts] | [+/-] | [pts] |
| [N-1] | [pts] | [pts] | [+/-] | [pts] |
| [N — current] | [pts] | [pts] | [+/-] | [pts] |

**4-Sprint Rolling Average**: [X pts]
**Trend**: [Improving / Stable / Declining] ([+/- X%] vs. prior 4-sprint window)

### DORA Metrics (Current Sprint / Week)

| Metric | Current | 4-Sprint Avg | Target | Status |
|--------|---------|-------------|--------|--------|
| Deployment Frequency | [X/day or X/week] | [X] | [≥ 1/day] | [Green/Amber/Red] |
| Lead Time for Change | [X hrs] | [X hrs] | [< 24 hrs] | [Green/Amber/Red] |
| Change Failure Rate | [X%] | [X%] | [< 5%] | [Green/Amber/Red] |
| Mean Time to Restore | [X hrs] | [X hrs] | [< 1 hr] | [Green/Amber/Red] |

### Predictability Score

**Predictability** = Delivered / Committed × 100

| Sprint | Score | Rating |
|--------|-------|--------|
| [N-5] | [%] | [High/Med/Low] |
| [N-4] | [%] | [High/Med/Low] |
| [N-3] | [%] | [High/Med/Low] |
| [N-2] | [%] | [High/Med/Low] |
| [N-1] | [%] | [High/Med/Low] |
| [N] | [%] | [High/Med/Low] |

> Rating thresholds: High ≥ 90% | Medium 70–89% | Low < 70%

## Blocker Analysis

### Active Blockers

| # | Description | Blocker Type | Days Active | Owner | ETA |
|---|-------------|-------------|-------------|-------|-----|
| 1 | [Description] | [Tech Debt / Dependency / Process / External] | [N] | [Name] | [Date] |

**Blocker impact on velocity**: [X pts blocked this sprint] / [Y% of committed capacity]

### Resolved Blockers (This Sprint)

| # | Description | Days to Resolve | Root Cause |
|---|-------------|----------------|------------|
| 1 | [Description] | [N days] | [Root cause] |

### Blocker Trend

[Increasing / Stable / Decreasing] — [1 sentence on trend and contributing factor]

## Capacity Analysis

### Planned vs. Actual Capacity

| Category | Planned Hrs | Actual Hrs | Delta |
|----------|-------------|------------|-------|
| Feature development | [X] | [X] | [+/-] |
| Bug fixes | [X] | [X] | [+/-] |
| Tech debt | [X] | [X] | [+/-] |
| Unplanned work | [0] | [X] | [+/-] |
| Ceremonies / meetings | [X] | [X] | [+/-] |
| **Total** | **[X]** | **[X]** | **[+/-]** |

**Unplanned work rate**: [X%] (target: < 20%)

## Recommendations

### Next Sprint Commitment

**Recommended commitment**: [X pts]
**Basis**: 4-sprint rolling average ([X pts]) × confidence factor ([0.85–1.05 based on carry-over and risk])

### Actions

| Priority | Action | Owner | Due |
|----------|--------|-------|-----|
| P1 | [Specific action to address top blocker or trend] | [Role] | [Date] |
| P2 | [Process or tooling improvement] | [Role] | [Date] |

## Appendix: Story Point Distribution

### By Ticket Type

| Type | Count | Points | % of Total |
|------|-------|--------|------------|
| Feature | [N] | [X] | [%] |
| Bug | [N] | [X] | [%] |
| Tech Debt | [N] | [X] | [%] |
| Spike | [N] | [X] | [%] |
| **Total** | **[N]** | **[X]** | **100%** |

### By Size Band

| Size | Label | Count | Completed |
|------|-------|-------|-----------|
| 1 pt | XS | [N] | [N] |
| 2 pts | S | [N] | [N] |
| 3 pts | M | [N] | [N] |
| 5 pts | L | [N] | [N] |
| 8 pts | XL | [N] | [N] |
| 13+ pts | Epic (should split) | [N] | [N] |
