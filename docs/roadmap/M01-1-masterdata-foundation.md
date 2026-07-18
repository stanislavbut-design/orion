# Milestone 1.1 — Master Data Foundation

## Step 1 — Create the application

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


**Commit 1**

---

## Step 2 — Organize the application

Refactor the default Django layout to match Orion's conventions.

Create the internal structure, for example:

**Commit 2**

---

## Step 3 — Implement `Organization`

Create the first Identity entity.

Initially, only the attributes required by the architecture and the framework.

Register it in the admin.

Generate and apply the migration.

Verify.

**Commit 3**

---

## Step 4 — Implement `Party`

Create the second Identity entity.

Initially, only the structural attributes.

Register it.

Generate and apply the migration.

Verify.

**Commit 4**

---

## Step 5 — Implement `Person`

Create the third Identity entity.

Register it.

Generate and apply the migration.

Verify.

**Commit 5**

---

## Step 6 — Review

Review:

- naming,
- relationships,
- admin,
- migrations,
- documentation.


Perform any required cleanup.

**Commit 6**


