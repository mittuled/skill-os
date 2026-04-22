---
name: case-study-extractor-pmm
description: >
  This skill extracts and structures customer case studies from CS and sales inputs into publishable narratives.
  Use when a customer success story needs to be turned into a reusable marketing asset. Also consider when
  sales requests proof points for a specific vertical or use case. Suggest when a customer renewal or
  expansion signals a strong outcome worth capturing before institutional memory fades.
department: product
agent: pmm-analyst-content-strategist
version: 1.0.0
complexity: medium
related-skills:
  - ga-announcement
  - in-app-announcement-writer
  - partner-activation-planner-pmm
  - changelog-publisher-pmm
  - content-engine-builder-pmm
triggers:
  - "extract case study"
  - "write case study pmm"
  - "create case study"
  - "customer case study"
  - "case study content"
---

# case-study-extractor-pmm

## Agent: PMM Analyst Content Strategist
L3 PMM analyst and content strategist (multi-instance) responsible for in-app announcements, changelog publishing, case study creation, and content engine operations.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description
Extracts and structures customer case studies from CS and sales inputs into publishable narratives that demonstrate measurable business outcomes.

## When to Use
- When a customer achieves a quantifiable win that sales can use as social proof in active deal cycles
- When entering a new vertical and the team needs a reference story to establish credibility with prospects
- When CS flags a renewal or expansion that reveals a compelling before-and-after transformation worth documenting

## Workflow
1. **Identify the candidate story**: Review CS health scores, expansion events, and sales win reports to select a customer with a clear, measurable outcome. Confirm the customer is referenceable and willing to participate. Deliverable: candidate brief with customer name, outcome summary, and participation status.
2. **Gather raw inputs**: Collect call transcripts, QBR decks, support tickets, onboarding notes, and any quantitative metrics from CS and sales. Request a 30-minute interview slot with the customer champion if gaps remain. Deliverable: raw input folder with all source materials tagged by theme.
3. **Extract the narrative arc**: Structure the story into situation, challenge, solution, and results. Identify the single most compelling metric and make it the headline. Deliverable: narrative outline with section headers and key quotes pulled verbatim.
4. **Draft the case study**: Write the full case study in the company voice. Lead with the outcome metric, provide enough context for a skeptical buyer to find the story credible, and close with a forward-looking quote from the customer. Keep the draft under 800 words. Deliverable: first draft in the standard case study template.
5. **Validate with stakeholders**: Send the draft to the CS account owner and the customer champion for factual review. Flag any metrics that lack source documentation. Deliverable: approved draft with tracked changes resolved and customer sign-off.
6. **Package for distribution**: Export the final case study into web, PDF, and slide-snippet formats. Tag it by vertical, use case, company size, and product area so sales can find it. Deliverable: published case study in the content library with metadata tags applied.

## Anti-Patterns
- **Vanity metrics only**: Featuring impressive-sounding numbers that the customer cannot substantiate or that lack baseline context. *Why*: Prospects and analysts will challenge unverified claims, eroding trust in all case studies.
- **Hero-less storytelling**: Writing the case study as a product feature tour instead of centering the customer's journey and decisions. *Why*: Buyers relate to people and problems, not feature lists; a product-centric case study reads like a brochure and fails to persuade.
- **Stale capture**: Waiting months after the outcome to begin extraction. *Why*: Key details, emotional context, and champion availability decay rapidly; stories captured late are vague and less compelling.

## Output
**On success**: A published, customer-approved case study in web, PDF, and slide-snippet formats -- tagged by vertical, use case, and company size -- with a headline metric, narrative arc, and at least one direct customer quote, ready for sales enablement and marketing distribution.

**On failure**: Report which stage stalled (customer declined participation, metrics could not be verified, stakeholder approval timed out), what partial materials exist, and recommend next steps such as anonymizing the story or escalating the approval request.

## Related Skills
- [`ga-announcement`](../ga-announcement/SKILL.md) — sibling skill under the same agent — combine with ga-announcement for end-to-end coverage
- [`in-app-announcement-writer`](../in-app-announcement-writer/SKILL.md) — sibling skill under the same agent — combine with in-app-announcement-writer for end-to-end coverage
- [`partner-activation-planner-pmm`](../partner-activation-planner-pmm/SKILL.md) — sibling skill under the same agent — combine with partner-activation-planner-pmm for end-to-end coverage
- [`changelog-publisher-pmm`](../changelog-publisher-pmm/SKILL.md) — sibling skill under the same agent — combine with changelog-publisher-pmm for end-to-end coverage
- [`content-engine-builder-pmm`](../content-engine-builder-pmm/SKILL.md) — sibling skill under the same agent — combine with content-engine-builder-pmm for end-to-end coverage
