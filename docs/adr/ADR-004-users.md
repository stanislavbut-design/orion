# ADR-004 — Custom Django User Model

**Status:** Approved

**Date:** 2026-07-02

## Context

User management and database organization should support future growth while remaining simple during the initial implementation.

## Decision

Orion shall use a custom Django User model from the beginning.

The operational database shall initially use a single PostgreSQL schema (public).

## Rationale

Custom user models are significantly easier to introduce at project start than later.

Using the default schema simplifies:

- migrations
- administration
- tooling
- backups

Additional schemas may be introduced later if justified.

## Consequences

- Authentication is based on the custom user model.
- All business tables initially reside in the public schema.
- Schema separation is deferred.

## Related Documents

- ARCH-001 Platform Architecture
- STD-002 Database