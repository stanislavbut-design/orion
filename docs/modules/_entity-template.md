# Entity Specification

## 1. Purpose

Why the entity exists.

---

## 2. Definition

A concise, normative business definition.

Usually one paragraph.

---

## 3. Conceptual Diagrams

One or more diagrams illustrating the entity's place in the domain model.

Business Structure
```text
Identity
├── Organization
├── Party
└── Person
```
or
```text
Organization
      │
      └── owns
             │
             ▼
           Party
```
Section 3 can simply contain multiple diagrams, each with a short title, for example:
### Business Structure

...

### Ownership

...

### Role Assignment

---

## 4. Responsibilities

What the entity is responsible for. Not what it stores.

---

## 5. Identity

Technical identifiers (id, public_id) should be mentioned only if they help explain the concept, not as implementation details.

| Attribute | Notes         |
| --------- | ------------- |
| Name      | Business name |

---

## 6. Lifecycle

Creation, modification, archival, deletion.

---

## 7. Relationships

Narrative description of relationships with other entities.

---

## 8. Business Rules

Stable identifiers:

ORG-001
PTY-001
PER-001

## 9. Planned Attributes

| Attribute | Required | Description |
| --------- | -------- | ----------- |

## 10. Notes

Future considerations, open questions, rationale.

## 10. Related Documents

For example:

ARCH-003
ADR-001
ADR-007
STD-001
