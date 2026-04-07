# Support Readiness Brief

## Brief Metadata (internal)

| Field | Value |
|-------|-------|
| Brief ID | [e.g. SRB-0018] |
| Release Name | [e.g. Workspace Settings v2] |
| Release Version / Build | [e.g. v4.12.0] |
| Release Date | [YYYY-MM-DD HH:MM timezone] |
| Release Tier | [T1 Critical / T2 High / T3 Medium / T4 Low] |
| Author | [Content Designer name] |
| Brief Delivered | [YYYY-MM-DD] |
| Walkthrough Scheduled | [YYYY-MM-DD HH:MM or N/A] |
| Support Team Lead | [Name] |
| PM Contact | [Name] |
| Engineering On-Call | [Name or rotation] |

---

## Release Summary

[2–4 sentences. What is shipping? Who does it affect? What is the highest-impact change? Is any action required from users?]

**Affected user segments**: [e.g. All workspace Admins / Free plan users / All users]

**User action required**: [Yes — [describe action and deadline] / No]

---

## Feature-by-Feature Breakdown

[One section per major change. Be specific about what changed, what users will see, and how it affects their existing workflows.]

### [Feature / Change 1 Name]

**What changed**: [Describe the change factually. What is different from before?]

**Why it changed**: [Brief rationale — this helps support agents explain the change credibly.]

**Who it affects**: [User segment, plan tier, permission level]

**What users will see**: [Describe the user-facing change. What will look different or work differently?]

**Impact on existing data or settings**: [Will existing configurations, saved items, or user data be affected? State explicitly.]

**Help article**: [Title + URL]

---

### [Feature / Change 2 Name]

**What changed**:

**Why it changed**:

**Who it affects**:

**What users will see**:

**Impact on existing data or settings**:

**Help article**: [Title + URL]

---

[Add sections for additional changes as needed.]

---

## Known Issues

[Document all known issues shipping with this release. If there are none, state "No known issues." Do not leave this section blank.]

| ID | Severity | Description | Affected Segment | Workaround | Fix Timeline |
|----|----------|-------------|-----------------|-----------|-------------|
| KI-01 | [P0 / P1 / P2 / P3] | [What the user experiences — describe symptoms, not root cause] | [Who is affected] | [Step-by-step workaround, if available. "No workaround available" if not.] | [e.g. v4.12.1 — expected YYYY-MM-DD] |
| KI-02 | | | | | |

---

## Anticipated Questions & Response Playbook

[Write suggested responses support agents can adapt. Keep responses factual, direct, and consistent with the help article content.]

### What Changed

**Q: [User question about what is different]**

Suggested response:
> [Support agent response. Start with the answer, then explain. 2–4 sentences. Include a help article link if applicable.]

---

**Q: [Second question about what changed]**

Suggested response:
> [Response.]

---

### How to Do X Now

**Q: [User question about completing a task after a workflow change]**

Suggested response:
> [Response. Include step-by-step if the task involves multiple actions.]

---

### Data and Settings

**Q: [User question about data or settings impact]**

Suggested response:
> [Response. Be explicit: "Your [X] settings are unchanged" or "Your [X] has been migrated to [Y]."]

---

### Known Issues

**Q: [User question arising from known issue KI-01]**

Suggested response:
> [Response. Acknowledge the issue, provide the workaround if available, state the fix timeline.]

---

[Add additional Q&A sections as needed for each category: Pricing & Plans, Migration & Deprecation, etc.]

---

## Escalation Paths

| Scenario | First Action | Escalate To | Escalation Method | SLA |
|----------|-------------|-------------|-------------------|-----|
| [e.g. User data not migrated after release] | [Apply manual migration script — ref: [link]] | [Engineering on-call: [name/channel]] | [Slack #eng-oncall / PagerDuty] | [2 hours] |
| [e.g. Billing discrepancy post-release] | [Document plan, charge, and affected date] | [PM: [name] + Finance: [name]] | [Email with subject "SRB-0018 billing issue"] | [24 hours] |
| [e.g. Issue not covered in this brief] | [Gather: user ID, exact error message, steps to reproduce] | [PM: [name] for triage] | [Slack #product-triage] | [Triage in 2 hours] |

---

## Help Content Links

| Topic | Article Title | URL | Status |
|-------|--------------|-----|--------|
| [Feature / Change 1] | [Title] | [URL] | [Live / Draft — expected YYYY-MM-DD] |
| [Feature / Change 2] | [Title] | [URL] | [Live / Draft — expected YYYY-MM-DD] |

---

## Brief Acknowledgement

[Support team lead signs off before release.]

| Name | Role | Acknowledged | Date | Notes |
|------|------|-------------|------|-------|
| [Name] | [Support Lead] | [Yes / No] | [YYYY-MM-DD] | [e.g. Question about KI-01 workaround — resolved in walkthrough] |
