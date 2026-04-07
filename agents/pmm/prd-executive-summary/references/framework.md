# Framework: PRD Executive Summary

Reference framework for translating product specifications into market-oriented executive summaries.

## Executive Summary Structure

| Section | Purpose | Length | Audience Question It Answers |
|---------|---------|--------|---------------------------|
| Market Context | Why this initiative matters now | 2-3 sentences | "Why should I care?" |
| Solution Overview | What the product will do in buyer-centric language | 3-4 sentences | "What are we building and for whom?" |
| Expected Impact | Metrics and outcomes | 3-5 bullet points | "What will success look like?" |
| Key Risks | Top risks with mitigations | 2-3 bullet points | "What could go wrong?" |

Total length: under 500 words or one page.

## Language Translation Rules

The executive summary translates engineering language into leadership language:

| Engineering Language | Leadership Language |
|---------------------|-------------------|
| "Implement microservice architecture" | "Enable the platform to scale independently across product areas" |
| "Migrate to PostgreSQL 16" | "Improve data reliability and reduce infrastructure costs" |
| "Build OAuth 2.0 integration" | "Allow customers to connect their existing identity provider in one click" |
| "Refactor the billing pipeline" | "Eliminate billing errors that cause 15% of support tickets" |
| "Add WebSocket support" | "Enable real-time collaboration so teams can work together live" |

### Translation Principle
Replace the **how** (implementation) with the **why** (buyer outcome). Leadership approves initiatives based on strategic fit and market impact, not technical approach.

## Market Context Framing

The market context section must answer:

| Question | Good Example | Bad Example |
|----------|-------------|-------------|
| Why now? | "Three of our top five competitors launched AI features in Q1; buyers now expect this as table stakes" | "AI is trending" |
| Why us? | "Our data pipeline already processes the signals needed; we have a 6-month head start on training data" | "We should build AI too" |
| Why this scope? | "Win/loss data shows 40% of lost deals cite this gap; the proposed scope addresses the top two buyer objections" | "Customers want more features" |

## Impact Measurement Framework

| Metric Type | Example | Measurement Approach |
|-------------|---------|---------------------|
| Revenue impact | "Expected to generate $500K incremental ARR in first 12 months" | Pipeline tracking + closed-won attribution |
| Efficiency gain | "Reduce onboarding time from 14 days to 3 days" | Product analytics + CS measurement |
| Competitive impact | "Close the feature gap cited in 40% of lost deals" | Win/loss tracking post-launch |
| Retention impact | "Reduce churn risk for 120 accounts that cited this as a gap" | Churn reason analysis + account health |

## Risk Documentation Template

Each risk should include:

| Component | Description |
|-----------|-------------|
| Risk | What could go wrong |
| Likelihood | High / Medium / Low |
| Impact | What happens if the risk materialises |
| Mitigation | Specific action to reduce the risk |
| Owner | Who is responsible for the mitigation |

## Quality Checklist

- [ ] Under 500 words / one page
- [ ] No engineering jargon (passed the "would a sales rep understand this?" test)
- [ ] Market context includes a "why now" with evidence
- [ ] Solution overview describes buyer outcomes, not implementation details
- [ ] Impact section has at least two quantified metrics
- [ ] Key risks include mitigations, not just risk statements
- [ ] Reviewed by the owning PM for accuracy
- [ ] Aligned with current positioning by PMM/marketing leadership
