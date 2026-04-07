# MEDDIC Overlay Framework

Defines the MEDDIC qualification overlay applied to leads scoring 6.0+ on the BANT composite to assess deal complexity, buying process maturity, and close probability.

## When to Apply

Apply MEDDIC only after BANT scoring produces a composite of 6.0 or higher. MEDDIC adds value for complex, multi-stakeholder deals where understanding the buying process is as important as confirming budget and need. For leads below 6.0, the BANT score alone is sufficient for tier assignment.

## MEDDIC Elements

### M — Metrics

**Definition**: The quantifiable business outcomes the prospect expects from a solution. Metrics answer "what does success look like in numbers?"

**How to Score from Public Signals**:
- Check company blog, investor updates, or earnings calls for stated KPIs or performance targets
- Review job postings for metrics mentioned in role descriptions (e.g., "improve pipeline conversion by 20%")
- Look for case studies from competitors referencing measurable outcomes in the same vertical
- Examine G2/Gartner reviews from similar companies describing ROI achieved

| Status | Evidence Required |
|--------|------------------|
| Confirmed | Prospect has publicly stated a quantified business goal the product directly impacts (e.g., "reduce onboarding time by 50%" in a job posting or press release) |
| Partial | Prospect operates in a context where standard metrics apply (e.g., SaaS company likely tracks CAC, LTV, churn) but no company-specific metric statement found |
| Unknown | No public evidence of quantified business goals related to the product category |

### E — Economic Buyer

**Definition**: The person with final budget authority and sign-off power for the purchase. Not the user, not the evaluator — the person who can say "yes" and write the check.

**How to Score from Public Signals**:
- Identify the likely economic buyer by title/role using org chart analysis (LinkedIn, company website)
- Check if the economic buyer has engaged with any content or attended events
- Assess reachability: public email, active LinkedIn, conference speaker, published author

| Status | Evidence Required |
|--------|------------------|
| Confirmed | Economic buyer identified by name, title confirmed via LinkedIn, and at least one engagement signal or accessible contact path exists |
| Partial | Economic buyer role identified (e.g., "VP Engineering probably owns this budget") but specific person not confirmed, or person identified but no engagement or contact path |
| Unknown | Cannot determine who holds budget authority; org chart is opaque; company may be too early-stage for defined budget ownership |

### D — Decision Criteria

**Definition**: The specific factors the prospect will use to evaluate and compare solutions. What matters most to them — price, integration ease, support quality, feature set, security compliance?

**How to Score from Public Signals**:
- Review RFP documents if publicly available
- Check G2 reviews from the company or similar companies for evaluation criteria mentioned
- Analyze job postings for tool requirements that reveal priority factors
- Look for conference talks or blog posts by prospect employees discussing evaluation approaches

| Status | Evidence Required |
|--------|------------------|
| Confirmed | Decision criteria explicitly stated in an RFP, review, or public communication (e.g., "We prioritized API flexibility and SOC 2 compliance when selecting our current vendor") |
| Partial | Likely decision criteria inferred from industry norms and company profile (e.g., enterprise fintech companies typically require SOC 2, GDPR, and bank-grade SLAs) |
| Unknown | No evidence of evaluation criteria; company has not publicly discussed vendor selection approach |

### D — Decision Process

**Definition**: The sequence of steps, approvals, and stakeholders involved in making the purchase decision. Answers "how does this company buy?"

**How to Score from Public Signals**:
- Research company size and industry to infer procurement complexity (enterprise = longer, startup = shorter)
- Check for a formal procurement department (job postings, LinkedIn profiles)
- Look for evidence of vendor review processes (G2 reviews mentioning "our evaluation team")
- Assess whether the company has purchased similar tools recently (signals a known procurement path)

| Status | Evidence Required |
|--------|------------------|
| Confirmed | Decision process mapped: number of stakeholders, approval stages, and timeline documented or inferable from recent similar purchases (e.g., company reviewed 3 competitors on G2 last quarter) |
| Partial | General process inferred from company size and industry (e.g., "200-person Series B startup likely has 2-3 approval stages, 4-8 week cycle") but no company-specific confirmation |
| Unknown | No evidence of how the company makes purchasing decisions; may be first-time buyer in this category |

### I — Identify Pain

**Definition**: The specific, confirmed pain point driving the evaluation. Not a general industry challenge — the prospect's actual, felt problem.

**How to Score from Public Signals**:
- Job postings describing problems to solve (e.g., "our current system can't scale beyond...")
- Glassdoor reviews mentioning tooling frustrations in relevant departments
- Support forum posts or community discussions by company employees
- Content engagement patterns (downloading content about solving specific problems)

| Status | Evidence Required |
|--------|------------------|
| Confirmed | Specific pain point identified with evidence: job posting describes the problem, Glassdoor reviews mention the frustration, or content engagement shows research into the specific issue |
| Partial | Pain point inferred from company context (e.g., "growing 50% YoY with no dedicated data team — likely experiencing data infrastructure pain") but no direct company statement |
| Unknown | No evidence of a specific pain point; engagement is generic or exploratory |

### C — Champion

**Definition**: An internal advocate who actively wants the solution, has influence in the organization, and will sell internally on the product's behalf.

**How to Score from Public Signals**:
- Identify contacts who have engaged multiple times with content (repeat webinar attendees, multiple content downloads)
- Look for contacts who have publicly advocated for similar solutions (blog posts, conference talks, social media)
- Check if any contact has used the product at a previous company (LinkedIn career history)

| Status | Evidence Required |
|--------|------------------|
| Confirmed | Specific person identified who has engaged 3+ times with content, has relevant title/influence, and shows pattern of advocacy for the solution category (e.g., "VP Eng who used our product at their previous company and has attended 2 webinars") |
| Partial | Contact with 1-2 engagement signals who has relevant influence but no clear advocacy pattern; or strong advocate identified but with limited organizational influence |
| Unknown | No contacts with repeated engagement; no evidence of internal advocacy for the solution category |

## MEDDIC Modifier Calculation

After assessing all 6 elements:

- **4+ elements Confirmed**: Multiply BANT composite by **1.1** (cap at 10.0). Rationale: a well-understood deal structure significantly increases close probability.
- **2+ elements Unknown**: Multiply BANT composite by **0.9**. Rationale: significant unknowns in the buying process indicate qualification gaps that will surface later in the sales cycle.
- **Otherwise**: No modifier applied.

## When MEDDIC Adds Value Over BANT Alone

MEDDIC is most valuable when:
1. **Deal size is significant** — larger deals involve more stakeholders and longer processes
2. **Multiple stakeholders** — BANT identifies the budget holder, MEDDIC maps the full committee
3. **Competitive displacement** — understanding decision criteria helps position against incumbents
4. **New category creation** — when prospects have no established buying process, MEDDIC reveals whether they can actually execute a purchase
5. **Enterprise sales** — companies with 500+ employees typically have procurement processes that BANT alone cannot capture
