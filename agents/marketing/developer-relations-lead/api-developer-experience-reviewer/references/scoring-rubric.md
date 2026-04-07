# Scoring Rubric: api-developer-experience-reviewer

Evaluates the quality of an API's developer experience across onboarding, documentation, SDK support, error handling, authentication, and code sample coverage.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Onboarding Friction | 25% | Time and steps required for a new developer to make their first successful API call |
| 2 | Documentation Quality | 20% | Completeness, accuracy, and navigability of API reference and guides |
| 3 | SDK Completeness | 20% | Coverage across target languages, consistency, and maintenance activity |
| 4 | Error Message Clarity | 15% | Actionability and specificity of error responses |
| 5 | Authentication Complexity | 10% | Ease of obtaining and using credentials for first call |
| 6 | Code Sample Coverage | 10% | Presence and correctness of runnable samples per endpoint per language |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = absent/completely broken, 5 = functional with significant friction, 10 = best-in-class, no friction

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | TTFHW < 5 min, zero documentation gaps, SDKs in all target languages, self-explanatory errors | Maintain; publish as reference implementation |
| A | 8.0–8.9 | Strong | TTFHW < 15 min, minor doc gaps, SDKs in primary languages, clear errors | Schedule quarterly review; no blockers |
| B | 7.0–7.9 | Good | TTFHW < 30 min, some doc sections incomplete, 1–2 language gaps, most errors actionable | Plan improvements in next cycle; log issues |
| C | 5.0–6.9 | Adequate | TTFHW 30–60 min, docs missing key sections, SDK gaps causing workarounds, generic errors | Prioritize high-impact fixes; consider freeze on new API work |
| D | 3.0–4.9 | Weak | TTFHW > 1 hour, docs unreliable, no official SDK in 1+ target language, cryptic errors | Urgent improvement sprint required before broader adoption |
| F | 0.0–2.9 | Failing | Integration not completable without internal help, docs absent or wrong, errors reveal internals | Do not ship/promote until reworked |

## Signal Tables

### Onboarding Friction

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | First call completable in < 5 minutes from reading docs; zero prerequisite setup not covered in quickstart; live playground available |
| 7–8 | First call completable in < 15 minutes; 1–2 steps require searching outside main docs; no environment-specific blockers |
| 5–6 | First call takes 15–30 minutes; missing a prerequisite step in docs; requires trial-and-error on auth or base URL |
| 3–4 | First call takes 30–60 minutes; multiple undocumented steps; developer must inspect network traffic or read source code |
| 0–2 | First call not completable without internal help or community forum search; docs lead to dead ends or broken endpoints |

### Documentation Quality

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every endpoint documented with description, all parameters, response schemas, and at least one example; changelog maintained; no broken links |
| 7–8 | 95%+ endpoints documented; minor parameter descriptions missing; changelog present but occasionally late |
| 5–6 | 80–94% endpoints documented; response schemas incomplete for 10–20% of endpoints; changelog absent or irregular |
| 3–4 | 50–79% endpoints documented; significant gaps in parameters or response descriptions; outdated code samples present |
| 0–2 | < 50% endpoints documented; response schemas absent; docs not updated to match current API behaviour |

### SDK Completeness

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Official SDKs in all target languages; updated within last 30 days; > 80% endpoint coverage; idiomatic code patterns |
| 7–8 | SDKs in 80%+ target languages; updated within last 90 days; > 70% endpoint coverage |
| 5–6 | SDKs in 50–79% target languages; last update 3–6 months ago; community workarounds needed for some endpoints |
| 3–4 | SDK exists for only 1 language; last update > 6 months; < 50% endpoint coverage; breaking bugs reported |
| 0–2 | No official SDK; developers must hand-roll HTTP clients; no community SDK activity |

### Error Message Clarity

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Every error includes: HTTP status, machine-readable code, human-readable message, cause, and remediation step |
| 7–8 | Errors include status + code + message; most include cause; remediation present for common errors |
| 5–6 | Errors include status + generic message; codes inconsistent; no remediation guidance |
| 3–4 | Errors include status only; messages are stack traces or internal identifiers; cause unknown without support ticket |
| 0–2 | Errors return 200 with error buried in body, or 500 with no information; no distinction between client and server errors |

### Authentication Complexity

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | API key or OAuth token obtainable in < 2 minutes; credentials work in all sample code; no scope configuration required for basic use |
| 7–8 | Credentials obtainable in < 5 minutes; minor scope/permission confusion; sample code works with default credentials |
| 5–6 | Credential setup takes 5–15 minutes; requires navigating 2+ dashboard pages; scope errors not clearly documented |
| 3–4 | Auth setup takes > 15 minutes; requires support contact or non-obvious configuration; sample code auth does not match production requirements |
| 0–2 | No self-service credential creation; auth system broken or undocumented; developer cannot authenticate without internal access |

### Code Sample Coverage

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Runnable samples in all target languages for every endpoint; samples use current SDK; copy-paste executes without modification |
| 7–8 | Samples in primary languages for 90%+ endpoints; minor version drift in 1–2 samples; curl examples for all endpoints |
| 5–6 | Samples in 1–2 languages for 70–89% endpoints; some samples have syntax errors or use deprecated methods |
| 3–4 | Samples only in curl; 50–69% endpoint coverage; samples require non-trivial modification to run |
| 0–2 | No runnable samples; only request/response schema descriptions; developer must construct all calls from scratch |
