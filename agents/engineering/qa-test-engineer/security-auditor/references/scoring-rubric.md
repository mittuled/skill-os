# Scoring Rubric: Security Auditor

Evaluates the thoroughness of a QA-driven security audit covering code, configuration, dependencies, and infrastructure.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | SAST and Dependency Scanning | 20% | Automated static analysis and vulnerability database coverage |
| 2 | Auth and Access Control Review | 25% | Depth of authentication, authorization, and session management inspection |
| 3 | Input Validation and Injection | 20% | Coverage of injection vectors (SQL, XSS, command) and input/output encoding |
| 4 | Secrets and Configuration | 15% | Audit of secrets management, infrastructure configuration, and encryption |
| 5 | Finding Classification and Remediation | 20% | Quality of severity ratings, exploitation scenarios, and fix recommendations |
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
| A+ | 9.0 – 10.0 | Exceptional | Full automated and manual audit; all findings classified with exploitation scenarios and code-level fixes | Clear for release; no security blockers |
| A | 8.0 – 8.9 | Strong | Comprehensive audit with minor gaps; critical/high findings remediated; medium findings documented | Release with scheduled medium-finding remediation |
| B | 7.0 – 7.9 | Good | Automated tools run; auth and injection reviewed; some areas incomplete; findings classified | Conditional release after critical fixes |
| C | 5.0 – 6.9 | Adequate | Partial audit coverage; automated only or manual only; findings lack exploitation context | Block release; expand audit to missing areas |
| D | 3.0 – 4.9 | Weak | Minimal audit; single tool run without review; findings vague | Block release; full security audit required |
| F | 0.0 – 2.9 | Failing | No security audit performed | Reject; security audit mandatory |

## Signal Tables

### SAST and Dependency Scanning
| Score | Evidence |
|-------|----------|
| 9-10 | SAST tool (Semgrep/CodeQL/Bandit) and dependency scanner (npm audit/Snyk) run; all findings triaged; direct and transitive dependencies checked against CVE databases |
| 7-8 | Both SAST and dep scanning run; most findings triaged; transitive deps spot-checked |
| 5-6 | One of SAST or dep scanning run; findings partially triaged |
| 3-4 | Tool run but output not reviewed |
| 0-2 | No automated scanning |

### Auth and Access Control Review
| Score | Evidence |
|-------|----------|
| 9-10 | Authentication flows tested for bypass; authorization checked for privilege escalation; session management reviewed for fixation/hijacking; token handling verified (expiry, rotation, storage) |
| 7-8 | Auth flows and basic authorization reviewed; session management checked; minor edge cases not tested |
| 5-6 | Login flow reviewed; authorization spot-checked; session management not reviewed |
| 3-4 | Auth code read but not tested for attack scenarios |
| 0-2 | No auth review performed |

### Input Validation and Injection
| Score | Evidence |
|-------|----------|
| 9-10 | All input surfaces tested for SQL injection, XSS, command injection; output encoding verified; parameterized queries confirmed; content-type validation checked |
| 7-8 | Primary input surfaces tested; parameterized queries confirmed; XSS and SQL injection tested |
| 5-6 | Input validation code reviewed; injection testing limited to one vector |
| 3-4 | Input handling reviewed at code level only; no injection testing |
| 0-2 | No input validation review |

### Secrets and Configuration
| Score | Evidence |
|-------|----------|
| 9-10 | No hardcoded secrets in source or config; infrastructure reviewed for open ports, permissive IAM, missing encryption; secrets rotation policy verified |
| 7-8 | No hardcoded secrets found; basic infrastructure review; encryption at rest and in transit confirmed |
| 5-6 | Secrets grep performed; infrastructure configuration not reviewed |
| 3-4 | Quick scan for obvious secrets; no infrastructure review |
| 0-2 | No secrets or configuration audit |

### Finding Classification and Remediation
| Score | Evidence |
|-------|----------|
| 9-10 | Each finding has severity (CVSS or equivalent), exploitation scenario, affected component, and specific remediation with code example; findings prioritized for engineering |
| 7-8 | Severity assigned; exploitation context for critical/high; remediation guidance for all findings |
| 5-6 | Severity assigned; remediation descriptive but not code-level; exploitation context missing |
| 3-4 | Findings listed without severity or remediation |
| 0-2 | No structured findings |
