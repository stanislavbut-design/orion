# STD-002 — Database

**Status:** Approved

**Date:** 2026-07-18

## Purpose

This standard defines the database design conventions used throughout Orion.

Its purpose is to ensure that the database remains consistent, maintainable, performant and extensible throughout the lifetime of the project.

This standard complements ADR-003 (PostgreSQL as the Primary Database) by defining how the database shall be designed and implemented.

---

## Scope

This standard applies to:

- Django models
- PostgreSQL database objects
- Database migrations
- Constraints
- Indexes
- Views
- Database functions
- Database transactions

---

## Standard

### 1. General Principles

1.1 The database shall be treated as an integral part of the application architecture.

1.2 Business rules shall be enforced by the database whenever practical.

1.3 Data integrity shall take precedence over application convenience.

1.4 Database design shall prioritize long-term maintainability over short-term implementation simplicity.

---

### 2. Data Classification

All persistent data shall belong to one of the following categories:

- Master Data
- Transactional Data
- Derived Data
- Configuration Data
- Audit Data
- Temporary Data

The data category shall influence lifecycle, maintenance and security decisions.

---

### 3. Naming

3.1 Database object names shall use *snake_case*.

3.2 Django model names shall be singular.

3.3 Database table names shall be plural.

3.4 Column names shall be descriptive and use *snake_case*.

3.5 Database object names shall be written in English.

---

### 4. Primary Keys and Business Codes

4.1 Every persistent entity shall define a surrogate primary key.

4.2 Primary keys shall use *BigAutoField*.

4.3 Entities exposed outside Orion may additionally define a *UUID* public identifier.

4.4 Business codes shall remain independent of primary keys.

&emsp;4.4.1 Business codes shall be stored in dedicated columns.

&emsp;4.4.2 Business codes shall not be used as primary keys.

&emsp;4.4.3. Business codes shall be protected by appropriate uniqueness constraints where required by the business domain.

---

### 5. Relationships

5.1 Foreign keys shall enforce referential integrity.

5.2 The default deletion policy shall be PROTECT.

5.3 Other deletion policies shall require explicit justification.

5.4 Many-to-many relationships shall be introduced only when they accurately represent the business domain.

---

### 6. Constraints

6.1 Database constraints shall be preferred over application validation whenever possible.

6.2 Uniqueness shall be enforced by the database.

6.3 Check constraints shall be used where appropriate.

6.4 Constraint names shall be meaningful.

---

### 7. Indexes

7.1 Indexes shall be created only when justified.

7.2 Every additional index shall have a documented purpose.

7.3 Redundant indexes shall be avoided.

---

### 8. Nullability

8.1 Fields shall be NOT NULL unless a NULL value has explicit business meaning.

8.2 NULL shall represent "unknown" or "not applicable", not "empty".

8.3 Default values shall not replace meaningful business data.

---

### 9. Transactions

9.1 Business operations affecting multiple entities shall execute within database transactions.

9.2 Transactions shall remain as short as practical.

9.3 Partial updates shall be avoided.

---

### 10. PostgreSQL Features

10.1 PostgreSQL capabilities may be used where they provide measurable value.

Examples include:

- constraints
- indexes
- views
- JSONB
- stored functions
- full-text search

10.2 PostgreSQL-specific functionality shall not be used solely because it exists.

---

### 11. Migrations

11.1 All schema changes shall be performed through Django migrations.

11.2 Manual schema modifications shall be avoided.

11.3 Every migration shall be reversible whenever practical.

---

### 12. Performance

12.1 Database performance shall be measured before optimization.

12.2 Premature optimization shall be avoided.

12.3 Correctness shall take precedence over performance.

---

### 13. Normalization

The database shall be normalized unless denormalization provides a measurable and documented benefit.

---

### 14. Temporary Data

Historical business data shall be preserved unless explicit business rules require replacement.

---

### 15. Extensibility

The database design shall avoid assumptions that unnecessarily restrict future evolution.

---

## Exceptions

Exceptions to this standard shall be documented together with the technical rationale.

---

## Related Documents

- ADR-002 — Modular Architecture
- ADR-003 — PostgreSQL as the Primary Database
- ADR-007 — Entity Identification
- ADR-008 — Master Data Organization
- STD-001 — Coding
