# Stage 1 - Core Domain Foundation

# Milestone 1.2 — Relationship Framework

## Step 1 — Define the Relationship architecture ✅ COMPLETED

### Deliverables

- Review and refine ARCH-003 to finalise.
- Business Architecture
- Core Concepts
- Identity Architecture
- Relationship Matrix
- Architectural Principles

### Commit 1:

S01-M01.02.01 Refine ARCH-003 architectural baseline


## Step 2 — Define Business Relationship Framework

`business-relationship-framework.md`

### Commit 2:

S01-M01.02.02 Define Business Relationship Framework

## Step 3 — Relationship and Role constants

S01-M01.02.03 Define Relationship and Role constants







## Step 5 — Define Party–Role relationships

This is where we establish how a Party acquires Roles.

Questions to settle include:

- Can a Party hold multiple Roles simultaneously? (I believe yes.)
- Can the same Role be assigned to multiple Parties? (Again, yes.)
- Should assignments have effective dates? (Initially no; later yes.)


We'll document the relationship before implementing it.

## Step 6 — Implement Role assignments

Create the entity that associates a Party with a Role.

Initially it might include:

- Party
- Role
- Active flag


Future versions could add:

- Effective From
- Effective To
- Assignment reason

## Step 7 — Validate the framework

Test scenarios such as:

- One Party with multiple Roles.
- Multiple Parties sharing the same Role.
- An Individual Party acting as both Customer and Supplier.
- A legal entity acting as both Supplier and Employer.

## Step 8 — Documentation and review

Update ARCH-003 if necessary.
Update the repository roadmap.
Review naming consistency.

## Commit 8
S01-M01.02.08 Complete Role Frameworkt

---

