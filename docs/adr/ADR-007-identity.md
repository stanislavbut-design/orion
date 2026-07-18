# ADR-007 — Entity Identification

**Status:** Approved

**Date:** 2026-07-18

## Context

Orion requires identifiers serving different purposes: internal database relationships, external integrations, and business processes.

## Decision

Each persistent entity shall use:

- *BigAutoField* as the internal primary key.
- *UUIDField* only for entities exposed outside Orion.
- Domain-specific business identifiers where appropriate.

These three identifiers are independent.

## Rationale

This approach combines efficient database performance with secure external integration and flexible business numbering schemes.

## Consequences

- Internal foreign keys remain compact.
- External systems use stable opaque identifiers.
- Business numbering can evolve independently of database design.

## Related Documents

- ARCH-002 Platform Architecture
- STD-002 Database