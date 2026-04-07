# Research-to-Action Framework

## Purpose

A framework for ensuring research findings are systematically incorporated into product and design decisions — preventing the common pattern of research being produced but not acted upon.

## The Research-to-Action Chain

Research only has value when it influences a decision. Each link in the chain must be intact:

```
Evidence → Insight → Implication → Decision → Artefact → Shipped feature
```

| Link | Definition | Common Break Point |
|------|------------|-------------------|
| Evidence | Raw data from sessions, surveys, or analytics | Data collected but never analysed |
| Insight | Pattern distilled from evidence | Analysis done but insight not formulated clearly |
| Implication | What the insight means for design or product | Insight not translated into an actionable direction |
| Decision | What the team will do differently as a result | Implication discussed but no one commits to action |
| Artefact | Design change, updated spec, or new ticket | Decision made verbally but not recorded |
| Shipped feature | Change deployed to users | Artefact created but deprioritised out of scope |

## Feedback Loop System Design

A formalised feedback loop requires three components:

### 1. Input Standards
Define which feedback sources feed the system and in what format:

| Source | Collection Method | Review Cadence | Owner |
|--------|------------------|---------------|-------|
| User interview sessions | Synthesis report after each study | Per study | UX Researcher |
| Session recordings | Bi-weekly session analysis batch | Bi-weekly | Visual Interaction Designer |
| Support tickets | Weekly tag review in support tool | Weekly | Support + UX Researcher |
| NPS / CSAT surveys | Monthly theme extraction | Monthly | UX Researcher |
| In-app feedback | Weekly review | Weekly | UX Researcher |
| Sales call notes | Monthly synthesis | Monthly | UX Researcher + PM |

### 2. Processing Standards
Define how raw feedback becomes an actionable insight:

| Step | Standard | Tool |
|------|----------|------|
| Tagging | Every insight tagged with product area, user segment, and severity | [Research repo / Notion / Dovetail] |
| Pattern threshold | 3+ independent sources = strong signal; 1-2 = weak signal | Researcher judgment |
| Insight format | "We know [observation] because [evidence]. This means [implication]." | Standardised template |
| Priority classification | P0 (block ship) / P1 (must address) / P2 (consider) / P3 (backlog) | Based on severity + frequency |

### 3. Output Standards
Define how insights reach the teams that can act on them:

| Output | Format | Audience | Cadence |
|--------|--------|---------|--------|
| Insight brief (single finding) | 1-page summary with evidence + recommendation | PM + Designer | As needed |
| Research synthesis report | Full findings document | Design + Product + Engineering leads | Per study |
| Monthly research digest | Top 5 insights with action status | Leadership + cross-functional | Monthly |
| Research repository | Searchable archive of all findings | All teams | Always-on |

## Closing the Loop: Action Tracking

Research is only complete when the finding is either actioned or consciously deprioritised with a documented reason.

| Status | Definition |
|--------|------------|
| Open | Finding documented; no action taken yet |
| In progress | Action assigned and in sprint or backlog |
| Complete | Design or product change shipped |
| Closed — not actioned | Deprioritised with documented reason and revisit date |
| Superseded | Replaced by more recent or contradicting evidence |

Track every insight to one of these statuses. A finding that stays "Open" for more than 2 sprints is a system failure.

## Research Calendar Template

| Activity | Cadence | Owner | Output |
|----------|---------|-------|--------|
| Discovery research (interviews) | Quarterly or per initiative | UX Research Lead | Findings report |
| Session analysis | Bi-weekly | Visual Interaction Designer | Session analysis report |
| Usability test | Per major feature | UX Research Lead | Usability test report |
| Support ticket theme review | Weekly | UX Researcher | Insight brief if pattern found |
| Research digest | Monthly | UX Researcher | Digest sent to leadership |
| Research roadmap review | Quarterly | UX Research Lead + PM | Updated research calendar |

## Failure Mode Diagnostic

| Symptom | Root Cause | Fix |
|---------|-----------|-----|
| Research reports are produced but not referenced in design work | Findings not integrated into design brief format | Add a "Research Basis" section to all design briefs |
| The same user problems recur in session analysis | Action not taken after findings were surfaced | Add action tracking to all findings; review open items weekly |
| PM and Engineering teams say "we didn't know about this" | Distribution problem — findings not reaching decision-makers | Add PM and Engineering lead to all research readout invites |
| Research insights are lost when team members leave | No searchable repository | Invest in a research repository with tagging |
| Research feels like "extra work" to product team | Research not integrated into product planning cycle | Schedule research readout before each sprint planning |
