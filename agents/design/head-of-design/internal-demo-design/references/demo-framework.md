# Internal Design Demo Framework

A guide for structuring and facilitating internal design showcases that generate useful feedback and build stakeholder alignment.

---

## Core Methodology

An effective internal design demo answers three questions for every attendee:
1. **Why does this problem matter?** (problem context)
2. **What did we design and why?** (design rationale)
3. **What do we need from you?** (focused ask)

Without all three, demos produce unfocused feedback or passive observation.

---

## Demo Types

| Type | Purpose | Fidelity | Duration |
|------|---------|---------|---------|
| Concept exploration | Align on direction before committing to production | Lo-fi (sketches, wireframes) | 20–30 min |
| Design direction review | Get buy-in on the visual and interaction direction | Mid-fi (styled wireframes, mid-fidelity prototype) | 30–45 min |
| Milestone showcase | Share progress on an ongoing initiative | Hi-fi (production-ready frames) | 45–60 min |
| Design system update | Share new components or pattern changes | Component demos in Figma | 15–30 min |
| Post-launch retro share | Share what shipped and what we learned | Production screenshots + data | 20–30 min |

---

## Demo Narrative Structure

### 1. Problem Context (5 min)
- User problem statement: who is affected, what they struggle with, and evidence for the problem
- Constraints: what the team was working within (technical, scope, timeline)
- Success criteria: what "solved" looks like

### 2. Design Walkthrough (15–30 min)
- Primary user flow first (happy path)
- Key decisions: where the team made a choice and why
- Trade-offs considered and discarded
- Edge cases and error states (if relevant to the demo)

### 3. Open Questions (5–10 min)
- 3 or fewer specific questions for the audience
- Distinguish: directional questions ("Should we go with Option A or B?") vs. input questions ("Does this match your mental model?")
- Avoid fishing for general approval

### 4. Feedback Collection (10 min)
- Designate a note-taker
- Capture feedback against the open questions first
- Allow spontaneous feedback after structured questions
- Distinguish: actionable feedback (will change the design) vs. logged feedback (noted but not actioned now)

---

## Prototype Fidelity Guide

| Demo Goal | Recommended Fidelity | What to Include |
|-----------|---------------------|-----------------|
| Concept validation | Lo-fi (grey-box) | Flow logic, content structure, user steps |
| Interaction validation | Mid-fi (clickable prototype) | Key interactions, transitions, state changes |
| Stakeholder alignment | Hi-fi (production design) | Visual polish, real content, all states |
| Engineering handoff preview | Hi-fi + annotations | Specs, tokens, interaction notes |

**Rule:** Use the minimum fidelity that answers the demo's objective. Higher fidelity signals finality and suppresses early-stage feedback.

---

## Feedback Collection Format

Use this structure to capture feedback during the session:

| # | Feedback Item | Source (name/role) | Type | Screen / Element | Action |
|---|--------------|-------------------|------|-----------------|--------|
| 1 | | | Direction / Concern / Question / Praise | | Address now / Log for later / No action |

**Feedback types:**
- **Direction** — Shapes a design decision (act on it)
- **Concern** — Flags a potential issue (investigate)
- **Question** — Requires clarification (answer and document)
- **Praise** — Confirms what's working (preserve it)

---

## Demo Preparation Checklist

- [ ] Demo brief written: objectives, audience, what alignment is needed
- [ ] Narrative structured: problem → rationale → open questions
- [ ] Prototype or walkthrough tested end-to-end (no dead ends)
- [ ] Realistic content in prototype (no lorem ipsum)
- [ ] Speaker notes prepared for each key decision point
- [ ] Note-taker assigned
- [ ] Feedback capture format ready (note-taking doc or whiteboard)
- [ ] Recording enabled (if appropriate)
- [ ] Invite sent with context: what attendees should come prepared to evaluate

---

## Post-Demo Synthesis

Within 24 hours:
1. Compile feedback notes into themes
2. Categorise each item: act now / log for later / no action
3. Identify action items with owners and due dates
4. Distribute demo summary to all attendees and design team
5. Update Figma or project management tool with action items
