# Skill OS — Operating Philosophy

We believe work agents should produce output indistinguishable from
the best human practitioners in each domain. Not adequate output.
Not technically correct output. Excellent output — the kind that
makes a hiring manager nod and say "this person gets it."

## Principles

1. **Depth over breadth**: A skill that does one thing with genuine
   domain expertise is worth more than ten skills that skim the surface.
   Every workflow step, every anti-pattern, every output template should
   reflect how the best practitioners actually work — not how a
   generalist imagines they work. Research before writing. Cite
   frameworks. Name the tradeoffs.

2. **Explain the why, not just the what**: Today's AI agents are smart.
   They have theory of mind. A skill that explains *why* a step matters
   enables the agent to generalize to novel situations. A skill that
   only lists rules produces brittle, pattern-matched output. Reasoning
   scales. Rules don't.

3. **Completeness is cheap, incompleteness is expensive**: When an AI
   agent executes a skill, the marginal cost of being thorough is near
   zero. The cost of missing a step — a forgotten compliance check, an
   overlooked stakeholder, an unhandled failure mode — compounds into
   real damage. Define the success case *and* the failure case. Document
   what to do *and* what to avoid. Cover the workflow *and* the edge
   cases.

4. **Opinionated over neutral**: Generic advice is noise. "Consider
   stakeholder alignment" is useless. "Schedule a 15-minute pre-read
   with the engineering lead 48 hours before the review because cold
   reviews waste everyone's time" is actionable. Every ethos profile,
   every workflow, every anti-pattern should take a stance. If two
   reasonable people could disagree, pick the better position and
   explain why.

5. **Lean bodies, deep references**: Not every consumer runs a large
   model. Skill bodies stay within strict word limits (500/1,000/1,500)
   so they fit in any context window. Depth lives in references,
   examples, scripts, and assets — loaded on demand, not forced into
   every invocation. Progressive disclosure respects both the user's
   attention and the model's capacity.

6. **Continuously improving**: No skill is ever finished. The first
   enrichment is v1.0.0, not the final version. Domain expertise
   deepens, best practices evolve, anti-patterns emerge from real usage.
   Every skill should get better over time through iteration, feedback,
   and testing against real prompts.

## Decision Priorities

When facing a tradeoff, prioritize in this order:

1. **Correctness** over speed — wrong output erodes trust permanently
2. **Domain accuracy** over generic coverage — one excellent skill beats five mediocre ones
3. **Actionability** over comprehensiveness — a practitioner should be able to act on every sentence
4. **Clarity** over completeness — if you can't say it within the word limit, split the skill
