# Content Design Specification: Flowline

| Field | Value |
|-------|-------|
| Product | Flowline |
| Brand | Flowline |
| Product Type | Developer Tool / B2B SaaS |
| Voice Attributes | 3 defined |
| Primary Personas | Software Engineers, DevOps Engineers |
| Skill | content-design-spec |

## Context

**Primary personas:**
- Software Engineers
- DevOps Engineers
- Engineering Managers

**Key product surfaces covered:**
- Onboarding flow
- Pipeline dashboard
- Error messages
- Settings
- Empty states
- Notifications

## Voice and Tone Framework

### Voice Attributes

### Direct, not Blunt

**Do**: Your deployment failed. Check the error log →

**Don't**: Oops! It looks like something might have gone wrong with your deployment attempt.

### Precise, not Technical-for-its-own-sake

**Do**: Pipeline ran in 2m 14s (32% faster than average)

**Don't**: The CI/CD orchestration process completed execution successfully within the allocated compute window

### Confident, not Arrogant

**Do**: Deploy in 10 minutes. No config required.

**Don't**: We believe Flowline might be one of the better options for teams who want faster deployments

### Tone by Context

| Context | Tone Direction |
|---------|----------------|
| Success / Celebration | Warm but understated. Confirm clearly. Skip superlatives. |
| Error / Failure | Empathetic, not apologetic. Focus on resolution, not the problem. |
| Onboarding | Encouraging and instructive. Assume intelligence; explain only what is genuinely new. |
| Destructive actions | Direct and specific. No softening language. Consequences must be unambiguous. |
| Empty states | Helpful and forward-looking. Guide the next action. |
| Settings / Config | Precise and informative. User expertise is assumed. |
| Notifications | Concise. Lead with what changed, follow with what to do. |

## Terminology Glossary

| Term | Definition | Approved Usage | Avoid |
|------|-----------|----------------|-------|
| **Pipeline** | A configured CI/CD workflow that runs on triggers | Create a pipeline. Run the pipeline. | Job (generic), workflow (ambiguous with GitHub Actions workflows) |
| **Run** | A single execution of a pipeline | View the run. The run failed. | Build (confusing with build step), execution |
| **Step** | An individual unit of work within a pipeline | The test step failed. | Task, job, action |

## Copy Pattern Library

### Button Labels

**Rule**: Use verb + object. Avoid 'OK', 'Yes', 'Submit'. Make buttons predict the outcome.

  - **Do**: _Save changes_  |  **Don't**: ~~Submit~~
  - **Do**: _Delete project_  |  **Don't**: ~~Yes~~
  - **Do**: _Start free trial_  |  **Don't**: ~~OK~~

### Error Messages

**Rule**: State what went wrong + what to do next. Never blame the user.

  - **Do**: _Your file exceeds 10MB. Try a smaller file._  |  **Don't**: ~~Upload failed.~~
  - **Do**: _This email is already in use. Sign in instead?_  |  **Don't**: ~~Invalid email.~~

### Empty States

**Rule**: Explain what belongs here + provide a clear first action. Never leave a blank space.

  - **Do**: _You haven't created any pipelines yet. Create your first pipeline →_  |  **Don't**: ~~No pipelines.~~
  - **Do**: _Your team hasn't shared any files. Upload a file to get started._  |  **Don't**: ~~No files yet.~~

### Success Messages

**Rule**: Confirm what happened, briefly. Don't over-celebrate. Skip 'Congratulations!'

  - **Do**: _Pipeline deployed successfully._  |  **Don't**: ~~Great job! Your pipeline has been deployed!~~
  - **Do**: _Settings saved._  |  **Don't**: ~~Congrats! Settings have been saved successfully!~~

### Form Validation

**Rule**: Inline, specific, actionable. Show on blur (not on submit). Use friendly language.

  - **Do**: _Enter a valid email address._  |  **Don't**: ~~Email is invalid.~~
  - **Do**: _Password must be at least 8 characters._  |  **Don't**: ~~Password too short.~~

### Loading States

**Rule**: Tell the user what is happening. Use active present tense.

  - **Do**: _Running tests..._  |  **Don't**: ~~Loading...~~
  - **Do**: _Deploying your pipeline..._  |  **Don't**: ~~Please wait.~~

### Destructive Actions

**Rule**: Be explicit about the consequence. Use the specific noun, not generic 'this'.

  - **Do**: _Delete 'Production Pipeline'? This cannot be undone._  |  **Don't**: ~~Are you sure?~~
  - **Do**: _Remove Sarah Chen from this project? She will lose access immediately._  |  **Don't**: ~~Confirm?~~

## Grammar and Mechanics

| Rule | Standard |
|------|---------|
| Capitalisation | Sentence case for all UI text (headings, labels, buttons). Title Case only for product names and proper nouns. |
| Punctuation | No full stops in button labels, headings, or single-line UI text. Use full stops in multi-sentence body text. |
| Numbers | Spell out one through nine; use numerals for 10+. Always use numerals for data values. |
| Dates | Use unambiguous formats: 'March 31, 2026' or '31 Mar 2026'. Avoid '03/31/26'. |
| Abbreviations | Spell out on first use: 'Application Programming Interface (API)'. Use the abbreviation thereafter. |
| Ampersand | Use 'and' in prose. Ampersand (&) only acceptable in navigation and tight UI space. |
| Contractions | Use contractions to sound natural (you're, it's, we'll). Avoid in formal/legal contexts. |
| Exclamation marks | Limit to one per feature area maximum. Reserve for genuine moments of delight, not routine confirmations. |

## Accessibility Copy Standards

| Standard | Implementation |
|----------|---------------|
| Alt text | Describe the function, not the appearance. Decorative images: alt=''. Icons with labels: alt=''. |
| ARIA labels | Add aria-label when the visible text is insufficient. Be specific: 'Delete project: Flowline Production' not 'Delete'. |
| Link text | Links must make sense out of context. Use 'View deployment logs' not 'click here'. |
| Error association | Error messages must be programmatically associated with the input (aria-describedby). |
| Loading announcements | Dynamic loading states must be announced via aria-live='polite'. |
| Button vs link | Use <button> for actions, <a> for navigation. Never use 'click here' as visible text. |

## Living Document Protocol

This spec is a living document. Update when:
- A new product surface introduces copy patterns not covered here
- Terminology changes following a rename or repositioning
- Voice calibration feedback from research reveals misalignment
- Accessibility audit identifies a pattern gap

**Owner**: Content Design Lead
**Review cadence**: Quarterly or triggered by above conditions
**Change log**: Maintain at the bottom of the document with date + summary of change
