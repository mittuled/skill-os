# Scoring Rubric: support-readiness-confirmer

Evaluates whether the support team is prepared to handle customer inquiries for an upcoming release before go-live approval is granted.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Agent Knowledge | 30% | Agents can accurately describe what changed, expected customer questions, and recommended responses |
| 2 | Runbook and Macro Readiness | 25% | Runbooks updated and macros deployed for all new or changed ticket types introduced by the release |
| 3 | Help Article Accuracy | 25% | Help centre articles covering the release are live, accurate, and verified against the current product |
| 4 | Tooling Access | 10% | All agents have confirmed access to the tools needed to handle release-related tickets |
| 5 | Escalation Path Clarity | 10% | Agents know whom to escalate to for release-specific issues they cannot resolve at tier-1 |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | All agents passed knowledge checks; all runbooks, macros, and articles confirmed; zero access issues | Issue go-live sign-off; no conditions |
| A | 8.0 – 8.9 | Strong | Minor gaps in 1 criterion; no agent-facing blockers; escalation paths confirmed | Issue conditional sign-off; track minor gaps for post-launch follow-up |
| B | 7.0 – 7.9 | Good | 1-2 agents have knowledge gaps; most macros deployed; articles live with minor accuracy issues | Issue sign-off with remediation plan; remediate gaps within 48 hours |
| C | 5.0 – 6.9 | Adequate | Significant knowledge gaps; runbooks not updated; some articles not live | Delay sign-off; require remediation before launch or limit rollout |
| D | 3.0 – 4.9 | Weak | Most agents unprepared; multiple runbooks missing; help articles not published | Block go-live sign-off; escalate to Support Manager for emergency preparation |
| F | 0.0 – 2.9 | Failing | Readiness briefing not delivered; no runbooks, macros, or articles exist for this release | Block go-live; notify product and engineering to delay launch |

## Signal Tables

### Agent Knowledge

| Score | Evidence |
|-------|----------|
| 9-10 | Every agent correctly describes the feature change, lists 3+ expected customer questions, and provides accurate recommended responses without prompting |
| 7-8 | Most agents pass knowledge check; 1-2 agents need prompts to recall specific details but provide correct answers when prompted |
| 5-6 | At least 50% of agents pass; remaining agents have notable gaps in expected questions or recommended responses |
| 3-4 | Fewer than half of agents can accurately describe what changed; agents would need to research tickets on the fly |
| 0-2 | No agents can accurately describe the release; readiness briefing was either not delivered or not absorbed |

### Runbook and Macro Readiness

| Score | Evidence |
|-------|----------|
| 9-10 | All new or changed ticket categories have updated runbook entries; all new macros deployed and tested in the ticketing system |
| 7-8 | Runbooks updated for all critical ticket types; 1-2 edge-case macros pending but workarounds documented |
| 5-6 | Core runbooks updated; macros for non-critical ticket types missing but agents can handle manually |
| 3-4 | Only partial runbook updates; agents would need to improvise responses for a significant portion of expected ticket types |
| 0-2 | No runbook or macro updates for this release; agents have no procedural reference |

### Help Article Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | All help articles covering changed features are live; each article verified step-by-step against current product; no known inaccuracies |
| 7-8 | Articles live with 1-2 minor inaccuracies flagged; customers can complete the task despite minor errors |
| 5-6 | Articles live but contain 3+ inaccuracies; customers likely to contact support even after reading the article |
| 3-4 | Articles partially updated; some describe removed or changed workflows that would confuse customers |
| 0-2 | Help articles not yet updated; customers relying on help centre will receive incorrect guidance |

### Tooling Access

| Score | Evidence |
|-------|----------|
| 9-10 | All agents confirmed access to every tool needed for this release (e.g., new admin panel, debugging dashboard); access tested and working |
| 7-8 | 1-2 agents have minor access issues (e.g., permission level mismatch) with a workaround available |
| 5-6 | A shared tool all agents need is accessible but requires manual steps; slows resolution time |
| 3-4 | One or more agents cannot access a tool required to resolve a primary ticket type for this release |
| 0-2 | Tooling access not verified; agents discover access issues when first tickets arrive |

### Escalation Path Clarity

| Score | Evidence |
|-------|----------|
| 9-10 | Every agent can name the correct escalation contact for release-specific issues, with a backup; escalation contacts confirmed available on launch day |
| 7-8 | Escalation path documented; most agents aware; 1-2 agents unsure of backup contact |
| 5-6 | Primary escalation contact known but backup unclear; escalation criteria not well-defined |
| 3-4 | Escalation path not communicated; agents would use the general escalation queue rather than a release-specific path |
| 0-2 | No escalation path established for this release |
