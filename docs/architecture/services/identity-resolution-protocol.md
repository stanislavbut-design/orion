# Identity Resolution Protocol

## Purpose

The **Identity Resolution Protocol** defines the architectural procedure by which a **Module Entity** becomes associated with a **Core Identity**.

The protocol guarantees identity consistency, preserves historical information, and prevents duplicate Core Identities.

## 1. Triggers

Identity Resolution may be initiated by one or more business events.

Examples include:

| Module | Business Event |
|--------|----------------|
| HR | Hire Applicant |
| CRM |	Win Lead |
| Procurement |	Approve Supplier Candidate |

The triggering event belongs to the functional module.

The Identity Resolution mechanism belongs to the Core architecture.

## 2. Resolution Sequence

Identity Resolution shall proceed through the following stages.

### Stage 1 — Collect Identity Data

The module gathers the identity attributes required for matching.

Examples:

- Legal name
- Personal name
- Business ID
- Tax number
- National identifier
- Email
- Phone

The Core does not prescribe which attributes shall be collected.

### Stage 2 — Search

The Core searches for matching Core Identities using configurable matching rules.

The result may be:

- no match;
- one match;
- multiple potential matches.

### Stage 3 — Resolution

The outcome shall be one of:

- associate an existing Core Identity;
- create a new Core Identity;
- require user confirmation.

The Core shall never automatically create duplicate identities.

### Stage 4 — Traceability

A permanent association shall be recorded between:

- the originating Module Entity; and
- the resolved Core Identity.

### Stage 5 — Continue Module Workflow

After successful resolution, the module continues its own workflow.

Identity Resolution does not determine business outcomes.

## 3. Responsibilities

### Core Domain

Responsible for:

- duplicate prevention;
- identity creation;
- identity association;
- traceability.

### Functional Module

Responsible for:

- business rules;
- workflow;
- lifecycle status;
- user interaction.

## 4. Idempotency

Identity Resolution shall be idempotent.

Executing the protocol multiple times for the same Module Entity shall not create additional Core Identities.

## 5. Promotion

Promotion is a business event that may invoke Identity Resolution.

Promotion does not replace the Module Entity.

Promotion does not modify historical records.

Promotion only changes the business meaning of the Module Entity within its owning module.

## 6. Architectural Invariants

### IRP-001

Identity Resolution shall either:

- associate an existing Core Identity; or
- create exactly one new Core Identity.

### IRP-002

Duplicate Core Identities shall not be created automatically.

### IRP-003

Every successful Identity Resolution shall preserve traceability.

### IRP-004

Identity Resolution shall be idempotent.

### IRP-005

Business workflow remains the responsibility of the owning module.