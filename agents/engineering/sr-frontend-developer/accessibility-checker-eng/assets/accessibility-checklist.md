# Accessibility Checklist: [Component / Feature Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Sr Frontend Developer |
| Component / Feature | [Name] |
| Standard | WCAG 2.2 Level AA |
| Skill | accessibility-checker-eng |

## Quick Checks (Required Before Every PR)

### Keyboard Navigation
- [ ] All interactive elements reachable by Tab key
- [ ] Tab order is logical (follows visual reading order)
- [ ] Focus indicator is visible on all focusable elements
- [ ] No keyboard traps (can always Tab or Esc out)
- [ ] All functionality operable without a mouse

### Semantic HTML
- [ ] Buttons use `<button>` (not `<div>` or `<span>`)
- [ ] Links use `<a href>` (not `<button>` for navigation)
- [ ] Form fields have associated `<label>` elements (not just placeholder)
- [ ] Headings nest logically: h1 → h2 → h3 (no skipping)
- [ ] Lists use `<ul>` / `<ol>` / `<li>` (not styled divs)
- [ ] Tables use `<th>` with `scope` attribute for headers

### ARIA
- [ ] Icon buttons have `aria-label` (e.g., `aria-label="Close dialog"`)
- [ ] Images have `alt` text (descriptive for meaningful, `alt=""` for decorative)
- [ ] Loading states have `aria-busy="true"` or `aria-live` region
- [ ] Error messages linked to inputs via `aria-describedby`
- [ ] Modals/dialogs have `role="dialog"` and `aria-labelledby`
- [ ] No redundant ARIA (e.g., `role="button"` on a `<button>`)

### Color and Contrast
- [ ] Text contrast ≥ 4.5:1 for normal text (use browser DevTools or axe)
- [ ] Text contrast ≥ 3:1 for large text (≥ 18pt or 14pt bold)
- [ ] UI component contrast ≥ 3:1 (borders, icons, input outlines)
- [ ] Information not conveyed by color alone (also uses text, icon, or pattern)

### Forms
- [ ] Required fields indicated in text (not color alone)
- [ ] Error messages describe what went wrong AND how to fix it
- [ ] Error messages linked to the specific field (`aria-describedby`)
- [ ] Autocomplete attributes set for personal data fields (`name`, `email`, `tel`)

### Motion and Animation
- [ ] Animations respect `prefers-reduced-motion` media query
- [ ] No content flashes more than 3 times per second

## Component-Specific Checks

### Modal / Dialog
- [ ] Focus moves into modal when opened
- [ ] Focus trapped inside modal while open (Tab cycles within modal)
- [ ] Focus returns to trigger element when modal closes
- [ ] Escape key closes modal
- [ ] `aria-modal="true"` set

### Dropdown / Select
- [ ] Trigger button announces state: `aria-expanded="true/false"`
- [ ] Menu has `role="listbox"` or `role="menu"` as appropriate
- [ ] Options navigable by arrow keys
- [ ] Selected option announced: `aria-selected="true"`

### Toast / Notification
- [ ] Uses `role="alert"` for urgent messages (reads immediately)
- [ ] Uses `role="status"` for non-urgent updates (reads when idle)
- [ ] Dismiss button has `aria-label`

## Automated Check Results

| Tool | Pass/Fail | Issues Found |
|------|-----------|-------------|
| axe browser extension | [Pass/Fail] | [N issues] |
| Lighthouse accessibility | [Score/100] | |

**Note**: Automated tools find ~30–40% of issues. Manual testing is required.

## Final Sign-off

- [ ] All automated checks passed (0 critical/serious violations)
- [ ] Keyboard navigation tested manually
- [ ] Screen reader spot-check completed (VoiceOver on macOS/iOS or NVDA)
- [ ] Contrast ratios verified

**Developer sign-off**: [Name] | Date: [YYYY-MM-DD]
