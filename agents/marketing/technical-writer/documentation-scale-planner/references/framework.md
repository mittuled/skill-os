# Framework: documentation-scale-planner

Defines the stack assessment model, bottleneck diagnosis criteria, tooling comparison matrix, IA scale patterns, and migration planning template for scaling documentation infrastructure.

## Documentation Stack Assessment

Evaluate the current stack across six dimensions before projecting scale requirements.

| Dimension | Key Questions | Health Indicators | Warning Signs |
|-----------|-------------|-----------------|--------------|
| Authoring | How do writers create content? Can engineers contribute? | Git-based authoring, PR review for docs | Copy-paste into CMS, no review workflow |
| Build pipeline | How long does a docs build take? Is CI/CD in place? | < 5-minute build, automated deploys | > 15-minute build, manual FTP/upload |
| Hosting and CDN | Is the docs site fast globally? Uptime SLA? | CDN-backed, < 200ms TTFB globally | Shared hosting, no CDN |
| Search | Can developers find what they need? | Accurate results, < 3s response | No search, broken search, Ctrl+F dependent |
| Analytics | Do you know which content is used? | Page-level analytics, search term tracking | No analytics, no exit-rate data |
| Contribution workflow | Can external contributors submit PRs or issues? | GitHub-based, clear CONTRIBUTING.md | No contribution path, or email-based only |

## Bottleneck Diagnosis Criteria

| Symptom | Likely Bottleneck | Diagnosis Test |
|---------|-----------------|---------------|
| Build times > 10 minutes | Content volume or unoptimized build | Run build with 1 page vs. 1,000 — linear scaling indicates content issue; exponential indicates build config |
| Search quality degrading | Content structure or search index config | Search for a term you know exists — if it returns wrong or no result, indexing is the issue |
| Writers spending > 20% on tooling | Authoring tool friction | Ask writers to time their publish workflow — any step > 15 min on tooling (not content) is bottleneck |
| Navigation confusion at > 200 pages | IA too flat or deep | Measure docs depth: > 4 levels = too deep; all content at 1 level = too flat |
| Content duplication > 20% | No content reuse mechanism | Run a full-text similarity check across docs — > 20% overlap means reuse tooling needed |
| External contributors < 5/quarter | Contribution friction | Ask last 10 issue reporters why they did not submit a PR — identify the friction point |

## IA Scale Patterns

| Pattern | Description | Best For | Pages Before Needed |
|---------|-------------|---------|---------------------|
| Flat | All content at same hierarchy level | Small API, single product | < 50 pages |
| Hierarchical | Topic → subtopic → page nesting | Multi-feature product | 50–500 pages |
| Faceted | Same content accessible via multiple navigation paths | Multi-persona or multi-language product | > 200 pages |
| Hub-and-spoke | Product docs hub links out to product-specific microsites | Multi-product company | > 3 distinct products |
| Versioned | Full or partial docs snapshot per product version | APIs with long-lived versions (> 18 months) | When supporting 2+ versions simultaneously |

## Tooling Comparison Matrix

| Tool Category | Popular Options | Best For | Scale Ceiling | Docs-as-Code? |
|--------------|----------------|---------|--------------|--------------|
| Static site generators | Docusaurus, MkDocs, Sphinx, Hugo | Developer docs, open-source | Very high | Yes |
| Managed docs platforms | ReadMe.com, Stoplight, GitBook | API reference, quick setup | Medium | Partial |
| Content management | Contentful, Sanity | Marketing-heavy mixed content | Medium | No |
| API doc generators | Swagger UI, Redoc, OpenAPI Generator | Auto-generated reference from spec | High (reference only) | Yes |
| Search | Algolia DocSearch, Meilisearch | Developer docs search | High | — |
| Analytics | Google Analytics, Posthog, Plausible | Docs usage tracking | High | — |

**Evaluation criteria** (score each 1–5 for your context):
1. Build time at projected scale
2. Contributor onboarding time (time for first contribution)
3. Search accuracy and response time
4. Analytics integration
5. Versioning support
6. Migration cost from current stack

## Maintenance Burden Formula

Estimate ongoing maintenance cost before committing to a tooling choice.

```
Monthly Maintenance Hours = (Pages × avg_update_frequency_per_page_per_month) 
                          + (Tools × avg_hours_per_tool_per_month)
                          + (Contributors × avg_onboarding_hours × churn_rate)
```

**Benchmark targets:**
- Writer time on tooling (not content): < 15% of total docs time
- Build failure rate: < 2% of PRs fail due to tooling (not content errors)
- Contributor first-PR time: < 30 minutes from clone to PR open

## Migration Phases

For any tooling migration, follow this phased approach:

| Phase | Activities | Duration Estimate | Risk Level |
|-------|-----------|------------------|-----------|
| Proof of concept | Migrate 5–10 representative pages to new stack | 1–2 weeks | Low |
| Parallel run | Run old and new stacks simultaneously; redirect 10% of traffic | 2–4 weeks | Low |
| Progressive migration | Migrate sections by priority; redirect each as completed | 4–12 weeks | Medium |
| Full cutover | Redirect all traffic to new stack; keep old on standby 30 days | 1 week | Medium |
| Decommission | Remove old stack after 30-day incident-free period | 1 week | Low |

**Rollback gate**: If traffic to new stack produces > 2× support tickets in the first 72 hours, revert to old stack immediately.
