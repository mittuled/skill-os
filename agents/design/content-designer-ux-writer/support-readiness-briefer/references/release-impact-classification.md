# Release Impact Classification

## Purpose

A framework for assessing the support impact of a product release and calibrating brief depth, lead time, and walkthrough requirements accordingly.

## Release Impact Tiers

| Tier | Label | Description | Examples |
|------|-------|-------------|---------|
| T1 | Critical Impact | Breaking changes, data migrations, permission model changes, pricing changes | Auth system overhaul, new required field in existing forms, plan feature removal |
| T2 | High Impact | Significant UI changes, workflow changes, new mandatory steps, deprecations | Redesigned navigation, changed primary flow, feature sunset with migration path |
| T3 | Medium Impact | New optional features, UI improvements, expanded capabilities | New dashboard widget, additional filter option, new export format |
| T4 | Low Impact | Bug fixes, performance improvements, minor copy changes | Button label fix, loading time improvement, tooltip correction |

---

## Brief Requirements by Tier

| Requirement | T1 Critical | T2 High | T3 Medium | T4 Low |
|-------------|-------------|---------|-----------|--------|
| Full support brief | Required | Required | Required | Optional (release note only) |
| Live walkthrough with support team | Required | Required | Optional | No |
| Brief lead time before release | 5 business days | 3 business days | 1 business day | N/A |
| Known-issue documentation | Required | Required | Required if applicable | N/A |
| Escalation path definition | Required | Required | Recommended | N/A |
| Help article link included | Required | Required | Required | N/A |
| Response playbook (Q&A) | Required (full) | Required | Abbreviated (top 5 Qs) | N/A |

---

## Anticipated Question Category Framework

Structure anticipated questions by category to help support agents navigate the brief:

| Category | Description | Examples |
|----------|-------------|---------|
| What changed | Questions about what is different | "Why does my dashboard look different?" |
| Why it changed | Questions about the reason for the change | "Why did you remove the export button from this location?" |
| How to do X now | Questions about completing a task after a workflow change | "How do I invite a member now?" |
| Data and settings | Questions about whether user data, preferences, or settings are affected | "Will my saved reports still work?" |
| Pricing and plans | Questions about whether the change affects cost or plan access | "Do I need to upgrade to use this?" |
| Known issues and workarounds | Questions arising from a bug or limitation that is shipping with the release | "The filter is missing — is that a bug?" |
| Migration and deprecation | Questions about moving off deprecated features | "How long do I have before X is removed?" |
| Escalation | Issues that require engineering or PM involvement | "My account is still in the old state after migration" |

---

## Escalation Path Decision Table

Define the escalation path for each issue class before the brief is delivered:

| Issue Class | First Response | If Unresolved After | Escalate To | Expected SLA |
|-------------|---------------|--------------------|-----------| ------------|
| Blocker (user cannot access core feature) | Support agent — apply workaround if available | 30 minutes | Engineering on-call | 2 hours |
| Data integrity concern (user reports data looks wrong) | Support agent — gather exact details | 15 minutes | PM + Engineering | 1 hour |
| Migration failure (user not transitioned after deadline) | Support agent — run manual migration script if available | 1 hour | Engineering | 4 hours |
| Billing / plan discrepancy post-release | Support agent — document details | 1 hour | Finance + PM | 24 hours |
| Feature request or confusion (expected behaviour) | Support agent — explain change, link to help article | N/A — no escalation | — | — |
| Unknown error (not covered in brief) | Support agent — gather details | Immediately | PM for triage | Triage within 2 hours |

---

## Known-Issue Severity Classification

Rate each known issue before including it in the brief:

| Severity | Label | Description | Workaround Required |
|----------|-------|-------------|---------------------|
| P0 | Blocking | Prevents users from completing a primary task | Yes — must include workaround in brief |
| P1 | Major | Significantly degrades experience; workaround required | Yes |
| P2 | Minor | Noticeable but does not block primary task completion | Recommended |
| P3 | Cosmetic | Visual defect only; no functional impact | No |

Ship with P2 and P3 known issues only. P0 and P1 should delay release unless a documented workaround exists and is included in the brief.

---

## Brief Quality Checklist

Before delivering the brief to the support team:

- [ ] Release tier assessed (T1–T4)
- [ ] All changed product areas documented
- [ ] Known issues documented with severity and workaround (if applicable)
- [ ] Anticipated questions generated across all categories
- [ ] Response playbook drafted for each anticipated question
- [ ] Escalation paths defined for P0 and P1 scenarios
- [ ] Help article links verified as live and up to date
- [ ] Brief lead time met (see tier requirements)
- [ ] Live walkthrough scheduled (if T1 or T2)
- [ ] Support team acknowledgement received before release
