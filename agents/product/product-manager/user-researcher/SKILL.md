---
name: user-researcher
description: >
  This skill conducts user research interviews and synthesises findings into actionable product insights.
  Use when the team needs first-hand understanding of user behaviour, pain points, or unmet needs before making product decisions.
  Also consider when quantitative data shows a trend but the team lacks qualitative context to explain it.
  Suggest when a feature is being designed based on internal assumptions rather than validated user evidence.
department: product
agent: product-manager
version: 1.0.0
complexity: complex
related-skills: []
---

# user-researcher

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Conducts user research interviews and synthesises findings into actionable product insights.

## When to Use
- When the team is entering discovery for a new initiative and needs to validate assumptions about user problems before committing to a solution direction
- When quantitative metrics (drop-off rates, low adoption, churn spikes) reveal a pattern but the team lacks qualitative understanding of why users behave that way
- When a feature redesign is proposed and the PM needs to understand current user workflows, workarounds, and mental models before defining requirements
- When stakeholders disagree about user priorities and the team needs direct evidence to resolve the debate and align on what to build
- When entering a new market segment where the team has no prior user exposure and must build foundational persona knowledge from scratch

## Workflow
1. **Define the research objective**: Articulate the specific question the research must answer. Frame it as a decision the team needs to make — e.g., "Should we invest in workflow X or workflow Y?" or "What prevents trial users from reaching activation?" Scope the research to one objective per study to maintain focus. Deliverable: research brief containing the objective, the decision it informs, target participant profile, and timeline.

2. **Design the interview guide**: Write a semi-structured interview guide with 8-12 open-ended questions. Start with context-setting questions about the participant's role and environment. Progress to behaviour questions ("Walk me through the last time you...") before exploring pain points and unmet needs. Avoid leading questions that suggest a desired answer. Include 2-3 follow-up probes per question to dig deeper when participants give surface-level responses. Deliverable: interview guide with questions, probes, and estimated timing per section.

3. **Recruit participants**: Identify participants who match the target profile. Source from existing customers, trial users, churned accounts, or prospect lists depending on the research objective. Aim for 5-8 participants — enough to identify patterns without diminishing returns. Screen candidates with a short qualifying questionnaire to confirm they match the profile. Deliverable: confirmed participant list with scheduled interview slots and screening responses.

4. **Conduct the interviews**: Run each interview for 30-45 minutes. Follow the guide but adapt to follow unexpected threads when they are relevant to the objective. Take structured notes during the session — capture direct quotes, observed emotions, and described behaviours separately from your own interpretations. Record sessions (with consent) for later reference. Ask the participant to demonstrate their current workflow when possible rather than relying solely on their verbal description. Deliverable: raw interview notes per participant with timestamped quotes, behavioural observations, and workflow descriptions.

5. **Analyse and code the data**: Review all interview notes and identify recurring themes. Use affinity mapping to cluster related observations. Tag each observation with a theme label and frequency count across participants. Distinguish between stated preferences (what users say they want) and revealed behaviours (what users actually do) — weight the latter more heavily. Identify contradictions between participants and note where opinions diverge by segment or role. Deliverable: affinity map with theme clusters, frequency counts, and a divergence log noting where findings split across participant segments.

6. **Synthesise into insights**: Translate themes into actionable product insights. Each insight must follow the structure: "We observed [behaviour/pattern] because [underlying motivation]. This means we should [product implication]." Rank insights by frequency and impact. Connect each insight back to the original research objective and the decision it informs. Deliverable: insight report containing 3-7 ranked insights, supporting evidence (participant quotes and observation counts), and a recommendation for the product decision the research was designed to inform.

7. **Present and distribute findings**: Walk the product team, engineering, and design through the insight report. Use direct participant quotes to ground abstract findings in real user language. Explicitly state what the research suggests the team should do next — build, pivot, investigate further, or deprioritise. Archive the research artifacts (guide, notes, recordings, report) for future reference. Deliverable: presentation delivered to stakeholders, insight report shared in the team's knowledge base, and research artifacts archived.

## Anti-Patterns
- **Leading questions**: Asking "Don't you think feature X would solve your problem?" instead of "How do you handle this situation today?" *Why*: Leading questions produce confirmation bias — participants agree with the suggested answer rather than revealing their actual behaviour, making the research useless for decision-making.

- **Recruiting convenience participants**: Interviewing internal colleagues, friends, or the most responsive customers instead of users who match the target profile. *Why*: Convenience samples skew findings toward power users or sympathetic respondents, missing the behaviours and pain points of the actual target segment.

- **Premature solutioning during interviews**: Pitching product ideas mid-interview and asking participants to evaluate them. *Why*: This shifts the conversation from understanding the problem space to gathering opinions about a solution, which is a different research method (concept testing) requiring a different study design.

- **Ignoring disconfirming evidence**: Dropping findings that contradict the team's hypothesis or preferred direction. *Why*: Selective reporting turns research into a rubber-stamp exercise and eliminates its value as an independent check on assumptions.

- **Over-generalising from small samples**: Treating a single participant's strong opinion as representative of the entire user base. *Why*: One person's frustration may be idiosyncratic rather than systemic. Patterns require corroboration across multiple participants before they warrant product action.

- **Research without a decision**: Conducting interviews "to learn more" without a specific product decision the findings will inform. *Why*: Undirected research produces interesting but non-actionable observations that sit in a document and change nothing, wasting both team and participant time.

## Output
**On success**: A user research insight report containing 3-7 ranked insights (each with observed behaviour, underlying motivation, and product implication), supporting evidence drawn from 5-8 participant interviews, an affinity map showing theme clusters, and a clear recommendation for the product decision the study was designed to inform — archived alongside the interview guide, raw notes, and recordings for future reference.

**On failure**: Report which research activities could not be completed (insufficient participant recruitment, cancelled interviews, too few participants to identify patterns), what data was collected, preliminary observations from whatever interviews did occur, and recommend specific actions to recover — such as expanding the recruitment pool, adjusting the participant profile criteria, extending the study timeline, or pivoting to a lightweight survey to supplement the incomplete interview data.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
