# DEV-001 — Workflow

**Status:** Approved  

**Date:** 2026-07-18

---

## Purpose

This document defines the standard development workflow for the Orion project.

Its purpose is to establish a common vocabulary, ensure consistent planning and execution, and provide a traceable relationship between planning, implementation, documentation, and source control.

---

## Scope

This document applies to all development activities within the Orion project.

---

## Workflow Hierarchy

Development work shall be organized using the following hierarchy:

```text
Project
│
├── Stage
│     │
│     ├── Milestone
│     │      │
│     │      ├── Step
│     │      │
│     │      └── Commit
```

---

## Definitions

### Project

The complete Orion development effort.

A project consists of one or more stages.

---

### Stage

A major development period with a strategic objective.

A stage consists of one or more milestones.

Examples:

- Stage 0 — Foundation
- Stage 1 — Core Domain
- Stage 2 — Finance

---

### Milestone

A measurable achievement within a stage.

Each milestone shall define:

- Objective
- Deliverables
- Acceptance Criteria

A milestone is considered complete only after all acceptance criteria have been satisfied.

---

### Step

A planned engineering activity.

A step is the smallest unit of planned work.

Examples:

- Create the `masterdata` application.
- Implement the `Party` model.
- Register the model in Django Admin.
- Create the initial migration.

---

### Commit

A source control record representing one or more completed steps.

Commits document implementation history.

A commit shall leave the project in a consistent and working state.

Commit messages shall follow the convention defined in STD-003 — Git. Each commit should normally correspond to a single completed Step and reference its associated Stage and Milestone.

---

### Working state

A working state is one in which the project builds successfully, migrations are consistent, tests relevant to the change pass, and the application starts without known errors.

---

## Planning Principles

### General

Development work shall be planned before implementation begins.

Planning shall proceed from larger objectives toward executable steps.

---

### Stage Planning

Each stage shall define:

- Objective
- Expected outcomes
- Major milestones

---

### Milestone Planning

Each milestone shall define:

- Objective
- Deliverables
- Acceptance Criteria

---

### Step Planning

Steps shall:

- be executable,
- have a clearly defined outcome,
- normally be completed within a single working session.

---

## Implementation Principles

### Incremental Development

Implementation shall proceed in small, verifiable increments.

The project shall remain in a working state after each completed step whenever practical.

---

### Documentation

Documentation shall be updated as part of the same logical change as the implementation.

Implementation affecting architecture, standards, or development practices shall not be considered complete until the corresponding documentation has been updated.

---

### Verification

Each completed milestone shall be verified against its acceptance criteria.

A Step shall be considered complete only when:

- The implementation satisfies the approved entity specification.
- All applicable business rules are enforced, or explicitly deferred with documented justification.
- The project passes verification (tests, migrations, system checks, etc.).
- The implementation is committed according to the Git convention defined in STD-003.

---

## Commits

Commits shall:

- represent a logical unit of work,
- leave the project in a working state,
- include related documentation updates where applicable.

A commit may include the outcomes of one or more completed steps.

---

## Traceability

Development artifacts shall be traceable.

The following relationships should exist where practical:

- Stage → Milestones
- Milestone → Steps
- Steps → Commits
- Commits → Documentation

---

## Related Documents

- STD-003 — Git
- STD-004 — Documentation
- ARCH-004 — Repository Structure