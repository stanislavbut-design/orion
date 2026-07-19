# Organization Specification

## 1. Purpose

An Organisation identifies the Orion installation.

## 2. Definition

An Organization represents the entire business managed by an Orion installation.

The Organization is not business data; it is part of the system configuration.

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
- created once upon installation;
- never deleted;
- name may change.

## 6. Relationships

```text
Organization
├── owns Parties
└── owns Persons
```

## 7. Business Rules

### ORG-001
Exactly one Organization shall exist in an Orion installation.

### ORG-002
The Organization shall be created during installation.

### ORG-003
Users shall not create additional Organizations.

### ORG-004
Users shall not delete the Organization.

### ORG-005

Organizations are completely isolated from one another. Business data shall never be shared directly between Organizations.

### ORG-006

The Organization name may be changed.

---

## 8. Planned Attributes

| Attribute | Required | Description |
| --------- | -------- | ----------- |
| None

## 9. Notes

An Organisation is necessary for organising a multi-organization support in the future.

## 10. Related Documents

- ARCH-003
- ADR-001
- ADR-007