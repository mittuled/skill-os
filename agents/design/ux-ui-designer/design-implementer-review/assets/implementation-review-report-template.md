# Design Implementation Review Report

## Metadata

| Field | Value |
|-------|-------|
| Review Date | YYYY-MM-DD |
| Feature | |
| Reviewer | |
| Engineer | |
| Figma Spec | [Link] |
| Staging URL | [Link] |
| PR / Branch | [Link] |
| Review Outcome | Approved / Conditional / Requires Rework |

---

## Review Scope

**Screens / states in scope:**
- [ ] Screen 1 — [description]
- [ ] Screen 2 — [description]

**Breakpoints tested:** Mobile (375px) / Tablet (768px) / Desktop (1280px) / [others]

---

## Visual Fidelity Checklist

| Element | Expected (Figma) | Actual (Staging) | Pass / Fail | Notes |
|---------|-----------------|-----------------|-------------|-------|
| Spacing | | | | |
| Typography (family / size / weight / line-height) | | | | |
| Colour tokens | | | | |
| Border radius | | | | |
| Elevation / shadow | | | | |
| Icons | | | | |

---

## Interaction State Checklist

| State | Designed? | Implemented? | Correct? | Notes |
|-------|-----------|-------------|----------|-------|
| Default / resting | ✓ | | | |
| Hover | ✓/N/A | | | |
| Focus | ✓ | | | |
| Active / pressed | ✓ | | | |
| Disabled | ✓/N/A | | | |
| Loading | ✓/N/A | | | |
| Error | ✓/N/A | | | |
| Empty | ✓/N/A | | | |
| Success / confirmation | ✓/N/A | | | |

---

## Responsive Behaviour Checklist

| Breakpoint | Layout Correct | Component Adaptation | Content Truncation | Pass / Fail |
|-----------|---------------|---------------------|-------------------|------------|
| 375px (mobile) | | | | |
| 768px (tablet) | | | | |
| 1280px (desktop) | | | | |
| 1440px (large desktop) | | | | |

---

## Accessibility Implementation Checklist

| Check | Result | Notes |
|-------|--------|-------|
| Focus order logical | Pass / Fail / N/A | |
| Keyboard navigation complete | Pass / Fail | |
| ARIA labels present and correct | Pass / Fail | |
| Colour contrast — text (4.5:1) | Pass / Fail | |
| Colour contrast — UI elements (3:1) | Pass / Fail | |
| Screen reader announcements (spot check) | Pass / Fail / Not tested | |
| Error messages associated with inputs | Pass / Fail / N/A | |

---

## Design System Compliance

| Check | Result | Notes |
|-------|--------|-------|
| Correct components used per mapping | Pass / Fail | |
| No detached instances | Pass / Fail | |
| All tokens from design system | Pass / Fail | |

---

## Deviation Log

| # | Screen | Element | Expected | Actual | Figma Ref | Severity | Ticket |
|---|--------|---------|---------|--------|-----------|----------|--------|
| 1 | | | | | [Link] | Blocking / Minor | |
| 2 | | | | | | | |

**Severity definitions:**
- **Blocking** — Must fix before release; incorrect interaction state, accessibility failure, or major visual drift
- **Minor** — Noticeable but not blocking; address in next iteration

---

## Verdict

**Outcome:** Approved / Conditionally Approved (minor fixes) / Requires Rework

**Summary:**
> (1–3 sentences on overall implementation quality and any patterns of deviation.)

**Blocking issues to resolve before release:**
1.
2.

**Distribution:** Engineer, Engineering Lead, Product Manager
