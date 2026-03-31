# Brand Identity v1: Flowline

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Brand Designer | Brand Designer |
| Brand | Flowline |
| Version | 1.0 |
| Skill | brand-identity-v1 |

## Logo System

**Concept**: Wordmark in geometric sans-serif with a horizontal flow mark icon

**Required variants**:
- Primary (colour on light background)
- Reversed (light on dark background)
- Monochrome (single colour)
- Icon only (for favicons, app icons)
- Wordmark only (for horizontal space constraints)

**Usage rules**:
- Minimum size: 120px wide for wordmark, 32px for icon
- Clear space: equal to height of capital letter on all sides
- Never distort, rotate, or apply effects to the logo
- Only approved colour combinations

**Formats to deliver**: SVG (master), PNG (web), PDF (print)

## Colour System

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| Primary | Electric Blue | `#0F62FE` | Primary actions, links, key UI elements |
| Secondary | Near Black | `#161616` | Primary text, dark backgrounds |
| Accent | Deep Purple | `#6929C4` | Highlights, hover states, gradients |
| Background | White | `#FFFFFF` | Default page background |
| Text | Near Black | `#161616` | Body copy |
| Success | Green | `#24A148` | Positive states, success messages |
| Error | Red | `#DA1E28` | Error states, destructive actions |

**Accessibility**: All text/background combinations must meet WCAG 2.1 AA (4.5:1 for normal text, 3:1 for large text). `#0F62FE` on `#FFFFFF` achieves 4.54:1 — passes AA.

**Combination rules**:
- Primary on Background: `#0F62FE` on `#FFFFFF` ✓
- Text on Background: `#161616` on `#FFFFFF` achieves 16:1 — exceeds AAA
- Never use `#6929C4` (accent) as background for body text

## Typography System

| Role | Family | Weight | Size Range | Usage |
|------|--------|--------|-----------|-------|
| Display | IBM Plex Sans | 700 | 48-96px | Marketing headlines |
| Heading | IBM Plex Sans | 600 | 24-48px | Section headers, feature titles |
| Body | IBM Plex Sans | 400 | 14-18px | Body copy, descriptions |
| Code | IBM Plex Mono | 400 | 12-14px | Code snippets, technical strings |

**Usage rules**:
- Use only IBM Plex Sans and IBM Plex Mono (Google Fonts; zero cost)
- Never stretch or condense font widths
- Line height: 1.5x for body copy, 1.2x for headings
- Letter spacing: default, except ALL CAPS labels (+0.05em)

## Usage Guidelines

**Documentation URL**: https://brand.flowline.com/guidelines

## Deliverables Checklist

- [ ] Logo files in all 5 variants × 3 formats (15 files)
- [ ] Colour tokens in CSS variables, Figma styles, and Tailwind config
- [ ] Typography scale in Figma styles and CSS
- [ ] Brand guide PDF (20-30 pages)
- [ ] Figma component library with brand applied
