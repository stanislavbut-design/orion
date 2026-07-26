# Business Object Specification

## 1. Purpose

Business Objects constitute the operational layer of the Orion architecture.

They record persistent business information required to execute, control, or document Business Processes.

Business Objects provide the operational bridge between Business Processes, Business Relationships, Core Identities, and Module Entities.

---

## 2. Scope

This specification defines:

- Business Objects;
- Root Business Objects;
- Child Business Objects;
- Business Object hierarchy;
- Business Object lifecycle;
- Business Object relationships with Business Processes;
- Business Object relationships with Business Relationships;
- Business Object relationships with Core Identities and Module Entities.

It does not define specific Business Object types.

## 3. Business Object

### 3.1. Definition

A **Business Object** is a persistent operational artefact that records business information required to execute, control, or document a Business Process.

Business Objects represent operational state rather than business actors.

Business Objects may be created, modified, or retired during execution of Business Activities.

---

### 3.2. Characteristics

Every Business Object:

- has a unique identity;
- has a lifecycle;
- belongs to exactly one Business Object hierarchy;
- may reference Core Identities;
- may reference Module Entities;
- exists within the operational context of a Business Process.

### 3.3. Responsibilities

A Business Object may:

- record business information;
- coordinate Business Activities;
- reference Business Relationships;
- establish or modify Business Relationships (Root Business Objects only).

Business Objects never define business semantics of identities or relationships.

---

## 4. Root Business Object

### 4.1. Definition

A **Root Business Object** is an independent Business Object that represents the primary operational artefact of a Business Object hierarchy.

### 4.2. Characteristics

A Root Business Object:

- has no parent Business Object;
- may establish or modify a Business Relationship;
- may optionally be associated with a Business Process;
- defines the operational context for all Child Business Objects.

### Examples

- Employment Agreement
- Sales Agreement
- Purchase Order
- Service Agreement
- Loan Agreement


## 5. Child Business Object

### 5.1. Definition

A **Child Business Object** is a Business Object whose business meaning depends upon another Business Object.

### 5.2. Characteristics

A Child Business Object:

- has exactly one parent Business Object;
- belongs to exactly one Business Object hierarchy;
- inherits the Business Process from the Root Business Object;
- operates within the Business Relationship established by the Root Business Object;
- never establishes or modifies a Business Relationship directly.

### Examples

- Shipment Note
- Payment
- Time Record

## 6. Business Object Hierarchy

A Business Object hierarchy consists of:

- one Root Business Object;
- zero or more Child Business Objects.

The hierarchy represents one operational context.

Business Process assignment, where present, applies to the Root Business Object and is inherited by all descendants.

## 7. Business Object Lifecycle

Business Objects have independent lifecycles.

Business Activities may:

- create Business Objects;
- modify Business Objects;
- change Business Object status;
- retire Business Objects.

Changes of Business Object status do not create new Business Objects.

## 8. Relationship with Business Processes

Business Processes provide the operational context in which Business Objects are created, modified, and used.

Business Activities performed within a Business Process may create new Business Objects or modify existing ones.

Business Objects record business information resulting from Business Activities.

Not every Business Object represents the final output of a Business Process.

## 9. Relationship with Business Relationships

Business Relationships define structural associations between Core Identities.

Business Objects operate within those relationships.

Only Root Business Objects may establish or modify Business Relationships.

Child Business Objects operate within the Business Relationship established by their Root Business Object.

## 10. Relationship with Identities

Business Objects may reference:

- Core Identities;
- Module Entities.

Only Core Identities participate directly in Business Relationships.

Module Entities remain local to their functional modules.

Business Objects provide the operational bridge between Module Entities and the Core Identity Model.

## 11. Invariants

### BO-001

Every Business Object belongs to exactly one Business Object hierarchy.

### BO-002

Every Business Object hierarchy has exactly one Root Business Object.

### BO-003

Only Root Business Objects may establish or modify Business Relationships.

### BO-004

Every Child Business Object has exactly one parent Business Object.

### BO-005

If a Root Business Object is associated with a Business Process, all Child Business Objects inherit that Business Process from the Root Business Object.

### BO-006

Business Activities may create new Business Objects or modify existing Business Objects.

Changes of Business Object status do not create new Business Objects.

### BO-007

Business Objects may reference both Core Identities and Module Entities.

Only Core Identities participate directly in Business Relationships.


## 12. Notes

Structural components of a Business Object (for example, invoice lines or purchase order lines) are not Business Objects unless they possess an independent business identity and lifecycle.

## 13. Related Documents

- ARCH-003

