# ADR-001 — Vision

**Status:** Approved

**Date:** 2026-07-02

## Context

Orion is intended to evolve into a comprehensive business management platform. The initial implementation should minimize complexity while preserving the ability to grow without major architectural redesign.

## Decision

Orion will initially operate as a single-company platform.

The architecture shall avoid assumptions that prevent future multi-company support, but multi-company functionality will not be implemented until a clear business need exists.

## Rationale
- Faster development.
- Lower implementation complexity.
- Simpler testing.
- Simpler security model.
- Avoids premature optimization.
- Consequences
- All business entities currently belong to a single company.
- Future multi-company support should extend the existing architecture rather than replace it.
- Multi-tenancy is explicitly outside the scope of the initial releases.


## Related Documents
- ARCH-00 Vision
- ARCH-03 Domain Model