# Translation Framework: plain-english-translator

Legalese patterns, plain-English equivalents, readability scoring, and preservation rules.

## Common Legalese Patterns and Plain-English Equivalents

| # | Legalese | Plain English |
|---|----------|---------------|
| 1 | hereinafter referred to as | called |
| 2 | whereas | background / because |
| 3 | notwithstanding the foregoing | even though the above says |
| 4 | in the event that | if |
| 5 | prior to | before |
| 6 | subsequent to | after |
| 7 | in accordance with | following / under |
| 8 | shall | must / will |
| 9 | hereby | (remove — adds no meaning) |
| 10 | aforementioned | mentioned above |
| 11 | pursuant to | under / following |
| 12 | indemnify and hold harmless | pay for any losses and protect from claims |
| 13 | to the fullest extent permitted by law | as much as the law allows |
| 14 | without limitation | including but not limited to |
| 15 | represents and warrants | promises and guarantees |
| 16 | in lieu of | instead of |
| 17 | mutatis mutandis | with the necessary changes |
| 18 | force majeure | events beyond either party's control |
| 19 | liquidated damages | a pre-set penalty amount |
| 20 | severability | if one part is invalid, the rest still applies |
| 21 | waiver | giving up a right |
| 22 | assigns and successors | anyone who takes over for either party |
| 23 | good faith | honestly and fairly |
| 24 | material breach | a serious violation of the agreement |
| 25 | cure period | time to fix the problem |
| 26 | governing law | the laws that apply to this contract |
| 27 | consequential damages | indirect losses (lost profits, lost business) |
| 28 | aggregate liability | total maximum amount one party can owe |
| 29 | pro rata | proportionally |
| 30 | ipso facto | automatically because of that fact |
| 31 | ab initio | from the beginning |
| 32 | pari passu | on equal terms |
| 33 | inter alia | among other things |
| 34 | bona fide | genuine / in good faith |
| 35 | de minimis | too small to matter |
| 36 | make whole | fully compensate |
| 37 | time is of the essence | deadlines are strict and binding |
| 38 | not to exceed | up to a maximum of |
| 39 | sole and exclusive remedy | the only way to fix this |
| 40 | at its sole discretion | can decide on its own |
| 41 | covenant not to sue | promise not to take legal action |
| 42 | hold harmless | not hold responsible |
| 43 | best efforts / reasonable efforts | try hard / try reasonably |
| 44 | commercially reasonable | what a sensible business would do |
| 45 | as-is, where-is | no guarantees about condition |
| 46 | without prejudice | without giving up any rights |
| 47 | jointly and severally | each party is fully responsible |
| 48 | in perpetuity | forever |
| 49 | survival | continues after the contract ends |
| 50 | entire agreement | this document is the complete deal |

## Readability Scoring

### Flesch-Kincaid Grade Level (Target: 8 or below)

```
Grade Level = 0.39 × (total words / total sentences) + 11.8 × (total syllables / total words) - 15.59
```

- Grade 8 = readable by a typical 13-14 year old
- Average sentence length target: 15-20 words
- Average word length target: 1.5 syllables

### Gunning Fog Index (Reference)

```
Fog Index = 0.4 × [(words / sentences) + 100 × (complex words / total words)]
```

- Complex word = 3+ syllables (excluding common suffixes like -ed, -ing, -es)
- Target: 10 or below

## Legal Significance Taxonomy

| Flag | Symbol | Meaning | Stakeholder Impact |
|------|--------|---------|-------------------|
| Binding Obligation | OBLIGATION | You must do this | Creates a duty — failure may be breach |
| Right | RIGHT | You can do this | Grants permission or entitlement |
| Limitation | LIMITATION | You cannot do this | Restricts what you can do or claim |
| Risk | RISK | This could happen to you | Describes exposure or potential liability |

## Preservation Rules

Translation must NOT change legal meaning. Preserve original language (with explanatory note) when:

1. **Defined terms with expanded scope**: The defined term captures more than its plain-English equivalent (e.g., "Services" defined to include support, maintenance, and future products)
2. **Legal terms of art**: Words with specific legal meanings different from everyday meaning (e.g., "consideration" means something of value exchanged, not "thinking about it")
3. **Conditional chains**: Nested if-then structures where simplification would lose a condition
4. **Quantified obligations**: Specific numbers, dates, or thresholds that must be preserved exactly
5. **Regulatory references**: Citations to specific laws or regulations that must remain precise

When preserving original language, format as:

> **Original**: [exact legal text]
> **What this means**: [plain-English explanation]
> **Why we kept the original**: [reason simplification would change meaning]
