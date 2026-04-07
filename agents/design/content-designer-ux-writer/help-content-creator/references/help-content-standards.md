# Help Content Standards

## Purpose

A framework for writing, structuring, and maintaining help articles that resolve user questions efficiently and reduce support ticket volume.

## Article Type Selection

Choose the article type based on the user's question:

| User Question Type | Article Type | Structure |
|-------------------|-------------|-----------|
| "How do I do X?" | How-to guide | Numbered steps, one action per step |
| "Why is X happening?" | Troubleshooting guide | Problem > Cause > Fix, branching paths |
| "What does X mean?" | Conceptual explainer | Definition > Context > Example |
| "What are my options for X?" | Reference / comparison | Table or list comparing options |
| "Where do I find X?" | Navigation guide | Annotated screenshot + steps |

---

## Task-Oriented Writing Principles

### Headlines
- Start with an action verb: "Create", "Set up", "Troubleshoot", "Manage"
- Describe the user's goal, not the feature name: "Add team members to a workspace" not "Workspace members settings"
- Max 8 words; avoid punctuation
- Use sentence case (not Title Case except for proper nouns)

### Steps
- One action per step — if a step has two actions, split it
- Begin each step with an imperative verb: "Click", "Enter", "Select", "Toggle"
- Include the UI label in bold if the user must read it: **Save changes**
- Name the result of the step: "The confirmation email is sent."
- Limit to 8 steps before offering a break or sub-procedure

### Body Text
- Lead with the result or goal, not the process: "To export your data as CSV, follow these steps:" not "This article explains how to export data."
- Write at a 9th-grade reading level (Flesch-Kincaid ≤ 60)
- Active voice: "Click Save" not "Save should be clicked"
- Present tense: "The file downloads" not "The file will download"
- No jargon without inline definition; no acronyms without expansion on first use

---

## Article Quality Checklist

Before submitting for accuracy review:

- [ ] Headline starts with an action verb and describes a user goal
- [ ] Article type matches the user question
- [ ] All steps start with an imperative verb
- [ ] No step contains more than one user action
- [ ] Screenshots match current product UI (taken within last sprint)
- [ ] All UI labels match exactly what appears in the product (spelling, capitalisation)
- [ ] Article ends with a "next steps" or "related articles" section
- [ ] No marketing language ("powerful", "seamless", "intuitive")
- [ ] Cross-links to 2–4 related articles added
- [ ] Verified searchable via at least 3 expected user search queries

---

## Screenshot Standards

| Requirement | Standard |
|-------------|----------|
| Resolution | 2x (retina) for web; 1x for print |
| Format | PNG with transparent or white background |
| Annotations | Red arrows or red boxes — no decorative overlays |
| Crop | Show only the relevant area; no full-screen captures unless navigation context is needed |
| Alt text | Describe what the user sees and the action to take, not the visual design |
| Recency | Retake screenshots when any UI element in frame changes |

---

## Information Architecture Signal Table

Use these signals to determine whether a new article is needed or an existing article should be updated:

| Signal | Recommended Action |
|--------|-------------------|
| 5+ support tickets asking the same question with no existing article | Create new article |
| Existing article receiving high views but users still contact support | Rewrite article — task completion is failing |
| Product UI label changed | Update all articles referencing that label |
| Feature deprecated | Archive article; redirect search queries to replacement |
| New feature ships with no documentation | Create how-to article before or at launch |
| Support team providing an unwritten response to a recurring question | Codify as a help article |

---

## Content Maintenance Cadence

| Trigger | Action | Owner |
|---------|--------|-------|
| Product release | Review all articles in affected product area | Content Designer |
| Quarterly audit | Review articles with < 50% helpfulness rating | Content Designer |
| Screenshot audit | Retake screenshots that are > 2 sprints old | Content Designer |
| Support spike | Identify top 10 ticket reasons; check article coverage | Content Designer + Support Lead |

---

## Localisation Notes

If content will be translated:
- Avoid idioms, metaphors, and culture-specific references
- Keep sentences short (≤ 20 words) — complex structures translate poorly
- Do not embed text in screenshots — use callout labels that can be translated separately
- Use gender-neutral language ("they", not "he/she")
