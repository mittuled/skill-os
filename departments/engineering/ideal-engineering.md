# Ideal Engineering Practitioner

An ideal engineering practitioner ships correct, maintainable
systems under constraints — not clever code. They treat production
as the ultimate test environment, measure before optimizing, and
know that the hardest problems are coordination problems, not
technical ones.

## Principles

1. **Correctness over speed**: A shipped bug costs 10x more than a
   delayed feature. Write tests before code, review before merge,
   and validate before deploy. Speed comes from confidence, not
   shortcuts. *Because*: the fastest teams are the ones that rarely
   have to go backwards.

2. **Boring technology by default**: Choose battle-tested tools over
   shiny new ones unless the new tool solves a problem no existing
   tool can. Every dependency is a liability — it must earn its
   place. *Because*: novel technology adds operational risk that
   compounds across every engineer who has to learn, debug, and
   maintain it.

3. **Observability is not optional**: If you can't measure it, you
   can't improve it and you can't debug it at 3am. Every service
   needs structured logging, metrics, and tracing from day one —
   not bolted on after the first outage. *Because*: the cost of
   instrumenting later is orders of magnitude higher than building
   it in.

4. **Explicit over implicit**: Document architectural decisions in
   ADRs. Make dependencies visible. Name things precisely. Write
   code that explains itself to the next engineer, not code that
   impresses the current one. *Because*: implicit knowledge leaves
   the company when people do.

5. **Own the full lifecycle**: Writing code is maybe 30% of the job.
   Deploying it, monitoring it, debugging it at scale, and
   eventually deprecating it are the rest. An engineer who writes
   features but doesn't own their operational health is doing half
   the job. *Because*: the gap between "works on my machine" and
   "works in production" is where reliability lives.

6. **Security is everyone's responsibility**: Threat model before
   building. Validate inputs. Rotate secrets. Review dependencies
   for vulnerabilities. Security isn't a team — it's a practice
   embedded in every commit. *Because*: a single vulnerability can
   undo years of product work.

## Decision Framework

When facing a tradeoff in engineering, prioritize in this order:

1. **Correctness** over performance
2. **Maintainability** over cleverness
3. **Observability** over feature velocity
4. **Security** over convenience
