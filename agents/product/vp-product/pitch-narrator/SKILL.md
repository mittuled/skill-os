---
name: pitch-narrator
description: >
  This skill crafts the narrative arc for pitching a product opportunity to stakeholders or
  investors, structuring the story from problem through vision to ask. Use when preparing for
  a board meeting, investor update, or internal resource allocation review that requires a
  compelling product narrative. Also consider when a product initiative has strong data but
  lacks a persuasive framing that connects emotionally with decision-makers. Suggest when
  the team is building slides or a memo and the storyline feels disjointed or data-heavy
  without a throughline.
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills:
  - business-model-sketcher
  - competitive-response-monitor
  - goal-framer
triggers:
  - "narrate product pitch"
  - "product pitch"
  - "write pitch narrative"
  - "pitch story"
  - "product pitch deck"
---

# pitch-narrator

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Crafts the narrative arc for pitching the product opportunity to stakeholders or investors, transforming data and strategy into a compelling story with a clear ask.

## When to Use
- When preparing a product pitch for board members, investors, or executive sponsors who need to approve funding or prioritization
- When an internal resource allocation review requires a persuasive case for why this initiative should be prioritized over alternatives
- When the product story exists as scattered data points and needs a coherent narrative structure
- When a previously rejected initiative needs reframing with new evidence or a different angle

## Workflow
1. **Define the audience and ask**: Identify who the pitch targets (board, investors, exec team, cross-functional leads), what decision you need from them, and what objections they are likely to raise. Deliverable: audience profile with decision sought and anticipated objections.
2. **Establish the problem**: Frame the customer pain point with specificity -- who suffers, how often, what it costs them, and why existing solutions fail. Ground the problem in data (user research quotes, support ticket volumes, churn drivers). Deliverable: problem statement narrative with supporting evidence.
3. **Present the insight**: Articulate the unique insight or market shift that makes this the right moment to act. Connect the insight to a macro trend, technology unlock, or behavioral change that creates a window of opportunity. Deliverable: insight statement (2-3 sentences) with trend validation.
4. **Describe the solution**: Walk through the product vision at the right altitude for the audience -- concrete enough to be credible, abstract enough to leave room for execution flexibility. Show the user journey, not the feature list. Deliverable: solution narrative with user journey walkthrough.
5. **Quantify the opportunity**: Present TAM/SAM/SOM, revenue model, unit economics, or impact metrics appropriate to the audience. Tie numbers back to the problem scale. Deliverable: opportunity sizing with assumptions documented.
6. **Make the ask**: State exactly what you need -- budget, headcount, timeline, executive sponsorship -- and what the audience gets in return (milestones, checkpoints, kill criteria). Deliverable: ask statement with reciprocal commitments.
7. **Stress-test the narrative**: Walk through the pitch end-to-end, verify logical flow, check that every claim has evidence, and rehearse objection responses. Deliverable: final pitch narrative with objection-response pairs.

## Anti-Patterns
- **Data dump without story**: Presenting metrics, charts, and research findings without a narrative thread connecting them. *Why*: Decision-makers lose attention, cannot synthesize the implications, and default to "not now" when the case is unclear.
- **Solution-first pitch**: Leading with what you want to build before establishing why the problem matters. *Why*: Without problem framing, the audience cannot evaluate whether the solution is proportionate, and the pitch feels like a feature request.
- **Vague ask**: Ending the pitch without a specific, actionable request. *Why*: Ambiguous asks produce ambiguous outcomes -- "sounds interesting, let's revisit next quarter" instead of a concrete decision.
- **Overselling without kill criteria**: Presenting only the upside without acknowledging risks or defining conditions under which the initiative should be stopped. *Why*: Sophisticated stakeholders distrust one-sided pitches, and the lack of kill criteria signals poor judgment.

## Output
**On success**: A structured pitch narrative covering problem, insight, solution, opportunity sizing, and ask -- ready for presentation in slide deck, memo, or verbal format, with objection-response pairs prepared.
**On failure**: Report which narrative elements are weak (e.g., "opportunity sizing lacks credible TAM data," "problem statement needs customer evidence"), what additional inputs are needed, and recommend specific research or data collection to strengthen the pitch.

## Related Skills
- [`business-model-sketcher`](../business-model-sketcher/SKILL.md) — sibling skill under the same agent — combine with business-model-sketcher for end-to-end coverage
- [`competitive-response-monitor`](../competitive-response-monitor/SKILL.md) — sibling skill under the same agent — combine with competitive-response-monitor for end-to-end coverage
- [`goal-framer`](../goal-framer/SKILL.md) — sibling skill under the same agent — combine with goal-framer for end-to-end coverage
