# Paperclip Role → Skill OS Agent Mapping

Use this table to find which Skill OS agent directory and skills match each Paperclip role. All 16 Skill OS departments are represented.

**How to use:**
1. Find your Paperclip role in the left column
2. Browse the linked Skill OS agent directories
3. Pick the skill that matches your task type (see "Start here" column)
4. Set that skill's path as `instructionsFilePath` in your agent `adapterConfig`

---

| Paperclip Role | Skill OS Department(s) | Agent Directories | Start here (recommended first skill) |
|----------------|----------------------|-------------------|--------------------------------------|
| `cto` | Engineering | `agents/engineering/tech-architect/`, `agents/engineering/vp-engineering/`, `agents/engineering/tech-lead-pr-reviewer/` | `tech-architect/system-design-author` |
| `engineer` | Engineering | `agents/engineering/sr-backend-developer/`, `agents/engineering/sr-frontend-developer/`, `agents/engineering/devops-infrastructure-engineer/`, `agents/engineering/security-engineer/`, `agents/engineering/ai-ml-engineer/`, `agents/engineering/platform-engineer/`, `agents/engineering/data-engineer/` | `sr-backend-developer/builder` |
| `qa` | Engineering | `agents/engineering/qa-test-engineer/` | `qa-test-engineer/test-plan-author` |
| `devops` | Engineering | `agents/engineering/devops-infrastructure-engineer/`, `agents/engineering/platform-engineer/` | `devops-infrastructure-engineer/ci-pipeline-builder` |
| `pm` | Product | `agents/product/product-manager/`, `agents/product/vp-product/`, `agents/product/product-operations-analyst/` | `product-manager/prd-author` |
| `designer` | Design | `agents/design/ux-ui-designer/`, `agents/design/ux-researcher/`, `agents/design/brand-designer/`, `agents/design/content-designer-ux-writer/` | `ux-ui-designer/wireframe-creator` |
| `cmo` | Marketing | `agents/marketing/vp-marketing/`, `agents/marketing/demand-gen-manager/`, `agents/marketing/content-marketer/`, `agents/marketing/pr-communications-manager/` | `vp-marketing/gtm-planner-marketing` |
| `cfo` | Finance | `agents/finance/cfo-vp-finance/`, `agents/finance/fpa-analyst/`, `agents/finance/controller-accounting/` | `fpa-analyst/unit-economics-tracker` |
| `researcher` | Applied Research, Data & Growth | `agents/applied-research/applied-research-lead/`, `agents/data-growth/analytics-lead/`, `agents/data-growth/data-analyst/`, `agents/data-growth/growth-lead/` | `data-growth/data-analyst/sql-query-author` |
| `ceo` | All (strategic) | `agents/sales/vp-sales/`, `agents/marketing/vp-marketing/`, `agents/engineering/vp-engineering/`, `agents/product/vp-product/` | `product/vp-product/roadmap-owner` |
| `general` | Sales, Legal, Customer Success, Customer Support, Revenue Ops, Account Mgmt, Implementation, Technical Ops, Agent Ops | `agents/sales/`, `agents/legal/`, `agents/customer-success/`, `agents/customer-support/`, `agents/revenue-operations/`, `agents/account-management/`, `agents/implementation/`, `agents/technical-operations/`, `agents/agent-operations/` | `sales/account-executive/deal-qualifier` |

---

## Coverage verification

All 16 Skill OS departments are represented above:

| # | Department | Paperclip Role(s) |
|---|-----------|-------------------|
| 1 | Engineering | `cto`, `engineer`, `qa`, `devops` |
| 2 | Product | `pm` |
| 3 | Marketing | `cmo` |
| 4 | Design | `designer` |
| 5 | Data & Growth | `researcher` |
| 6 | Finance | `cfo` |
| 7 | Legal & Compliance | `general` |
| 8 | Sales | `general`, `ceo` |
| 9 | Customer Success | `general` |
| 10 | Customer Support | `general` |
| 11 | Revenue Operations | `general` |
| 12 | Account Management | `general` |
| 13 | Implementation | `general` |
| 14 | Technical Operations | `general` |
| 15 | Agent Operations | `general` |
| 16 | Applied Research | `researcher` |

✅ All 16 departments covered.

---

## Notes

- A single Paperclip `engineer` agent can use **different Skill OS skills** depending on the issue label — see `skill-routing-table.yaml` for examples
- The `general` role covers all remaining departments; use issue labels to route to the right skill within each domain
- For `ceo` agents: strategic skills work best with `claude-opus-4-6` model override
