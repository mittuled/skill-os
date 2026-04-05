# Framework: developer-gtm-planner

Defines the developer adoption funnel, channel selection model, activation experience design, and GTM metrics framework for launching and scaling developer products.

## Developer Adoption Funnel

| Stage | Definition | Key Question | Primary Metric | Conversion Benchmark |
|-------|-----------|-------------|---------------|---------------------|
| Discover | Developer encounters the product | "Have they heard of us?" | Brand awareness (surveys) | — |
| Evaluate | Developer reads docs, watches demo, visits pricing | "Will they try it?" | Docs page views, quickstart starts | 20–40% of discoverers |
| Integrate | Developer makes first successful API call | "Can they get a win?" | TTFHW, activation rate | 30–60% of evaluators |
| Build | Developer integrates into a real project or product | "Is it useful in practice?" | Weekly API calls, project creation | 30–50% of integrators |
| Scale | Developer expands usage, adds teammates, or upgrades | "Do they commit?" | MAU, expansion revenue, team seats | 20–40% of builders |
| Advocate | Developer recommends, speaks, writes, contributes | "Do they multiply us?" | Referrals, content, contributions | 1–5% of scaled users |

## Developer Persona Framework

For each target persona, define:

| Dimension | Questions | Example |
|-----------|---------|---------|
| Role | Job title, seniority, team context | "Backend engineer at a seed-stage startup" |
| Tech stack | Primary languages, frameworks, cloud | "Python, FastAPI, AWS Lambda" |
| Motivation | What problem are they solving? | "Need to add payments without rebuilding checkout" |
| Watering holes | Where they learn, ask questions, build reputation | "Hacker News, r/Python, PyCon talks" |
| Decision factor | What makes them choose or reject a tool | "SDK quality, docs completeness, community activity" |
| Blocker | What stops them from integrating? | "Enterprise security review, budget approval" |

## Channel Selection Matrix

Score each channel 1–5 on persona fit and scalability. Select top 3–4 channels for initial GTM.

| Channel | Persona Fit | Scalability | Time to Impact | Best Maturity Stage |
|---------|------------|------------|---------------|---------------------|
| Developer blog / tutorials | All developers | Very high | 3–6 months | Early (awareness) |
| Conference talks (DevConf, KubeCon, etc.) | Senior devs, decision-makers | Low | 6–12 months | Growth (credibility) |
| Hackathons | Hobbyists, students, early adopters | Medium | 1–3 months | Early (adoption spike) |
| Open-source project / GitHub presence | Technical contributors | Very high | 6–18 months | All stages |
| Developer newsletter | Subscribed / retained users | High | 2–4 months | Growth (retention) |
| Paid search (Google, Stack Overflow) | High-intent searchers | High | 1–2 months | Scale (demand capture) |
| Developer influencers / advocates | Community followers | Medium | 1–3 months | Growth (trust amplification) |
| Product-led growth (free tier, sandbox) | Self-serve evaluators | Very high | Immediate | All stages |
| Partnerships / platform marketplaces | Ecosystem developers | Medium | 3–9 months | Scale (distribution) |

## Activation Experience Design Principles

| Principle | Standard | Why |
|-----------|----------|-----|
| TTFHW target | < 10 minutes for new developer | Every extra minute reduces conversion by ~5% |
| Self-serve default | No sales contact required for basic integration | Developers expect autonomy; gating creates immediate rejection |
| Sandbox before signup | Try the API before creating account | Reduces the commitment barrier for evaluation |
| Language-native SDKs | SDK in top 3 languages of target personas | Developers integrate in their language; HTTP-only increases friction |
| First-run email sequence | 3-email onboarding over 7 days | 40–60% of sign-ups who do not activate in first 24h never return without prompting |

## GTM Metrics Framework

| Funnel Stage | KPI | Leading Indicator | Target |
|-------------|-----|------------------|--------|
| Discover | Monthly website visits (developer pages) | SEO impressions | [Set by team] |
| Evaluate | Quickstart page visits | Docs bounce rate | — |
| Integrate | Activation rate (first API call) | Sandbox starts | > 30% within 7 days |
| Build | Weekly Active Developers (WAD) | API call frequency | [Set by team] |
| Scale | Monthly Active Developers (MAD) | Team seat additions | MoM growth > 10% |
| Advocate | Developer-sourced signups | Referral link clicks | > 15% of new signups |

## Developer GTM Anti-Patterns Checklist

Use this as a pre-launch gate:

- [ ] Product experience validated before driving traffic (DX review grade B or above)
- [ ] No gated content or mandatory demo for self-serve tier
- [ ] TTFHW measured and < 15 minutes
- [ ] Activation email sequence configured
- [ ] Community channel (Discord/Slack/forum) live and moderated before launch
- [ ] SDK in at least one primary target language available at launch
- [ ] Measurement stack in place (activation event tracked in analytics)
