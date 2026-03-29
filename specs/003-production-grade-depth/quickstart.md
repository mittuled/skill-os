# Quickstart: Deepening a Skill to Production-Grade

**Branch**: `003-production-grade-depth` | **Date**: 2026-03-28

## Before You Start

1. Know the skill's classification: **assessment**, **output-producing**, or **workflow-only**
2. Have the domain-cluster research for this skill's family
3. Have the contracts: `contracts/scoring-rubric-contract.md` and `contracts/output-template-contract.md`

## Step-by-Step: Deepen an Assessment Skill

```bash
# Example: deepening threat-modelling (security-engineer)
SKILL_DIR="agents/security-engineer/threat-modelling"
```

1. **Read the current SKILL.md** and identify:
   - What is being assessed/evaluated?
   - What criteria matter?
   - What evidence distinguishes good from bad?

2. **Create the scoring rubric** at `$SKILL_DIR/references/scoring-rubric.md`:
   - 3-6 weighted criteria (sum to 100%)
   - 0-10 scale per criterion
   - Grade bands: A+ (9.0-10.0), A (8.0-8.9), B (7.0-7.9), C (5.0-6.9), D (3.0-4.9), F (0-2.9)
   - Signal tables: for each criterion, 4-6 rows mapping evidence to score ranges
   - Follow `contracts/scoring-rubric-contract.md` exactly

3. **Create the output template** at `$SKILL_DIR/assets/<assessment>-report-template.md`:
   - Title, metadata, executive summary
   - Per-criterion scoring sections
   - Overall grade and recommendations
   - Follow `contracts/output-template-contract.md`

4. **Update SKILL.md workflow**:
   - Add explicit reference to rubric: "Apply scoring rubric at `references/scoring-rubric.md`"
   - Add explicit reference to template: "Produce report using template at `assets/<name>-template.md`"
   - Make generic steps specific: replace "evaluate X" with "score X using criteria Y with weights Z"

5. **Validate and commit**:
   ```bash
   python3 scripts/validate.py $SKILL_DIR/SKILL.md
   git add $SKILL_DIR/
   git commit -m "Deepen skill: threat-modelling for Security Engineer"
   ```

## Step-by-Step: Deepen an Output-Producing Skill

```bash
# Example: deepening prd-author (product-manager)
SKILL_DIR="agents/product-manager/prd-author"
```

1. **Read the current SKILL.md** and identify:
   - What document/artifact is produced?
   - What sections does it need?
   - What makes a good vs. bad version?

2. **Create the output template** at `$SKILL_DIR/assets/<output>-template.md`:
   - Every section pre-defined with heading, purpose, placeholder content
   - "Good example" and "bad example" annotations per section
   - Formatting guidance (tables, lists, diagrams)

3. **Create at least one reference file**:
   - `references/framework.md` — methodology details (e.g., PRD best practices)
   - OR `references/checklist.md` — quality checklist for the output
   - OR `references/signal-table.md` — decision criteria for content choices

4. **Update SKILL.md workflow**:
   - Reference the template: "Use template at `assets/<name>-template.md`"
   - Make steps domain-specific: replace "write the document" with specific section-by-section guidance

5. **Validate and commit** (same as above)

## Step-by-Step: Deepen a Workflow-Only Skill

```bash
# Example: deepening stakeholder-alignment-driver (vp-product)
SKILL_DIR="agents/vp-product/stakeholder-alignment-driver"
```

1. **Read the current SKILL.md** and identify:
   - What methodology or framework does this workflow follow?
   - What decisions must be made at each step?
   - What domain-specific knowledge is needed?

2. **Create at least one reference file**:
   - `references/framework.md` — detailed methodology (e.g., RACI matrix, stakeholder mapping)
   - OR `references/checklist.md` — step verification checklist
   - OR `references/decision-matrix.md` — decision criteria for key workflow steps

3. **Update SKILL.md workflow**:
   - Replace generic steps with specific ones: "Identify stakeholders" → "Map stakeholders using Power/Interest grid, classify as Manage Closely / Keep Satisfied / Keep Informed / Monitor"
   - Name specific frameworks at each step
   - Define explicit deliverables per step

4. **Validate and commit** (same as above)

## Common Mistakes

- **Bloating SKILL.md**: If your workflow update pushes past the word limit, move detail to `references/`. The body is the map, references are the territory.
- **Generic rubrics**: "Quality: 0-10" is not a signal table. "Quality: 9-10 = all sections complete with evidence, 7-8 = minor gaps in 1-2 sections, ..." is.
- **Copy-paste templates**: Each template must be specific to the skill's output type. A PRD template is not a design doc template.
- **Missing workflow references**: If you create a rubric/template but don't update the workflow to point to it, the agent won't know it exists.
- **Forgetting validation**: Always run `python3 scripts/validate.py` before committing.

## Commit Format

```
Deepen skill: <skill-slug> for <Agent Role>
```

One skill per commit. Never batch multiple skills.
