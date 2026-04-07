# Framework: UX Copy Writing

Defines standards for writing UX copy across all product surfaces — microcopy, labels, error messages, empty states, and instructional text — grounded in UX writing principles.

## Copy Quality Principles

### Clarity Hierarchy

Apply this priority order when copy goals conflict:

1. **Clarity first** — The user must understand what they are reading and what to do.
2. **Accuracy second** — Technical correctness; do not trade clarity for precision.
3. **Brevity third** — Remove every word that does not add meaning. Brevity without clarity is worse than verbose clarity.
4. **Voice last** — Brand personality is applied after the above three are satisfied.

*Rationale: In a task-mode product context, users read to act. Copy that is "on-brand" but unclear fails its primary function.*

### Flesch-Kincaid Reading Level Targets

| Surface | Target Grade Level | Rationale |
|---------|------------------|-----------|
| Error messages | Grade 6-8 | Users are stressed; reduce cognitive load |
| Onboarding / getting started | Grade 6-8 | New users need maximum clarity |
| Empty states and CTAs | Grade 6-8 | First-use moments are high stakes |
| Tooltips and help text | Grade 8-10 | More complex concepts; some context assumed |
| Settings descriptions | Grade 8-10 | Technical audience; precise language |
| Legal / compliance notices | No target — accuracy governs | Legal copy is governed by legal review |

Target: Hemingway Grade 8 or below for all user-facing instructional copy.

## Copy String Inventory Framework

### Element Types to Inventory per Screen

| Element Type | What to Capture | Notes |
|-------------|----------------|-------|
| Page / modal title | Heading text | Sets context for the entire screen |
| Body copy | Descriptive paragraphs | Avoid copy in body that belongs in a label |
| Button labels (primary) | Action text + confirmation state if applicable | Max 3 words for primary CTA |
| Button labels (secondary) | Cancel/back/alternative action | Match destructiveness to label weight |
| Form field labels | Label text | Every input must have a visible label, not just a placeholder |
| Placeholder text | Example or format hint | Not a substitute for the label |
| Inline validation (success) | Positive confirmation if field validates | Optional; use for high-stakes fields (passwords, email) |
| Inline validation (error) | Specific error + resolution | Required for all validated fields |
| Empty state (first-time) | Message + CTA | Must explain value and invite first action |
| Empty state (no-results) | Context + suggestion | Must reference what was searched/filtered |
| Success confirmation | What completed + next step if needed | Inline toast or persistent state |
| Loading state text | Current action in progress | Show after 300ms; include progress if >3s |
| Destructive warning | Consequence + what cannot be undone | Explicit about permanence |
| Tooltip | Brief description of non-obvious element | ≤60 chars; not for critical information |
| Notification copy | Event description + optional action | Max 2 lines |

## Error Message Writing Rules

### Error Message Formula

```
[What happened] + [Why it happened, if knowable] + [What the user should do]
```

| Good | Bad | Reason |
|------|-----|--------|
| "Your session expired. Sign in again to continue." | "Error 401: Unauthorised" | User-language vs. technical code |
| "That email address is already in use. Try signing in instead." | "Email already exists" | Actionable vs. dead-end |
| "Your file is 24MB. The limit is 10MB. Try compressing it before uploading." | "File too large" | Specific vs. vague |
| "We couldn't connect to our servers. Check your internet connection and try again." | "An error occurred" | Diagnosable vs. useless |

### Error Message Rules

- Never blame the user. Use passive voice or system-focus: "We couldn't save" not "You failed to save".
- Always provide a resolution path. If no resolution exists, say so: "Contact support if this continues."
- Use the word "couldn't" not "failed to" — softer without being dishonest.
- Do not apologise unless the error is a system fault the user could not prevent.

## Empty State Writing Framework

### Empty State Types

| Type | User Context | Formula | Example |
|------|-------------|---------|---------|
| First-use empty | New user; has never added content | [What you can do here] + [Why it matters] + [CTA] | "No projects yet. Create your first project to start organising your work." [Create project] |
| Post-action empty | User deleted or archived all items | [Acknowledge the state] + [What to do next] | "You've archived all tasks. Add new tasks to get started again." |
| Zero-search-results | User searched; nothing matched | [Reflect the search term] + [Suggestion] | "No results for 'onboarding'. Try a different keyword or browse all articles." |
| Filtered-empty | User applied filter; nothing matches | [Reflect the filter] + [Action to clear] | "No tasks matching 'High priority'. [Clear filter]" |
| Permission-empty | User lacks access to content | [Explain why] + [How to get access] | "You don't have access to this project. Ask your admin to add you." |

## Progressive Disclosure in UX Copy

Apply progressive disclosure to avoid overwhelming users with information at the wrong moment:

| Level | Copy Role | Example |
|-------|-----------|---------|
| Primary (always visible) | Label + essential action | "File name" label; "Upload" button |
| Secondary (on interaction) | Contextual help, format hints | Character count appears when typing; tooltip on hover |
| Tertiary (on demand) | Detailed explanation, edge cases | "Learn more" link; expandable help text section |

Rule: Never put information at Level 1 that belongs at Level 2. Cluttered primary UI copy indicates missing progressive disclosure architecture.

## Constraint Validation Checklist

Before submitting copy for design review:

| Check | Standard |
|-------|---------|
| Button label word count | Primary: ≤3 words; secondary: ≤4 words |
| Toast notification length | ≤2 lines at standard viewport; test at 320px width |
| Tooltip length | ≤60 characters |
| Modal heading | ≤6 words |
| Error message | 1-2 sentences; never more than 3 |
| Empty state body | ≤2 sentences plus CTA |
| Pluralisation handled | All variable-count strings tested at 0, 1, 2, 100+ |
| Variable interpolation | All [name], [count], [date] variables defined and tested |
