# Research: Product Domain — Skill Deepening

Compiled for task T057. Covers product skill families, key frameworks, reference databases, common anti-patterns, and recommended reference types to guide enrichment of `vp-product` and related product agent skills.

---

## 1. Product Skill Families

### 1.1 Strategy
Skills that define direction, position, and long-term bets.
Examples: opportunity-framer, north-star-metric-reviewer, moat-analyzer, business-model-sketcher, goal-framer, competitive-response-monitor, idea-critic, assumption-mapper.

### 1.2 Execution
Skills that drive delivery, prioritisation, and sprint-level decisions.
Examples: prd-assembler, mvp-definer, gate-12-evaluator, sla-definer.

### 1.3 Analytics & Measurement
Skills that close the loop between output and outcome.
Examples: product-feedback-ingestion, north-star-metric-reviewer.

### 1.4 Go-to-Market & Commercialisation
Skills that bridge product to market and revenue.
Examples: launch-coordinator, packaging-designer, pricing-v1-setter, pitch-narrator.

### 1.5 Partnership & Discovery
Skills that source external insight and validation.
Examples: design-partner-programme-builder, assumption-mapper.

---

## 2. Key Frameworks by Skill Family

### Strategy
| Framework | Purpose | Applicable Skills |
|-----------|---------|-------------------|
| Jobs-to-be-Done (JTBD) | Reframe customer problems as jobs, separate from solutions | opportunity-framer, idea-critic |
| Opportunity Solution Tree (OST) | Map desired outcomes to opportunities and experiments | opportunity-framer, assumption-mapper |
| Competitive Moat Canvas | Identify durable defensibility sources (network effects, data, switching cost, scale, brand) | moat-analyzer |
| Business Model Canvas (BMC) | Nine-block visual of value proposition, channels, revenue, cost structure | business-model-sketcher |
| OKRs (Objectives and Key Results) | Align goals to measurable outcomes at company, team, and individual level | goal-framer, north-star-metric-reviewer |
| Porter's Five Forces | Analyse industry structure and competitive intensity | competitive-response-monitor, moat-analyzer |
| Blue Ocean Strategy | Identify uncontested market space by raising and reducing value dimensions | opportunity-framer |

### Execution & Prioritisation
| Framework | Purpose | Applicable Skills |
|-----------|---------|-------------------|
| RICE (Reach × Impact × Confidence ÷ Effort) | Quantitative feature prioritisation | prd-assembler, mvp-definer |
| MoSCoW (Must / Should / Could / Won't) | Scope negotiation and release planning | prd-assembler, mvp-definer, sla-definer |
| Kano Model | Classify features as basic needs, performance, or delighters | prd-assembler, idea-critic |
| Hypothesis-Driven Development | Structure every feature as a testable hypothesis | mvp-definer, assumption-mapper |
| Story Mapping (Jeff Patton) | Organise user stories by activity and release slices | prd-assembler |
| Pre-mortem | Identify failure modes before building | gate-12-evaluator, assumption-mapper |

### Analytics & Measurement
| Framework | Purpose | Applicable Skills |
|-----------|---------|-------------------|
| HEART (Happiness, Engagement, Adoption, Retention, Task Success) | User-centric product health metrics from Google | north-star-metric-reviewer, product-feedback-ingestion |
| AARRR / Pirate Metrics (Acquisition, Activation, Retention, Revenue, Referral) | Growth funnel measurement | north-star-metric-reviewer |
| North Star Metric + Input Metrics tree | Single metric that best captures value delivered; broken down into leading indicators | north-star-metric-reviewer, goal-framer |
| Amplitude PACE framework | Product analytics maturity: Predict, Act, Collaborate, Experiment | product-feedback-ingestion |
| Cohort Analysis | Track behaviour of user groups over time to measure retention and churn | product-feedback-ingestion |

### Go-to-Market & Commercialisation
| Framework | Purpose | Applicable Skills |
|-----------|---------|-------------------|
| Crossing the Chasm (Moore) | Stage-gate model for technology adoption; early market vs. mainstream | launch-coordinator, packaging-designer |
| Pricing Ladder / Value Metric | Align pricing to the unit of value customers receive | pricing-v1-setter, packaging-designer |
| Jobs-to-be-Done for Pricing | Match price point to the job the customer is hiring the product to do | pricing-v1-setter |
| STP (Segmentation, Targeting, Positioning) | Structure go-to-market targeting decisions | packaging-designer, pitch-narrator |
| Pitch Narrative Arc (Problem → Solution → Evidence → Ask) | Investor and executive communication | pitch-narrator |

### Partnership & Discovery
| Framework | Purpose | Applicable Skills |
|-----------|---------|-------------------|
| Design Partner Programme Structure | Staged engagement model: co-discover → co-design → validate → referenceable | design-partner-programme-builder |
| Assumption Mapping (Strategyzer) | Two-axis plot of importance vs. confidence; route to validation experiments | assumption-mapper |

---

## 3. Reference Databases to Use

| Source | URL / Access | Use For |
|--------|-------------|---------|
| Amplitude product analytics documentation | amplitude.com/docs | HEART metrics, event tracking patterns, cohort analysis, PACE framework |
| ProductPlan blog and templates | productplan.com/learn | Roadmap formats, Now/Next/Later, RICE calculator, OKR templates |
| Reforge articles and frameworks | reforge.com/blog | North Star Metric, growth loops, retention curves, activation patterns |
| Strategyzer tools | strategyzer.com | Business Model Canvas, Value Proposition Canvas, Assumption Mapping |
| Silicon Valley Product Group (SVPG) | svpg.com/articles | Product discovery, empowered product teams, OKRs in practice |
| Mind the Product | mindtheproduct.com | Feature prioritisation, stakeholder management, roadmap communication |

---

## 4. Common Anti-Patterns by Skill Type

### Strategy Skills
- **Moat = current competitive advantage**: Moat analysis confuses today's differentiation with durable defensibility. Test each moat source for durability under scale and adversarial conditions.
- **Goal-setting without measurement**: OKRs written as activities ("we will launch feature X") instead of outcomes ("activation rate increases from 30% to 45%").
- **Assumption mapping as documentation**: Assumption maps filled out after a decision is made, used to justify rather than test.

### Execution Skills
- **RICE scores as output**: Presenting RICE scores as conclusions rather than as inputs to a conversation. Teams anchor on the number and stop reasoning.
- **MoSCoW without a constraint**: "Must have" lists that exceed scope without a forcing function.
- **PRDs as waterfall specs**: PRDs written as complete specifications that engineering must implement rather than as living hypothesis documents.

### Analytics Skills
- **Vanity metrics as north star**: Tracking total signups or page views as the north star when they do not correlate to retained value.
- **HEART without baselines**: Running HEART surveys without historical baselines, making it impossible to measure change.
- **Pirate metrics in isolation**: Optimising one AARRR stage (e.g., acquisition) while ignoring downstream stages (activation, retention).

### GTM Skills
- **Pricing before value metric**: Setting a price tier structure before defining what unit of value customers pay for.
- **Launch as finish line**: Treating launch day as completion; successful launches require 30-60-90 day post-launch activation plans.

---

## 5. Recommended Reference Types by Skill Pattern

| Skill Pattern | Best Reference Type | Rationale |
|---------------|---------------------|-----------|
| Assessment / evaluation skill (e.g., gate-12-evaluator, idea-critic) | `scoring-rubric.md` | Provides explicit criteria, weights, and grade thresholds |
| Document-generation skill (e.g., prd-assembler, pitch-narrator) | `assets/<output>-template.md` | Gives the agent a fill-in scaffold to produce consistent output |
| Workflow / process skill (e.g., launch-coordinator, assumption-mapper) | `references/framework.md` | Defines the conceptual model, stages, and decision rules |
| Analysis skill (e.g., competitive-response-monitor, moat-analyzer) | `references/scoring-rubric.md` or `framework.md` | Scoring rubric if output is a grade; framework if output is a structured analysis |
| Planning skill (e.g., design-partner-programme-builder, goal-framer) | `references/framework.md` + `assets/<plan>-template.md` | Framework for methodology; template for the deliverable |

---

## 6. Notes on vp-product Agent Enrichment

The `vp-product` agent in this repo contains 18 skills (as of branch 003-production-grade-depth). All 18 skills have been enriched with `references/` content (either `framework.md`, `scoring-rubric.md`, or `checklist.md`). Skills requiring the most depth improvement are those generating structured deliverables that currently lack output `assets/` templates:

- `prd-assembler` — would benefit from an `assets/prd-template.md`
- `pitch-narrator` — would benefit from an `assets/pitch-deck-structure.md`
- `pricing-v1-setter` — would benefit from an `assets/pricing-model-template.md`
- `launch-coordinator` — would benefit from an `assets/launch-runbook-template.md`

These four skills produce the most externally-visible deliverables and are strong candidates for the next enrichment pass (T059+).
