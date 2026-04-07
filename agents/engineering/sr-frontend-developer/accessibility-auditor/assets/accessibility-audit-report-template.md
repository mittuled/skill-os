# Accessibility Audit Report: [Page / Component / Feature]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Auditor | Sr Frontend Developer |
| Scope | [Page URL / Component name / Feature] |
| Standard | WCAG 2.2 Level AA |
| Tools Used | [axe-core / Lighthouse / NVDA / VoiceOver / JAWS / Manual] |
| Skill | accessibility-auditor |
| Status | [Pass / Fail / Conditional Pass] |

## Verdict

**Overall result**: [PASS — meets WCAG 2.2 AA / FAIL — N critical violations / CONDITIONAL PASS — N items to resolve by Date]
**Critical violations (must fix before release)**: [N]
**Serious violations (should fix in current sprint)**: [N]
**Moderate violations (track in backlog)**: [N]
**Minor issues (optional improvements)**: [N]

## Violation Summary

| ID | WCAG Criterion | Level | Severity | Component | Status |
|----|---------------|-------|----------|-----------|--------|
| A-001 | [1.1.1 Non-text Content] | [A] | [Critical] | [Component or page] | [Open] |
| A-002 | [1.4.3 Contrast (Minimum)] | [AA] | [Serious] | | |
| A-003 | [2.4.7 Focus Visible] | [AA] | [Serious] | | |

## Detailed Violations

### A-001 — [Violation Title]

**WCAG Criterion**: [1.1.1 Non-text Content — Level A]
**Severity**: Critical
**Impact**: [Screen reader users cannot determine the purpose of this element]
**Component / Location**: [ComponentName at /page/path, line N in component]

**Evidence**
```html
<!-- Current (non-compliant) -->
<img src="/hero-image.jpg" />

<!-- Required (compliant) -->
<img src="/hero-image.jpg" alt="Team celebrating product launch at company headquarters" />
```

**Remediation**: Add descriptive `alt` text to all meaningful images. For decorative images use `alt=""`.
**Estimated effort**: [< 1 hour]

---

### A-002 — [Violation Title]

[Repeat structure for each violation]

## Screen Reader Testing Results

### Keyboard Navigation

| Flow | Expected | Result | Issue |
|------|----------|--------|-------|
| Tab through form | All fields reachable in logical order | [Pass/Fail] | [Issue if fail] |
| Submit form with Enter | Form submits | [Pass/Fail] | |
| Modal open/close | Focus trapped in modal; returns on close | [Pass/Fail] | |
| Dropdown navigation | Arrow keys navigate options | [Pass/Fail] | |
| Skip to main content | Skip link visible on first Tab; functional | [Pass/Fail] | |

### Screen Reader Announcements (NVDA / VoiceOver)

| Element | Expected Announcement | Actual Announcement | Pass? |
|---------|----------------------|---------------------|-------|
| [Button] | "Submit order, button" | [Actual] | [Yes/No] |
| [Error message] | Alert announced immediately on error | [Actual] | |
| [Loading state] | "Loading, please wait" | [Actual] | |
| [Success message] | Status announced after action | [Actual] | |

## Color and Contrast Audit

| Element | Foreground | Background | Ratio | Required | Pass? |
|---------|-----------|-----------|-------|----------|-------|
| Body text | [#333333] | [#FFFFFF] | [12.6:1] | 4.5:1 | Pass |
| Secondary text | [#999999] | [#FFFFFF] | [2.8:1] | 4.5:1 | FAIL |
| Button text | [#FFFFFF] | [#1A73E8] | [5.1:1] | 4.5:1 | Pass |
| Link (default) | [#1A73E8] | [#FFFFFF] | [3.7:1] | 4.5:1 | FAIL |
| Focus indicator | [#1A73E8] | [#FFFFFF] | [3.7:1] | 3:1 | Pass |

## Automated Scan Results

| Tool | Issues Found | Critical | Serious | Moderate |
|------|-------------|---------|---------|---------|
| axe-core (browser extension) | [N] | [N] | [N] | [N] |
| Lighthouse accessibility score | [X/100] | — | — | — |

**Note**: Automated tools detect approximately 30–40% of accessibility issues. Manual testing is required for the remainder.

## Remediation Plan

| ID | Severity | Action | Owner | Sprint |
|----|----------|--------|-------|--------|
| A-001 | Critical | [Add alt text to all images in HeroSection] | [Frontend dev] | [Current] |
| A-002 | Serious | [Increase secondary text color contrast to ≥ 4.5:1] | [Frontend dev] | [Current] |
| A-003 | Moderate | [Add visible focus ring to all interactive elements] | [Frontend dev] | [Next] |
