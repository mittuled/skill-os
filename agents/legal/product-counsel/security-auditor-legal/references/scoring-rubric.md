# Scoring Rubric: security-auditor-legal

Evaluates the completeness of a legal review of security audit findings covering classification, disclosure analysis, notification coordination, and privilege management.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Findings Classification | 25% | Quality of classifying findings by data type, exposure scope, and actual vs. potential unauthorized access |
| 2 | Disclosure Obligation Analysis | 30% | Thoroughness of mapping findings against notification statutes across all applicable jurisdictions |
| 3 | Notification Coordination | 25% | Quality of notification drafting, timing coordination, and distribution planning across jurisdictions |
| 4 | Privilege Management | 20% | Effectiveness of attorney-client privilege protection in remediation documentation and disclosure language |

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
| A+ | 9.0 – 10.0 | Exceptional | All findings classified, all jurisdictions mapped, notifications drafted and timed, privilege protected | Execute notification plan as documented |
| A | 8.0 – 8.9 | Strong | Findings classified, major jurisdictions mapped, notifications in progress | Execute with minor refinements |
| B | 7.0 – 7.9 | Good | Findings classified, most jurisdictions analysed, notification drafts started | Complete jurisdiction analysis within 24 hours |
| C | 5.0 – 6.9 | Adequate | Findings partially classified, disclosure analysis incomplete | Urgent: complete disclosure analysis (72-hour GDPR deadline at risk) |
| D | 3.0 – 4.9 | Weak | Classification incomplete, disclosure obligations unclear | Critical: engage outside counsel immediately |
| F | 0.0 – 2.9 | Failing | No legal review of security findings | Critical: immediate legal engagement required |

## Signal Tables

### Findings Classification

| Score | Evidence |
|-------|----------|
| 9-10 | Each finding classified by: data type (PII, PHI, financial, trade secrets), exposure scope (record count, duration, actor type), actual vs. potential access determination, affected jurisdictions identified |
| 7-8 | Major findings classified across all dimensions, minor findings have partial classification |
| 5-6 | Data types identified for most findings, exposure scope estimated, actual vs. potential access partially determined |
| 3-4 | Findings listed without systematic classification by data type or exposure scope |
| 0-2 | No classification of security findings performed |

### Disclosure Obligation Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Each material finding mapped against: GDPR 72-hour notification, per-state breach notification statutes (with encryption safe harbor analysis), HIPAA breach notification, contractual DPA requirements, SEC materiality assessment. Triggering statute, deadline, required content, and recipient documented per obligation. |
| 7-8 | GDPR and major US states analysed, contractual DPA obligations reviewed, most deadlines calculated |
| 5-6 | Primary notification statutes identified but per-state analysis incomplete, DPA obligations partially reviewed |
| 3-4 | Generic awareness of notification obligations without statute-specific analysis |
| 0-2 | No disclosure obligation analysis performed |

### Notification Coordination

| Score | Evidence |
|-------|----------|
| 9-10 | Notification letters drafted for regulators, individuals, and contractual counterparties. Timing coordinated across jurisdictions to meet earliest deadline. Distribution list complete. Content calibrated: accurate without unnecessarily expanding liability scope. |
| 7-8 | Notifications drafted for primary recipients, timing coordinated for major jurisdictions |
| 5-6 | Notification drafts started but incomplete for some recipients or jurisdictions |
| 3-4 | Notification need identified but no drafts prepared |
| 0-2 | No notification coordination performed |

### Privilege Management

| Score | Evidence |
|-------|----------|
| 9-10 | Remediation documentation prepared under attorney-client privilege with clear privilege markers. Public disclosure language reviewed to avoid unnecessarily expanding liability. Outside counsel engaged where appropriate. Litigation hold assessed. |
| 7-8 | Privilege-protected remediation memo prepared, disclosure language reviewed |
| 5-6 | Privilege awareness noted but remediation documentation not systematically protected |
| 3-4 | No privilege protection for remediation documentation |
| 0-2 | No privilege management considered |
