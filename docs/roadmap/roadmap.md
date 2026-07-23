# Roadmap

# Stage 0 — Foundation ✅ Completed

| Completion Date | 2026-07-17 |
|----------|-------|

| Milestones | Commits |
|----------|-------|
| Sprint 0 — Platform Foundation | S0.2 Initialize Orion project structure |
| | S0.3 Improve .gitignore |
| | S0.4 Consolidate project structure |
| Orion Architecture & Documentation Baseline | M0.1 Orion Documentation |
| | M0.2 Refine domain model and architecture documentation |

## Deliverables:

***Technical Foundation***
- Development environment (Python, PostgreSQL, VS Code, Git)
- Django project initialized and verified
- Repository structure established
- GitHub repository configured and synchronized
- Documentation framework created

***Architecture***

- Vision
- Engineering Principles (ARCH-01)
- Domain Model (ARCH-03)
- Development Standards
- Documentation conventions

***Conceptual Domain***

- Organization model
- Party as the stable legal identity
- Identity / Role separation
- Business Relationship
- Business Object
- Business Process as a first-class concept
- Responsibility Centre introduced
- Conceptual Questions
- Business Object Validation Matrix

***Documentation***

- Glossary established
- Architecture documents cross-linked
- Mermaid diagrams integrated
- Living documentation process defined


## Outcome:

Orion now has a stable architectural and conceptual foundation from which implementation can proceed.

---

# Stage 1 — Core Domain Foundation

| Completion Date | YYYY-MM-DD |
|----------|-------|

| Milestones | Commits | Reference Doc |
|----------|-------|----------|
| Milestone 1.1 - Master Data Foundation | S01-M01.01.01 Master Data Foundation   | S01-M01-01-masterdata-foundation.md |
|                                        | S01-M01.01.02 Organize masterdata application structure ||
|                                        | S01-M01.01.03 Implement Organization ||
|                                        | S01-M01.01.04 Complete Organization lifecycle ||
|                                        | S01-M01.01.05 Implement Party ||
|                                        | S01-M01.01.06 Implement Person ||
|                                        | S01-M01.01.07 Complete Milestone 1.1 ||
|                                        | S01-M01.01.08 Complete Milestone 1.1 Adjutment 1 ||
| Milestone 1.2 - Relationship Framework | S01-M01.02.01 Refine ARCH-003 architectural baseline | S01-M01-02-relationship-framework.md |
|                                        | S01-M01.02.02 Define Business Relationship Framework ||
| Milestone 1.3 - Business Relationships |   | S01-M01-03-business-relationships.md |
| Milestone 1.4 - Contact Information |   | S01-M01-04-contact-info.md |
| Milestone 1.5 - Core Services |   | S01-M01-05-core-services.md |

## Objective

Implement the foundational domain model and application structure defined by Orion's architecture.

## Expected Outcomes

- The application structure matches the approved architecture.
- The masterdata application exists.
- The Identity model is implemented.
- The project is ready for subsequent business modules (CRM, Finance, HR, etc.).

## Milestone 1.1 — Master Data Foundation ✅ COMPLETED

### Objective

Create the `masterdata` application and implement the Identity framework.

### Deliverables
- `masterdata` application
- Identity models:
    - Organization
    - Party
    - Person
- Initial migration
- Django Admin registration
- Updated documentation (if required)

### Acceptance Criteria

- `masterdata` application is created.
- Models compile successfully.
- Migrations apply successfully.
- Entities are visible in Django Admin.
- PostgreSQL schema matches the models.
- Project starts without errors.


## Milestone 1.2 — Business Relationships and Role Participation

### Objective

Establish the conceptual and technical framework for modelling Business Relationships between Identities.



## Milestone 1.3 — Business Relationships
- BusinessRelationship
- Relationship types
- Relationship management

## Milestone 1.4 — Contact Information
- Address
- ContactMethod
- Validation and administration

## Milestone 1.5 — Core Services
- Common managers
- QuerySets
- Validation
- Reusable services

