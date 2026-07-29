# ADR-003 — PostgreSQL as the Primary Database

**Status:** Approved

**Date:** 2026-07-02

## Context

The project requires a robust relational database capable of supporting advanced business applications.

## Decision

PostgreSQL is the primary database platform for Orion.

Orion may leverage PostgreSQL-specific features where they provide clear architectural or performance benefits.

## Rationale

PostgreSQL provides:

- ACID transactions
- constraints
- indexes
- views
- stored functions when appropriate
- full-text search
- JSONB support
- excellent Django integration


## Consequences

Database portability is not a design goal.

Schema design may rely on PostgreSQL capabilities when justified.

## Related Documents

- ARCH-002 Platform Architecture
- STD-002 Database