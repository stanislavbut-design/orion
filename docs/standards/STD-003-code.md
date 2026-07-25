# Code Organization

## Overarching Principles

### STD-003-P001

Source code artifacts shall be organized according to ownership and responsibility rather than implementation convenience.




`__init__.py` shall normally remain empty.

Objects should be imported from the module that defines them. Re-exporting through `__init__.py` should be used only when a package intentionally exposes a simplified public API.

# Constants

## Purpose

Define where different categories of constants shall be stored.

## Guiding principle

Constants shall be stored according to ownership, not convenience.

- Shared concepts belong to core.
- Module concepts belong to their module.
- User-facing messages belong to the centralized validation resources.

## 1. Shared semantic constants

Shared semantic constants define Orion's canonical vocabulary.

They shall be stored under:

`apps/core/constants/`

Examples:

- RelationshipType
- RoleType
- IdentityType
- PartyType

These constants may be referenced by any application.

## 2. Module semantic constants

Semantic constants used exclusively by a single application shall be stored under that application's constants package.

Example:
```
apps/finance/constants/
apps/hr/constants/
apps/crm/constants/
```

These constants should not be moved to core unless they become shared across multiple applications.

## 3. Validation messages

Validation messages are user-facing resources.

They shall be stored centrally under:

```apps/core/constants/validation/```

and organized by application.

Example:
```
validation/
    masterdata.py
    finance.py
    hr.py
```
This supports:

- consistent wording;
- centralized maintenance;
- future internationalization.

## 4. Configuration defaults

Configuration constants (default formats, naming conventions, limits, etc.) shall reside alongside the functionality they configure.

Shared defaults belong to core:

```apps/core/constants/config/```

Module-specific defaults belong to the owning module.

