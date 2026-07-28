# Module Integration Pattern

## 1. Purpose

The Module Integration Pattern defines the architectural contract by which functional modules participate in the Orion Core Domain while remaining independent of it.

The pattern specifies how module-specific models interact with the Core through Identity Resolution without requiring inheritance from common framework classes.

---

## 2. Principle

Each functional module shall define its own models according to its business requirements.

The Core Domain shall not prescribe a common base model for Module Entities.

Module models remain independent and encapsulate their own business semantics.

---

## 3. Eligibility

A module model becomes eligible for Identity Resolution by implementing the Module Integration Pattern.

Module eligibility is determined by behavior rather than inheritance.

---

## 4. Required Capabilities

A module model participating in Identity Resolution shall provide:

### Identity information

The information required to identify or create a Core Identity.

**Examples include:**

- personal names;
- legal names;
- business identifiers;
- tax identifiers;
- contact information.

The required data depends upon the Core Identity being resolved.

### Lifecycle

The module shall manage its own lifecycle.

**Examples:**
```
Lead
──────────────
New
Contacted
Qualified
Won
Lost
```

```
Applicant
──────────────
Applied
Interviewed
Offered
Hired
Rejected
```

Lifecycle management remains entirely within the module.

### Identity Resolution trigger

The module determines when Identity Resolution shall be requested.

**Examples include:**

- Hire Applicant
- Win Lead
- Approve Supplier Candidate

The Core shall not determine when resolution occurs.

### Traceability

The module shall permanently retain the association with the resolved Core Identity.

---

## 5. Responsibilities

### Module

Responsible for:

- business workflow;
- lifecycle management;
- user interaction;
- deciding when Identity Resolution is required.

### Core

Responsible for:

- Identity Resolution;
- duplicate prevention;
- Core Identity creation;
- traceability support.

---

## 6. Dependency Direction

The dependency graph shall remain:
```
Functional Module
        │
        ▼
Identity Resolution Service
        │
        ▼
Core Domain
```
The Core Domain shall never depend upon a functional module.

---

## 7. Extension Principle

Functional modules may introduce additional Module Entities without modification of the Core Domain.

Examples:
```
CRM
 └── Lead

HR
 └── Applicant

Procurement
 └── Supplier Candidate

Future modules
 └── Additional entities
```
The architecture therefore remains open for extension while closed for modification.

---

## 8. Architectural Invariants

### MIP-001

Each module defines its own operational models.

### MIP-002

The Core Domain shall not require Module Entities to inherit from a common base class.

### MIP-003

Module participation in Identity Resolution is defined by architectural contract rather than inheritance.

### MIP-004

Module lifecycle management remains entirely within the module.

### MIP-005

The Core Domain remains independent of all functional modules.