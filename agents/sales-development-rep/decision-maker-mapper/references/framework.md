# Framework: Buying Committee Mapping

This framework defines the buying committee roles, influence scoring methodology, multi-threading tactics, and common organizational patterns used by the decision-maker-mapper skill.

## Buying Committee Roles

### Economic Buyer

The person who controls the budget and has final sign-off authority. There is exactly one Economic Buyer per deal. They care about ROI, total cost of ownership, and strategic alignment. They may never attend a demo but will approve or reject the purchase order.

**Identification signals**: Budget line authority, signs contracts, mentioned in procurement workflows, C-suite or VP title in the relevant function.

**Engagement approach**: Executive-to-executive alignment. Lead with business outcomes, ROI projections, and risk mitigation. Never pitch features.

### User Buyer

The person (or group) who will use the product daily. They care about ease of use, workflow fit, and whether the product solves their specific pain. There can be multiple User Buyers.

**Identification signals**: Currently performing the job the product automates or augments, complains about the status quo in discovery calls, attends demos and asks detailed workflow questions.

**Engagement approach**: Hands-on demonstrations, proof-of-concept environments, testimonials from peers in similar roles.

### Technical Buyer

The person who evaluates whether the product meets technical requirements: security, compliance, integration, scalability. Often IT, InfoSec, or Engineering. They have veto power but rarely initiate purchases.

**Identification signals**: Asks about APIs, SSO, SOC2, data residency, SLAs. Reviews security questionnaires. Owns the technical evaluation checklist.

**Engagement approach**: Technical deep-dives, architecture diagrams, security documentation, sandbox environments. Respect their evaluation process — shortcuts trigger distrust.

### Coach

An internal ally who provides information about the organization's decision-making process, politics, and priorities. A Coach may not have buying authority but knows who does and how decisions get made.

**Identification signals**: Shares information about internal politics, timelines, competing priorities, or budget cycles. Often a former customer, conference connection, or someone who found you through content.

**Engagement approach**: Reciprocal value exchange. Provide them with insights they can use internally (industry benchmarks, competitive intel). Never put them in a position that risks their credibility.

### Champion

A stakeholder who actively advocates for your solution internally. Unlike a Coach, a Champion has influence and is willing to spend political capital to push the deal forward. The strongest deals have a Champion who is also a User Buyer or Technical Buyer.

**Identification signals**: Introduces you to other stakeholders, shares your materials internally, argues your case in meetings you are not in, asks "what do you need from me to move this forward?"

**Engagement approach**: Equip them with ammunition — ROI calculators, competitive battle cards, executive summaries, and objection-handling guides. Make their internal selling easy.

### Gatekeeper

A person who controls access to other stakeholders, often an executive assistant, procurement manager, or project coordinator. They do not make the decision but determine who gets in the room.

**Identification signals**: Manages calendars for the Economic Buyer, runs the procurement process, coordinates vendor evaluations, sends RFPs.

**Engagement approach**: Respect their role. Provide complete, well-formatted information on the first ask. Never try to go around them — they will block you permanently.

### Blocker

A stakeholder who is actively opposed to the purchase. They may prefer a competitor, fear the change, or have political reasons to maintain the status quo. Not every deal has a Blocker, but enterprise deals frequently do.

**Identification signals**: Raises objections that are not about product capability, advocates for a competitor or internal build, does not attend meetings when invited, provides negative feedback through back-channels.

**Engagement approach**: Do not confront directly. Understand their concerns through your Coach or Champion. Address root causes (fear of change, loss of control, competitor loyalty) indirectly through proof points and risk mitigation. If a Blocker has veto power and cannot be neutralized, escalate to the Economic Buyer with a business case.

## Influence Scoring Methodology

Score each stakeholder 1-5 based on three factors:

| Factor | Weight | 1 (Low) | 3 (Medium) | 5 (High) |
|--------|--------|---------|------------|----------|
| **Title Seniority** | 30% | Individual contributor | Director / Senior Manager | VP / C-suite |
| **Budget Authority** | 40% | No budget influence | Influences budget allocation | Owns budget line item |
| **Organizational Proximity** | 30% | Different department, no overlap | Adjacent team, occasional interaction | Same team as the problem owner |

**Composite Influence Score** = (Title x 0.3) + (Budget x 0.4) + (Proximity x 0.3), rounded to nearest integer.

### Interpretation

| Score | Label | Implication |
|-------|-------|-------------|
| 5 | Critical | Must be engaged — deal cannot close without their support |
| 4 | High | Should be engaged directly — significant influence on outcome |
| 3 | Medium | Worth engaging — can accelerate or slow the deal |
| 2 | Low | Monitor — limited influence but can provide intel |
| 1 | Minimal | Awareness only — no direct engagement needed |

## Multi-Threading Tactics

### Warm Introduction Path
Best for: reaching Economic Buyers and senior stakeholders.
Method: Ask your Champion or Coach to introduce you via email or in a meeting. Provide a pre-written blurb they can forward.
Success rate: Highest conversion — warm intros to senior stakeholders convert 3-5x better than cold outreach.

### Content-Based Outreach
Best for: engaging Technical Buyers and User Buyers who are in research mode.
Method: Share relevant case studies, white papers, or benchmark reports that address their specific concerns. Personalize the message to their role and industry.
Success rate: Moderate — works when the content directly addresses a known pain point.

### Event-Based Engagement
Best for: Gatekeepers and Blockers who are difficult to reach directly.
Method: Invite to a webinar, roundtable, or industry event where they can engage on neutral ground. Position as peer learning, not sales.
Success rate: Good for initial contact — low commitment ask makes it easier to accept.

### Executive Alignment
Best for: Economic Buyers in large enterprise deals.
Method: Arrange an executive-to-executive meeting between your leadership and theirs. Focus on strategic vision and partnership, not product features.
Success rate: High when well-timed — most effective after Champion has built internal momentum.

### LinkedIn Engagement Sequence
Best for: stakeholders where no warm path exists.
Method: Connect, engage with their content (thoughtful comments, not likes), share relevant insights, then request a brief conversation after establishing visibility.
Success rate: Low per-touch but builds familiarity over time — best for long-cycle deals.

## Common Org Chart Patterns by Company Size

### Startup (1-50 employees)
- Buying committee: 1-2 people, often CEO + Head of the relevant function
- Economic Buyer: Usually CEO or co-founder
- Decision speed: Days to weeks
- Key risk: Single point of failure — if one person says no, deal is dead
- Multi-threading strategy: Minimal — focus on finding the right 1-2 people

### Scale-up (50-500 employees)
- Buying committee: 3-5 people, typically VP + Director + team lead + IT
- Economic Buyer: VP of the function, sometimes CFO for larger deals
- Decision speed: Weeks to months
- Key risk: Emerging procurement processes that add friction mid-deal
- Multi-threading strategy: Engage the VP (Economic Buyer) and a Director-level Champion simultaneously. Loop in IT early to prevent Technical Buyer surprises.

### Mid-Market (500-5,000 employees)
- Buying committee: 5-8 people across 2-3 departments
- Economic Buyer: SVP or VP with budget authority, may need CFO approval above threshold
- Decision speed: 1-3 months
- Key risk: Cross-departmental politics and competing priorities
- Multi-threading strategy: Build Champions in each affected department. Map Gatekeepers early. Expect a formal evaluation process.

### Enterprise (5,000+ employees)
- Buying committee: 8-15+ people across multiple departments, regions, and layers
- Economic Buyer: C-suite or SVP, but budget may route through procurement and finance separately
- Decision speed: 3-12 months
- Key risk: Organizational complexity, procurement bureaucracy, Blockers in adjacent teams, executive sponsor changes
- Multi-threading strategy: Full committee mapping required. Identify and engage at least 3-5 stakeholders across roles. Maintain a Champion and a Coach at minimum. Plan for multiple rounds of internal selling. Expect security reviews, legal reviews, and procurement negotiations as separate workstreams.
