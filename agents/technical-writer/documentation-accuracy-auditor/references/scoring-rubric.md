# Scoring Rubric: documentation-accuracy-auditor

Evaluates the technical accuracy of documentation against the current product implementation, covering code sample correctness, API reference fidelity, procedure completeness, and freshness.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Code Sample Correctness | 30% | Percentage of code samples that execute without error against the current product version |
| 2 | API Reference Fidelity | 25% | Accuracy of documented endpoint signatures, parameters, response schemas, and error codes vs. actual API behaviour |
| 3 | Procedure Accuracy | 20% | Percentage of step-by-step tutorials and guides that produce the documented outcome when followed exactly |
| 4 | Content Freshness | 15% | Age of content relative to product releases; percentage of pages not updated since a release that changed their subject |
| 5 | Link Integrity | 10% | Percentage of internal and external links that resolve without 404 or redirect chains |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = completely broken, 5 = significant inaccuracies exist but some content works, 10 = fully accurate, no issues.

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Score | Label | Description | Recommended Action |
|-------|-------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Accurate | ≥ 99% code samples pass, zero reference mismatches, all procedures verified, < 30-day freshness lag | Maintain current cadence; no urgent remediation |
| A | 8.0–8.9 | Strong | ≥ 95% code samples pass, minor schema gaps, procedures mostly correct | Fix specific issues found; maintain quarterly audit |
| B | 7.0–7.9 | Good | 85–94% code samples pass, some response schema gaps, 1–2 procedure steps wrong | Plan focused remediation sprint |
| C | 5.0–6.9 | Adequate | 70–84% code samples pass, multiple reference inaccuracies, some guides lead developers astray | Prioritize audit remediation; pause new doc production until backlog cleared |
| D | 3.0–4.9 | Unreliable | 50–69% code samples fail, significant reference inaccuracies, multiple broken procedures | Urgent remediation sprint; add accuracy review to publish gate |
| F | 0.0–2.9 | Failing | < 50% code samples work, reference docs do not match API, guides produce errors | Stop directing developers to docs until remediated; escalate to engineering |

## Signal Tables

### Code Sample Correctness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | ≥ 99% of code samples execute successfully against current product version; no deprecated methods; syntax is idiomatic for language |
| 7–8 | 85–98% of samples pass; 1–2 samples require minor modification (version number, endpoint path); no samples crash |
| 5–6 | 70–84% of samples pass; several samples use deprecated parameters; some samples produce different output than documented |
| 3–4 | 50–69% of samples pass; multiple samples crash on first run; import statements broken or packages removed |
| 0–2 | < 50% of samples execute; documentation samples not tested against product; entirely different API version represented |

### API Reference Fidelity

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every documented parameter matches API; all response schemas match actual responses; all error codes match documented behaviour |
| 7–8 | ≥ 95% parameter accuracy; 1–2 response schema fields missing or wrong; error code list has minor gaps |
| 5–6 | 85–94% parameter accuracy; several response fields undocumented or wrong type; some error codes missing |
| 3–4 | 70–84% parameter accuracy; response schemas significantly incomplete; error codes do not match runtime behaviour |
| 0–2 | < 70% parameter accuracy; response schemas absent or completely wrong; error documentation does not reflect current API |

### Procedure Accuracy

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every step in every guide produces the stated outcome; no steps assume undocumented prerequisites; all screenshots current |
| 7–8 | 90–99% of steps produce correct outcome; 1–2 minor UI changes not reflected; no guide leads to a dead end |
| 5–6 | 75–89% of steps correct; 2–3 guides have steps that require workarounds; some outcomes differ from description |
| 3–4 | 50–74% of steps correct; multiple guides produce errors or unexpected outcomes; developer cannot complete without help |
| 0–2 | < 50% of procedures produce correct outcomes; guides systematically broken; following them causes worse state than starting fresh |

### Content Freshness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | No page not updated since a release that affected its content; last major product release reflected within 5 business days |
| 7–8 | ≥ 90% of release-affected pages updated within 2 weeks; minor features may have 2–4 week lag |
| 5–6 | 75–89% of release-affected pages updated; 1–2 major features released > 30 days ago without doc updates |
| 3–4 | 50–74% of release-affected pages updated; multiple major features not yet documented; > 60-day lag common |
| 0–2 | < 50% of release-affected pages updated; documentation lags behind product by a full version or more |

### Link Integrity

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | 0 broken internal links; 0 broken external links; no redirect chains > 1 hop |
| 7–8 | ≤ 2 broken links found; all core navigation links work; no broken links in quickstart or critical path |
| 5–6 | 3–10 broken links; some broken links in key content areas; redirect chains present but not blocking |
| 3–4 | 11–25 broken links; multiple broken links in primary navigation; important reference links return 404 |
| 0–2 | > 25 broken links; structural navigation broken; cross-references throughout docs do not resolve |
