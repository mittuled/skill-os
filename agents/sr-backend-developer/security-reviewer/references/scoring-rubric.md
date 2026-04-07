# Scoring Rubric: Security Reviewer

Evaluates the thoroughness of a backend security code review covering OWASP Top 10, dependency chain, and data handling.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Static Analysis Coverage | 15% | Completeness of SAST tool execution and result triage |
| 2 | OWASP Top 10 Review | 25% | Manual inspection depth across all 10 OWASP categories |
| 3 | Dependency Audit | 20% | CVE/advisory database check for direct and transitive dependencies |
| 4 | Data Handling Assessment | 20% | Verification of encryption, secrets management, and PII protection |
| 5 | Remediation Guidance | 20% | Specificity and actionability of fix recommendations per finding |
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
| A+ | 9.0 – 10.0 | Exceptional | Full SAST scan, OWASP review, dep audit, data handling check; all findings have code-level fixes | Approve merge; no security blockers |
| A | 8.0 – 8.9 | Strong | Comprehensive review with minor gaps in one category; remediation provided for all critical/high findings | Approve merge with follow-up for medium findings |
| B | 7.0 – 7.9 | Good | SAST and OWASP review complete; dep audit done; some remediation guidance generic | Approve after critical fixes applied; schedule medium fixes |
| C | 5.0 – 6.9 | Adequate | Partial review coverage; dep audit incomplete; findings classified but remediation vague | Block merge; expand review scope |
| D | 3.0 – 4.9 | Weak | SAST only with no manual review; deps not audited; data handling unchecked | Block merge; full security review required |
| F | 0.0 – 2.9 | Failing | No security review performed | Reject; mandatory security review for this code path |

## Signal Tables

### Static Analysis Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | Semgrep/CodeQL run on full codebase with custom rules for project patterns; all flagged issues triaged as true/false positive with rationale |
| 7-8 | SAST tools run on target code paths; most issues triaged; custom rules not yet configured |
| 5-6 | Default SAST ruleset run; results reviewed but not fully triaged |
| 3-4 | SAST tool run but output not reviewed or triaged |
| 0-2 | No static analysis performed |

### OWASP Top 10 Review
| Score | Evidence |
|-------|----------|
| 9-10 | Each OWASP category explicitly checked with pass/fail; injection, auth, access control, and XSS tested with concrete attack scenarios; business logic bypass reviewed |
| 7-8 | All 10 categories reviewed; injection and auth thoroughly tested; some categories checked at surface level |
| 5-6 | 6-7 categories reviewed; injection and auth checked; XSS and access control partially reviewed |
| 3-4 | 3-5 categories reviewed; review limited to code patterns rather than attack scenarios |
| 0-2 | No OWASP-structured review; ad-hoc code reading only |

### Dependency Audit
| Score | Evidence |
|-------|----------|
| 9-10 | Direct and transitive deps checked against CVE/GitHub Advisory; upgrade paths documented for all vulnerable packages; no critical or high CVEs unresolved |
| 7-8 | Direct deps audited; transitive deps spot-checked; critical CVEs resolved; medium CVEs documented |
| 5-6 | Direct deps audited with `npm audit` or equivalent; transitive deps not reviewed; upgrade paths not documented |
| 3-4 | Audit tool run but results not reviewed or acted upon |
| 0-2 | No dependency audit performed |

### Data Handling Assessment
| Score | Evidence |
|-------|----------|
| 9-10 | PII encrypted at rest and in transit verified; no hardcoded secrets in source/config; sensitive data excluded from logs; secrets rotation documented |
| 7-8 | Encryption verified; no hardcoded secrets found; log output reviewed for PII; minor gaps in rotation documentation |
| 5-6 | Encryption in transit verified; at-rest encryption not confirmed; log review incomplete |
| 3-4 | Basic check for hardcoded secrets; encryption and logging not reviewed |
| 0-2 | No data handling review performed |

### Remediation Guidance
| Score | Evidence |
|-------|----------|
| 9-10 | Every finding has specific fix with code example; CVSS score or equivalent severity; exploitation scenario described; effort estimated |
| 7-8 | Critical and high findings have code-level fixes and exploitation context; medium findings have descriptive guidance |
| 5-6 | Findings have fix descriptions but no code examples; severity assigned without exploitation context |
| 3-4 | Generic recommendations like "sanitize input" without specific implementation guidance |
| 0-2 | No remediation guidance provided |
