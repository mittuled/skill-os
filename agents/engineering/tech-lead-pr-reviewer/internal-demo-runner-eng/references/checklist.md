# Checklist: internal-demo-runner-eng

Ensures internal engineering demos are prepared, executed, and followed up consistently to generate actionable stakeholder feedback.

## Pre-Demo Preparation (Day Before)

### Environment
- [ ] Demo environment deployed with the current release build (not local dev)
- [ ] Demo environment smoke-tested: confirm all features to be shown are working
- [ ] Fallback plan documented: if live demo breaks, have screenshots or recording ready
- [ ] Test data seeded: realistic data in place that makes the demo coherent (not "test user 1", "fake company")
- [ ] Environment access confirmed for all presenters

### Script
- [ ] Demo script written: ordered list of features to show, with the expected talking point for each
- [ ] Happy path and at least one edge case per feature included in the script
- [ ] Time estimate: allocate ~2 minutes per feature; total demo should not exceed 30 minutes including Q&A
- [ ] Presenter assigned for each section (one presenter per workstream: BE, FE, if applicable)
- [ ] Demo script shared with all presenters 24 hours in advance

### Invitees
- [ ] Stakeholder list confirmed: product, design, engineering leadership, and any customer success / sales if applicable
- [ ] Calendar invite sent with agenda and link to the demo environment
- [ ] Recording tool configured (Loom, Zoom record, or equivalent)

## During the Demo

### Opening (2 minutes)
- [ ] State the sprint or milestone this demo covers
- [ ] State what will and will NOT be shown (set expectations explicitly)
- [ ] Start recording before any feature is shown

### Feature Demonstration
- [ ] Follow the script — do not free-style unless explicitly adding a stakeholder-requested item
- [ ] Show each feature in a working, deployed environment — not mockups or local builds
- [ ] Call out edge cases and error states, not just happy paths
- [ ] Leave 1 minute for questions after each major feature section

### Feedback Collection
- [ ] Designate a note-taker (separate from the presenter)
- [ ] Capture every piece of feedback verbatim or in close paraphrase — not summarized in the moment
- [ ] For each feedback item, ask: "Is this a bug, a UX change, or a new feature request?" before moving on
- [ ] If a feedback item is out of scope, state explicitly: "That's logged — it's out of scope for this sprint and will go to the backlog"

## Post-Demo (Same Day)

### Feedback Processing
- [ ] Raw feedback notes exported from the session
- [ ] Each feedback item categorized: Bug / Usability Issue / Missing Feature / Enhancement / Out of Scope
- [ ] Each item added to the project management tool with appropriate category label
- [ ] Bugs and missing-feature items flagged for triage in the next backlog grooming session
- [ ] Demo recording uploaded and shared with absent stakeholders (link in project channel)

### Follow-Up Communication
- [ ] Summary message sent to all invitees within 24 hours:
  - What was demoed
  - Key feedback items received
  - Which items are being actioned and in which sprint
  - Items that are out of scope (with brief rationale)
- [ ] Any blocking feedback that changes sprint priorities escalated to the tech lead and PM immediately

## Demo Quality Standards

| Condition | Action |
|-----------|--------|
| Environment is broken at demo start | Show pre-recorded walkthrough; reschedule live demo within 48h |
| Presenter goes over time (> 5 min past schedule) | Cut to Q&A; defer remaining features to async recording |
| Stakeholder raises out-of-scope scope creep as a blocker | Log it; state it requires change control; do not commit to it in the session |
| Feedback volume is very high (> 20 items) | Triage immediately after demo; categorize before the session closes |
