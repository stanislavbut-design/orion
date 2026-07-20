# Stage 1 - Core Domain Foundation

# Milestone 1.1 — Master Data Foundation

## Step 1 — Create the application ✅ COMPLETED

Create the `masterdata` Django app under apps/.

Add it to INSTALLED_APPS.

Verify the application starts correctly.


### Task 1. Create the application

From the repository root:

Activate virtual environment:

    python -m venv .venv
    source .venv/Scripts/activate

Create app:

    python manage.py startapp masterdata apps/masterdata

Django creates:

```text
apps/
└── masterdata/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py 
```
---

### Task 2. Configure `apps.py`

Verify it contains:

```
from django.apps import AppConfig

class MasterdataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.masterdata"
```

### Task 3. Register the application

In `config/settings.py`

add:

`"apps.masterdata",`

to INSTALLED_APPS.

### Task 4. Verify

Run:

`python manage.py check`

Expected:

`System check identified no issues (0 silenced).`

Run:

`python manage.py runserver`

The server should start normally.

### Task 5. Verify Git

`git status`

You should see something similar to:

```
new file: apps/masterdata/__init__.py
new file: apps/masterdata/admin.py
new file: apps/masterdata/apps.py
new file: apps/masterdata/models.py
...
modified: config/settings.py
```

No migrations should exist yet except the empty migrations/__init__.py.


### Commit 1:

S01-M01.01.01 Master Data Foundation

---

## Step 2 — Organize the application ✅ COMPLETED

### Objective

Transform the default Django application into Orion's standard application layout.

The goal is not to add functionality yet, but to establish a scalable structure that all future applications can follow.

### Task 1. Models package

Instead of:

`models.py`

we'll have:

```
models/
    __init__.py
```

### Task 2. Tests package

Likewise:

```
tests/
    __init__.py
```

instead of: `tests.py`

Create:

```text
    ├── templates/
    └── static/
```
### Commit 2

S01-M01.01.02 Organize masterdata application structure

---

## Step 3 — Implement `Organization` ✅ COMPLETED

### Objective

Implement the Organization entity and enforce its lifecycle in accordance with:
- ARCH-003 — Domain Model
- ADR-007 — Entity Identification
- `docs/modules/masterdata/organization.md`

At this step, we should implement only what the specification requires—no speculative fields or future-proofing beyond our approved architecture.

### Task 1. Create the model

Create: `apps/masterdata/models/organization.py`

The initial model should be intentionally minimal. From the specification, the business attributes are: `name`

From our architectural decisions, every entity will also have:
- surrogate primary key (`BigAutoField` provided by Django)
- public_id (`UUID`, immutable, for external references)

So I propose the first implementation to contain only:

```text
Organization
├── id
├── public_id
└── name
```
We can introduce a common base model later, once we've implemented several entities and have evidence that those fields are universally needed. That aligns with our principle of introducing complexity only when justified.

***apps/masterdata/models/organization.py***
```
import uuid

from django.core.exceptions import ValidationError
from django.db import models


class Organization(models.Model):
    """
    Represents the entire business managed by an Orion installation.

    An Organization is the highest-level identity in the Orion domain model.
    It defines the ownership boundary for all Parties and Persons.
    """
    SINGLETON_ERROR = (
        "Exactly one Organization may exist in an Orion installation."
    )

    # Duplicated intentionally.
    # A common base entity will be introduced only after shared
    # attributes have been validated across multiple domain entities.
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    name = models.CharField(
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ["name"]
    
    def clean(self):
        super().clean()

        if not self.pk and Organization.objects.exists():
            raise ValidationError(self.SINGLETON_ERROR)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
```

### Task 2. Export the model:

***apps/masterdata/models/__init__.py***

```
from .organization import Organization

__all__ = [
    "Organization",
]
```


### Task 3. Register in Django Admin

***apps/masterdata/admin.py***

```
from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "public_id",
    )

    search_fields = (
        "name",
    )

    readonly_fields = (
        "public_id",
    )

    ordering = (
        "name",
    )
```

### Task 4. Generate the migration

```
python manage.py makemigrations masterdata
```
Before applying it, open the generated migration and verify that it creates only:
- id
- public_id
- name

Then:
```
python manage.py migrate
```

### Task 5. Verify

Run:
```
python manage.py check
python manage.py runserver
```

Open Django Admin and verify that:

- **Organizations** appears in the sidebar.
- You can create an Organization.
- `public_id` is generated automatically.
- `public_id` is read-only.
- The object is displayed by its name.

### Commit 3

S01-M01.01.03 Implement Organization


## Step 4 — Complete Organization lifecycle ✅ COMPLETED

### Objective

Implement the remaining business rules governing the Organization lifecycle.

### Task 1 — Prevent creating additional Organizations from the Admin

Add to ***apps/masterdata/admin.py***
```
def has_add_permission(self, request):
    from .models import Organization
    return not Organization.objects.exists()
```
### Task 2 — Prevent deletion from the Admin

Still in `OrganizationAdmin`, add:
```
def has_delete_permission(self, request, obj=None):
    return False
```

### Task 3 — Prevent deletion in the model

Open:

***apps/masterdata/models/organization.py***

Add:
```
def delete(self, *args, **kwargs):
    raise ValidationError(
        "The Organization cannot be deleted."
    )
```
### Task 4 — Create a data migration

Generate an empty migration:

`python manage.py makemigrations masterdata --empty --name create_default_organization`

You'll get something like:

`apps/masterdata/migrations/0002_create_default_organization.py`

Edit it to create the default record using RunPython. This ensures every new Orion installation starts with exactly one Organization. 
```
from uuid import uuid4

from django.db import migrations


def create_default_organization(apps, schema_editor):
    Organization = apps.get_model("masterdata", "Organization")

    if not Organization.objects.exists():
        Organization.objects.create(
            public_id=uuid4(),
            name="New Organization",
        )


class Migration(migrations.Migration):

    dependencies = [
        ("masterdata", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_default_organization,
            # The Organization is part of the installation's
            # structural state and is therefore not removed on rollback.
            migrations.RunPython.noop,
        ),
    ]
```

### Task 5 — Verify

After applying migrations:

`python manage.py migrate`

Check that:
- Exactly one Organization exists.
- The Add button is gone.
- There is no Delete button.
- The name remains editable.

### Commit 4

S01-M01.01.04 Complete Organization lifecycle



---

## Step 5 — Implement `Party`

### Objective

Implement the foundational Party entity.

### Task 1. Entity specification

Update `Party.md` with the agreed refinements.
- Purpose
- Definition
- Conceptual Diagrams
- Responsibilities
- Identity
- Lifecycle
- Relationships
- Business Rules
- Planned Attributes
- Notes
- Related Documents

### Task 2. Create the model

`apps/masterdata/models/party.py`

```
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from .organization import Organization

PTY_EMPTY_PERSON_ERROR = (
        "A Party must have at least one Person associated with it."
    )

class PartyTypes(models.TextChoices):
    LEGAL_ENTITY = "LEGAL_ENTITY", "Legal Entity"
    INDIVIDUAL = "INDIVIDUAL", "Individual"

class Party(models.Model):

    # Duplicated intentionally.
    # A common base entity will be introduced only after shared
    # attributes have been validated across multiple domain entities.
    id = models.BigAutoField(
        primary_key=True,
    )
        
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="parties",
    )

    name = models.CharField(
        max_length=60,
        unique=True,
    )

    legal_name = models.CharField(
        max_length=200,
        blank=True,
    )

    party_type = models.CharField(
        max_length=20,
        choices=PartyTypes.choices,
        default=PartyTypes.LEGAL_ENTITY,
    )

    business_id = models.CharField(
        max_length=20,
        blank=False,
    )

    party_code = models.CharField(
        max_length=10,
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Party"
        verbose_name_plural = "Parties"

        constraints = [
            models.UniqueConstraint(
                fields=["organization", "party_code"],
                name="uq_party_party_code",
            ),
            
            models.CheckConstraint(
                condition=Q(party_type__in=[
                    PartyTypes.LEGAL_ENTITY,
                    PartyTypes.INDIVIDUAL,
                ]),
                name="chk_party_party_type",
            ),
        ]

    def __str__(self) -> str:
        return self.name
```
### Task 3. Register in the admin

Initially:
- list display:
    - name
    - party_type
    - legal_name
    - business_id
    - party_code
-search:
    - name
    - legal_name
    - business_id

### Task 4. Create and apply migrations
```
python manage.py makemigrations
python manage.py migrate
```
### Task 5. Test in the admin

Create at least:

- one legal entity;
- one sole trader (Party type = Person).

At this stage, the embodied Person doesn't exist yet—that will come in the next milestone.

### Commit 5:

S01-M01.01.05 Implement Party

---

## Step 6 — Implement `Person`

### Objective

Implement the foundational Person entity.

### Task 1. Create the Person Specification

`docs/modules/masterdata/entities/person.md`

### Task 2.  Implement the model

Create:

`apps/masterdata/models/person.py`

### Task 3. Register in Django Admin

Hide the Organization field and assign it automatically, exactly as we now do for Party.

### Task 4. Create and apply migrations
```
python manage.py makemigrations
python manage.py migrate
```
### Task 5. Test

### Commit 6

S01-M01.01.06 Implement Person

---

## Step 7 — Milestone Review

### Objectives
- Organization implemented
- Party implemented
- Person implemented
- Identity model established
- Django Admin operational
- Specifications synchronized with implementation

### Decisions made

- One model per file.
- Organization is a singleton.
- Organization assigned automatically in Admin.
- public_id on all business entities.
- Store derived names (full_name, short_name).
- Use named constants for validation and naming.
- Current-state identities only; temporal history deferred.
- Business rules drive validation.

### Technical debt

- Identity Relationships.
- Address entity.
- Contact Method entity.
- Identity Document entity.
- Temporal history.
- Organization naming preferences.
- Shared base entity.

### Commit 7

S01-M01.01.07 Complete Milestone 1.1

