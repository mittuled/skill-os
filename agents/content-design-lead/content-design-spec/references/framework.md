# Framework: Content Design Specification

Defines the architecture for a product content design spec, covering voice definition methodology, pattern library structure, and accessibility copy standards.

## Voice Attribute Architecture

### Voice Spectrum Model

Each voice attribute is defined as a spectrum to prevent misinterpretation. The spectrum format shows what the attribute IS and what it is NOT.

| Attribute | Is | Is Not | Why the Distinction Matters |
|-----------|-----|--------|----------------------------|
| Direct | Clear and efficient; respects user time | Blunt or dismissive; lacks warmth | Distinguishes brevity-with-care from terse developer writing |
| Approachable | Conversational, human, warm | Informal, slangy, unprofessional | Prevents the attribute from being used to justify casual errors |
| Empowering | Frames users as capable agents | Condescending; over-explains obvious steps | Ensures instructions assume competence |
| Honest | States facts including negative ones; no spin | Alarmist; dramatises or catastrophises | Allows honest bad news without creating user anxiety |

Minimum: 3 voice attributes. Maximum: 5. More than 5 cannot be operationalised consistently by multiple writers.

### Tone Modulation Matrix

Voice is constant; tone varies by context. Define tone behaviour across these six key contexts:

| Context | Emotional Register | Tone Adjustments | Example Trigger |
|---------|------------------|-----------------|----------------|
| Onboarding / first use | Welcoming, encouraging | Warmer, more explicit guidance, forward-looking | "Welcome to [Product]" |
| Success confirmation | Celebratory, affirming | Lighter, positive energy | "Your project was created" |
| Error / failure state | Empathetic, solution-focused | Acknowledge the problem; focus on fix, not blame | "We couldn't save your file" |
| Destructive action warning | Serious, clear | Drop warmth; prioritise clarity and consequence | "Deleting this removes all members" |
| Settings / configuration | Neutral, informative | Factual; minimal personality; precision over warmth | "Notification preferences" |
| Empty state (first time) | Inviting, motivating | Task-oriented; call to action; show the value | "No projects yet. Create your first one." |

## Copy Pattern Library Architecture

### Pattern Types

| Pattern Type | Structure Formula | Required Examples | Implementation Notes |
|-------------|-----------------|------------------|---------------------|
| Button labels | [Verb] + [Object] (max 3 words for primary actions) | Primary CTA, secondary action, destructive | Sentence case; no trailing punctuation |
| Inline form validation (error) | [What went wrong] + [How to fix it] | Required field, format error, conflict error | Associate message with field via aria-describedby |
| Empty state (first-time) | [Context] + [Value prop] + [CTA] | Empty list, empty search results, empty onboarding step | Include illustration guidance |
| Empty state (filtered/zero results) | [What was searched/filtered] + [Suggestion] | Search with no match, filter with no match | Do not use "No results found" without a suggestion |
| Destructive confirmation | [Action being taken] + [Consequence] + [Cannot undo warning if applicable] | Delete, archive, revoke access | Two-button: Cancel (left) + Destructive verb (right) |
| Success confirmation (inline) | [What was done] + [Optional: what happens next] | Save, submit, send | Disappears after 3-5 seconds for non-critical actions |
| Notification / toast | [Event] + [Optional: action link] | Background task complete, error in background | Toast: max 2 lines; persistent banner for critical state |
| Tooltip | [What it does / when to use it] (≤60 chars) | Icon button, form field with non-obvious purpose | Triggered on hover/focus; not for critical information |
| Loading state | [Present-tense action being performed] | Loading list, processing form, analysing data | Show after 300ms delay; add progress indicator if >3s |
| Placeholder text | [Example or hint, not instructions] | Input expecting format, input with example | Never use placeholder as a substitute for label |

### Pattern Anti-Patterns Reference

| Anti-Pattern | Correct Approach |
|-------------|-----------------|
| "Click here" as link text | Descriptive: "View your invoice" |
| "Error: field required" | "Enter your email address to continue" |
| "Are you sure?" confirmation | State the consequence: "Deleting this project removes all 14 tasks permanently" |
| "Loading..." without context | "Loading your projects..." |
| "Success!" without detail | "Your password was updated" |

## Grammar and Mechanics Rules

### Capitalisation Reference

| Element | Rule | Example |
|---------|------|---------|
| UI headings and labels | Sentence case | "Account settings" not "Account Settings" |
| Button labels | Sentence case | "Save changes" not "Save Changes" |
| Navigation items | Title case (product convention — override if brand specifies otherwise) | "Getting Started" |
| Proper nouns and product names | Title case always | "Google Drive", "Slack" |
| Feature names (approved) | Title case per glossary | Use the glossary; do not capitalise generic terms |
| Error message openers | Sentence case | "Your session has expired" |

### Punctuation Rules

| Context | Rule |
|---------|------|
| Button labels | No trailing punctuation |
| Short UI labels (1-4 words) | No trailing punctuation |
| Full sentences in body copy | Terminal period |
| List items in UI (all fragments or all sentences) | Consistent: either all have periods or none do |
| Tooltip text | No trailing period if single sentence; period if multi-sentence |
| Error messages (full sentence) | Terminal period |

## Accessibility Copy Standards

### Alt Text Framework

| Image Type | Alt Text Rule | Example |
|-----------|--------------|---------|
| Informative image | Describe the meaning, not the appearance | "Bar chart showing monthly revenue growth of 34%" not "A bar chart" |
| Decorative image | Empty alt="" + aria-hidden="true" | Purely visual flourish with no content meaning |
| Functional image (button icon) | Describe the action | alt="Close dialog" |
| Complex chart/diagram | Short alt + long description via aria-describedby | Short: "Revenue by segment Q3 2025"; long: full data table |

### ARIA Label Patterns

| Element | ARIA Pattern |
|---------|-------------|
| Icon-only button | aria-label="[Action verb + object]" |
| Progress indicator | aria-live="polite" aria-label="[Current step] of [Total steps]" |
| Error message | aria-live="assertive" id linked to input via aria-describedby |
| Modal dialog | aria-labelledby pointing to modal heading |
| Toggle / switch | aria-pressed="true/false" with descriptive label |

### Screen Reader Link Text Principles

- Link text must describe the destination or action when read out of context.
- Banned: "click here", "read more", "here", "this link", URLs as link text.
- Required: specific destination — "Read the privacy policy", "Download the Q3 report (PDF, 1.2MB)".

## Glossary Structure

Each glossary entry must include:

| Field | Description |
|-------|-------------|
| Term | The approved term, with approved capitalisation |
| Definition | One sentence defining what it means in this product |
| Usage in UI | Example of the term used in a UI string |
| Deprecated alternatives | Any previous or commonly used variants to avoid |
| Notes | Any edge cases or surface-specific guidance |
