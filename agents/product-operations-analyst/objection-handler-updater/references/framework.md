# Framework: Objection Handler Updates

## Core Model

An objection handler is a living sales enablement document that maps common buyer objections to evidence-backed responses. Updates are triggered by product changes, new competitive moves, or sales team feedback — and must be grounded in actual customer language, not marketing copy.

## Objection Categories

| Category | Definition | Update Trigger |
|----------|-----------|----------------|
| Feature gap | "Your product doesn't do X" | New feature ships that closes the gap |
| Competitor comparison | "Competitor Y does this better" | Competitor ships new capability; product ships differentiator |
| Price / value | "Too expensive for what it does" | Pricing change; new ROI data available |
| Trust / risk | "How do I know this will work for us?" | New case study; certification; SLA update |
| Technical / integration | "It won't integrate with our stack" | New integration shipped; API improvement |
| Timing | "We'll evaluate again next quarter" | Urgency trigger: new penalty for inaction; end-of-quarter pressure |

## Objection Handler Entry Format

Each handler entry must contain:

```
Objection: [Verbatim customer phrasing — use real language, not paraphrases]
Root concern: [The underlying fear driving the objection]
Response: [2-3 sentence response the rep delivers]
Proof point: [One piece of evidence: case study, data point, demo flow, or feature reference]
Competitor note: [If objection is competitive, name the competitor and the differentiation]
Last updated: [YYYY-MM-DD]
Owner: [Product / PMM / Sales]
```

## Update Process

1. **Identify the trigger**: Feature release, competitive shift, or sales feedback
2. **Collect affected objections**: Review the current handler for entries that are now outdated or newly addressable
3. **Draft updated responses**: Write in the rep's voice — assertive, specific, concise (never more than 3 sentences per response)
4. **Add proof points**: Every response must have a concrete proof point; remove entries that lack one
5. **Flag for removal**: Any objection that no longer applies (e.g., gap is closed) should be archived, not silently deleted
6. **Brief the sales team**: Post a summary of changes; do not make reps hunt for updates in a diff

## Response Quality Standards

A good response:
- Acknowledges the concern before refuting it ("That's a fair concern...")
- States the direct answer in the first sentence
- Provides one specific proof point (not "many customers")
- Ends with a forward move (demo offer, reference call, documentation link)

A bad response:
- Immediately becomes defensive
- Uses vague claims ("We're actually really good at this")
- Cites internal opinions instead of evidence
- Has no next step

## Update Frequency

| Event | Update Required |
|-------|----------------|
| Major feature release | Within 2 days of launch |
| Competitor product announcement | Within 5 business days |
| Sales reports new recurring objection (3+ reps) | Within 1 week |
| Quarterly review | Regardless of triggers — audit for staleness |
