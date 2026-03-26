---
name: backlog-populator
description: >
  This skill converts validated requirements, discovery insights, and stakeholder requests into prioritised backlog items with enough structure to enter grooming. Use when new feature requests, customer feedback, or strategic initiatives need to become trackable work items. Also consider after a discovery cycle produces validated opportunities or when a roadmap update introduces new themes. Suggest when the backlog depth falls below two sprints of capacity.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - backlog-groomer
  - requirements-extractor
  - jtbd-to-stories
  - roadmap-placer
---

# backlog-populator

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
The backlog populator converts validated requirements, discovery outputs, and stakeholder requests into structured backlog items -- epics, stories, or enablers -- with initial RICE scores, acceptance-criteria stubs, and traceability back to the originating source. It keeps the backlog deep enough that grooming always has a pipeline of candidate work.

## When to Use
- A customer discovery cycle or demand validation round has produced confirmed opportunities that need to become work items.
- The product roadmap has been updated and new themes or initiatives require decomposition into epics and stories.
- The backlog depth drops below two sprints of estimated capacity, risking a planning gap.
- Stakeholders submit ad-hoc requests via intake channels (Slack, email, support escalation) that need triage into the backlog.
- A post-mortem or retrospective surfaces improvement items that should be tracked as stories.

## Workflow
1. Collect inputs: validated discovery findings, requirements documents, roadmap themes, and raw stakeholder requests.
2. For each input, determine the appropriate backlog level -- epic, story, or enabler -- based on scope.
3. Draft each item with a title, one-line summary, initial acceptance-criteria stub, and source link for traceability.
4. Assign a preliminary RICE score using available reach and impact data; mark Confidence as low where data is thin.
5. Tag each item with the relevant epic, product area, and any known dependency labels.
6. Deduplicate against existing backlog items; merge or link where overlap is found.
7. Insert items into the backlog at the position implied by their RICE rank.
8. Notify the backlog groomer that new items are queued for refinement.

## Anti-Patterns
- **Populating without source traceability.** Creating stories that cannot be traced back to a customer need or strategic initiative makes prioritisation arbitrary. *Why: items without provenance resist meaningful RICE scoring and become backlog noise.*
- **Over-specifying at population time.** Writing full acceptance criteria and edge cases before grooming duplicates effort and discourages engineering collaboration. *Why: population provides structure; grooming provides precision.*
- **Treating every request as a story.** Dumping unfiltered requests into the backlog without decomposition inflates item count and obscures real priorities. *Why: a cluttered backlog degrades grooming velocity and planning accuracy.*
- **Skipping deduplication.** Adding items without checking for overlap creates duplicate work and split context. *Why: engineers may unknowingly work on the same problem from two different tickets.*

## Output

**Success:**
- New backlog items with titles, summaries, acceptance-criteria stubs, RICE scores, and source links inserted at the correct priority position.
- The groomer is notified and the backlog depth is at or above two sprints of capacity.

**Failure:**
- Items are added without source links or RICE scores, making downstream prioritisation unreliable.
- Duplicates are introduced, causing confusion during grooming or sprint planning.

## Related Skills
- `backlog-groomer` -- refines and estimates the items this skill creates.
- `requirements-extractor` -- produces the validated requirements that feed population.
- `jtbd-to-stories` -- translates Jobs-to-be-Done into story-level items for the backlog.
- `roadmap-placer` -- determines which roadmap theme a new backlog item belongs to.
