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

## Step 2 — Define Business Relationship Framework ✅ COMPLETED

`business-relationship-framework.md`

### Commit 2:

S01-M01.02.02 Define Business Relationship Framework

## Step 3 — Relationship and Role constants ✅ COMPLETED

### Commit 3:

S01-M01.02.03 Define Relationship and Role constants

## Step 4. Implement BusinessRelationship model ✅ COMPLETED

### Commit 4:

S01-M01.02.04 Implement BusinessRelationship model

## Step 5. BusinessRelationshipParticipant model ✅ COMPLETED

`apps/masterdata/models/business_relationship_participant.py`

### Commit 5:

S01-M01.02.05 Implement BusinessRelationshipParticipant model

## Step 6. Validation ✅ COMPLETED

### Task 1. Create validation messages
`apps/core/constants/validation/masterdata.py`

### Task 2. Relationship Matrix constants

Create `apps/core/constants/relationship_matrix.py`

### Task 3. Imports

In `business_relationship_participant.py`

### Task 4. Add clean()

### Commit 6

S01-M01.02.06 Implement Relationship Framework validation

## Step 7. Testing ✅ COMPLETED

### Test 1 

Create a valid **Employment** relationship

Pass

### Test 2

Create a **BusinessRelationshipParticipant** with both a ***Party*** and a ***Person*** populated.

Expected result:

`Exactly one of Organization, Party or Person shall be specified.`

Pass

### Test 3 — No identity specified

Create a new **BusinessRelationshipParticipant** and leave all three identity fields empty:

Organization: (hidden by Admin)
Party: empty
Person: empty

Choose a valid:

Business Relationship
Role Type (for example, Employee)

Save.

Expected result

`Validation error: Exactly one of Organization, Party or Person shall be specified.`

Pass

### Test 4 — Role ↔ Identity validation

Now let's verify that a Role Type is compatible with the selected Identity Type.

**Scenario**

Use an existing Employment relationship.

Create a participant with:

Role Type: Director
Party: select any Company (Party)
Person: empty

Save.

Expected result

Validation error:

`The selected Role Type is not valid for the specified Identity.`

Tests 3 and 4 passed. But there's another issue: When I add new BusinessRelationshipParticipant with valid set of attributes, e.g.: Business Relationship = EMPLOYMENT Role Type = Employee Person specified It saves correctly. But when I open it for editing, no changes is made, it fails with a validation error "Exactly one of Organization, Party or Person shall be specified." The same for other types of relationship.

### Test 5 — Relationship ↔ Role validation

Create a participant with:

Relationship Type: EMPLOYMENT
Role: Supplier
Person or Party chosen appropriately

Expected:

`The selected Role Type is not permitted for this Relationship Type.`

Passed

### Test 6 — Effective date validation

Create a participant with

effective_from = 01.01.2026
effective_to   = 31.12.2025

Expected:

`Effective To must not precede Effective From.`

Passed

## Step 8 — Architecture Refactoring ✅ COMPLETED

### 8.1 Remove ownership from business models

Remove the ownership FK from:

Party
Person
BusinessRelationship
BusinessRelationshipParticipant

Generate a migration.

### 8.2 Simplify Admin

Remove:

OrganizationOwnedAdminMixin
exclude = ("organization",)

### 8.3 Introduce Organization as a participant identity

Add a genuine participant field:

organization
party
person

to BusinessRelationshipParticipant.

Now the validation becomes semantically correct.

### 8.4 Update validation

Identity validation now counts:

organization
party
person

only.

No infrastructure concepts remain.

### 8.5 Clean constants

Rename any messages or comments referring to the ownership Organization where necessary.

## Step 9 — Regression Testing ✅ COMPLETED

Repeat all **Step 7** tests.

### Test 1 

Create a valid **Employment** relationship

Pass

### Test 2

Create a **BusinessRelationshipParticipant** with both a ***Party*** and a ***Person*** populated.

Passed

### Test 3 — No identity specified

Passed

### Test 4 — Role ↔ Identity validation

Passed

### Test 5 — Relationship ↔ Role validation

Passed

### Test 6 — Effective date validation

Passed

### Test 7

Additionally, verify the scenario that exposed today's issue:

Create participant.
Save.
Reopen.
Edit.
Save again.

Expected: No validation error.

Passed

### Commit 7

S01-M01.02.07 Architecture Refactoring

## Step 10 — Documentation ✅ COMPLETED

- ARCH-001
- ARCH-003
- STD-003
- ADR-009

### Commit 8

S01-M01.02.08 Documentation Update


## Step 11 — Complete Identity Integrity Validation ✅ COMPLETED

### Task 11.1 Individual Party requires Person

If party_type == INDIVIDUAL then person != None

### Task 11.2 Non-individual Party must not reference Person

If party_type != INDIVIDUAL then person == None

This prevents accidental assignment of a Person to a Company, Government Agency, Charity, etc.

### Task 11.3 One-to-one mapping

A Person may belong to exactly one Individual Party.

Implementation is straightforward:
```
Party.objects.filter(
    person=self.person,
    party_type=PartyType.INDIVIDUAL,
).exclude(pk=self.pk).exists()
```
If one exists, raise the corresponding validation error.

### Task 11.4 Validation messages

Following the new constants policy, the messages belong in

apps/core/constants/validation/masterdata.py

Something like:
```
PTY_INDIVIDUAL_PERSON_REQUIRED = (
    "An Individual Party must be associated with a Person."
)

PTY_PERSON_NOT_ALLOWED = (
    "Only Individual Parties may be associated with a Person."
)

PTY_PERSON_ALREADY_ASSOCIATED = (
    "The selected Person is already associated with another Individual Party."
)
```

### Task 11.5 Tests

Three tests should be sufficient:

✅ Create Individual Party without Person → fails.
✅ Create Company with Person assigned → fails.
✅ Associate the same Person with two Individual Parties → fails.

Passed

### Commit 9

S01-M01.02.09 Complete Identity Integrity Validation