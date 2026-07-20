# Party Specification

## 1. Purpose

A Party represents an identifiable business participant within an Organization.

A Party provides a stable business identity independent of the roles it may perform. It is the central identity through which Orion records and manages interactions with external and internal business participants.

---

## 2. Definition

A Party is an identifiable business entity belonging to the Organization.

A Party does not define its business function. Instead, it may assume one or more Roles within different Business Processes over time.

Examples include companies, sole traders, government authorities, banks, non-profit organizations, and other identifiable organizations with which the Organization interacts.

---

## 3. Conceptual Diagrams


### Business Structure
```text
Identity
├── Organization
├── Party
└── Person
```
### Ownership
```text
Organization
      │
      └── owns
             │
             ▼
           Party
```



### Role Assignment
```text
Party
   │
   └── plays
          │
          ▼
        Role
```
A Party may perform multiple Roles simultaneously or acquire new Roles throughout its lifecycle.

---

## 4. Responsibilities

A Party is responsible for:

- providing a stable business identity;
- serving as the owner of one or more Roles;
- acting as the anchor point for business relationships;
- participating in Business Processes through its assigned Roles.

A Party shall not contain business-process-specific information.

---

## 5. Identity

### Business Identity

| Attribute | Notes         |
| --------- | ------------- |
| Name      | Abbreviated name or business name used throughout Orion |
| Party Type | Indicates whether the Party represents a legal entity or an individual |
| Legal Name | Registered legal name of the company or the person's full legal name |
| Business ID | Company registration number, personal tax number, or another applicable official identifier |
| Party Code | Internal business code used for numbering schemes, references, reporting and quick identification |

### Technical Identity

Each Party is identified internally by:
- surrogate primary key (`id`);
- immutable public identifier (`public_id`).

Technical identifiers are implementation details and do not form part of the business identity.

---

## 6. Lifecycle

A Party:
- is created when first recorded by the Organization;
- may be renamed;
- may acquire additional Roles throughout its lifecycle;
- shall normally remain in the system even after it is no longer active in business operations.

Deletion policy will be defined separately.

---

## 7. Relationships

  A Party:
  - belongs to exactly one Organization;
  - may own zero or more Role Assignments;
  - may participate in zero or more Business Relationships;
  - may be associated with zero or more Addresses;
  - may be associated with zero or more Contact Methods;
  - may be related to zero or more Persons.

---

## 8. Business Rules

### PTY-001

Every Party shall belong to exactly one Organization.

---

### PTY-002

A Party shall have a Name. 

A Party may additionally have a Legal Name and a Business ID.

---

### PTY-003

Every Party shall be classified as either a Legal Entity or an Individual.

---

### PTY-004

A Party may perform zero or more Roles.

---

### PTY-005

A Party shall remain independent of any specific Business Process.

---

### PTY-006

A Party classified as an Individual shall be associated with exactly one Person through an Identity Relationship of type Embodiment.

A Party of any type may be associated through Identity Relationships of type Representation with any number of Persons.

### PTY-007

If assigned, a Party Code shall be unique within the Organization.

---

## 9. Planned Attributes

Additional attributes will be introduced as business requirements emerge.

## 10. Notes

Customer, Supplier, Partner, Employee and similar concepts are **Roles**, not Parties.

Separating identity from roles ensures that a business participant maintains a single identity regardless of the number of functions it performs within Orion.

This approach minimizes duplication and preserves a consistent business identity throughout the system.

## 10. Related Documents

- ARCH-003 — Domain Model
- ADR-001 — Vision and Scope of Orion
- ADR-007 — Entity Identification
- STD-001 — Coding Standards

