# Design Iteration Prioritisation Framework

A weighted scoring model for ranking design iteration candidates against user impact, business value, effort, and accessibility severity.

---

## Core Methodology

Each backlog item is scored across four dimensions. The composite score determines its tier. The process is explicitly evidence-based: every score must cite a source (session data, analytics, audit report, support ticket).

**Composite Score = (User Impact × 0.35) + (Business Value × 0.25) + (Effort Inversion × 0.25) + (Accessibility Severity × 0.15)**

*Effort Inversion: score 10 for XS, 8 for S, 6 for M, 4 for L, 2 for XL — lower effort = higher score.*

---

## Scoring Dimensions

### 1. User Impact (35%)

Measures how severely and broadly users are affected.

| Score | Description |
|-------|-------------|
| 9–10 | Blocks task completion for a large user segment; supported by session data or usability study |
| 7–8 | Causes significant friction or confusion; observed in multiple sessions or feedback channels |
| 5–6 | Noticeable friction; reported by some users; moderate session evidence |
| 3–4 | Minor annoyance; low frequency; anecdotal reports |
| 1–2 | Edge case; affects very few users; no session evidence |

### 2. Business Value (25%)

Measures potential effect on conversion, retention, or revenue.

| Score | Description |
|-------|-------------|
| 9–10 | Directly affects a primary conversion metric or retention driver; data-backed |
| 7–8 | Affects a secondary metric or supports a key business initiative |
| 5–6 | Moderate business relevance; relationship to metrics is indirect |
| 3–4 | Low business relevance; nice-to-have quality improvement |
| 1–2 | No measurable business impact |

### 3. Effort Inversion (25%)

Lower design effort = higher score (XS work that unblocks users is more valuable per unit of effort).

| T-Shirt Size | Design Hours | Score |
|-------------|-------------|-------|
| XS | < 4 h | 10 |
| S | 4–8 h | 8 |
| M | 8–24 h | 6 |
| L | 24–60 h | 4 |
| XL | 60+ h | 2 |

### 4. Accessibility Severity (15%)

WCAG-based severity of the accessibility issue, if any.

| Score | Description |
|-------|-------------|
| 10 | WCAG 2.1 Level A violation (must-fix; blocks assistive technology users) |
| 8 | WCAG 2.1 Level AA violation (strong-fix; standard compliance threshold) |
| 5 | WCAG 2.1 Level AAA violation or best-practice gap |
| 2 | No accessibility component to the issue |

---

## Priority Tiers

| Tier | Composite Score | Label | Action |
|------|----------------|-------|--------|
| P0 | 8.0–10.0 | Must-Do | Address in current or next sprint; blocking quality or compliance issue |
| P1 | 6.0–7.9 | Should-Do | Schedule within 1–2 cycles; high user or business impact |
| P2 | 4.0–5.9 | Could-Do | Address when capacity allows; quality improvement |
| P3 | < 4.0 | Deferred | Log and revisit quarterly; low evidence or impact |

---

## Normalised Backlog Item Format

Each item in the scored backlog must include:

```
ID:              [auto-generated]
Problem:         [1–2 sentences describing the user pain point]
Surface:         [Figma file, screen, component]
Source:          [session analysis / usability test / support ticket / accessibility audit / analytics]
User Impact:     [score] / Evidence: [citation]
Business Value:  [score] / Evidence: [citation]
Effort:          [T-shirt size] → Effort Inversion Score: [score]
A11y Severity:   [score / WCAG criterion if applicable]
Composite Score: [calculated]
Tier:            [P0 / P1 / P2 / P3]
Owner:           [designer name]
```

---

## Design Debt Identification

Use the following signals to identify and surface design debt items for the backlog:

| Signal | Debt Type | Priority Boost |
|--------|-----------|---------------|
| Detached Figma components | Component debt | +0.5 if engineering reports inconsistency |
| Interaction states missing (error, empty, loading) | State debt | +1.0 if missing state causes user confusion |
| Deprecated tokens in use | Token debt | +0.5 if affects > 5 screens |
| Inconsistent pattern across surfaces | Pattern debt | +0.5 if users navigate between inconsistent areas |
| Accessibility issues not filed as P0/P1 | A11y debt | Full A11y severity score applies |

---

## Re-Prioritisation Cadence

| Trigger | Action |
|---------|--------|
| New session analysis report | Re-score User Impact for affected items |
| Quarterly OKR update | Re-score Business Value for all P2/P3 items |
| New accessibility audit | Re-score A11y Severity for flagged items |
| Completed sprint | Archive resolved items; promote any blocked P0s |
| Major product release | Full backlog review against new surface area |
