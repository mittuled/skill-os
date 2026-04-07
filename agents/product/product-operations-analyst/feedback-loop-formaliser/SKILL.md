---
name: feedback-loop-formaliser
description: >
  This skill formalises the feedback loop between customers, support, and product to ensure signals drive action.
  Use when feedback from customers or support reaches product inconsistently or gets lost between teams.
  Also consider when the team suspects valuable signal is being collected but never acted upon.
  Suggest when multiple teams mention hearing the same customer complaint but no one owns routing it to product.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills: []
---

# feedback-loop-formaliser

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Formalises the feedback loop between customers, support, and product to ensure signals drive action.

## When to Use
- When customer feedback reaches product inconsistently — some through Slack, some through tickets, some through sales calls, with no unified flow
- When the support team escalates issues ad hoc and product lacks a structured intake process
- When the product team makes roadmap decisions without systematic access to customer signal
- When a feedback process exists on paper but compliance is low and signal leaks are frequent

## Workflow
1. **Map existing feedback channels**: Inventory every path feedback currently travels — support tickets, NPS surveys, sales call notes, CS check-ins, social media, in-app feedback widgets, direct emails. For each channel, identify who collects, who routes, and where it lands. Deliverable: feedback channel inventory with source, collector, router, and destination for each.
2. **Identify signal leaks**: Find where feedback drops — channels with no routing, routing with no destination, destinations with no owner. Quantify the gap where possible (e.g., "40% of support tickets tagged 'feature request' have no product visibility"). Deliverable: signal leak report with gap descriptions and estimated volume lost.
3. **Design the formalised loop**: Define the standard flow from feedback collection through categorisation, routing, acknowledgement, and action tracking. Assign ownership at each stage. Specify SLAs for routing (e.g., product-relevant tickets routed within 24 hours) and acknowledgement (e.g., feedback submitter notified of status within 5 business days). Deliverable: feedback loop process document with stages, owners, SLAs, and tooling requirements.
4. **Define categorisation taxonomy**: Create a shared vocabulary for feedback types — bug report, feature request, usability issue, performance complaint, billing question, praise. Map each category to the appropriate product team or backlog. Deliverable: categorisation taxonomy with routing rules per category.
5. **Establish the closure mechanism**: Define how feedback submitters (customers, support agents, sales reps) learn what happened with their feedback — status updates, release notes referencing the feedback, or direct follow-up. Deliverable: closure process with templates and triggers for each feedback category.
6. **Launch and monitor compliance**: Roll out the formalised loop with the relevant teams. Track adoption of the new process — percentage of feedback routed through the formal channel, SLA adherence, and closure rate. Deliverable: compliance dashboard or periodic compliance report.

## Anti-Patterns
- **Building the process without input from support and sales**: Designing routing rules that do not reflect how frontline teams actually work. *Why*: A feedback loop that ignores the workflow of the people who collect feedback will not be adopted, regardless of how well-designed it is.
- **Over-engineering categorisation**: Creating a taxonomy with 30+ categories that requires training to use correctly. *Why*: Complex taxonomies reduce compliance — the simpler the categorisation, the more consistently it gets applied.
- **Collecting without closing the loop**: Routing feedback to product but never communicating back what happened. *Why*: Feedback submitters who never see outcomes stop submitting, and the loop atrophies from the collection end.

## Output
**On success**: A formalised feedback loop process document covering channel inventory, categorisation taxonomy, routing rules with SLAs, closure mechanisms, and a compliance tracking plan — adopted by support, sales, CS, and product teams.
**On failure**: Report which teams or channels could not be integrated (e.g., sales team uses a CRM with no API, support tool lacks tagging capability), what partial process was designed, and recommend workarounds or tooling changes to close the gaps.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
