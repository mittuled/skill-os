# Framework: Design Implementation Standards

Reference for translating Figma designs into production-quality frontend code, covering layout systems, responsive breakpoints, accessibility requirements, and performance budgets.

## Implementation Quality Tiers

Every design implementation is assessed against three tiers. Target Tier 1 for all user-facing work:

| Tier | Description | Acceptable For |
|------|-------------|---------------|
| Tier 1 — Pixel Perfect | Matches design in spacing, typography, color, motion, and states | All production features |
| Tier 2 — Functionally Correct | Correct layout and behavior; minor token or spacing deviations | Internal tools, admin panels |
| Tier 3 — Structural Only | Correct component structure; visual polish deferred | Prototypes, spikes |

## Layout System

### Spacing Scale

Use the 4-point grid. All spacing values must be multiples of 4px:

| Token | Value | Common Use |
|-------|-------|-----------|
| `--spacing-1` | 4px | Icon padding, fine adjustments |
| `--spacing-2` | 8px | Inline element gaps |
| `--spacing-3` | 12px | Small component internal padding |
| `--spacing-4` | 16px | Standard internal component padding |
| `--spacing-6` | 24px | Section separation within a card |
| `--spacing-8` | 32px | Card internal padding, form field stacks |
| `--spacing-12` | 48px | Section separation between components |
| `--spacing-16` | 64px | Page section separation |

**Non-4-point values are a code smell.** Exception: 1px borders and 2px fine rules only.

### Grid System

| Breakpoint | Name | Min Width | Columns | Gutter | Margin |
|-----------|------|-----------|---------|--------|--------|
| xs | Mobile S | 320px | 4 | 16px | 16px |
| sm | Mobile L | 480px | 4 | 16px | 24px |
| md | Tablet | 768px | 8 | 24px | 32px |
| lg | Desktop | 1024px | 12 | 24px | 40px |
| xl | Wide | 1280px | 12 | 32px | 80px |
| 2xl | Ultra-wide | 1440px | 12 | 32px | Auto (max-width: 1280px centered) |

## Responsive Implementation Strategy

### Breakpoint Decision Tree

```
Is the layout change purely a column-count shift?
  └── Yes → Use CSS grid with auto-fill/auto-fit; no JS needed
  └── No → Does it require hiding/showing different content?
       └── Yes → Use CSS display:none at breakpoint; verify screen reader impact
       └── No → Does it require different interaction patterns (tap vs. click)?
            └── Yes → Conditional component render via JS (lazy-loaded)
            └── No → Pure CSS layout change only
```

### Mobile-First Implementation Rules

1. Write base styles for mobile first; add `@media (min-width: Xpx)` for larger breakpoints.
2. Never use `max-width` media queries — they are harder to maintain and override.
3. Test all breakpoints before marking a component complete: 320px, 768px, 1024px, 1440px.
4. Verify touch target size: minimum 44×44px for any interactive element on mobile.

## Typography Implementation

### Type Scale

| Token | Size | Line Height | Weight | Use |
|-------|------|------------|--------|-----|
| `--type-display-2xl` | 72px | 1.1 | 700 | Hero headlines |
| `--type-display-xl` | 60px | 1.2 | 700 | Page headings |
| `--type-heading-xl` | 36px | 1.25 | 600 | Section headings |
| `--type-heading-lg` | 28px | 1.3 | 600 | Card headings |
| `--type-heading-md` | 22px | 1.35 | 600 | Sub-section headings |
| `--type-body-lg` | 18px | 1.6 | 400 | Long-form body text |
| `--type-body-md` | 16px | 1.6 | 400 | Standard body text |
| `--type-body-sm` | 14px | 1.5 | 400 | Secondary/helper text |
| `--type-label-md` | 14px | 1.4 | 500 | Form labels, badges |
| `--type-label-sm` | 12px | 1.4 | 500 | Captions, metadata |
| `--type-code` | 14px | 1.7 | 400 | Code blocks (monospace) |

## Core Web Vitals Targets

| Metric | Good | Needs Improvement | Poor |
|--------|------|------------------|----|
| LCP (Largest Contentful Paint) | ≤ 2.5s | 2.5–4.0s | > 4.0s |
| FID / INP (Interaction to Next Paint) | ≤ 200ms | 200–500ms | > 500ms |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | 0.1–0.25 | > 0.25 |
| TTFB (Time to First Byte) | ≤ 800ms | 800ms–1.8s | > 1.8s |
| FCP (First Contentful Paint) | ≤ 1.8s | 1.8–3.0s | > 3.0s |

### Implementation Rules for Web Vitals

**For LCP**:
- Preload the LCP image: `<link rel="preload" as="image" href="...">`
- Serve images via CDN with proper cache headers
- Use `fetchpriority="high"` on the LCP `<img>` element
- Avoid lazy-loading the LCP element

**For CLS**:
- Always set explicit `width` and `height` on `<img>` elements
- Reserve space for dynamic content (skeleton loaders, not layout shifts)
- Avoid injecting content above existing content after page load
- Use `transform` for animations instead of layout-affecting properties

**For INP**:
- Break up long tasks: any JS task > 50ms blocks the main thread
- Use `requestAnimationFrame` for visual updates
- Debounce search inputs: ≥ 300ms
- Virtualize long lists (> 50 items visible at once)

## Accessibility Standards (WCAG 2.2 AA)

### Minimum Requirements

| Criterion | Requirement |
|-----------|------------|
| Color contrast (text) | 4.5:1 for normal text; 3:1 for large text (≥ 18pt or 14pt bold) |
| Color contrast (UI components) | 3:1 against adjacent colors |
| Focus indicator | Visible; ≥ 3:1 contrast ratio; not removed with `outline: none` without replacement |
| Keyboard navigation | All interactive elements reachable and operable via keyboard |
| ARIA labels | All icon buttons and inputs without visible labels have `aria-label` |
| Alt text | All meaningful images have descriptive `alt` text; decorative images have `alt=""` |
| Heading hierarchy | Single `<h1>` per page; headings nest logically (no skipping h2→h4) |
| Form labels | All form inputs have an associated `<label>` (not just `placeholder`) |
| Error messaging | Form errors identified in text (not color alone); linked to the input via `aria-describedby` |
| Motion | Animations respect `prefers-reduced-motion` media query |

## Component State Implementation Checklist

Before marking a component implementation complete:

- [ ] Default state matches design
- [ ] Hover state implemented (where applicable)
- [ ] Focus state visible and accessible
- [ ] Active/pressed state implemented
- [ ] Disabled state: cursor `not-allowed`, reduced opacity, not interactive
- [ ] Loading state: skeleton or spinner with `aria-busy="true"`
- [ ] Error state: error color token + error message with `role="alert"`
- [ ] Empty state: placeholder content or empty state component
- [ ] Dark mode: tokens applied (not hardcoded values)
- [ ] Responsive: tested at all 4 breakpoints
- [ ] RTL: layout mirrors correctly if RTL is supported

## Performance Budget

| Asset Type | Budget per Component | Budget per Page |
|------------|---------------------|----------------|
| JavaScript (parsed + executed) | < 10 KB | < 150 KB (compressed) |
| CSS | < 5 KB | < 50 KB (compressed) |
| Images | — | < 500 KB total (WebP / AVIF) |
| Fonts | — | ≤ 2 custom font families; ≤ 4 weight/style variants |
| Third-party scripts | — | < 100 KB (compressed) |
