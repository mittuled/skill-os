# API Documentation Design Plan

**Version**: 1.0  
**Owner**: Technical Writer  
**API / Product**: [Name]  
**Prepared**: YYYY-MM-DD  
**Target Audience**: [e.g. Backend engineers, Full-stack developers, Platform engineers]  

---

## 1. Documentation Scope

| Documentation Type | In Scope | Owner | Target Completion |
|-------------------|----------|-------|-------------------|
| Getting Started guide | Yes / No | [Name] | [Date] |
| Authentication guide | Yes / No | [Name] | [Date] |
| API Reference (all endpoints) | Yes / No | [Name] | [Date] |
| SDK / Client library docs | Yes / No | [Name] | [Date] |
| Error code reference | Yes / No | [Name] | [Date] |
| Webhook guide | Yes / No | [Name] | [Date] |
| Rate limiting / pagination guide | Yes / No | [Name] | [Date] |
| Tutorials / How-to guides | Yes / No | [Name] | [Date] |
| Changelog | Yes / No | [Name] | [Date] |
| OpenAPI / Swagger spec | Yes / No | [Name] | [Date] |

---

## 2. Audience Analysis

### Primary Audience
| Attribute | Detail |
|-----------|--------|
| Role | [e.g. Senior Backend Engineer] |
| Experience level | [e.g. Intermediate — familiar with REST APIs; may be new to this product] |
| Goal | [e.g. Integrate [Product] into existing [Platform] application within a sprint] |
| Primary pain in existing docs | [e.g. No working code examples; can't find error explanations] |
| Discovery path | [e.g. Finds docs via Google search; starts at quickstart] |

### Secondary Audience
| Attribute | Detail |
|-----------|--------|
| Role | [e.g. Solutions Engineer evaluating the API] |
| Goal | [e.g. Verify API capabilities before recommending to customer] |
| Docs needs | [e.g. Comprehensive endpoint coverage; clear auth model] |

---

## 3. Information Architecture

### Top-Level Navigation Structure
```
docs/
├── Getting Started
│   ├── Introduction
│   ├── Authentication
│   ├── Quickstart (5-minute guide)
│   └── First API Call (runnable example)
├── Guides
│   ├── [Use case 1]
│   ├── [Use case 2]
│   └── [Use case 3]
├── API Reference
│   ├── [Resource A]
│   │   ├── List [Resource A]
│   │   ├── Create [Resource A]
│   │   ├── Get [Resource A]
│   │   ├── Update [Resource A]
│   │   └── Delete [Resource A]
│   └── [Resource B]
├── SDKs & Libraries
│   ├── Python
│   ├── Node.js
│   └── [Other languages]
├── Webhooks
├── Error Reference
├── Rate Limits & Pagination
└── Changelog
```

---

## 4. Content Standards

### API Reference — Required Fields Per Endpoint
- [ ] HTTP method + endpoint path
- [ ] Description (what it does; when to use it)
- [ ] Authentication requirements
- [ ] Request parameters (path, query, body) — name, type, required/optional, description
- [ ] Request body example (JSON)
- [ ] Response body schema
- [ ] Response example (success — 200/201)
- [ ] Error responses (with error codes and descriptions)
- [ ] Code examples in minimum 3 languages (Python, Node.js, cURL)
- [ ] Rate limit notes (if endpoint-specific)

### Writing Standards
| Standard | Rule |
|----------|------|
| Voice | Active, second person ("Call the endpoint to…", not "The endpoint may be called to…") |
| Tense | Present tense |
| Code samples | Always runnable; always tested against live API |
| Jargon | Define on first use; link to glossary |
| Version references | Always explicit (e.g. "API v2", not "the latest version") |

---

## 5. Endpoint Inventory

| Endpoint | Method | Description | Status | Assigned To | Due |
|----------|--------|-------------|--------|-------------|-----|
| /[resource] | GET | List [resource] | [ ] Draft / [ ] Review / [ ] Published | [Name] | [Date] |
| /[resource] | POST | Create [resource] | [ ] | [Name] | [Date] |
| /[resource]/{id} | GET | Get single [resource] | [ ] | [Name] | [Date] |
| /[resource]/{id} | PUT/PATCH | Update [resource] | [ ] | [Name] | [Date] |
| /[resource]/{id} | DELETE | Delete [resource] | [ ] | [Name] | [Date] |

---

## 6. Code Example Languages

| Language | SDK Provided | Example Format | Tester |
|----------|-------------|----------------|--------|
| cURL | No | Shell command | [Name] |
| Python | Yes / No | requests / [SDK name] | [Name] |
| Node.js | Yes / No | fetch / [SDK name] | [Name] |
| Go | Yes / No | net/http / [SDK name] | [Name] |
| Ruby | Yes / No | Net::HTTP / [SDK name] | [Name] |

---

## 7. Review & Approval Workflow

| Stage | Reviewer | SLA | Checklist |
|-------|----------|-----|-----------|
| Technical accuracy | [Engineer / PM] | 2 business days | All endpoints tested; no broken examples |
| Editorial review | [Senior Tech Writer / Editor] | 1 business day | Voice, clarity, completeness |
| Security review | [Security team] | 1 business day | No sensitive data in examples; auth described correctly |
| Final approval | [DevRel Lead / Head of Docs] | 1 business day | Ready to publish |

---

## 8. Toolchain

| Tool | Purpose |
|------|---------|
| [ReadMe.io / Mintlify / Stoplight / Docusaurus] | Docs platform / hosting |
| [OpenAPI / Swagger] | API spec — source of truth |
| [Postman] | Testing code examples |
| [GitHub] | Version control for docs source |
| [Grammarly / Vale] | Writing style linting |

---

## 9. Launch Checklist

- [ ] All in-scope endpoints documented
- [ ] Every endpoint has ≥ 1 working code example (tested)
- [ ] Error reference complete with all error codes
- [ ] Getting Started guide reviewed and tested by external developer
- [ ] OpenAPI spec published and validated
- [ ] Changelog entry for this documentation release
- [ ] Docs announced in developer community
- [ ] Google Search Console / analytics tracking active
