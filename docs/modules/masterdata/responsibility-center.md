# Responsibility Center Specification

## 1. Purpose

A **Responsibility Center** represents a persistent functional accountability unit within an Organization.

A Responsibility Center is a Core Entity and provides a cross-module reference for business activities that require functional responsibility or accountability.

## 2. Business Definition

> **A Responsibility Center is a Core Entity representing a persistent functional area of accountability within an Organization.**

A Responsibility Center organizes responsibility by function rather than by legal or hierarchical structure.

Responsibility Centers may be organized hierarchically and may therefore represent different levels of functional accountability.

A Responsibility Center may encompass Departments belonging to different Companies within the same Organization.

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

A Responsibility Center may represent functional areas such as:

* Sales;
* Marketing;
* Production;
* Information Technology;
* Administration;
* Research and Development;
* Customer Service.

Responsibility Centers may be organized into hierarchical structures of arbitrary depth.

The Core shall remain neutral regarding the particular responsibilities, processes, or accounting methods associated with a Responsibility Center.

## 5. Responsibilities

A Responsibility Center shall:

* provide a stable identity for a functional accountability unit;
* provide basic descriptive information;
* provide a stable cross-module reference;
* provide a hierarchical functional accountability structure;
* allow organizational units to be associated with functional accountability areas;
* allow Business Objects to reference the functional area responsible for a business activity.

A Responsibility Center shall not, in the Core:

* define or execute Business Processes;
* represent a Business Process;
* replace a Department;
* own Companies or Departments;
* manage employees;
* define budgets;
* perform accounting;
* manage projects.

These concerns belong to the appropriate capabilities or Structural Associations.

## 6. Core Attributes

The Core Responsibility Center shall contain attributes having enterprise-wide semantic meaning or required for practical management of the functional accountability structure.

### 6.1 Public ID

A Responsibility Center shall have a persistent unique public identifier.

### 6.2 Code

A Responsibility Center shall have a Code.

The Code provides a concise human-readable identifier used for navigation, selection, hierarchy management, reporting, and administrative reference.

The Code does not itself carry semantic meaning required by the Core domain model.

### 6.3 Name

A Responsibility Center shall have a Name.

The Name provides the primary human-readable identification of the Responsibility Center.

### 6.4 Description

A Responsibility Center may have a Description.

Description provides general descriptive information about the functional accountability area.

### 6.5 Parent Responsibility Center

A Responsibility Center may have a Parent Responsibility Center.

The Parent Responsibility Center establishes the Responsibility Center hierarchy.

A Responsibility Center without a Parent Responsibility Center is a root Responsibility Center.

## 7. Responsibility Center Hierarchy

The Responsibility Center hierarchy shall be managed in Master Data.

A Responsibility Center may have one Parent Responsibility Center and may have zero or more Child Responsibility Centers.

A Responsibility Center shall not be its own Parent Responsibility Center.

The hierarchy may contain multiple levels.

For example:

```text
Operations
├── Production
│   ├── Assembly
│   └── Packaging
└── Logistics

Administration
├── Finance
└── Human Resources
```

The hierarchy represents levels of functional accountability.

## 8. Department Association

A Responsibility Center may be associated with one or more Departments through Organizational Relationships.

Only **leaf Responsibility Centers** may be directly associated with Departments.

A Department may participate in at most one direct Organizational Relationship with a Responsibility Center.

The association is optional.

Therefore:

* a Department may have no direct Responsibility Center association;
* a Department may have one direct Responsibility Center association;
* a Department shall not have more than one direct Responsibility Center association.

A Responsibility Center may have zero, one, or many associated Departments.

## 9. Responsibility Center Inheritance

Responsibility Center association may be inherited through the Department hierarchy.

If a Department has a direct Responsibility Center association, all of its descendant Departments shall inherit that association unless a nearer ancestor establishes another direct association.

A Department shall not establish a direct Responsibility Center association when a Responsibility Center is inherited.

The effective Responsibility Center of a Department shall therefore be determined as follows:

1. If the Department has a direct Responsibility Center association, that Responsibility Center applies.
2. Otherwise, the Department inherits the Responsibility Center of its nearest ancestor having a direct Responsibility Center association.
3. If neither the Department nor any ancestor has a direct association, the Department has no effective Responsibility Center association.

For example:

```text
Department hierarchy

Operations Department ─────────────► Operations RC
│
├── Production Department
│      │
│      ├── Assembly Department
│      └── Packaging Department
│
└── Logistics Department
```

If `Operations Department` is directly associated with `Operations RC`, then:

```text
Operations Department  → Operations RC
Production Department  → inherited Operations RC
Assembly Department   → inherited Operations RC
Packaging Department  → inherited Operations RC
Logistics Department  → inherited Operations RC
```

The child Departments do not require separate Organizational Relationships.

## 10. Business Rules

### RCN-001 — Code Required

A Responsibility Center shall have a Code.

### RCN-002 — Name Required

A Responsibility Center shall have a Name.

### RCN-003 — Description Optional

A Responsibility Center may have a Description.

### RCN-004 — Persistent Identity

Every Responsibility Center shall have a unique persistent identity within Orion.

### RCN-005 — Parent Responsibility Center

A Responsibility Center may have one Parent Responsibility Center.

### RCN-006 — No Self-Parenting

A Responsibility Center shall not be its own Parent Responsibility Center.

### RCN-007 — Hierarchy Managed in Master Data

The Responsibility Center hierarchy shall be maintained as Master Data.

### RCN-008 — Direct Department Association Optional

A Department may have at most one direct Responsibility Center association.

### RCN-009 — Direct Association Target

A direct Department–Responsibility Center association shall target a leaf Responsibility Center.

### RCN-010 — Responsibility Center Propagation

A direct Responsibility Center association established on a Department shall propagate to all descendant Departments and replace any existing Responsibility Center associations within that subtree.

### RCN-011 — No Lower-Level Override

A Responsibility Center association propagated from a higher-level Department shall take precedence over any existing association on descendant Departments.

Descendant Departments shall not retain or re-establish conflicting Responsibility Center associations while the propagated association remains in effect.

### RCN-012 — Cross-Company Scope

A Responsibility Center may be associated, directly or through inheritance, with Departments belonging to different Companies within the same Organization.

The Responsibility Center therefore represents functional accountability across the legal structure rather than belonging to a particular Company.

### RCN-013 — No Direct Business Relationship Participation

A Responsibility Center shall not participate directly in a Business Relationship.

A Responsibility Center is an organizational accountability entity rather than a Business Actor.

### RCN-014 — Business Object Reference

A Business Object may reference a Responsibility Center when the recorded business activity is attributable to or accountable to that Responsibility Center.

### RCN-015 — Independent Existence

A Responsibility Center may exist without any associated Department or Business Object.

Its existence is therefore not dependent on a particular organizational assignment or operational activity being recorded in Orion.

## 11. Relationship to Department

Department and Responsibility Center are independent Core Entities.

Their relationship represents two orthogonal dimensions of organizational structure:

* **Department** represents legal and hierarchical organizational structure;
* **Responsibility Center** represents functional accountability.

The Department hierarchy and Responsibility Center hierarchy are therefore maintained independently.

A Responsibility Center does not become part of a Company's legal structure merely because one or more Departments of that Company are associated with it.

Similarly, a Department does not cease to belong to its Company because its effective Responsibility Center spans multiple Companies.

## 12. Relationship to Business Processes

A Responsibility Center and a Business Process are separate concepts.

A Business Process defines a stable model of how business activities are organized.

A Responsibility Center represents functional accountability.

A Responsibility Center may be associated with responsibility for one or more Business Processes through an appropriate Structural Association, but it shall not contain or implement a Business Process.

The Business Process hierarchy and Responsibility Center hierarchy are independent structures.

## 13. Relationship to Person

A Person and a Responsibility Center are independent Core Entities.

A Person may be associated with a Responsibility Center through an appropriate Structural Association where the organizational model requires responsibility to be assigned directly to individuals.

Such an association shall not be represented by embedding Persons in the Responsibility Center entity.

## 14. Functional Extensions

Functional capabilities may extend Responsibility Center with additional information.

Examples include:

| Capability         | Possible extensions                                       |
| ------------------ | --------------------------------------------------------- |
| Accounting         | Cost allocation, accounting dimensions                    |
| Finance Management | Budgets, responsibility accounting, financial performance |
| Reporting          | Analytical classifications and reporting structures       |
| HR Management      | Personnel responsibility assignments                      |
| Project Management | Project responsibility or accountability                  |

Such extensions shall not redefine the identity of the Core Responsibility Center.

## 15. Core Boundary

The Core Responsibility Center model shall remain focused on functional identity, hierarchy, and organizational accountability.

The following are explicitly outside the Core unless future architectural decisions establish an enterprise-wide semantic requirement:

* budget;
* financial targets;
* actual costs;
* revenue;
* profit;
* accounting classification;
* manager;
* employees;
* performance indicators;
* project assignments;
* detailed Business Process responsibility;
* reporting-specific hierarchies.

These concerns may be represented through Structural Associations or introduced by functional capabilities.

## 16. Summary

The Core Responsibility Center represents **a persistent functional area of accountability within an Organization**.

Responsibility Centers form their own hierarchy, managed in Master Data.

The Responsibility Center hierarchy and Department hierarchy are independent and orthogonal:

* **Department hierarchy** represents the legal and organizational structure;
* **Responsibility Center hierarchy** represents functional accountability.

Only leaf Responsibility Centers may be the direct target of Department associations.

Department associations are optional and may be inherited through the Department hierarchy. The nearest direct association determines the effective Responsibility Center for a Department and its descendants.

This allows a Responsibility Center to span Departments and Companies while preserving the independent legal structure represented by Departments.
