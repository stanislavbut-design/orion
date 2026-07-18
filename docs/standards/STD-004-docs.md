# STD-004 — Documentation

**Status:** Approved  

**Date:** 2026-07-18

## Purpose

This standard defines the documentation structure and governance used throughout the Orion project.

Its purpose is to ensure that the project's documentation remains accurate, consistent, maintainable, and synchronized with the implementation throughout the lifetime of Orion.

---

## Scope

This standard applies to all project documentation maintained within the Orion repository.

---

## Standard

### 1. General Principles

1.1 Documentation shall be considered part of the Orion codebase.

1.2 Documentation shall be maintained with the same discipline as source code.

1.3 Every document shall have a clearly defined purpose.

1.4 Every fact shall have a single authoritative source within the Orion documentation. Other documents shall reference that source rather than duplicate the information.

1.5 Documentation shall describe the current state of the project unless explicitly designated as historical.

---

### 2. Language

2.1 Documentation shall be written in English.

2.2 American English shall be used where applicable.

2.3 Technical terminology shall remain consistent throughout the project.

---

### 3. Document Categories

Orion documentation is organized into the following categories:

- Vision
- Architecture (ARCH)
- Architecture Decision Records (ADR)
- Standards (STD)
- Development Guides (DEV)
- Glossary

Each category has a distinct purpose and shall not duplicate another category.

Each document shall belong to exactly one documentation category.

---

### 4. Architecture

4.1 Architecture documents (ARCH) define the current target architecture of Orion.

4.2 Architecture documents are living documents.

4.3 Architecture documents shall always reflect the cumulative effect of all approved Architecture Decision Records (ADRs).

4.4 Architecture documents are the primary reference for understanding Orion's architecture.

---

### 5. Architecture Decision Records

5.1 ADRs document significant architectural decisions.

5.2 ADRs shall progress through the following lifecycle:

- Draft
- Approved
- Superseded
- Deprecated

5.3 Once an ADR is approved, its Decision section shall be immutable.

5.4 Changes to architectural decisions shall be documented in a new ADR.

5.5 Superseded ADRs shall remain part of the permanent project history.

---

### 6. Relationship Between ARCH and ADR

6.1 Approved ADRs authorize changes to Orion's architecture.

6.2 Every approved ADR affecting the architecture shall be reflected in the corresponding ARCH document.

6.3 An architectural change is not complete until the corresponding ARCH document has been updated.

---

### 7. Standards

7.1 Standards (STD) define implementation and engineering conventions.

7.2 Standards are living documents.

7.3 Standards shall remain consistent with the current architecture.

---

### 8. Development Guides

8.1 Development Guides (DEV) describe engineering processes and workflows.

8.2 Development Guides shall describe recommended project practices without duplicating Standards.

---

### 9. Document Structure

9.1 Every governance document shall include:

- Title
- Status
- Date
- Purpose (or Context for ADRs)
- Scope (where applicable)
- Main content
- Related Documents

9.2 Governance documents shall use consistent section headings.

---

### 10. File Naming

10.1 Document filenames shall consist of:

- document identifier
- short descriptive name

10.2 Filenames are identifiers rather than document titles.

10.3 The complete document title belongs within the document itself.

10.4 Document identifiers shall use uppercase (e.g., ADR-001, ARCH-003, STD-002).

10.5 Filenames shall begin with the document identifier, followed by a lowercase descriptive name using hyphens as word separators (e.g., ADR-001-vision.md).

10.6 Cross-references shall use document identifiers. Filenames shall not be used as document references.

10.7 The descriptive part of the filename should normally consist of one to three words. The complete document title shall be specified within the document itself.

Examples:

&emsp;Filename: ADR-003-postgresql.md

&emsp;Title:    ADR-003 — PostgreSQL as the Primary Database

---

### 11. Documentation Structure

11.1 The `docs` directory shall contain a top-level `README.md` serving as the documentation entry point.

11.2 Each major documentation category shall maintain its own `INDEX.md`.

11.3 Index documents shall provide navigation and shall not duplicate document content.

---

### 12. Cross References

12.1 Governance documents shall include a "Related Documents" section.

12.2 Cross-references shall use document identifiers. Document titles may be included for readability.

Example:

- ADR-003 — PostgreSQL as the Primary Database
- ARCH-003
- STD-002

---

### 13. Synchronization

13.1 Documentation shall be updated as part of the same logical change as the implementation.

13.2 A feature affecting architecture shall not be considered complete until both the implementation and the corresponding documentation have been updated.

13.3 Documentation and implementation shall evolve together.

---

## Exceptions

Exceptions to this standard shall be explicitly documented together with the rationale.

---

## Related Documents

- ADR-001 — Vision and Scope
- ADR-002 — Modular Architecture
- STD-001 — Coding
- DEV-001 — Workflow