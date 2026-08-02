# Project Specification

## 1. Purpose

A **Project** represents a persistent enterprise initiative undertaken to achieve a defined business objective.

A Project provides a common reference point for Business Objects originating from multiple Business Processes and business capabilities.

---

## 2. Definition

**A Project is a Core Entity representing a persistent body of work undertaken by an Organization to achieve one or more organizational objectives within a defined scope.**

A Project exists independently of individual Business Processes and Business Objects.

Business Objects may reference a Project throughout its lifecycle.

---

## 3. Responsibilities

A Project shall:

- provide a stable identity for an enterprise initiative;
- maintain its own lifecycle;
- serve as a common reference across business capabilities;
- support reporting across multiple operational areas;
- support extension by specialised modules

A Project **shall not**:

- execute Business Processes;
- manage tasks;
- schedule resources;
- manage milestones;
- calculate profitability.

These responsibilities belong to specialised modules.

---

## 4. Architectural Classification

| Property         | Value                              |
| ---------------- | ---------------------------------- |
| Structural Layer | Core Entity                        |
| Category         | Enterprise Object *(working term)* |
| Owner            | Organization                       |
| Lifecycle        | Independent                        |
| Referenced by    | Business Objects                   |
| Cross-module     | Yes                                |

---

## 5. Scope

A Project may represent:

- customer engagements;
- internal improvement initiatives;
- implementation projects;
- research projects;
- investment projects;
- compliance projects.

The Core deliberately does not distinguish between project types.

A Project has an independent existence and identity. Its lifecycle management is delegated to the Project Management capability.

---

## 6. Relationships

A Project:

- belongs to one Organization;
- may be referenced by multiple Business Objects;
- does not participate directly in Business Relationships;
- may participate in Structural Associations in future if required.

---

## 7. Business Rules

### PRJ-001

A Project shall have a Name.

### PRJ-002

A Project may have a Description.

### PRJ-003

Every Project shall have a unique persistent identity.

### PRJ-004

A Project belongs to exactly one Organization.

(Implicit through ADR-009.)

### PRJ-005

A Project shall not participate directly in a Business Relationship.

### PRJ-006

A Business Object may reference a Project when the recorded business activity occurs within the context of that Project.

### PRJ-007

A Project may exist independently of any Business Object.

## 8. Lifecycle

Typical lifecycle:
```
Planned
    ↓
Approved
    ↓
Active
    ↓
Completed
    ↓
Closed
```
The exact lifecycle is implementation-dependent.

The Core only requires that a Project possesses an independent lifecycle.

## 9. Cross-module Usage

Potential consumers include:

| Capability | Usage                  |
| ---------- | ---------------------- |
| Sales      | Customer projects      |
| Purchases  | Procurement by project |
| Inventory  | Material consumption   |
| Assets     | Capital projects       |
| Payroll    | Labour allocation      |
| Accounting | Cost allocation        |
| Reporting  | Project reporting      |

## 10. Core Attributes
```
Project
├── public_id       required
├── name            required
└── description     optional
```

## 11. Future Extensions

Specialised modules may extend a Project with:

- tasks;
- milestones;
- budgets;
- schedules;
- resource allocation;
- risks;
- profitability;
- portfolio management.

The Core Project model shall remain independent of these concerns.
