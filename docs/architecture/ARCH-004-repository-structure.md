# ARCH-04 — Repository Structure

**Status:** Approved

**Date:** 2026-07-18

---

## Purpose

This document defines the directory structure of the Orion repository.

Its purpose is to provide a consistent organization for source code, documentation, configuration, scripts and supporting resources throughout the lifetime of the project.

---

## Scope

This document applies to the entire Orion source repository.

---

## Principles

### Separation of Responsibilities

The repository shall separate:

- source code
- documentation
- configuration
- scripts
- static assets

into dedicated directories.

---

### Stable Top-Level Structure

Top-level directories shall remain stable.

Changes affecting the repository layout shall be documented in this document.

---

### Application Isolation

Each business domain shall be implemented as an independent Django application located under:

src/apps/

---

### Documentation

Documentation is a first-class project artifact and shall be maintained under the docs directory.

---


## Repository Layout

```text
orion/
│
├── .git/               GitHub workflows and templates              Done       
├── apps/               Application source code                     Done
├── config/             Django project configuration                Done
├── docs/               Project documentation                       Done 
├── requirements/       Python dependency definitions               Done
├── scripts/            Utility and maintenance scripts             Done
│
├── .env                                                            Done
├── .gitignore                                                      Done
├── LICENSE
├── manage.py                                                       Done
├── pyproject.toml
└── ...
```

---

## Application Source Layout

```text
apps/
│
├── apps/
│   ├── core/                                                       Done
│   ├── masterdata/
│   ├── crm/
│   ├── hr/
│   ├── payroll/
│   ├── finance/
│   ├── assignments/
│   ├── pipelines/
│   ├── reporting/
│   ├── documents/
│   ├── integration/
│   └── administration/
│
└── __init__.py
```

### Masterdata Layout

```text
masterdata/
│
├── __init__.py
├── admin.py
├── apps.py
├── views.py
│
├── migrations/
│   └── __init__.py
│
├── models/             is split into focused modules
│   ├── __init__.py
│
├── tests/
│   └── __init__.py9
│
├── templates/
└── static/
```
---

## Documentation Layout

```text
docs/
│
├── README.md
│
├── adr/
├── architecture/
├── development/
├── glossary/
├── modules/
├── roadmap/
└── standards/
```

Each documentation category shall maintain its own Index.md describing its contents.

---

## Django Project Configuration Layout

```text
config/
│
├── settings.py
├── urls.py
├── asgi.py
├── wsgi.py
└── __init__.py
```

## Related Documents

- ARCH-002 — Platform Architecture
- STD-004 — Documentation