# Identity Resolution Service Architecture

## 1. Purpose

The **Identity Resolution Service** is the architectural component responsible for executing the Identity Resolution Protocol.

It performs identity resolution on behalf of functional modules while preserving the independence of the Core Domain.

The service owns no business workflow and contains no module-specific business rules.

---

## 2. Responsibilities

The **Identity Resolution Service** is responsible for:

- receiving identity resolution requests;
- searching for existing Core Identities;
- determining the appropriate resolution outcome;
- creating Core Identities when required;
- establishing traceability;
- returning the resolution result.


The service shall not:

- manage module workflows;
- modify module entities;
- interpret module lifecycle states.

---

## 3. Inputs

The service receives:

- the requesting module;
- the requesting Module Entity;
- the target Core Identity type;
- identity attributes required for matching.

The service does not prescribe the internal structure of module entities.

---

## 4. Outputs

The service returns exactly one resolution result.

Possible outcomes are:

- Existing Core Identity associated.
- New Core Identity created.
- Manual resolution required.
- Resolution failed.

The result shall be explicit and deterministic.

---

## 5. Identity Matching

The service delegates identity matching to identity-specific matching strategies.

Matching rules depend upon the target Core Identity.

Examples:

| Core Identity |	Possible matching attributes |
|---------------|------------------------------|
| Person	| Personal ID, name, birth date |
| Party |	Business ID, legal name |
| Product (future) | Product code |

The Identity Resolution Service coordinates matching but does not define matching rules.

---

## 6. Core Identity Creation

When no suitable identity exists, the service may create a new Core Identity.

Creation shall satisfy all invariants of the target identity.

Creation shall occur only once for a given resolution request.

---

## 7. Traceability

The service establishes the permanent association between:
```
Module Entity
        │
        ▼
Core Identity
```
The service does not determine how modules persist this association.

---

## 8. Extension Principle

The service shall support future Core Identity types without modification of its public interface.

Adding a new Core Identity shall require only the addition of an identity-specific matching strategy.

---

## 9. Dependency Direction
```
Functional Module
        │
        ▼
Identity Resolution Service
        │
        ▼
Identity Matching Strategy
        │
        ▼
Core Identity
```
Dependencies always point toward the Core Domain.

---

## 10. Architectural Invariants

### IRS-001

The Identity Resolution Service owns no business workflow.

### IRS-002

The service shall execute the Identity Resolution Protocol.

### IRS-003

The service shall return exactly one deterministic resolution outcome.

### IRS-004

Identity-specific matching rules are delegated to matching strategies.

### IRS-005

The public interface of the service shall remain independent of individual functional modules.

### IRS-006

The service shall remain extensible to future Core Identity types.
