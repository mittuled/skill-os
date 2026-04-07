# Developer Launch Kit

## Metadata

| Field | Value |
|-------|-------|
| Product / API Name | [Product name and version] |
| Launch Type | [New Product / Major Version / Minor Version / Patch] |
| Target Launch Date | [YYYY-MM-DD] |
| Developer Relations Lead | [Name] |
| Engineering Owner | [Name] |
| Docs Owner | [Name] |
| Status | [Planning / In Progress / Gate Review / Ready / Launched] |
| Skill | developer-launch-packager |

---

## Pre-Launch Readiness Summary

[GUIDANCE: Complete after all four readiness gates are signed off. Summarise the launch readiness state and any outstanding risks.]

**Gate 1 — Engineering Sign-off:** [Pass / Fail — date]
**Gate 2 — Documentation Readiness:** [Pass / Fail — date]
**Gate 3 — Asset Completeness:** [Pass / Fail — date]
**Gate 4 — First-Run Experience Validated:** [Pass / Fail — date]

**Launch Recommendation:** [Go / No-go / Conditional go]
**Outstanding Risks:** [List any P1 or P2 issues that are accepted risks for launch]

---

## Asset Checklist

[GUIDANCE: Mark each asset with its readiness state. All Required assets must reach "Staged" or "Live" before any announcement asset is published.]

| Asset | Required? | Owner | Due Date | State | Notes |
|-------|-----------|-------|----------|-------|-------|
| SDK — Python | [Yes/No] | | | [Not started / In progress / In review / Approved / Staged / Live] | |
| SDK — JavaScript / TypeScript | [Yes/No] | | | | |
| SDK — Go | [Yes/No] | | | | |
| SDK — Java | [Yes/No] | | | | |
| SDK — [Other language] | [Yes/No] | | | | |
| API reference docs | [Yes/No] | | | | |
| Quickstart guide | [Yes/No] | | | | |
| Sample app — Python | [Yes/No] | | | | |
| Sample app — JavaScript | [Yes/No] | | | | |
| Sample app — [Other language] | [Yes/No] | | | | |
| Migration guide | [Yes/No — Major only] | | | | |
| Changelog entry | Yes | | | | |
| Launch blog post | [Yes/No] | | | | |
| Release notes | [Yes/No] | | | | |
| Social media posts (Twitter/X, LinkedIn) | [Yes/No] | | | | |
| Developer newsletter section | [Yes/No] | | | | |
| Demo video / GIF | [Yes/No — New product/Major] | | | | |

---

## Announcement Content

### Launch Blog Post

**Title:** [Working title]
**Author:** [Name]
**Target URL:** [/blog/...]
**Publish target:** T+15 min

**Outline:**
1. [Hook — what changed and why it matters to developers]
2. [Key capability 1 with code snippet]
3. [Key capability 2 with code snippet]
4. [Migration note (major versions) or upgrade path (minor)]
5. [Call to action — link to docs, quickstart, changelog]

**Review status:** [Not started / Draft / In review / Approved]

---

### Social Media Posts

**Twitter/X (280 chars max):**

```
[Post text — include @mentions, hashtags, and link to blog post]
```

**LinkedIn:**

```
[Post text — slightly longer, more professional tone, include link]
```

**Review status:** [Not started / Draft / Approved by brand]

---

### Developer Newsletter Section

**Subject line:** [Newsletter subject if standalone; section header if embedded]
**Tone:** [Informational — developers trust tone, no hype words]

```
[Newsletter section text — typically 100–200 words]

What's new:
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]

[Link to docs] | [Link to changelog] | [Link to blog post]
```

**Review status:** [Not started / Draft / Approved]

---

## Changelog Entry

[GUIDANCE: Follow Keep a Changelog format. Copy this into the product changelog file.]

```markdown
## [version] — YYYY-MM-DD

### Added
- [New feature or capability]

### Changed
- [Backward-compatible behaviour change]

### Deprecated
- [Feature to be removed in a future major version]

### Removed
- [Feature removed in this version — major versions only]

### Fixed
- [Bug corrected]

### Security
- [Vulnerability addressed — include CVE if applicable]
```

---

## Launch Sequence Execution Log

[GUIDANCE: Complete in real time on launch day. Record actual publish timestamps against planned times.]

| Step | Asset | Planned Time | Actual Time | Published By | URL | Notes |
|------|-------|-------------|------------|--------------|-----|-------|
| 1 | SDK packages (all package managers) | T+0:00 | | | | |
| 2 | API reference docs | T+0:00 | | | | |
| 3 | Changelog | T+0:05 | | | | |
| 4 | Migration guide (major only) | T+0:05 | | | | |
| 5 | Sample apps updated (GitHub) | T+0:10 | | | | |
| 6 | Launch blog post | T+0:15 | | | | |
| 7 | Social media posts | T+0:15 | | | | |
| 8 | Developer newsletter | T+1:00 | | | | |

**Launch declared complete at:** [Timestamp]
**Post-launch monitoring assigned to:** [Name]

---

## Post-Launch Monitoring Checklist

Complete within 24 hours of launch:

- [ ] SDK download counts confirmed on package manager dashboards
- [ ] Docs page views reviewed in analytics
- [ ] Community channels monitored (Discord, Slack, forum, Stack Overflow) for issues
- [ ] Error rate on new API endpoints within acceptable range
- [ ] Any P1 issues filed and assigned
- [ ] Launch retrospective scheduled (within 1 week)

**Issues found post-launch:**

| Issue | Severity | Reported By | Assigned To | Status |
|-------|---------|-------------|-------------|--------|
| | | | | |
