---
name: customer-discovery-planner
description: >
  This skill designs end-to-end customer discovery programs -- from hypothesis framing through participant recruitment, discussion-guide authoring, session facilitation logistics, and synthesis methodology. Use when a new product area, feature bet, or market expansion requires direct evidence of customer needs before committing engineering resources. Also consider when existing usage data is ambiguous, NPS commentary flags unmet needs, or a pivot is under evaluation. Suggest when the team is about to invest more than one sprint of effort in a direction that lacks primary customer evidence.
department: product
agent: product-manager
version: 1.0.0
complexity: complex
related-skills:
  - demand-validator
  - user-researcher
  - requirements-extractor
  - jtbd-to-stories
  - market-sizer
---

# customer-discovery-planner

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
The customer discovery planner designs structured programs that surface real customer problems, validate or invalidate product hypotheses, and produce actionable insight artifacts that feed downstream requirements extraction and backlog population. It orchestrates participant selection criteria, discussion-guide design, session logistics, bias-mitigation protocols, and synthesis frameworks so that discovery yields decision-grade evidence rather than anecdotal noise. The skill operates at the program level -- planning a cohesive series of sessions around a central hypothesis -- not at the level of a single ad-hoc interview.

## When to Use
- A new product initiative or feature bet exceeding one sprint of engineering effort lacks primary customer evidence.
- Quantitative usage data (funnels, retention curves, feature adoption) is ambiguous and cannot distinguish between competing explanations.
- NPS verbatims, support tickets, or churn interviews surface a recurring theme that has not been systematically explored.
- The team is evaluating a market expansion, new persona, or pricing change and needs to understand buyer/user motivations before modelling demand.
- A strategic pivot is under consideration and leadership requires structured customer evidence to support or reject the direction.
- Post-launch adoption is below forecast and the root cause is not clear from telemetry alone.

## Workflow
1. **Frame the hypothesis.** Articulate the core assumption to validate or invalidate in a single falsifiable statement (e.g., "Mid-market ops managers spend >3 hours/week reconciling vendor invoices manually").
2. **Define the learning objectives.** List 3-5 specific questions the discovery program must answer. Each objective maps to a decision the team will make with the evidence (build, defer, pivot, or kill).
3. **Design the participant profile.** Specify the target persona, firmographic/demographic filters, and screening criteria. Include inclusion and exclusion rules to avoid sampling bias (e.g., exclude users who participated in the last discovery cycle within 90 days).
4. **Determine the session format.** Choose between one-on-one interviews, paired interviews, contextual inquiry, diary studies, or focus groups based on the learning objectives. Justify the format choice in the plan.
5. **Set the sample size.** Use saturation-based reasoning: plan for 8-12 sessions per persona segment, with a checkpoint after 5 to assess whether new themes are still emerging.
6. **Author the discussion guide.** Structure the guide in three acts:
   - Act 1 (Context): open-ended questions about the participant's current workflow, tools, and pain points -- no leading questions.
   - Act 2 (Exploration): deeper probes on the hypothesis area, including "show me how you do X today" tasks for contextual inquiry.
   - Act 3 (Reaction): concept or prototype exposure (if applicable), capturing first impressions, perceived value, and willingness-to-pay signals.
   Include facilitator notes on when to probe deeper and when to move on. Avoid confirmation-biased phrasing.
7. **Plan recruitment logistics.** Identify recruitment channels (customer success introductions, panel providers, in-app intercepts), draft the outreach message, set the incentive structure, and establish a scheduling cadence that avoids participant fatigue.
8. **Define the synthesis methodology.** Specify how raw session notes will be coded:
   - Affinity-mapping for qualitative themes.
   - Jobs-to-be-Done (JTBD) framework for structuring unmet needs.
   - Frequency and intensity scoring per theme to enable prioritisation.
   Assign synthesis roles (note-taker, coder, reviewer) and set the turnaround target.
9. **Establish bias-mitigation controls.** Document at least three safeguards: interviewer rotation, blind coding of transcripts, and a pre-mortem on the hypothesis to surface team assumptions that could colour interpretation.
10. **Build the timeline.** Map recruitment, sessions, synthesis, and readout to calendar weeks. Include buffer for recruitment shortfalls (plan to invite 2x the target to account for no-shows).
11. **Define the readout format.** Specify the deliverable: a discovery brief containing the hypothesis verdict (validated / invalidated / inconclusive), top themes ranked by frequency and intensity, JTBD cards, and recommended next steps (proceed to demand validation, iterate the hypothesis, or abandon).
12. **Distribute the plan for review.** Share with the user-researcher for methodology feedback, the requirements-extractor for downstream readiness, and the product lead for alignment on learning objectives.

## Anti-Patterns
- **Leading questions in the discussion guide.** Phrasing like "Would you find it useful if we..." primes participants toward confirmation and produces unreliable signal. *Why: discovery exists to challenge assumptions, not to collect agreement. Leading questions yield false positives that misallocate engineering investment.*
- **Convenience sampling.** Recruiting only from the existing power-user cohort skips the segments where the product is weakest and most needs insight. *Why: power users have already self-selected; their needs may not represent the addressable market.*
- **Skipping the hypothesis statement.** Running discovery without a falsifiable hypothesis turns sessions into open-ended conversations with no decision criteria. *Why: without a clear hypothesis, synthesis has no anchor and the readout degrades into a theme dump that does not drive action.*
- **Single-interviewer, single-coder pipeline.** Having the same person facilitate, take notes, and code themes introduces unchecked bias at every stage. *Why: role separation is the primary control against interpretation drift.*
- **Treating discovery as a one-shot event.** Running a single round and declaring the hypothesis validated ignores the iterative nature of discovery. *Why: early sessions refine the questions; later sessions test the refined understanding. Cutting short forfeits the compounding insight.*
- **Over-indexing on sample size over saturation.** Scheduling 30 sessions when themes converge at session 8 wastes participant goodwill and calendar time. *Why: saturation, not sample size, determines evidence quality in qualitative research.*

## Output

**Success:**
- A complete discovery plan document containing: falsifiable hypothesis, learning objectives, participant profile with screening criteria, discussion guide (three-act structure), recruitment plan with channels and incentives, synthesis methodology with role assignments, bias-mitigation controls, timeline, and readout format.
- Stakeholder sign-off on learning objectives and timeline before recruitment begins.
- A clear decision framework: what evidence would validate, invalidate, or leave the hypothesis inconclusive.

**Failure:**
- The plan lacks a falsifiable hypothesis, making synthesis directionless and the readout non-actionable.
- Recruitment criteria are too narrow or too broad, producing a participant pool that does not represent the target persona.
- The discussion guide contains leading questions, compromising data integrity and yielding false confidence.
- No synthesis methodology is defined, causing raw notes to sit unprocessed and discovery investment to go unrealised.

## Related Skills
- `demand-validator` -- takes discovery findings and tests whether quantitative demand supports the qualitative signal.
- `user-researcher` -- collaborates on methodology design and may co-facilitate sessions.
- `requirements-extractor` -- consumes the discovery brief to produce structured requirements.
- `jtbd-to-stories` -- translates the JTBD cards from synthesis into backlog-ready user stories.
- `market-sizer` -- provides TAM/SAM/SOM context that shapes participant profile and hypothesis scope.
