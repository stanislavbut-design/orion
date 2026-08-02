# Department Specification

## 1. Purpose

A **Department** represents a persistent organizational unit within the legal structure of an Organization.

A Department is a Core Entity and may be referenced by Business Objects and Structural Associations across Orion.

## 2. Business Definition

> **A Department is a Core Entity representing a persistent organizational unit within a Company.**

Departments may be organized hierarchically. The Department hierarchy represents the internal organizational structure of a Company and is managed as Master Data.

A Department's position in the hierarchy determines the Company to which it belongs.

## 3. Architectural Classification

| Property                            | Value                                        |
| ----------------------------------- | -------------------------------------------- |
| Structural Layer                    | Core Entity                                  |
| Category                            | Organizational Entity                        |
| Identity                            | Independent persistent identity              |
| Organization                        | Implicit                                     |
| Cross-module                        | Yes                                          |
| Referenced by                       | Business Objects and Structural Associations |
| Business Relationship participation | No                                           |
| Hierarchy management                | Master Data                                  |

## 4. Scope

A Department may represent organizational units such as:

* Sales Department;
* Accounting Department;
* Human Resources Department;
* IT Department;
* Production Department;
* Legal Department.

Departments may be arranged into hierarchical structures of arbitrary depth.

The Core shall remain neutral regarding the particular functions performed by a Department.

## 5. Core Attributes

The Core Department shall contain attributes having enterprise-wide semantic meaning or required for practical management of the organizational structure.

### 5.1 Public ID

A Department shall have a persistent unique public identifier.

### 5.2 Code

A Department shall have a Code.

The Code provides a concise human-readable identifier used for navigation, selection, hierarchy management, and administrative reference.

The Code does not itself carry semantic meaning required by the Core domain model.

### 5.3 Name

A Department shall have a Name.

The Name provides the primary descriptive identification of the Department.

### 5.4 Description

A Department may have a Description.

Description provides general descriptive information about the organizational unit.

### 5.5 Parent Department

A Department may have a Parent Department.

The Parent Department establishes the Department hierarchy.

A Department without a Parent Department is a root Department.

## 6. Department Hierarchy

The Department hierarchy shall be managed in Master Data.

A Department may have one Parent Department and may have zero or more Child Departments.

A Department shall not be its own Parent Department.

The hierarchy may contain multiple levels.

For example:

```text
Company A
│
├── Finance
│   ├── Accounting
│   └── Treasury
│
├── Sales
│   ├── Domestic Sales
│   └── International Sales
│
└── Operations
    ├── Production
    └── Logistics
```

The hierarchy is an intrinsic property of the organizational structure and shall not be represented as a collection of independent Structural Relationships.

## 7. Company Association

Only root Departments shall be directly associated with a Company.

The association shall be represented by an Organizational Relationship.

Child Departments inherit their Company association through their position in the Department hierarchy.

For example:

```text
Company A
    │
    └── Finance
          ├── Accounting
          │     └── Accounts Payable
          └── Treasury
```

Only `Finance` requires a direct Company association.

`Accounting`, `Accounts Payable`, and `Treasury` inherit their Company association from the root Department.

A Department shall therefore belong to exactly one Company, either directly or through inheritance from its root Department.

## 8. Business Rules

### DEP-001 — Name Required

A Department shall have a Name.

### DEP-002 — Code Required

A Department shall have a Code.

### DEP-003 — Description Optional

A Department may have a Description.

### DEP-004 — Persistent Identity

Every Department shall have a unique persistent identity within Orion.

### DEP-005 — Parent Department

A Department may have one Parent Department.

### DEP-006 — No Self-Parenting

A Department shall not be its own Parent Department.

### DEP-007 — Hierarchy Managed in Master Data

The Department hierarchy shall be maintained as Master Data.

### DEP-008 — Root Department Company Association

Every root Department shall be associated with exactly one Company through an Organizational Relationship.

### DEP-009 — Child Department Company Inheritance

A child Department shall inherit its Company association from its root Department.

### DEP-010 — Single Company Membership

Every Department shall belong to exactly one Company, either through a direct Organizational Relationship when it is a root Department or through inherited association when it is a child Department.

### DEP-011 — Responsibility Center Association

A Department may be directly associated with at most one Responsibility Center. 

If a Department has a direct Responsibility Center association, all descendant Departments inherit that association and shall not have direct Responsibility Center associations.

The direct association target shall always be a leaf Responsibility Center.

### DEP-012 — No Direct Business Relationship Participation

A Department shall not participate directly in a Business Relationship.

A Department is an organizational entity rather than a Business Actor.

### DEP-013 — Business Object Reference

A Business Object may reference a Department when the recorded business activity is attributable to, performed by, or otherwise associated with that Department.

### DEP-014 — Independent Existence

A Department may exist without any associated Business Object.

The existence of a Department is therefore not dependent on a particular operational activity being recorded in Orion.

## 9. Relationship to Responsibility Center

Department and Responsibility Center are independent Core Entities.

A Department may participate in at most one Organizational Relationships with a Responsibility Center.

Multiple Departments may participate in the same Responsibility Center.

Every Department has an effective Responsibility Center if either it or one of its ancestors has a direct association.

The effective Responsibility Center of a Department shall be determined by its nearest ancestor having a direct Responsibility Center association.

This allows the legal organizational hierarchy and the functional accountability structure to coexist as independent dimensions.

For example:

```text
Company A
│
├── Sales Department ───────────────┐
├── Marketing Department ───────────┼── Sales Responsibility Center
└── Customer Service Department ────┘
```

The Department hierarchy remains unchanged regardless of changes to Responsibility Center assignments.

## 10. Relationship to Business Processes

A Department and a Business Process are separate concepts.

A Business Process defines a stable model of how business activities are organized.

A Department represents an organizational unit.

A Department may therefore be associated with responsibility for one or more Business Processes, but a Department shall not contain or implement a Business Process.

Business Process hierarchy and Department hierarchy are independent structures.

## 11. Relationship to Person

A Person and a Department are independent Core Entities.

A Person may be associated with a Department through an appropriate Organizational Relationship, representing organizational membership or assignment.

The relationship shall not be represented by embedding a Person in the Department entity.

## 12. Functional Extensions

Functional capabilities may extend Department with additional information.

Examples include:

| Capability                      | Possible Department extensions                  |
| ------------------------------- | ----------------------------------------------- |
| HR Management                   | Staffing, positions, organizational assignments |
| Payroll                         | Payroll allocation information                  |
| Accounting / Finance Management | Cost allocation and accounting dimensions       |
| Reporting                       | Analytical classifications                      |
| Project Management              | Project participation or responsibility         |

Such extensions shall not redefine the identity of the Core Department.

## 13. Core Boundary

The Core Department model shall remain intentionally focused on organizational identity and structure.

The following are outside the Core unless future architectural decisions establish an enterprise-wide semantic requirement:

* department manager;
* employees;
* positions;
* headcount;
* budget;
* payroll allocation;
* accounting classification;
* project assignments;
* Business Process responsibility details.

These concerns may be represented through Structural Associations or introduced by functional capabilities.

## 14. Summary

The Core Department represents **a persistent organizational unit within a Company's legal structure**.

Its hierarchy is an intrinsic part of the organizational structure and is therefore managed as Master Data.

A root Department is associated with a Company through an Organizational Relationship. Child Departments inherit the Company association through the Department hierarchy.

The Department hierarchy and the Responsibility Center structure are independent organizational dimensions:

* **Department hierarchy** represents the legal/organizational structure;
* **Responsibility Center relationships** represent functional accountability.

Both structures may therefore coexist without requiring either entity to own or contain the other.
