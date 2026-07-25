# ADR-009 — Single-Tenant Deployment Model

**Status:** Approved

**Date:** 2026-07-25

## Context

Orion architecture shall conform to current vision without compromising possible multi-tenant architecture.

## Decision

Each Orion installation represents exactly one tenant.

A tenant owns one Organization, which acts as the root of the business identity model.

Ownership of business data is therefore implicit and shall not be represented by foreign keys in domain models.

## Rationale

Alternative Considered: Row-level tenant ownership

Store an owner_organization foreign key in every business entity.

Rejected because:

- it introduces redundant data in a single-tenant deployment;
- it conflates deployment concerns with business semantics;
- it complicates the domain model without providing current business value;
- it violates Orion's principle of avoiding speculative complexity.

## Consequences

- Business models shall not contain an owner_organization field.
- Organization in the domain model refers exclusively to the business identity, never to deployment ownership.
- If Orion later evolves into a shared-database SaaS architecture, tenant isolation will be implemented as an infrastructure concern without affecting the business domain model.
- Multi-tenancy shall be treated as a deployment architecture decision rather than a business modelling concern.

## Related Documents

- ARCH-002 Platform Architecture
- STD-002 Database