# Tasks — Phase 0: Foundation

**Input**: Design documents from `/specs/001-enrich-skill-directory/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

**Purpose**: Set up infrastructure that all subsequent phases depend on. No skill enrichment happens here.

---

## Phase 0: Setup & Infrastructure

- [x] T001 Write `ETHOS.md` at repo root — operating philosophy for the Skill OS. Research best-in-class company philosophies (Stripe's operating principles, GitLab's handbook values, gstack's ETHOS.md) then write the skill-os philosophy document covering: what this organization believes about work quality, how agents should approach ambiguity, and what separates excellent output from adequate output. No word limit but aim for concise (300–500 words). 1 commit.
- [x] T002 Create `departments/product/` directory
- [x] T003 Create `departments/engineering/` directory
- [x] T004 Create `departments/marketing/` directory
- [x] T005 Create `departments/design/` directory
- [x] T006 Create `departments/data-growth/` directory
- [x] T007 Create `departments/finance/` directory
- [x] T008 Create `departments/legal/` directory
- [x] T009 Create `departments/sales/` directory
- [x] T010 Create `departments/agent-operations/` directory
- [x] T011 Create `departments/customer-success/` directory
- [x] T012 Create `departments/customer-support/` directory
- [x] T013 Create `departments/technical-operations/` directory
- [x] T014 Create `departments/revenue-operations/` directory
- [x] T015 Create `departments/applied-research/` directory
- [x] T016 Create `departments/account-management/` directory
- [x] T017 Create `departments/implementation/` directory
- [x] T018 Create `_shared/references/` directory at repo root
- [x] T019 Create `_shared/scripts/` directory at repo root
- [x] T020 Create `_shared/assets/` directory at repo root
- [x] T021 Write `scripts/validate.py` — validation script per FR-023. Must check: valid YAML frontmatter, all 7 required fields populated, `name` matches directory name, `description` 50–1024 chars in third-person, body word count within limit for complexity class (hard error), all referenced files exist, all cross-reference paths resolve, cross-references are bidirectional (warning), ethos profile reference is valid. Support single-file mode (`python scripts/validate.py agents/product/product-manager/backlog-groomer/SKILL.md`) and full-repo mode (`python scripts/validate.py`). 1 commit.
- [x] T022 Update `CLAUDE.md` — reflect enriched skill format (constitution v2.0.0), new directory structure (`departments/`, `_shared/`, skill subdirectories), enrichment workflow from quickstart.md, and word limit enforcement. 1 commit.
- [x] T023 Update `AGENTS.md` — add enrichment status section noting new file path convention (`agents/<agent>/<skill>/SKILL.md`), link to status.md for progress tracking. 1 commit.

**Checkpoint**: Foundation ready. All directories exist, validation script works, ETHOS.md written. Phase 1 can begin.

---

## Dependencies

- T002–T017 (department dirs) can all run in parallel
- T018–T020 (_shared dirs) can all run in parallel
- T001 (ETHOS.md) is independent
- T021 (validate.py) is independent
- T022 and T023 should run last (they reference the completed structure)

## Notes

- T002–T020 are directory creations that can be batched into a single commit: `docs: create departments/ and _shared/ directory structure`
- T001 requires web research on company philosophies
- T021 requires reading data-model.md and contracts/frontmatter-schema.yaml for validation rules
