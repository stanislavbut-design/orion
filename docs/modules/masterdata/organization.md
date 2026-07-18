# Organization Specification

## 1. Purpose

An Organisation identifies the Orion installation.

## 2. Definition

An Organization represents the entire business managed by an Orion installation.

## 3. Responsibilities

An Organization:
- defines ownership boundary;
- owns Parties;
- owns Persons.

## 4. Identity

| Attribute | Notes         |
| --------- | ------------- |
| Name      | Business name |

## 5. Lifecycle

An Organization:
- created once;
- never deleted;
- name may change.

## 6. Relationships

```text
Organization
├── owns Parties
└── owns Persons
```

## 7. Business Rules

**ORG-001**
Exactly one Organization shall exist in an Orion installation.

**ORG-002**
An Organization owns all Parties.

**ORG-003**
An Organization owns all Persons.

**ORG-004**
An Organization shall not be deleted.

**ORG-005**
The Organization name may be changed.

## 8. Planned Attributes

| Attribute | Required | Description |
| --------- | -------- | ----------- |
| None

## 9. Notes

Future multi-organization support

## 10. Related Documents

- ARCH-003
- ADR-001
- ADR-007