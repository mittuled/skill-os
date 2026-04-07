# Scoring Rubric: developer-experience-reviewer

Evaluates the end-to-end developer experience across the full journey from signup to production deployment, covering onboarding, SDK usability, documentation, and the middle journey path.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Signup and Credential Acquisition | 15% | Ease of creating an account, obtaining API keys or tokens, and reaching a testable state |
| 2 | Quickstart Quality | 20% | Speed and clarity of the first successful integration, including documentation, samples, and sandbox |
| 3 | SDK Ergonomics | 20% | Installation ease, API design idiomaticity, debugging experience, and IDE integration quality |
| 4 | Documentation Depth | 15% | Coverage of advanced use cases, edge cases, error scenarios, and conceptual explanations beyond quickstart |
| 5 | Middle Journey (Prototype → Production) | 20% | Support for the path from working demo to production-grade deployment (auth hardening, error handling, scaling) |
| 6 | Developer Support Access | 10% | Ease of finding answers via docs, community, and support channels without human escalation |
| **Total** | | **100%** | |

## Scale

Each criterion scored **0–10**: 0 = absent/completely broken, 5 = functional with significant friction, 10 = best-in-class, no friction.

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Score | Label | Description | Recommended Action |
|-------|-------|-------|-------------|-------------------|
| A+ | 9.0–10.0 | Exceptional | TTFHW < 5 min, self-serve production deployment, zero support escalations needed | Maintain; use as public case study |
| A | 8.0–8.9 | Strong | TTFHW < 15 min, 1–2 minor friction points, docs cover 90%+ of use cases | Quarterly review; ship improvements opportunistically |
| B | 7.0–7.9 | Good | TTFHW < 30 min, some SDK roughness, docs miss edge cases, middle journey has gaps | Plan targeted improvements in next cycle |
| C | 5.0–6.9 | Adequate | TTFHW 30–60 min, SDK feels un-idiomatic, production path unclear, community support slow | Prioritize DX sprint; flag to product |
| D | 3.0–4.9 | Weak | TTFHW > 1 hour, SDK requires workarounds, docs outdated, production deployment requires support ticket | Urgent DX sprint; freeze on-boarding promotion |
| F | 0.0–2.9 | Failing | First integration not completable without internal help, SDK broken, docs absent | Do not promote until reworked; CEO/CTO flag |

## Signal Tables

### Signup and Credential Acquisition

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Account created and API key obtained in < 2 minutes; no email verification required for testing; sandbox auto-provisioned |
| 7–8 | Account and credentials in < 5 minutes; one email confirmation step; sandbox requires minor configuration |
| 5–6 | Setup takes 5–10 minutes; permission confusion; credentials found after navigating 3+ dashboard pages |
| 3–4 | Setup takes > 10 minutes; multiple approval or verification steps; developer blocked without docs open |
| 0–2 | No self-service signup; credentials require contacting sales or support; sandbox not available |

### Quickstart Quality

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | First successful API call completable in < 5 minutes from quickstart page; zero undocumented steps; live playground with pre-filled credentials |
| 7–8 | First call in < 15 minutes; 1–2 steps require searching outside quickstart; copy-paste code works immediately |
| 5–6 | First call takes 15–30 minutes; 3–4 undocumented prerequisites; code samples require minor modification |
| 3–4 | First call takes 30–60 minutes; multiple trial-and-error cycles; quickstart references features not yet available |
| 0–2 | Quickstart cannot be completed without community search or support contact; code samples broken |

### SDK Ergonomics

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | `pip install` / `npm install` in one command; auto-complete works in major IDEs; error messages include line numbers and fix suggestions; upgrade path documented |
| 7–8 | Installation straightforward; IDE support partial; errors include code but not remediation; upgrade guide exists |
| 5–6 | Installation requires config file setup; IDE integration absent; errors are numeric codes without context; manual migration required |
| 3–4 | SDK installation conflicts with common dependencies; no IDE integration; errors show stack traces; upgrade breaks code |
| 0–2 | No official SDK; developer must hand-roll HTTP client; no tooling support |

### Documentation Depth

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Advanced use cases covered with working examples; error scenarios documented; conceptual explanations for all domain concepts; changelog maintained |
| 7–8 | Common advanced use cases covered; most errors documented; changelog present; some edge cases missing |
| 5–6 | Basics well covered; advanced topics sparse; error reference incomplete; conceptual docs missing for some areas |
| 3–4 | Only reference docs exist; no advanced guides; errors undocumented; developer must experiment to understand behaviour |
| 0–2 | Documentation incomplete for basic use cases; no advanced guides; no error reference |

### Middle Journey (Prototype → Production)

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Production checklist provided; webhook security documented; rate limit handling examples; scaling guidance with architecture patterns |
| 7–8 | Production guide exists; key security steps covered; rate limit behaviour documented; some scaling guidance |
| 5–6 | Basic security docs; rate limits mentioned but not how to handle them; no scaling guidance; developer must figure out production config |
| 3–4 | No production guide; security configuration undocumented; developer must open support ticket for production deployment advice |
| 0–2 | No distinction between development and production configuration; no guidance for any production concern |

### Developer Support Access

| Score Range | Observable Evidence |
|-------------|-------------------|
| 9–10 | Docs search returns accurate results; active community forum with < 24h avg response; support SLA defined; escalation path clear |
| 7–8 | Docs searchable; community active but response time 1–3 days; support email responsive; escalation path exists |
| 5–6 | Docs search unreliable; community low-traffic; support email SLA undefined; developer must retry multiple channels |
| 3–4 | Docs hard to navigate; community inactive; support email takes > 5 days; no self-serve resolution path |
| 0–2 | No community; support email unresponsive; docs not searchable; developer abandoned |
