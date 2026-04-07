# Documentation Accuracy Audit Report

**Version**: 1.0  
**Owner**: Technical Writer  
**Audit Scope**: [Full docs site / Specific section / Single guide]  
**Audit Date**: YYYY-MM-DD  
**Auditor**: [Name], Technical Writer  

---

## 1. Audit Summary

| Dimension | Score (0–10) | Issues Found | Critical | High | Medium | Low |
|-----------|-------------|-------------|----------|------|--------|-----|
| Technical Accuracy | [X] | [X] total | [X] | [X] | [X] | [X] |
| Completeness | [X] | [X] total | [X] | [X] | [X] | [X] |
| Code Example Validity | [X] | [X] total | [X] | [X] | [X] | [X] |
| Link Integrity | [X] | [X] total | [X] | [X] | [X] | [X] |
| Version Currency | [X] | [X] total | [X] | [X] | [X] | [X] |
| **Overall Score** | **[X]** | **[X] total** | **[X]** | **[X]** | **[X]** | **[X]** |

**Audit Verdict**: Pass / Conditional Pass / Fail  
**Next Audit Due**: [Date]

---

## 2. Scope & Methodology

### Pages / Sections Audited
| Section | Pages Audited | Pages Skipped | Reason Skipped |
|---------|--------------|--------------|----------------|
| Getting Started | [X] | [X] | [Reason] |
| API Reference | [X] | [X] | [Reason] |
| Guides / Tutorials | [X] | [X] | [Reason] |
| SDK Documentation | [X] | [X] | [Reason] |
| **Total** | **[X]** | **[X]** | |

### Audit Methods Used
- [ ] Manual review against current product / API behavior
- [ ] Code examples tested against production API
- [ ] Code examples tested against sandbox / staging API
- [ ] Automated link checker run
- [ ] Screenshot comparison (UI-based docs)
- [ ] API spec diff (OpenAPI current vs documented)
- [ ] Customer feedback review (support tickets, community threads)

---

## 3. Critical Issues (Must Fix Before Next Release)

| ID | Page / Section | Issue Description | Evidence | Fix Required |
|----|---------------|------------------|----------|-------------|
| C-001 | [Page URL or title] | [Issue — e.g. "Deprecated authentication method still shown as current"] | [Evidence] | [Specific fix] |
| C-002 | [Page URL or title] | [Issue — e.g. "Code example uses removed parameter; throws 400 error"] | [Evidence] | [Specific fix] |
| C-003 | | | | |

---

## 4. High-Priority Issues (Fix Within 2 Weeks)

| ID | Page / Section | Issue Description | Fix Required | Owner | Due |
|----|---------------|------------------|-------------|-------|-----|
| H-001 | [Page] | [Issue] | [Fix] | [Name] | [Date] |
| H-002 | [Page] | [Issue] | [Fix] | [Name] | [Date] |
| H-003 | [Page] | [Issue] | [Fix] | [Name] | [Date] |

---

## 5. Medium-Priority Issues (Fix in Next Sprint)

| ID | Page / Section | Issue Description | Fix Required | Owner | Due |
|----|---------------|------------------|-------------|-------|-----|
| M-001 | [Page] | [Issue] | [Fix] | [Name] | [Date] |
| M-002 | [Page] | [Issue] | [Fix] | [Name] | [Date] |

---

## 6. Low-Priority Issues (Backlog)

| ID | Page / Section | Issue Description | Notes |
|----|---------------|------------------|-------|
| L-001 | [Page] | [Issue — e.g. outdated screenshot; cosmetic] | [Note] |
| L-002 | | | |

---

## 7. Code Example Validation Results

| Language | Examples Tested | Pass | Fail | Fail Rate |
|----------|----------------|------|------|-----------|
| cURL | [X] | [X] | [X] | [X]% |
| Python | [X] | [X] | [X] | [X]% |
| Node.js | [X] | [X] | [X] | [X]% |
| Go | [X] | [X] | [X] | [X]% |
| **Total** | **[X]** | **[X]** | **[X]** | **[X]%** |

### Failed Examples (Detail)
| Example Location | Language | Error Returned | Root Cause |
|-----------------|----------|---------------|-----------|
| [Page / endpoint] | [Lang] | [Error] | [Root cause — e.g. deprecated param] |

---

## 8. Link Integrity Check

| Link Type | Total Checked | Broken | Redirect | OK |
|-----------|--------------|--------|----------|-----|
| Internal links | [X] | [X] | [X] | [X] |
| External links | [X] | [X] | [X] | [X] |
| Code example links (GitHub repos) | [X] | [X] | [X] | [X] |

**Broken links requiring fix**: [List or attach file]

---

## 9. Version Currency Assessment

| Documented Version | Current Product Version | Lag | Impact |
|-------------------|------------------------|-----|--------|
| API | v[X] | v[X] | [X] versions | [Impact assessment] |
| SDK — Python | [X] | [X] | [X] versions | [Impact] |
| SDK — Node.js | [X] | [X] | [X] versions | [Impact] |

---

## 10. Remediation Plan

| Priority | Total Issues | Fix ETA | Owner |
|----------|-------------|---------|-------|
| Critical | [X] | [Date] | [Name] |
| High | [X] | [Date] | [Name] |
| Medium | [X] | [Date + sprint] | [Name] |
| Low | [X] | Backlog | [Name] |

**Estimated remediation effort**: [X] person-days

---

## 11. Audit Sign-Off

| Role | Name | Sign-Off | Date |
|------|------|----------|------|
| Technical Writer | [Name] | [ ] | |
| DevRel Lead / Docs Lead | [Name] | [ ] | |
| Engineering Representative | [Name] | [ ] | |
