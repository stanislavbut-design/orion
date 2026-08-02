# Asset Specification

## 1. Purpose

An **Asset** represents a persistent enterprise resource that is individually identifiable and owned or controlled by an Organization.

An Asset is a Core Entity and is independent of any particular business process or functional capability.

## 2. Business Definition

> **An Asset is a Core Entity representing a specific identifiable resource of an Organization that has persistent identity and may be referenced by Business Objects.**

An Asset represents a particular resource, rather than a class of goods or services.

For example:

* a particular laptop is an Asset;
* the laptop model is a Product;
* a particular vehicle is an Asset;
* the vehicle model is a Product.

## 3. Architectural Classification

| Property                            | Value                           |
| ----------------------------------- | ------------------------------- |
| Structural Layer                    | Core Entity                     |
| Category                            | Enterprise Object               |
| Identity                            | Independent persistent identity |
| Organization                        | Implicit                        |
| Cross-module                        | Yes                             |
| Referenced by                       | Business Objects                |
| Business Relationship participation | No                              |

## 4. Scope

An Asset may represent:

* tangible fixed assets;
* equipment;
* vehicles;
* computers and network equipment;
* buildings;
* land;
* intangible assets;
* software licenses;
* other individually identifiable enterprise resources.

The Core Asset model shall remain neutral regarding accounting treatment, operational management, and asset-management methodology.

## 5. Responsibilities

An Asset shall:

* provide a stable identity for an individual enterprise resource;
* provide basic descriptive information;
* provide a stable cross-module reference;
* allow Business Objects to identify the specific resource involved in a business activity;
* allow functional capabilities to extend its semantics where required.

An Asset shall not, in the Core:

* calculate depreciation;
* maintain book value;
* define depreciation methods;
* record acquisition transactions;
* maintain physical locations;
* assign custodians;
* manage maintenance;
* track utilization;
* manage disposal;
* determine tax treatment;
* define accounting classification.

These concerns belong to the appropriate capabilities.

## 6. Core Attributes

The Core Asset shall contain only attributes having enterprise-wide semantic meaning.

### 6.1 Public ID

An Asset shall have a persistent unique public identifier.

### 6.2 Name

An Asset shall have a Name.

The Name provides the primary human-readable identification of the Asset.

### 6.3 Description

An Asset may have a Description.

Description provides general descriptive information about the particular resource.

## 7. Business Rules

### AST-001 — Name Required

An Asset shall have a Name.

### AST-002 — Description Optional

An Asset may have a Description.

### AST-003 — Persistent Identity

Every Asset shall have a unique persistent identity within Orion.

### AST-004 — No Direct Business Relationship Participation

An Asset shall not participate directly in a Business Relationship.

Assets are not Business Actors.

### AST-005 — Business Object Reference

A Business Object may reference an Asset when the recorded business activity concerns that specific resource.

### AST-006 — Independent Existence

An Asset may exist without any associated Business Object.

The existence of an Asset therefore does not depend on a particular acquisition, accounting transaction, maintenance event, or other operational event being recorded in Orion.

## 8. Product Relationship

An Asset and a Product are distinct Core Entities.

A Product represents a good or service as an enterprise concept.

An Asset represents a specific identifiable resource.

For example:

```text
Product
"Lenovo ThinkPad T14"
        │
        ├── Asset #001 — laptop assigned to John
        ├── Asset #002 — laptop assigned to Mary
        └── Asset #003 — laptop in storage
```

The relationship between Product and Asset shall not be mandatory in the Core.

A future Asset capability may establish such a relationship where required.

An Asset may therefore exist without a corresponding Product.

## 9. Asset Classification

The Core shall **not introduce an Asset Type** at this stage.

Although different kinds of Assets have substantially different characteristics, no common classification is currently required to establish enterprise-wide semantic rules.

Future capabilities may introduce classifications required for their own purposes.

## 10. Functional Extensions

Functional capabilities may extend Asset with additional information.

Examples include:

| Capability         | Possible Asset extensions                                   |
| ------------------ | ----------------------------------------------------------- |
| Assets             | Acquisition information, basic asset accounting information |
| Asset Management   | Location, custodian, maintenance, condition, utilization    |
| Accounting         | Accounting classification, depreciation, book value         |
| Finance Management | Valuation, budgeting, financial analysis                    |
| Reporting          | Analytical classifications                                  |
| Documents          | Acquisition documents, warranties, certificates             |

Such extensions shall not redefine the identity of the Core Asset.

## 11. Relationship to Business Objects

An Asset is a Core Entity; a Business Object records a business activity involving the Asset.

For example:

```text
Asset
   │
   ├── Acquisition
   ├── Assignment
   ├── Transfer
   ├── Maintenance
   ├── Disposal
   └── Accounting Transaction
```

Each Business Object represents a particular business event or activity. The Asset represents the persistent enterprise resource to which those activities refer.

## 12. Relationship to Project

An Asset and a Project are independent Core Entities.

A Business Object may reference both when a business activity concerns a particular Asset within the context of a Project.

For example:

```text
Project
   │
   └── Asset Assignment
          └── Asset
```

The association between Project and Asset is therefore established through the relevant Business Object rather than by making either entity dependent on the other.

## 13. Core Boundary

The Core Asset model shall remain intentionally minimal.

The following are explicitly outside the Core unless future architectural decisions establish an enterprise-wide semantic requirement:

* Asset Type;
* asset category;
* serial number;
* manufacturer;
* model;
* acquisition date;
* acquisition cost;
* accounting value;
* depreciation;
* depreciation method;
* useful life;
* tax classification;
* physical location;
* custodian;
* maintenance status;
* condition;
* utilization;
* disposal information;
* ownership or custody details.

These attributes may be introduced by functional capabilities where their meaning and business rules are defined.

## 14. Summary

The Core Asset represents **a specific identifiable enterprise resource**, while functional capabilities determine **how that resource is accounted for, managed, maintained, assigned, or otherwise used**.

The distinction between Product and Asset is fundamental:

> **Product identifies what the enterprise deals with; Asset identifies a particular resource the enterprise possesses or controls.**

The Core therefore provides only the persistent identity and basic description required for an Asset to function as a cross-module reference.
