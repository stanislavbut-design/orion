# ADR-002 — Modular Architecture

**Status:** Approved

**Date:** 2026-07-02

## Context

A clear modular structure is required to keep Orion maintainable as new business capabilities are added.

## Decision

Orion shall be organized as a collection of independent Django applications representing major business domains.

Shared infrastructure belongs in ***core***. Master data belongs in ***masterdata***. Business functionality is implemented in dedicated applications (Finance, HR, CRM, etc.).

## Rationale

- Clear separation of responsibilities.
- Reduced coupling.
- Better maintainability.
- Easier testing.
- Supports incremental development.

## Consequences

- Business logic remains within its owning application.
- ross-module communication occurs through well-defined interfaces and shared domain models.
- Shared infrastructure must not depend on business modules.

## Related Documents

- ARCH-001 Engineering Principles
- ARCH-003 Domain Model