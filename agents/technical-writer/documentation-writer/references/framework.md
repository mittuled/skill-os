# Framework: documentation-writer

Defines the writing approach by documentation type, voice and style standards, code sample requirements, and the quality checklist for publishing technical documentation.

## Writing Approach by Documentation Type

| Type | Voice | Structure | Tone | Success Criterion |
|------|-------|-----------|------|------------------|
| Tutorial | Second person ("You will...") | Step-by-step, each step produces visible output | Encouraging, patient | Developer reaches stated goal without external help |
| How-to Guide | Second person, imperative ("Install the SDK by...") | Numbered steps only, no conceptual detour | Efficient, direct | Developer completes the specific task |
| Reference | Third person / technical ("The `POST /orders` endpoint...") | Tables, schemas, lists — no prose filler | Precise, complete | Developer finds the exact fact they need in < 30 seconds |
| Explanation | First or third person, analytical | Prose with diagrams — no numbered procedures | Thoughtful, insightful | Developer understands the concept without needing to re-read |

**Voice rule**: Never mix types on a single page. If an explanation paragraph is needed in a how-to, link out to a concept page instead.

## Writing Standards

### Sentence-Level Rules

| Rule | Wrong | Correct |
|------|-------|---------|
| Active voice for all procedure steps | "The file is saved by pressing Ctrl+S" | "Press Ctrl+S to save the file" |
| Present tense for API descriptions | "Will return a 200 status" | "Returns a 200 status" |
| Imperative mood for instructions | "You should click Submit" | "Click Submit" |
| Exact parameter names in code format | "Pass the customer identifier" | "Pass the `customer_id` parameter" |
| No jargon without definition on first use | "Use the MCP to configure scope" | "Use the Management Control Panel (MCP) to configure scope" |
| Concrete over vague | "It may take some time" | "The request typically responds in < 2 seconds" |

### Structure Rules

| Element | Standard |
|---------|----------|
| Page length | 400–1,500 words for guides; no limit for reference |
| Heading levels | H1 = page title; H2 = major section; H3 = subsection; never skip levels |
| Callouts | Use Note/Tip/Warning/Danger sparingly — maximum 2 per page |
| Screenshots | Include only for UI that changes rarely; always include alt text |
| Code blocks | Every code block must have a language identifier and a human-readable caption |
| Tables | Use for 3+ items that share the same attributes; never use a table for 2 items |

## Code Sample Requirements

Every code sample published in documentation must meet all of the following:

| Requirement | Standard | Why |
|-------------|----------|-----|
| Executable | Runs without modification in a fresh environment | Untested samples are the #1 documentation complaint |
| Language-idiomatic | Follows conventions for the target language | Developers learn patterns from docs; bad patterns proliferate |
| Complete | Includes imports, auth setup, and error handling | Partial samples force developers to guess the missing parts |
| Annotated | Inline comments on non-obvious lines | Reduces need to read separate explanation while using the sample |
| Current SDK version | Uses the most recent stable SDK version | Deprecated methods in docs signal abandonment and confuse developers |
| Copy-paste ready | No placeholder that looks like it should be replaced but is not | `YOUR_API_KEY` is correct; `api_key_value` is not |

## Pre-Publish Quality Checklist

Complete all items before marking a documentation page ready for review.

### Accuracy
- [ ] All code samples executed in a clean environment against current product version
- [ ] All parameter names verified against current API spec
- [ ] All response schemas verified against actual API responses
- [ ] All procedural steps walked through from scratch; each step produces documented outcome

### Completeness
- [ ] Page covers all use cases stated in the task requirements
- [ ] Prerequisites explicitly listed (no assumed knowledge)
- [ ] Next steps and related content linked at the bottom
- [ ] Error scenarios documented where relevant (for reference and how-to pages)

### Style
- [ ] Correct voice and tense for the documentation type
- [ ] No jargon used without first-use definition
- [ ] All cross-links point to correct pages and resolve without 404
- [ ] Code blocks have language identifiers and captions

### Review
- [ ] Technical review requested from the owning engineer or PM
- [ ] Engineering review comments addressed
- [ ] Peer review (another writer) completed for new guides and tutorials

## Research Interview Template

Use this structure when interviewing engineers for feature documentation:

| Phase | Questions | Goal |
|-------|---------|------|
| Feature overview (5 min) | "What does this do? What problem does it solve?" | Understand the purpose |
| Mechanics (10 min) | "Walk me through how it works step by step." | Build mental model |
| Common mistakes (5 min) | "What will developers get wrong? What is the most common support question?" | Identify anti-patterns and edge cases |
| Edge cases (5 min) | "What happens if [X]? Are there limits or constraints?" | Complete the reference |
| Sample code (5 min) | "Can you show me the simplest working example?" | Seed the first code sample |
