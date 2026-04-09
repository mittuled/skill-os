---
name: demand-validator
description: >
  This skill assesses whether real market demand exists for a proposed solution by triangulating qualitative discovery findings with quantitative signals such as search volume, waitlist conversion, fake-door tests, and competitive proxy data. Use when customer discovery has surfaced a promising opportunity but the team needs evidence of scale before committing engineering resources. Also consider when a feature request appears popular in support tickets but lacks revenue or adoption backing. Suggest when RICE scoring shows high impact but low confidence.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "experiment design"
  - "validate demand"
  - "experiment-designer"
  - "product experiment"
---

# demand-validator

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
The demand validator determines whether a proposed solution has sufficient real-world demand to justify development investment. It triangulates qualitative signals from customer discovery with quantitative proxies -- search trends, waitlist sign-ups, fake-door click-through rates, competitive feature adoption, and willingness-to-pay indicators -- to produce a demand verdict that feeds RICE confidence scores and roadmap decisions.

## When to Use
- Customer discovery has validated a problem but the team needs to gauge how many people share it before investing engineering effort.
- A feature request ranks high in support-ticket volume but has not been tested for willingness to pay or switch.
- RICE scoring on a backlog item shows high impact but confidence is rated low due to lack of quantitative demand evidence.
- A competitor has launched a similar capability and the team needs to assess whether the market pull is real or hype-driven.
- The roadmap includes a speculative bet that requires a go/no-go demand checkpoint before entering the next planning cycle.

## Workflow
1. Gather the qualitative inputs: discovery brief, JTBD cards, NPS verbatims, and support-ticket clusters related to the proposed solution.
2. Define the demand question in measurable terms (e.g., "Do at least 15% of target-persona accounts exhibit this workflow pain weekly?").
3. Identify quantitative proxies appropriate to the stage:
   - **Pre-build:** search volume (Google Trends, keyword tools), waitlist or landing-page sign-ups, fake-door test CTR.
   - **Competitor proxy:** feature-adoption data from public case studies, G2/Capterra review mining, job-posting signals.
   - **Internal proxy:** related-feature usage telemetry, expansion-revenue correlation, churn-reason tagging.
4. Design and run the cheapest viable test -- typically a fake-door experiment, survey, or concierge MVP -- with a pre-committed success threshold.
5. Collect results over the agreed measurement window; reject early reads that lack statistical stability.
6. Triangulate qualitative and quantitative findings into a demand verdict: **validated**, **inconclusive**, or **invalidated**.
7. Update the RICE confidence score for the relevant backlog items based on the verdict.
8. Publish the demand-validation brief and route to `roadmap-placer` for scheduling implications or to `backlog-populator` to create/archive items accordingly.

## Anti-Patterns
- **Validating demand with existing customers only.** Surveying the current user base measures satisfaction, not market demand; it misses the non-customer segment entirely. *Why: demand validation must include the addressable market, not just the installed base, to avoid survivorship bias.*
- **Accepting stated intent as demand.** "Would you use this?" surveys inflate demand because respondents face no cost for saying yes. *Why: only revealed preference (clicks, sign-ups, payments) reliably predicts adoption.*
- **Moving the goalposts after results arrive.** Lowering the success threshold post-hoc to rescue a favoured idea undermines the entire validation framework. *Why: pre-committed thresholds exist to counteract confirmation bias.*
- **Running validation without a time box.** Leaving the measurement window open-ended delays decisions and lets the team cherry-pick favourable data points. *Why: bounded windows force timely verdicts and prevent indefinite deferral.*

## Output

**Success:**
- A demand-validation brief containing the demand question, proxies tested, raw data, triangulated verdict (validated / inconclusive / invalidated), and updated RICE confidence score.
- A clear recommendation: proceed to build, run a deeper validation round, or archive the opportunity.

**Failure:**
- The verdict is declared without quantitative evidence, relying solely on qualitative enthusiasm.
- Success thresholds were changed after data collection, making the verdict unreliable for prioritisation.

## Related Skills
- `customer-discovery-planner` -- produces the qualitative inputs that demand validation triangulates against.
- `market-sizer` -- provides TAM/SAM context that frames the demand question at the right scale.
- `roadmap-placer` -- consumes the demand verdict to adjust roadmap positioning.
- `backlog-populator` -- creates or archives backlog items based on the validation outcome.
