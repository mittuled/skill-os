# Content Design Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Content Design Lead name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | content-design-spec |
| Product / Feature Scope | [Product name or feature area this spec covers] |
| Brand Foundation Reference | [Link to brand foundation document] |

## Executive Summary

[2-3 sentences stating the voice of the product in plain language, the primary copy problems this spec solves, and when this spec takes effect. Write for a new writer joining the team.]

GUIDANCE: Example — "Helio's product voice is direct, empowering, and approachable — an expert colleague who respects users' intelligence and time. This spec replaces ad hoc copy decisions with documented standards, primarily to fix inconsistent error message patterns and fragmented terminology across the onboarding and analytics surfaces. All new copy delivered after [date] should conform to this spec."

## 1. Voice and Tone

### Voice Attributes

[3-5 voice attributes, each defined with a spectrum. The spectrum format — "IS, NOT" — prevents misinterpretation.]

GUIDANCE: Use the spectrum model. "Friendly, not casual" is more useful than "Friendly" alone. Pair each attribute with a do/don't copy pair from the actual product.

| Attribute | Is | Is Not |
|-----------|-----|--------|
| [Attribute 1] | [What it means in practice] | [What it does not mean] |
| [Attribute 2] | | |
| [Attribute 3] | | |

**Do / Don't Examples**

| Attribute | Do | Don't |
|-----------|-----|-------|
| [Attribute 1] | "[Copy example that embodies it]" | "[Copy example that violates it]" |

### Tone Modulation

[Tone shifts by context even though voice stays constant. Document tone for each key context so writers know how personality adjusts.]

GUIDANCE: Good — "In error states, the tone shifts from direct to empathetic. Lead with acknowledgement ("We couldn't save your changes") before the fix." Bad — "Tone should be empathetic." With no context for when.

| Context | Tone Direction | Example |
|---------|--------------|---------|
| Onboarding / first use | | |
| Success confirmation | | |
| Error / failure state | | |
| Destructive action warning | | |
| Settings / configuration | | |
| Empty state (first time) | | |

## 2. Terminology Glossary

[Approved product terminology. Every term users encounter in the UI should be in this glossary with its approved form.]

GUIDANCE: Include capitalisation decisions. If the product calls it "Workspace" (capital W), document that. Deprecated alternatives prevent old terms from creeping back in.

| Term | Definition | Usage in UI | Deprecated Alternatives | Notes |
|------|-----------|------------|------------------------|-------|
| [Term 1] | [One-sentence definition] | "[Example UI string]" | [Old terms to avoid] | [Edge cases] |
| [Term 2] | | | | |

## 3. Copy Pattern Library

[Reusable copy patterns for common UI elements. Engineers and writers should be able to look up any element type and see the formula plus examples.]

GUIDANCE: Formulas with brackets show the structure. Examples show it applied. Include 2-3 examples per pattern. Patterns for: buttons, errors, empty states, confirmations, loading states, tooltips.

### Button Labels

**Formula**: [Verb] + [Object] (sentence case, no trailing punctuation)

| Action Type | Formula | Examples |
|------------|---------|---------|
| Primary CTA | [Verb] [Object] | "Create project", "Save changes", "Send invite" |
| Destructive | [Destructive verb] [Object] | "Delete project", "Remove member", "Revoke access" |
| Cancel/Back | Single word | "Cancel", "Back", "Discard" |

### Error Messages

**Formula**: [What happened] + [How to fix it]

| Error Type | Example |
|-----------|---------|
| Required field | "Enter your [field name] to continue." |
| Format invalid | "Enter a valid [format] — for example, [example]." |
| Conflict / already exists | "[Item] already exists. [Alternative action]." |
| System error | "We couldn't [action]. [Recovery step]." |

### Empty States

| Type | Formula | Example |
|------|---------|---------|
| First-time (no content yet) | [Context] + [Value] + [CTA] | "No projects yet. Create your first project to start organising your work." |
| Zero search results | [Search term reflected] + [Suggestion] | "No results for "[term]". Try a different keyword." |
| Filtered empty | [Filter reflected] + [Clear action] | "No tasks matching "High priority". [Clear filter]" |

### Destructive Action Confirmations

**Formula**: [Specific action] + [Consequence] + [Cannot undo if applicable]

Example: "Delete "[Project name]"? This removes all [N] tasks permanently and cannot be undone."

### Success Confirmations

| Type | Formula | Example |
|------|---------|---------|
| Inline toast | [What completed] | "Password updated" |
| Persistent success | [What completed] + [Next step] | "Your account is ready. Set up your first workspace." |

### Loading States

| Duration | Pattern | Example |
|---------|---------|---------|
| <300ms | No copy shown | — |
| 300ms – 3s | "[Action in progress]..." | "Loading your projects..." |
| >3s | "[Action] + progress indicator" | "Analysing data (step 2 of 4)..." |

## 4. Grammar and Mechanics

### Capitalisation

| Element | Rule | Example |
|---------|------|---------|
| UI headings and labels | Sentence case | "Account settings" |
| Button labels | Sentence case | "Save changes" |
| Approved feature names | Title case per glossary | [Per glossary] |
| Navigation items | [Sentence case / Title case — specify] | |

### Punctuation

| Rule | Detail |
|------|--------|
| Button labels | No trailing punctuation |
| Short UI labels | No trailing punctuation |
| Full sentences (body, errors) | Terminal period |
| List items | Consistent — all periods or none |

### Number and Date Formatting

| Element | Format | Example |
|---------|--------|---------|
| Numbers under 10 | [Spell out / Numeral — specify] | "three members" or "3 members" |
| Numbers 10+ | Numeral | "25 projects" |
| Dates | [DD Month YYYY / Month DD, YYYY — specify] | "6 April 2026" |
| Relative dates | [Specify convention] | "3 days ago", "Yesterday" |
| Percentages | Numeral + % | "34%" |

### Abbreviations

| Approved | Banned in UI |
|----------|-------------|
| [List approved abbreviations] | e.g., i.e., etc., info (use "information") |

## 5. Accessibility Copy Standards

### Alt Text Conventions

| Image Type | Rule | Example |
|-----------|------|---------|
| Informative image | Describe meaning, not appearance | "Bar chart: revenue grew 34% in Q3" |
| Decorative image | Empty alt + aria-hidden="true" | `alt=""` |
| Functional image / icon button | Describe the action | `alt="Close dialog"` |

### ARIA Labels

| Element | Pattern |
|---------|---------|
| Icon-only button | `aria-label="[Action verb] [Object]"` |
| Error message | `aria-live="assertive"` + `aria-describedby` on input |
| Modal | `aria-labelledby` pointing to modal heading |
| Progress | `aria-label="Step [N] of [Total]"` |

### Link Text

- Banned: "click here", "read more", "here", bare URLs
- Required: Specific destination or action — "View the privacy policy", "Download Q3 report (PDF, 1.2MB)"

## Appendices

### A. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Name] | Initial version |

### B. Open Decisions

[Copy decisions that are still unresolved, with context and who owns them.]

| Decision | Options | Owner | Target Resolution Date |
|---------|---------|-------|----------------------|
| [Decision 1] | [Option A / Option B] | [Name] | [Date] |
