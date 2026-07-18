# Stage 1 - Core Domain Foundation

# Milestone 1.1 — Master Data Foundation

## Step 1 — Create the application ✅ COMPLETED

Create the `masterdata` Django app under apps/.

Add it to INSTALLED_APPS.

Verify the application starts correctly.


### 1. Create the application

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

### 2. Configure `apps.py`

Verify it contains:

```
from django.apps import AppConfig

class MasterdataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.masterdata"
```

### 3. Register the application

In `config/settings.py`

add:

`"apps.masterdata",`

to INSTALLED_APPS.

### 4. Verify

Run:

`python manage.py check`

Expected:

`System check identified no issues (0 silenced).`

Run:

`python manage.py runserver`

The server should start normally.

### 5. Verify Git

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


**Commit 1:** S01-M01.01.01 Master Data Foundation

---

## Step 2 — Organize the application ✅ COMPLETED

### Objective

Transform the default Django application into Orion's standard application layout.

The goal is not to add functionality yet, but to establish a scalable structure that all future applications can follow.

### 1. Models package

Instead of:

`models.py`

we'll have:

```
models/
    __init__.py
```

### 2. Tests package

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
**Commit 2:** S01-M01.01.02 Organize masterdata application structure

---

## Step 3 — Implement `Organization`

### Objective

Implement the Organization entity in accordance with:
- ARCH-003 — Domain Model
- ADR-007 — Entity Identification
- `docs/modules/masterdata/organization.md`

At this step, we should implement only what the specification requires—no speculative fields or future-proofing beyond our approved architecture.

### 1. Create the model

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

### 2. Export the model:

***apps/masterdata/models/__init__.py***

```
from .organization import Organization

__all__ = [
    "Organization",
]
```


### 3. Register in Django Admin

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

### 4. Generate the migration

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

### 5. Verify

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

7. Commit
S01-M01.01.03 Implement Organization




**Commit 3:**

---

## Step 4 — Implement `Party`

Create the second Identity entity.

Initially, only the structural attributes.

Register it.

Generate and apply the migration.

Verify.

**Commit 4:**

---

## Step 5 — Implement `Person`

Create the third Identity entity.

Register it.

Generate and apply the migration.

Verify.

**Commit 5:**

---

## Step 6 — Review

Review:

- naming,
- relationships,
- admin,
- migrations,
- documentation.


Perform any required cleanup.

**Commit 6:**


