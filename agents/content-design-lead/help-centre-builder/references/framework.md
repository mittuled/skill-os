# Framework: Help Centre Building

Defines the information architecture methodology, content taxonomy, article template standards, and quality criteria for building a product help centre from scratch.

## Information Architecture Model

### Help Centre Taxonomy Levels

| Level | Name | Description | Examples |
|-------|------|-------------|---------|
| L1 | Category | Top-level navigation — aligned to user goals, not product features | "Getting started", "Managing your account", "Billing and payments" |
| L2 | Subcategory | Groupings within a category | "Getting started > Setting up your workspace" |
| L3 | Article | Individual help article | "How to invite team members" |

**IA Principle**: Organise by user task and question, not by product feature name. Users ask "how do I add a team member?" — not "what does the Workspace Management module do?"

### Category Design Heuristics

| Heuristic | Guidance |
|-----------|---------|
| 5-7 L1 categories | Fewer than 5 may under-represent the product; more than 7 creates navigation fatigue |
| Parallel naming | Category names should follow the same grammatical pattern — either all nouns ("Account security") or all gerunds ("Managing security") |
| Audience separation | If the product has multiple distinct audiences (end user / admin / developer), create separate sections or use audience tags |
| Feature-agnostic naming | "Working with files" not "Files module"; "Managing your team" not "Team Management settings" |

## Article Type Taxonomy

| Article Type | Purpose | Structure Pattern |
|-------------|---------|-----------------|
| Getting started guide | Introduce the product; get user to first value moment | Goal → Prerequisites → Step-by-step → Success state |
| How-to guide | Walk through a specific task | Goal → Steps (numbered) → Result |
| Troubleshooting article | Diagnose and fix a specific problem | Symptom → Cause → Fix → Prevention |
| Conceptual explainer | Explain what something is and why it matters | What it is → How it works → When to use it |
| Reference article | List of options, settings, or field definitions | Table-based; no narrative |
| FAQ | Answer common questions in scan-friendly format | Q&A pairs; link to fuller articles |

## Article Template Standards

### Universal Article Elements

| Element | Required | Guidance |
|---------|---------|---------|
| Title | Yes | Question or task format: "How to [action]" or "Understanding [concept]". Avoid: "[Feature] Overview". Max 70 chars for SEO |
| Short description (meta) | Yes | 1-2 sentences describing what the article covers. Used in search results |
| Time to read | Optional | Useful for troubleshooting articles and guides >5 min |
| Last updated date | Yes | Show recency; users distrust outdated help content |
| Related articles | Yes | 2-4 links to related content; drives self-service depth |
| "Was this helpful?" feedback | Yes (if platform supports) | Drives content improvement loop |

### How-To Article Template

```
## [Verb phrase: what the user will achieve]

[1-2 sentences: context for when to use this, and what the result looks like]

**Before you start**: [Prerequisites — access level, prior steps]

1. [Step 1 — imperative verb + specific action. Screenshot if >3 clicks]
2. [Step 2]
3. [Step 3]

[Result description: what the user should see when they're done]

**Next steps**: [Link to logical next action]
```

### Troubleshooting Article Template

```
## [Problem symptom as the title — what the user sees or experiences]

[1 sentence confirming this is the article for them]

### Why this happens
[Cause in plain language]

### How to fix it
1. [Step 1]
2. [Step 2]

### If this doesn't work
[Escalation path — contact support, try alternative fix]
```

## Content Priority Tiers

### Launch-Critical Content Criteria

| Tier | Criteria | Examples |
|------|---------|---------|
| P1 — Launch blocker | Users cannot achieve core product value without this | Getting started, first workspace setup, invite team members |
| P1 — Legal requirement | Compliance, privacy, data deletion | Data export, account deletion, privacy settings |
| P2 — High-frequency need | Top 10 anticipated support tickets | Password reset, billing questions, notification settings |
| P3 — Power user | Advanced features; low new-user frequency | API documentation, bulk operations, integrations |
| P4 — Post-launch | Can wait for 30-60 days post-launch | Edge cases, rarely used settings |

## Writing Standards for Help Content

### Readability Targets

| Metric | Target |
|--------|--------|
| Flesch-Kincaid grade level | ≤8 |
| Sentences per paragraph (how-to) | ≤3 |
| Steps per how-to guide (total) | ≤12; split into multiple articles if more |
| Screenshots per how-to | 1 per major decision point; not every step |

### Voice in Help Content

Help content applies the same product voice as the UI, with these adjustments:

| Adjustment | Reason |
|-----------|--------|
| More explicit instruction language | Users consulting help are stuck; clarity takes precedence over personality |
| Second person ("you") throughout | Direct instruction; avoids passive voice ("the user should...") |
| Imperative verbs for steps | "Click Save" not "You can click Save" |
| Avoid "simply" and "just" | These minimise user difficulty; the user is asking because it is not simple to them |

## Card Sorting Reference

Use card sorting to validate the IA taxonomy before publishing:

| Method | When to Use | Inputs Required |
|--------|------------|----------------|
| Open card sort | Building IA from scratch; no category names yet | 15-20 users; set of article titles |
| Closed card sort | Validating proposed category structure | Proposed categories; set of article titles |
| Tree testing | Testing navigability of final structure | Published IA tree; task scenarios |

Minimum: 15 participants for open sort. For a B2B product, 8-10 can yield usable signal if users are in-segment.

## Search Optimisation

| Practice | Detail |
|---------|--------|
| Title front-loading | Put the most important keyword first in article titles |
| Synonym coverage | Include common alternative terms in article body or metadata |
| Question-format alternatives | Index "How do I invite someone?" alongside "Invite team members" |
| Internal linking | Every article links to 2-4 related articles |
| Broken link audit | Verify all internal links after any structural change |
