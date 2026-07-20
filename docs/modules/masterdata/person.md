# Person Specification

## 1. Purpose

A Person provides a stable business identity independent of the roles it may perform. It is the central identity through which Orion records and manages interactions with individuals.

---

## 2. Definition

A Person represents an individual known to Orion.

A Person is structurally independent of any particular Party and may be associated with one or more Parties through Identity Relationships.

---

## 3. Conceptual Diagrams

### Business Structure
```text
Identity
├── Organization
├── Party
└── Person
```

### Business Structure

...

### Ownership
```text
Organization
      │
      └── owns
             │
             ▼
           Person
```
...

### Role Assignment
```text
Person
   │
   └── plays
          │
          ▼
        Role
```
A Person may perform multiple Roles simultaneously or acquire new Roles throughout its lifecycle.

---

## 4. Responsibilities

A Person is responsible for:

- providing a stable business identity;
- serving as the owner of one or more Roles;
- acting as the anchor point for any kinds of relationships with individuals other than business relationship, for which Parties is responsible;
- participating in Business Processes through its assigned Roles.

A Person shall not contain business-process-specific information.

---

## 5. Identity

### Business Identity

| Attribute | Required | Editable | Notes|
|-------|-------------|----------|---------|
| First Name | ✓ | ✓ | Current legal first name
| Middle Name |  | ✓ | Current legal middle name
| Last Name | ✓ | ✓ | Current legal last name
| Full Name | ✓ | ✗ | Automatically maintained according to the Organization's naming format
| Short Name | ✓ | ✗ | Automatically maintained compact name used for display
| Personal ID |  | ✓ | Official identifier such as a tax number or national identification number


Full Name and Short Name are subject to organizational preference settings, and are regenerated automatically when name components change.

### Technical Identity

Each Person is identified internally by:
- surrogate primary key (`id`);
- immutable public identifier (`public_id`).

Technical identifiers are implementation details and do not form part of the business identity.

---

## 6. Lifecycle

A Person:
- is created when first recorded by the Organization;
- may be renamed;
- may acquire additional Roles throughout its lifecycle;
- shall normally remain in the system even after it is no longer active in business operations.

---

## 7. Relationships

A Person:
- belongs to exactly one Organization;
- may own zero or more Role Assignments;
- may participate in zero or more Business Relationships;
- may be associated with zero or more Addresses;
- may be associated with zero or more Contact Methods;
- may be related to zero or more Parties.

---

## 8. Business Rules

### PER-001

Every Person shall belong to exactly one Organization.

### PER-002

Every Person shall have a First Name and a Last Name.

A person may have a Middle Name.

A Person maintains the current legal name of the individual. Future versions of Orion may maintain historical names.

### PER-003

Full Name shall be automatically derived from the Person's name components according to the Organization's configured naming format.

### PER-004

Short Name shall be automatically derived from the Person's name components according to the Organization's configured short-name format.

### PER-005

A Person may be associated with zero or more Parties through Identity Relationships.


## 9. Planned Attributes

| Attribute | Required | Description |
| --------- | -------- | ----------- |

## 10. Notes

A Person maintains the current legal name of the individual. Name components are editable and always represent the current state.

A future version of Orion may maintain the history of Person names (and, if required, Party names). When implemented, name changes shall be recorded automatically whenever a user modifies the current name. The user shall be able to specify the date from which the new name becomes effective. Historical business documents shall continue to preserve the names that were effective when those documents were created.

The current implementation stores the current Personal ID only. Future versions of Orion may support multiple identifiers, temporal validity, issuing authorities, and identifier types through dedicated entities, in the same manner as Addresses, Contact Methods and Identity Documents.

## 10. Related Documents

- ARCH-003 — Domain Model
- ADR-001 — Vision and Scope of Orion
- ADR-007 — Entity Identification
- STD-001 — Coding Standards
