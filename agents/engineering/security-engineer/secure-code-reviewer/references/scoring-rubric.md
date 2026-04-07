# Scoring Rubric: secure-code-reviewer

Evaluates the security quality of a code change across OWASP Top 10 coverage, language-specific risk assessment, dependency safety, review depth, and remediation guidance quality.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | OWASP Top 10 Coverage | 30% | Change set evaluated against all applicable OWASP Top 10 categories |
| 2 | Language-Specific Risk Review | 25% | Language and framework-specific vulnerabilities assessed beyond OWASP |
| 3 | Dependency Safety | 20% | New and modified dependencies assessed for CVEs, maintenance status, and supply chain risk |
| 4 | Review Depth | 15% | Context beyond the diff reviewed; surrounding code and data flow considered |
| 5 | Remediation Guidance Quality | 10% | Each finding has a specific, actionable fix recommendation |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely absent, 5 = partially present with significant gaps, 10 = fully present, no gaps.

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | All applicable OWASP categories checked, language-specific risks assessed, all dependencies vetted, surrounding context reviewed, specific fixes for every finding | Approve PR; no security blockers |
| A | 8.0–8.9 | Strong | All OWASP categories checked, 1–2 language risks noted but not deep, dependencies vetted, most context reviewed, specific fixes for major findings | Approve with minor remediation tracked in follow-up ticket |
| B | 7.0–7.9 | Good | OWASP categories checked but 1–2 not applicable to change were skipped without documentation, language review partial, dependencies mostly vetted | Conditional approval pending medium-severity fixes |
| C | 5.0–6.9 | Adequate | OWASP coverage incomplete, language-specific review surface-level, dependencies spot-checked only, diff-only review, generic remediation | Request changes — significant security review gaps |
| D | 3.0–4.9 | Weak | < 50% OWASP categories evaluated, no language-specific review, dependencies not assessed, no context review, findings without remediation | Block PR — security review is insufficient |
| F | 0.0–2.9 | Failing | SAST output copy-pasted without analysis, no manual review, dependencies ignored, no findings or only false positives | Block PR — security review provides false confidence |

## Signal Tables

### OWASP Top 10 Coverage

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All 10 OWASP categories assessed against the change set; each applicable category has explicit evidence of review (finding or "not applicable with rationale"); injection, access control, and cryptography always checked when change touches data or auth |
| 7–8 | 8–9 categories assessed; 1–2 inapplicable categories skipped without documentation; all injection and access control categories always reviewed |
| 5–6 | 6–7 categories assessed; injection and cryptography covered; access control and insecure design partially assessed; logging/monitoring and SSRF often skipped |
| 3–4 | 3–5 categories assessed; review focuses on the most obvious category for the change type; several critical categories not evaluated |
| 0–2 | 1–2 categories assessed or SAST output used as the review without validation; no structured OWASP assessment present |

### Language-Specific Risk Review

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Language-specific vulnerability classes assessed: prototype pollution (JS), deserialization gadget chains (Java), SQL via string concatenation (Python), path traversal via unsanitized input (all), unsafe eval patterns (JS/Python), timing attacks in cryptographic comparisons |
| 7–8 | Primary language risks for the change type assessed; 1–2 edge-case language risks (e.g., integer overflow in Go) not evaluated for low-risk changes |
| 5–6 | Generic vulnerability review applied regardless of language; 3–4 language-specific risks not evaluated; no framework-specific review (e.g., Django ORM raw query misuse) |
| 3–4 | OWASP applied generically; no language-specific assessment; framework-specific vulnerabilities (e.g., Rails mass assignment) not checked |
| 0–2 | No language awareness in review; vulnerabilities discussed in abstract terms not tied to the specific language and framework |

### Dependency Safety

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | All new/upgraded dependencies checked against NVD and GitHub Advisory; transitive dependencies reviewed for known CVEs; license compatibility confirmed; no unmaintained packages (last commit > 1 year) without documented acceptance |
| 7–8 | Direct dependencies checked against NVD; transitive dependencies spot-checked; license review present; 1–2 older dependencies noted but assessed as low risk |
| 5–6 | Direct dependencies checked; transitive dependencies not reviewed; license check absent; unmaintained packages not flagged |
| 3–4 | Dependencies noted but only checked for the most obvious CVEs; no structured database query; no transitive review |
| 0–2 | Dependencies not assessed; or only dependency names listed without any security assessment |

### Review Depth

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Surrounding context reviewed beyond the diff (caller functions, data flow paths, authorization context, existing error handling patterns); data flow traced from user input to output or storage |
| 7–8 | Immediately adjacent code reviewed; caller functions checked for security context; 1–2 upstream data sources not traced |
| 5–6 | Diff reviewed with minimal context; authorization model checked at the modified function level only; data flow not traced |
| 3–4 | Diff-only review; no surrounding context; no data flow analysis; security assessment limited to visible lines |
| 0–2 | Review limited to reading the diff without security analysis; no evidence of context investigation |

### Remediation Guidance Quality

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every finding has: specific code example of the fix, explanation of why the current code is vulnerable, and reference to the relevant standard (OWASP, CWE, NVD CVE ID) |
| 7–8 | Most findings have specific fix guidance; 1–2 findings have "consider using X" without showing how; all findings reference a standard |
| 5–6 | Findings describe the problem; fix guidance is directional ("add parameterized queries") but not shown as code; some findings lack standard references |
| 3–4 | Findings listed without fix guidance; developer must research the remediation independently |
| 0–2 | Findings listed as issue names only (e.g., "possible XSS") without description, evidence, or remediation |
