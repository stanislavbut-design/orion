# Module Entity Specification

## 1. Purpose

This specification defines the architectural principles governing module-specific entities and their interaction with the Orion Core Domain.

It establishes how functional modules extend the Core without compromising the integrity, consistency, or independence of the Core Identity Model.

---

## 2. Module Entity

### Definition

A **Module Entity** is a persistent business entity whose lifecycle, semantics, and management are confined to a single functional module.

Unlike Core Identities, Module Entities do not represent enterprise-wide business actors.

They exist solely to support the operational requirements of their owning module.

### Characteristics

A Module Entity:

- belongs to exactly one functional module;
- is managed exclusively by that module;
- may reference Core Identities;
- may participate in Business Objects belonging to its module;
- shall not be referenced directly by the Core Domain.

### Examples

| Module | Module Entity |
|--------|---------------|
| HR | Applicant |
| CRM |	Lead |

---

## 3. Core Identity

Core Identities represent enterprise-wide business actors.

They remain the single source of truth for identities shared across multiple modules.

Examples include:

- Organization
- Party
- Person

---

## 4. Separation of Responsibilities

The **Core Domain** is responsible for:

- identity management;
- business relationships;
- business processes;
- business object infrastructure.

**Functional modules** are responsible for:

- operational data;
- module-specific entities;
- module-specific business rules.

Modules extend the Core but do not modify its semantics.

---

## 5. Identity Resolution

**Identity Resolution** is the architectural mechanism by which a Module Entity becomes associated with a Core Identity.

Identity Resolution determines whether:

- an existing Core Identity shall be associated; or
- a new Core Identity shall be created.

Identity Resolution is independent of the business event that initiated it.

---

## 6. Promotion

**Promotion** is a business event that causes Identity Resolution to occur.

Promotion represents a change in business status rather than a change in identity.

Examples include:

| Module Entity |	Promotion Event |	Core Identity |
|---------------|-----------------|---------------|
| Applicant |	Hired |	Person |
| Lead | Won | Party |

Promotion shall preserve the complete history of the originating Module Entity.

Promotion does not replace or delete the Module Entity.

---

## 7. Traceability

Every successful Identity Resolution shall preserve traceability between:

- the originating Module Entity; and
- the associated Core Identity.

This association shall remain available throughout the lifetime of both entities.

---

## 8. Dependency Rules

The Core Domain shall not depend upon any functional module.

Functional modules may depend upon the Core Domain.

Module Entities may reference Core Identities.

Core Identities shall not reference Module Entities.

This dependency direction preserves the independence and stability of the Core Domain.

---

## 9. Architectural Invariants

### MIF-001

Every Module Entity belongs to exactly one functional module.

### MIF-002

Module Entities are not Core Identities.

### MIF-003

Module Entities may reference Core Identities.

Core Identities shall not reference Module Entities.

### MIF-004

Identity Resolution shall either:

- associate an existing Core Identity; or
- create a new Core Identity.

### MIF-005

Promotion shall preserve the originating Module Entity.

Promotion shall not delete or replace it.

### MIF-006

Every successful Identity Resolution shall preserve traceability between the Module Entity and the associated Core Identity.

### MIF-007

The Core Domain shall remain independent of all functional modules.

### MIF-008

Every Module Entity shall define and manage its own lifecycle. 

Module-specific lifecycle states are defined by the owning module and shall not be interpreted by the Core Domain.


## 10. Related Documents

ARCH-003

