# STD-001 — Coding

**Status:** Approved

**Date:** 2026-07-18

# STD-001 — Coding

**Status:** Approved  
**Date:** 2026-07-18

## Purpose

This standard defines the coding conventions used throughout the Orion project.

Its purpose is to ensure that the codebase remains consistent, readable, maintainable, and easy to evolve regardless of the number of contributors or the size of the project.

This standard establishes project-specific conventions in addition to the Python and Django community standards.

---

## Scope

This standard applies to all source code developed as part of Orion, including:

- Python code
- Django applications
- Management commands
- Database migrations
- Tests
- Scripts
- Configuration files where applicable

Third-party libraries and generated code are excluded.

---

## Standard

### 1. General Principles

1.1 Code shall prioritize clarity over brevity.

1.2 Simplicity shall be preferred over unnecessary abstraction.

1.3 Complexity shall be introduced only when justified by a concrete business or technical requirement.

1.4 Readability shall take precedence over cleverness.

1.5 Every module shall have a clearly defined responsibility.

1.6 Source code is part of the project's documentation and shall be written accordingly.

---

### 2. Language

2.1 All source code shall be written in English.

2.2 All identifiers shall be written in English.

2.3 Comments shall be written in English.

2.4 Commit messages shall be written in English.

2.5. American English shall be used where applicable.

---

### 3. Python Style

3.1 Python code shall conform to **PEP 8** unless a documented exception exists.

3.2 Descriptive names shall be preferred over abbreviations.

3.3 Functions and methods should perform one logical responsibility.

3.4 Deep nesting should be avoided.

3.5 Magic numbers and unexplained literals shall not appear in business logic.

3.6 Constants shall be defined explicitly.

---

### 4. Naming

#### Classes

4.1 Classes shall use *PascalCase*.

Examples:

- Party
- Customer
- Invoice

#### Functions and Methods

4.2 Functions and methods shall use *snake_case*.

Examples:

- calculate_balance()
- create_invoice()

#### Variables

4.3 Variables shall use descriptive *snake_case* names.

#### Constants

4.4 Constants shall use *UPPER_CASE*.

#### Modules

4.5 Module names shall use lowercase *snake_case*.

---

### 5. Django

5.1 Django model names shall be singular.

Examples:

- Party
- Invoice
- Currency

5.2 Business logic shall not reside in views.

5.3 Views shall coordinate requests and responses.

5.4 Models shall represent the business domain.

5.5 Shared infrastructure shall reside in the core application.

5.6 Business functionality shall reside in the owning application.

---

### 6. File Organization

6.1 Every module shall have a single primary responsibility.

6.2 Files shall not be split prematurely.

6.3 Large modules should be divided when doing so improves readability.

6.4 Circular dependencies shall be avoided.

---

### 7. Documentation

7.1 Public classes shall include a docstring when their purpose is not immediately obvious.

7.2 Complex algorithms shall explain the rationale rather than restating the implementation.

7.3 Comments shall explain **why**, not **what**, unless the code alone cannot express the intent.

7.4 Obsolete comments shall be removed.

---

### 8. Error Handling

8.1 Exceptions shall not be silently ignored.

8.2 Exceptions shall provide meaningful information.

8.3 Business exceptions shall be handled explicitly.

---

### 9. Imports

9.1 Imports shall be grouped in the following order:

1. Python standard library

2. Third-party packages

3. Orion modules

9.2 Unused imports shall be removed.

9.3 Wildcard imports shall not be used.

---

### 10. Future Compatibility

10.1 Code shall avoid unnecessary assumptions that restrict future architectural evolution.

10.2 Public interfaces should remain stable whenever practical.

10.3 Backward compatibility shall be considered when modifying shared components.

---

## Exceptions

Exceptions to this standard shall be documented within the affected source code together with the technical rationale.

Temporary exceptions should include a reference to the issue or ADR authorizing the deviation.

---

## Related Documents

- ADR-002 Modular Architecture
- ADR-003 PostgreSQL as the Primary Database
- ADR-007 Entity Identification
- STD-002 Database
