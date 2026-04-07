# Framework: api-documentation-designer

Defines the documentation type selection model (Divio system), information architecture patterns, page template specifications, and style standards for API reference documentation.

## Documentation Type Selection (Divio System)

Every API documentation need maps to one of four types. Use this table to determine what type of content to create.

| Type | Purpose | Reader State | Example Trigger | Format |
|------|---------|-------------|----------------|--------|
| Tutorial | Learning-oriented — teaches through doing | "I'm new, show me how to learn this" | New developer, no experience with the product | Step-by-step with expected outputs |
| How-to Guide | Task-oriented — solves a specific problem | "I know the basics, help me do X" | Experienced developer with a goal | Numbered steps, minimal explanation |
| Reference | Information-oriented — describes the system | "I know what I want, tell me the facts" | Developer implementing or debugging | Tables, schemas, formal spec |
| Explanation | Understanding-oriented — explains why | "I need to understand how this works" | Developer making architectural decisions | Conceptual prose with diagrams |

**Decision rule**: Never merge types. A tutorial that also serves as a reference breeds confusion. One page = one type.

## Information Architecture Patterns

| Pattern | Best For | Navigation Model | Example Structures |
|---------|---------|-----------------|-------------------|
| Task-first | Developer tools with specific use cases | Organized by what developers do | "Send a message", "Process a payment", "Authenticate a user" |
| Resource-first | REST APIs with well-defined resources | Organized by API resources | "Orders", "Customers", "Webhooks" |
| Concept-first | Complex platforms needing mental model | Organized by core concepts | "Understanding events", "Working with sessions" |
| Hybrid | Mature APIs with diverse users | Navigation split by experience level | "Getting started" → task-first; sidebar → resource-first |

**Recommended URL scheme for REST API docs:**
```
/docs/                           → Home / Overview
/docs/quickstart                 → Tutorial
/docs/guides/{task-slug}         → How-to guides
/docs/reference/{resource-slug}  → Reference
/docs/concepts/{concept-slug}    → Explanation
/docs/changelog                  → Versioned change history
/docs/errors                     → Error reference
```

## Page Template Specifications

### Endpoint Reference Template

Required sections in order:

| Section | Content | Format |
|---------|---------|--------|
| Method + path | `POST /v1/payments` | Code block |
| Short description | One sentence | Plain text |
| Authentication | Required auth method | Inline note |
| Request headers | Authorization, Content-Type, custom headers | Table: Name, Required, Description |
| Path parameters | Parameters in URL path | Table: Name, Type, Required, Description |
| Query parameters | URL query string parameters | Table: Name, Type, Required, Default, Description |
| Request body | JSON schema with field descriptions | Table + nested schema block |
| Response body | Success response schema | Table + example JSON |
| Error responses | HTTP codes this endpoint returns | Table: Code, Meaning, Example |
| Code samples | Working examples in target languages | Tabbed code blocks |

### Quickstart Template

Sections in order:
1. Goal (1 sentence — what the developer will achieve)
2. Prerequisites (explicit list — nothing assumed)
3. Step 1: [First step with numbered heading]
4. Step N: ... [Each step produces a visible output]
5. Next steps (links to relevant how-to guides)

**Rule**: Every step must produce observable output. If the developer cannot tell if a step worked, split it.

## API Documentation Style Standards

| Element | Convention | Example |
|---------|-----------|---------|
| Endpoint descriptions | Present tense, active voice | "Creates a new payment intent" not "Used to create" |
| Parameter names | Exact API name, code formatted | `customer_id` not "customer ID" |
| Type notation | JSON schema types | `string`, `integer`, `boolean`, `object`, `array` |
| Required vs. optional | Always explicit in table | Column: "Required" with Yes/No |
| Default values | Always stated when not null | Column: "Default" with value or `null` |
| Code samples | Executable without modification | Copy-paste must work |
| Error codes | Both HTTP status + application code | `400 invalid_parameter` |
| Authentication examples | Use placeholder, not real credentials | `Authorization: Bearer YOUR_API_KEY` |

## Cross-Linking Strategy

| Situation | Cross-Link To | Why |
|-----------|-------------|-----|
| First mention of a core concept | Explanation doc for that concept | Gives context without disrupting task flow |
| Error code in endpoint reference | Error reference page | Enables quick lookup |
| Step in how-to requires a prerequisite | That prerequisite's guide | Prevents dead ends |
| Related endpoint | That endpoint's reference | Reduces navigation dead-ends |
| Changelog entry for breaking change | Migration guide | Reduces developer time lost |
