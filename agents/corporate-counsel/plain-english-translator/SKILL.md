---
name: plain-english-translator
description: >
  This skill translates complex legal language into plain English at an 8th-grade
  reading level while preserving legal meaning. Use when non-legal stakeholders
  need to understand contract terms, when creating customer-facing contract
  summaries, or when a business team asks what a clause actually means. Suggest
  when business team forwards a contract with questions about specific terms.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: simple
related-skills:
  - ../contract-review-orchestrator/SKILL.md
  - ../contract-risk-analyst/SKILL.md
  - ../../general-counsel/missing-protections-finder/SKILL.md
triggers:
  - "translate to plain english"
  - "explain this clause"
  - "simplify contract language"
  - "what does this mean"
---

# plain-english-translator

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Translates complex legal language into plain English at an 8th-grade reading level while preserving legal meaning and annotating each clause with its legal significance.

## When to Use

- When a non-legal stakeholder (sales, product, executive) needs to understand what specific contract terms mean before making a business decision.
- When creating a customer-facing summary of contract terms that must be accurate but accessible.
- When a business team asks "what does this clause actually mean?" and needs a clear answer without scheduling a meeting with legal.

## Workflow

1. **Identify Legalese Patterns**: Scan the contract text for legalese patterns: defined terms with expanded scope, nested conditional structures, double negatives, archaic language (hereinafter, whereas, notwithstanding), and passive voice constructions. Catalog each pattern with its location. Deliverable: annotated pattern inventory. See [framework.md](references/framework.md) for common patterns.

2. **Rewrite in Plain English**: Translate each clause into plain English targeting Flesch-Kincaid Grade Level 8 or below. Break long sentences into shorter ones. Replace legal jargon with everyday equivalents. Preserve legal meaning — flag any clause where simplification would change the legal effect and keep the original language with an explanatory note. Deliverable: plain-English clause translations.

3. **Annotate Legal Significance**: Tag each translated clause with its legal significance: binding obligation (you must do this), right (you can do this), limitation (you cannot do this), or risk (this could happen to you). Highlight the key takeaway for each clause in one sentence. Deliverable: annotated translations with significance flags.

4. **Produce Plain-English Summary**: Assemble the output using the template (see [plain-english-output-template.md](assets/plain-english-output-template.md)). Include contract title, parties, plain-English summary table, overall summary, and a glossary of legal terms that could not be simplified without losing meaning. Deliverable: plain-English summary document.

## Anti-Patterns

- **Oversimplification that changes meaning**: Translating "indemnify and hold harmless" as "protect" without conveying that this creates a financial obligation to pay for losses. *Why*: a translation that changes legal meaning is worse than no translation — it creates false confidence and may lead stakeholders to agree to terms they do not understand.

- **Translating without significance flags**: Providing plain-English text without indicating whether each clause is an obligation, right, limitation, or risk. *Why*: stakeholders need to know not just what a clause says but what it means for them — a clause that "sounds fine" in plain English may still impose a significant obligation.

- **Ignoring defined terms**: Translating clause text at face value without checking how defined terms expand the scope. *Why*: "Confidential Information" might be defined to include all information ever shared, making a seemingly narrow confidentiality clause extremely broad.

## Output

**On success**: Produces a plain-English summary document with a clause-by-clause translation table (original text, plain English version, significance flag, key takeaway), an overall summary, and a glossary. Target Flesch-Kincaid Grade Level 8 or below. Delivered to the requesting business stakeholder.

**On failure**: Report which clauses could not be simplified without changing legal meaning, provide the original text with explanatory notes for those clauses, and recommend a meeting with legal to walk through the complex sections. Every untranslatable clause must include a reason.

## Related Skills

- [`contract-review-orchestrator`](../contract-review-orchestrator/SKILL.md) — Produces review reports that may need plain-English translation for non-legal stakeholders.
- [`contract-risk-analyst`](../contract-risk-analyst/SKILL.md) — Risk findings can be translated into plain English to help business teams understand specific risks.
- [`missing-protections-finder`](../../general-counsel/missing-protections-finder/SKILL.md) — Gap analysis results may need plain-English explanation for stakeholders deciding whether to accept the gaps.
