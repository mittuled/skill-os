# Quickstart: Skill Quality Improvements

## Onboard Your Tools

```bash
# Run the onboarding skill — it interviews you about your tool stack
# and connects everything via MCP servers
claude "Run the company-tooling-onboarder skill"
```

The onboarder will:
1. Ask about each tool category (Slack, GitHub, Jira, etc.)
2. Authenticate against each tool's API
3. Connect MCP servers for tools that have them
4. Offer to build MCP wrappers for tools that don't
5. Generate `allowed-tools.yaml` at repo root

## Configure Tool Access

Edit `allowed-tools.yaml` to control who can use what:

```yaml
schema_version: 1

company-wide:
  - name: slack
    mcp: true
    scopes: [read, send]
  - name: github
    mcp: true

department:
  engineering:
    - name: datadog
      mcp: true
```

Or use the tool-policy-manager skill:
```bash
claude "Add Datadog access for the Engineering department"
```

## Add Triggers to a Skill

Add `triggers` to the YAML frontmatter of any SKILL.md:

```yaml
---
name: backlog-groomer
triggers:
  - "groom the backlog"
  - "refine upcoming stories"
  - "clean up the backlog"
  - "prioritize the backlog"
# ... existing fields ...
---
```

## Add a Checkpoint Gate

Append `[GATE]` to any workflow step that needs human approval:

```markdown
## Workflow

1. **Analyze the contract**: Extract key terms and obligations. Deliverable: terms summary.
2. **Score risk factors**: Apply scoring rubric. Deliverable: risk score. [GATE]
3. **Generate counter-proposals**: Draft alternatives for high-risk clauses. Deliverable: negotiation brief.
```

## Add a Scoring Rubric

Create `references/scoring-rubric.md` in the skill's subdirectory:

```markdown
# Scoring Rubric: Vendor Risk Assessment

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Financial stability | 25% | 0-10 | Revenue trends, funding, burn rate |
| Security posture | 25% | 0-10 | SOC 2, pen test results, incident history |
| Contract terms | 20% | 0-10 | Liability caps, indemnification, termination |
| Technical fit | 15% | 0-10 | API quality, uptime SLA, integration effort |
| Vendor reputation | 15% | 0-10 | References, reviews, market position |

## Grade Bands

| Grade | Score Range | Label |
|-------|-----------|-------|
| A+ | 90-100 | Excellent — proceed with confidence |
| A | 75-89 | Good — minor concerns only |
| B | 60-74 | Acceptable — negotiate flagged items |
| C | 40-59 | Caution — significant risks to address |
| D | 20-39 | High risk — consider alternatives |
| F | 0-19 | Unacceptable — do not proceed |
```

Then reference it in the Workflow: "Apply the scoring rubric at `references/scoring-rubric.md`."

## Add Code Examples

Create `examples/` in the skill's subdirectory with input/output pairs:

```
agents/engineering/devops-infrastructure-engineer/ci-cd-pipeline-builder/
├── SKILL.md
└── examples/
    ├── github-actions-basic/
    │   ├── input.md      # "Set up CI for a Node.js project with tests and linting"
    │   └── output.yaml   # Complete .github/workflows/ci.yml
    └── jenkinsfile-multi-stage/
        ├── input.md
        └── output.groovy
```

## Check Tool Health

```bash
claude "Run the tool-health-checker skill"
```

Produces a health report showing connectivity, auth status, and remediation steps for any failures.

## Validate

```bash
python3 scripts/validate.py  # Checks triggers, [GATE], allowed-tools.yaml
```
