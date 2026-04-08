## What this PR adds or changes

<!-- List each skill added or modified. One skill per line.
     Format: `agents/<agent>/<skill>/SKILL.md` — brief description -->

## Validation checklist

- [ ] `python3 scripts/validate.py agents/<agent>/<skill>/SKILL.md` passes with no errors
- [ ] Word limit respected (Simple ≤500, Medium ≤1000, Complex ≤1500)
- [ ] `references/` subdirectory present with at least one file (50–120 lines)
- [ ] `assets/` subdirectory present with at least one template (80–150 lines)
- [ ] YAML frontmatter complete (`name`, `description`, `department`, `agent`, `version`, `complexity`, `related-skills`)
- [ ] All 9 required sections present
- [ ] Bidirectional cross-references added to related skills
- [ ] One skill per commit (no batching)
