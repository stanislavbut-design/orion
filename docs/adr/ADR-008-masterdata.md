# ADR-008 — Master Data Organization

**Status:** Approved

**Date:** 2026-07-18

## Context

Both reference data and business master data are maintained by administrators, have similar lifecycle characteristics, and are shared across all business modules.

## Decision

During the initial implementation, Orion shall maintain a single *masterdata* application for all master data.

Conceptual separation shall be achieved through internal package organization rather than multiple Django applications.

## Rationale

This reduces architectural complexity while preserving clear domain boundaries within the codebase.

## Consequences

- A single *masterdata* application.
- Static reference data (e.g., Country, Currency, Language) and business master data (e.g., Party, Role, Address, Contact) reside within the *masterdata* app.
- Conceptual separation is achieved through internal package organization.
- Simplified permissions, migrations, and administration.
- Future extraction into separate applications remains possible if justified by evolving business requirements..

## Related Documents

- ADR-002 Modular Architecture
- ARCH-003 Domain Model
- Glossary