# Phase 1 - Core Domain Foundation

# Milestone 1.6 — Core Model Implementation

## Step 1 — Reorganize the `masterdata` app ✅ COMPLETE

Target:
```
masterdata/
└── models/
    ├── organization.py
    |
    ├── base/
    │   └── core_entity_base.py
    |    
    ├── entities/
    │   ├── party.py
    │   ├── person.py
    │   ├── product.py
    │   ├── asset.py
    │   ├── project.py
    │   ├── department.py
    │   └── responsibility_center.py
    |
    ├── associations/
    │   ├── business_relationship.py
    │   ├── business_relationship_participant.py
    │   ├── identity_relationship.py
    │   └── structural_relationship.py
    |
    ├── classifications/
    │   ├── role_type.py
    │   └── relationship_type.py
    |
    └── operations/
        ├── business_process.py
        └── business_object.py
```

## Step 2 — Update imports ✅ COMPLETE
```
masterdata/models/__init__.py

from .organization import Organization

from .entities.party import Party
from .entities.person import Person

from .associations.business_relationship import BusinessRelationship
from .associations.business_relationship_participant import BusinessRelationshipParticipant

from .operations.business_process import BusinessProcess
from .operations.business_object import BusinessObject
```

At this point there should be no database changes.

Running:

`python manage.py makemigrations`

should produce:

`No changes detected`

## Step 3 Create Core Entities ✅ COMPLETE

### Step 3.1 Create CoreEntityBase ✅ COMPLETE
```
models/
    base/
        __init__.py
        core_entity_base.py
```

### Step 3.2 Implement Product ✅ COMPLETE
```
models/
    entities/
        product.py
```

### Step 3.3	Implement Asset	✅ COMPLETE
```
models/
    entities/
        asset.py
```

### Step 3.4	Implement Project	✅ COMPLETE
```
models/
    entities/
        project.py
```

### Step 3.5	Implement Department ✅ COMPLETE
```
models/
    entities/
        department.py
```

### Step 3.6	Implement ResponsibilityCenter ✅ COMPLETE
```
models/
    entities/
        responsibility-center.py
```
## Step 4. Implement Department - Responsibility Center Relationship ❌ DISCARDED
```
models/
    associations/
        structural_relationships/
            department_responsibility_center.py
```
## Step 4. Implement Role Type ✅ COMPLETE
```
masterdata/
    models/
        classifications/
            role_type.py
```

## Step 5. Department Associations ✅ COMPLETE

Changed the `Department` model to accommodate direct links to Company and Responsibility Center

**Removed**
```
models/
    associations/
        structural_relationships/
            department_responsibility_center.py
```

## Step 6. ✅ COMPLETE

```
apps/
└── masterdata/
    └── services/
        ├── __init__.py
        └── department_hierarchy_service.py
```

### Migrations
```
apps\masterdata\migrations\0010_asset_product_project_roletype_party_created_at_and_more.py
apps\masterdata\migrations\0011_alter_department_root_department.py
apps\masterdata\migrations\0012_alter_department_company.py
```

## Step 7. Tests ✅ COMPLETE

### Test 1. Create a root department ✅ PASS

- Create a company
- Create a root department
- Assert:
    - department.company == company
    - department.root_department = department
    - department.parent_department = None

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_initialize_root_department -v 2`

### Test 2. Create child department ✅ PASS

Assert:
- root_department == parent.root_department
- company == parent.company
- responsibility_center == parent.responsibility_center

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_initialize_child_department`

### Test 3. Assign company to root ✅ PASS

`def test_assign_company_propagates(self):`

Hierarchy:
```
Root
 └── Child
      └── Grandchild
```
Assign company to Root.

Assert all three departments receive the company.

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_assign_company_propagates`

### Test 4. Change parent ✅ PASS

`def test_change_parent_propagates_new_inherited_attributes(self):`

```
A
 └── X

B
```
Move X under B.

Assert:
- parent updated
- root updated
- company inherited from B
- responsibility center inherited from B

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_change_parent_propagates_new_inherited_attributes`

### Test 5. Circular hierarchy ✅ PASS

```
A
 └── B
      └── C
```
Attempt

A.parent = C

Expect

`ValidationError`

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_circular_parent_assignment_raises_validation_error`

### Test 6. Root company restriction ✅ PASS

Create child department.

Attempt

assign_company(child, company)

Expect

`ValidationError`

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_child_department_cannot_be_assigned_company`

### Test 7. Responsibility Center propagation ✅ PASS

Assign RC to root.

Verify entire subtree inherits it.

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_root_responsibility_center_propagates_to_children`

### Test 8. Leaf RC validation ✅ PASS

Create a non-leaf Responsibility Center.

Attempt assignment.

Expect

`ValidationError`

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_responsibility_center_must_be_leaf`

### Test 9. RC override validation ✅ PASS

Parent already has RC.

Attempt to assign a different RC to child.

Expect

`ValidationError`

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_responsibility_center_cannot_override_parent`

### Test 10. Orphan validation ✅ PASS

Attempt initialization with
```
parent=None
company=None
```
Expect

`ValidationError`

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_department_cannot_be_orphan_at_creation`

Attempt making a department orphaned

`$ python manage.py test apps.masterdata.tests.test_department_hierarchy_service.DepartmentHierarchyServiceTests.test_department_cannot_be_orphaned`


### Commit

S01.M01.06.01 Core Model Implementation
