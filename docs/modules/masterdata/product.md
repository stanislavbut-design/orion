# Product Specification

## 1. Purpose

A **Product** represents a persistent enterprise concept for a good or service that may be offered, purchased, supplied, consumed, stocked, or otherwise referenced by business activities.

The Product is a Core Entity and is independent of any particular business process or functional capability.

## 2. Business Definition

> **A Product is a Core Entity representing a good or service that has persistent identity within an Organization and may be referenced by Business Objects.**

A Product represents the thing or service being dealt with by the enterprise. It does not represent a particular sale, purchase, inventory movement, manufacturing event, or other business activity involving that Product.

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

A Product may represent:

* a physical good;
* a service;
* a manufactured product;
* a semi-finished good;
* a raw material;
* a consumable;
* another enterprise offering or resource that requires persistent product identity.

The Core Product model shall remain neutral regarding how the Product is used.

## 5. Responsibilities

A Product shall:

* provide a stable identity for a good or service;
* provide basic descriptive information;
* serve as a common reference across business capabilities;
* provide a stable reference for Business Objects;
* allow functional modules to extend its semantics where required.

A Product shall not, in the Core:

* define prices;
* maintain stock quantities;
* define warehouse locations;
* record purchases or sales;
* define suppliers or customers;
* manage manufacturing;
* define accounting treatment;
* maintain inventory valuation;
* define product-specific workflow.

These concerns belong to the appropriate capabilities.

## 6. Core Attributes

The Core Product shall contain only attributes having enterprise-wide semantic meaning.

### 6.1 Public ID

A Product shall have a persistent unique public identifier.

### 6.2 Name

A Product shall have a Name.

The Name provides the primary human-readable identification of the Product.

### 6.3 Description

A Product may have a Description.

Description provides general descriptive information and does not imply any particular operational use.

## 7. Business Rules

### PRD-001 — Name Required

A Product shall have a Name.

### PRD-002 — Description Optional

A Product may have a Description.

### PRD-003 — Persistent Identity

Every Product shall have a unique persistent identity within Orion.

### PRD-004 — No Direct Business Relationship Participation

A Product shall not participate directly in a Business Relationship.

Products are not Business Actors.

### PRD-005 — Business Object Reference

A Business Object may reference a Product when the recorded business activity concerns that Product.

### PRD-006 — Independent Existence

A Product may exist without any associated Business Object.

A Product therefore does not depend on a sale, purchase, inventory transaction, manufacturing activity, or other operational event for its existence.

## 8. Product Types

The Core shall **not introduce a Product Type** at this stage.

Although Products may represent fundamentally different things, such as goods and services, no Product Type is currently required to establish enterprise-wide semantic rules.

Future capabilities may introduce classifications required for their own purposes.

## 9. Functional Extensions

Functional capabilities may extend Product with additional information.

Examples include:

| Capability                         | Possible Product extensions                            |
| ---------------------------------- | ------------------------------------------------------ |
| Sales                              | Sales description, sales classification, selling price |
| CRM                                | Commercial categorization                              |
| Purchases / Procurement Management | Supplier-specific information, purchasing data         |
| Inventory                          | Stocking rules, units, inventory classification        |
| Warehouse                          | Storage and warehouse-specific attributes              |
| Manufacturing                      | Bill of materials, production specifications           |
| Accounting / Finance Management    | Accounting classification, valuation rules             |
| Reporting                          | Analytical classifications                             |

Such extensions shall not redefine the identity of the Core Product.

## 10. Relationship to Business Objects

A Product is a Core Entity; a Business Object records a business activity involving the Product.

For example:

```text
Product
   │
   ├── Sale
   ├── Purchase
   ├── Inventory Movement
   ├── Manufacturing Order
   └── Time / Service Record
```

Each Business Object represents a particular business event or activity. The Product represents the persistent enterprise concept to which those activities refer.

## 11. Relationship to Project

A Product and a Project are independent Core Entities.

A Business Object may reference both when a business activity concerns a particular Product within the context of a Project.

For example:

```text
Project
   │
   └── Purchase
          └── Product
```

The association between Project and Product is therefore established through the relevant Business Object rather than by making either entity dependent on the other.

## 12. Relationship to Asset

A Product and an Asset are distinct Core Entities.

A Product represents a class or identifiable offering of goods or services.

An Asset represents a specific enterprise resource.

For example:

> "Dell Latitude 5550" may be a Product, while a particular laptop acquired and recorded as an enterprise resource is an Asset.

The Core shall not establish a direct dependency between Product and Asset. A future Asset capability may establish the appropriate relationship when required.

## 13. Core Boundary

The Core Product model shall remain intentionally minimal.

The following are explicitly outside the Core unless future architectural decisions establish an enterprise-wide semantic requirement:

* Product Type;
* SKU or internal commercial codes;
* barcode;
* unit of measure;
* price;
* currency;
* tax classification;
* inventory status;
* stock quantity;
* warehouse location;
* supplier;
* customer;
* bill of materials;
* accounting classification;
* lifecycle status.

These attributes may be introduced by functional capabilities where their meaning and business rules are defined.

## 14. Summary

The Core Product represents **what the enterprise deals with**, while functional capabilities determine **how the enterprise deals with it**.

The Core therefore provides only the persistent identity and basic description required for a Product to function as a cross-module reference.
