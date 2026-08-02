# Phase 1 - Core Domain Foundation

# Milestone 1.5 — Architectural Review

## Objectives:
- Verify consistency across all architectural documents.
- Check terminology (Identity, Entity, Object, Process, Service, Pattern, Strategy).
- Eliminate duplicated or conflicting concepts.
- Ensure ADRs, ARCH documents and standards all align with the implemented framework.
- Identify any opportunities to simplify before functional modules begin.

## Step 1 — Architectural Consistency Review ✅ COMPLETE

### Identity Model

- Organization
- Party
- Person
- Future Core Identities (Asset, Product)

Questions:

- Is every identity clearly defined?
- Are responsibilities separated?
- Are invariants complete?

We have already identified a need for additional Core Identities (Asset, Product). However, we haven't make an attempt to define them.



### Business Process

Review:

hierarchy
decomposition
invariants

Questions:

Are lowest-level processes correctly distinguished?
Can future modules define additional processes?

### Business Object

Review:

hierarchy
lifecycle
process association

Questions:

Are statuses clearly separated from Business Objects?
Are child objects properly represented?

### Identity Resolution

Review:

protocol
service
integration pattern

Questions:

Can new Core Identities be added without changing the framework?
Can modules remain independent?

## Step 1A — Candidate Core Concept Review ✅ COMPLETE

Evaluate each candidate against explicit criteria:

| Candidate    | Cross-module | Persistent | Independent lifecycle | Core? |
| ------------ | -----------: | ---------: | --------------------: | :---: |
| Organization |            ✔ |          ✔ |                     ✔ |   ?   |
| Party        |            ✔ |          ✔ |                     ✔ |   ?   |
| Person       |            ✔ |          ✔ |                     ✔ |   ?   |
| Asset        |            ✔ |          ✔ |                     ✔ |   ?   |
| Product      |            ✔ |          ✔ |                     ✔ |   ?   |
| Project      |            ✔ |          ✔ |                     ✔ |   ?   |

Organization is the **root** of the enterprise model, whereas the other candidates are enterprise objects that exist within that root.

That distinction is architectural, not merely functional.

| Property                                    | Organization         | Party | Person | Asset | Product | Project |
| ------------------------------------------- | -------------------- | ----- | ------ | ----- | ------- | ------- |
| Persistent identity                         | ✔                    | ✔     | ✔      | ✔     | ✔       | ✔       |
| Cross-module reference                      | Limited              | ✔     | ✔      | ✔     | ✔       | ✔       |
| Independent lifecycle                       | Effectively infinite | ✔     | ✔      | ✔     | ✔       | ✔       |
| Can be created/retired                      | Normally no          | ✔     | ✔      | ✔     | ✔       | ✔       |
| Participates in ordinary business processes | No                   | ✔     | ✔      | ✔     | ✔       | ✔       |
| Enterprise boundary                         | ✔                    | ✘     | ✘      | ✘     | ✘       | ✘       |

So we draw the model like this:

```text
Enterprise Root
    └── Organization

Enterprise Concepts
    ├── Party
    ├── Person
    ├── Asset
    ├── Product
    └── Project
```
| Characteristic                         | Party | Person | Asset | Product | Project |
| -------------------------------------- | :---: | :----: | :---: | :-----: | :-----: |
| Persistent identity                    |   ✔   |    ✔   |   ✔   |    ✔    |    ✔    |
| Independent lifecycle                  |   ✔   |    ✔   |   ✔   |    ✔    |    ✔    |
| Cross-module reference                 |   ✔   |    ✔   |   ✔   |    ✔    |    ✔    |
| Referenced by Business Objects         |   ✔   |    ✔   |   ✔   |    ✔    |    ✔    |
| Extended by modules                    |   ✔   |    ✔   |   ✔   |    ✔    |    ✔    |
| Participates in Business Relationships |   ✔   |    ✔   |   ✘   |    ✘    |    ✘    |

**Core Concept** — a persistent enterprise concept that:

- has an independent lifecycle;
- is shared across multiple business capabilities;
- is referenced by Business Objects; and
- may be extended by business modules.

**Organization** remains the Enterprise Root.

**Party, Person, Asset, Product, and Project** are Core Concepts.

**Business Actor** becomes a specialization of Core Concepts that can participate in Business Relationships

## Step 1B — Review of Business Relationships ✅ COMPLETE

What is the true architectural purpose of Business Relationships?

A **Business Relationship** is a persistent structural association between Business Actors that establishes or governs future business interactions.

## Step 1C — Structural Layer Review ✅ COMPLETE

What are the fundamental kinds of structural objects in Orion?

| Concept               | Purpose                      | Lifecycle   | Referenced by Business Objects | Cross-module |
| --------------------- | ---------------------------- | ----------- | ------------------------------ | ------------ |
| Organization          | Enterprise boundary          | Infinite    | Rarely                         | Global       |
| Party                 | Business actor               | Independent | ✔                              | ✔            |
| Person                | Business actor               | Independent | ✔                              | ✔            |
| Asset                 | Enterprise resource          | Independent | ✔                              | ✔            |
| Product               | Enterprise offering/resource | Independent | ✔                              | ✔            |
| Project               | Enterprise initiative        | Independent | ✔                              | ✔            |
| Business Relationship | Structural authorization     | Independent | Indirectly                     | ✔            |

### 1. Enterprise Root

**Organization**

Characteristics:

- defines enterprise boundary;
- owns all structural concepts;
- almost never participates in operational activities;
- singleton per tenant (ADR-009).

### 2. Core Entities

```
Party
Person
Asset
Product
Project
Department
Responsibility Center
```

Shared characteristics:
- persistent;
- independent lifecycle;
- cross-module references;
- referenced by Business Objects;
- extensible by modules.

Notice this category is defined by architecture, not by business semantics.

```
Core Entities
|
├── Business Actors
│     ├── Party
│     └── Person
│
├── Enterprise Objects
│     ├── Asset
│     ├── Product
│     └── Project
│
└── Organizational Entities
      ├── Department
      └── Responsibility Center
```

### 3. Structural Association

```
Structural Association
├── Identity Relationship
├── Structural Relationship
└── Business Relationship
```

**Business Relationship**

Characteristics:

- persistent;
- connects Business Actors;
- authorizes or governs future activities;
- independent lifecycle;
- cross-module.

### Deliverables of Step 1

```
Structural Layer
│
├── Enterprise Root
│     └── Organization
│
├── Core Entities
│     ├── Party
│     ├── Person
│     ├── Asset
│     ├── Product
│     └── Project
│
└── Structural Associations
      ├── Identity Relationship
      ├── Structural Relationship
      └── Business Relationship
```
Business Relationships are now recognized as one specialization of Structural Associations rather than the primary abstraction.

## Step 2 — Product Capability Review ✅ COMPLETE

Review the overall functional roadmap.

### Progressive Capability

Review every planned module.

Determine whether it belongs to:

- Base Capability
- Extended Capability

**Current draft:**

| Base	| Extended |
|-------|----------|
| Accounting | Finance Management |
| Sales | CRM |
| Inventory | Warehouse |
| Assets | Asset Management |
| Payroll |	HR |

Also identify missing capabilities.

**Revised Draft**
| Workspace (UI) | Base             | Extended          | Notes         |
|----------------|------------------|-------------------|---------------|
| Administration | Administration   |                   |
| Operations     |                  |                   |
|                | Master Data      |                   |Platform Service |
|                | Documents        |                   |Platform Service |
|                | Sales            | CRM               |
|                | Purchases        | Procurement Management|
|                | Inventory        | Warehouse         |
|                | Assets           | Asset Management  |
|                | Payroll          | HR Management     |
| Accounting     | Accounting       | Finance Management|
| Reporting      | Reporting        | Reporting Suite   |

### Deliverables of Step 2

```
Product Layer
│
├── Workspaces
│     ├── Administration
│     ├── Operations
│     ├── Accounting
│     └── Reporting
│
├── Platform Service
│     ├── Master Data
│     └── Documents
│
├── Base Capabilities
│     ├── Sales
│     ├── Purchases
│     ├── Inventory
│     ├── Assets
│     ├── Payroll
│     ├── Accounting
│     └── Reporting
|
└── Extended Capabilities
      ├── CRM
      ├── Procurement Management
      ├── Warehouse
      ├── Asset Management
      ├── HR Management
      ├── Finance Management
      └── Reporting Suite
```


## Step 3 — Core Entity Review ✅ COMPLETE

Review whether additional entities should become Core Entities.

Determine:

- scope
- ownership
- interaction with modules

### Deliverables of Step 3

The review identified four missing Core Entities:

- Product
- Asset
- Project
- Department
- Responsibility Center

| Core Entity           | Primary architectural role                                                       |
| --------------------- | -------------------------------------------------------------------------------- |
| Product               | Persistent object representing goods or services offered, purchased, manufactured, or consumed, referenced by many modules.              |
| Asset                 | Persistent enterprise object representing long-lived resources owned or controlled by the organization, used across operations, accounting and reporting. |
| Project               | Enterprise object representing a persistent business initiative or body of work that spans modules.|
| Department            | Persistent organizational entity representing units within the legal structure.                     |
| Responsibility Center | Persistent functional organizational entity representing functional accountability across the organization.  |

**Module Entity pattern**

Module-level entities remain the correct extension mechanism.

## Step 4 — Documentation Review ✅ COMPLETE

| Document Purpose      | File Reference                    | Status   |
|-----------------------|-----------------------------------|----------|
| Project Specification | docs/modules/masterdata/project.md| Complete |
| Product Specification | docs/modules/masterdata/product.md| Complete |
| Asset Specification   | docs/modules/masterdata/asset.md  | Complete |
| Department Specification | docs/modules/masterdata/department.md | Complete |
| Responsibility Center Specification | docs/modules/masterdata/responsibility-center.md  | Complete |

## Step 5 — Base Capability Architecture Review ✅ COMPLETE

- what constitutes a Base capability versus an Extended capability;
- how Base capabilities own their foundational entities;
- how Extended capabilities extend Base entities without becoming prerequisites;
- how cross-module references work within this dependency direction;
- how the Base mini-apps relate to the Workspace/UI concept;
- where Operation and Accounting fit into this model;
- and how this affects the existing Django app structure.

## Step 6 — Roadmap Review ✅ COMPLETE

### 6.1 Reconstruct the current capability model

| Base       | Extended               |
| ---------- | ---------------------- |
| Sales      | CRM                    |
| Purchases  | Procurement Management |
| Inventory  | Warehouse              |
| Assets     | Asset Management       |
| Payroll    | HR Management          |
| Accounting | Finance Management     |
| Documents  | Document Management    |
| Reporting  | Reporting Suite        |

Additionally:

- Master Data — Base capability without an identified Extended counterpart
- Administration — separate foundational capability
- Operations — Workspace, not a single technical module

The major functional conclusion we reached earlier was that a viable small-business product needs more than our original roadmap suggested.

In particular, the Base layer now provides the basic operational coverage:
- Sales
- Purchases
- Inventory
- Assets
- Payroll
- Accounting

### 6.2 Capability Layers

**Layer 1 — Core**
``'
Organization
Party
Person
Product
Asset
Project
Department
Responsibility Center
Business Relationships
Business Processes
``'
These are stable and largely independent of any particular capability.

**Layer 2 — Foundation**

Infrastructure that every installation needs.
```
Administration
Master Data
Documents
Reporting
```
These are not operational business capabilities, but they enable everything else.

**Layer 3 — Base Operations**

The smallest complete operational suite.
```
Sales
Purchases
Inventory
Assets
Payroll
Accounting
```

**Layer 4 — Management**

Progressive capability extensions.
```
CRM
Procurement Management
Warehouse
Asset Management
HR Management
Finance Management
Document Management
Reporting Suite
```

### 6.3 Check architectural dependencies against sequencing
```
Core
  ↓
Master Data
  ↓
Base capabilities
  ↓
Extended capabilities
```
but the Base capabilities themselves have dependencies:
```
Sales ──────► Inventory
Assets ─────► Payroll
Accounting ─► Sales
Accounting ─► Purchases
Accounting ─► Inventory
Accounting ─► Assets
Accounting ─► Payroll
Reporting ──► Accounting
```

Therefore, implementation order cannot simply follow the Workspace order or the Base/Extended pairs.

A module may be conceptually "Base" but still need another Base capability to exist first.

### 6.4 Milestone implications

Our recent review has already exposed several things that weren't adequately represented in the original roadmap:
- **Assets** was promoted from a prospective PPE module to a Base capability.
- **Inventory** became a Base capability, while Warehouse became Extended.
- **Payroll** became a Base capability, with HR Management above it.
- **Project** became a Core Entity rather than merely an Assignment concept.
- **Department** and **Responsibility Center** became Core Entities.
- **Position** became a Payroll-owned module entity.
- **Documents** became a Base capability with a cross-cutting role.
- **Master Data** became the administrative capability for Core Entities.
- **Accounting** became explicitly separate from operational capabilities.
- **Reporting** became a Base capability rather than merely a reporting add-on.

### 6.4 Revised Roadmap

**Production Stage 1 — Build a complete operational system**

The objective is not to perfect individual modules, but to reach the point where a small business can genuinely run Orion in production.
```
Core
        ↓
Foundation
        ↓
Operations
        ↓
Accounting
```
At this point Orion becomes a usable ERP for a consulting firm or other SME.

Only after that do we begin adding optimization and management capabilities.

**Production Stage 2 — Progressive enhancement**

Now every new capability increases business sophistication without being required for day-to-day operation.
```
Sales        → CRM
Purchases    → Procurement Management
Inventory    → Warehouse
Assets       → Asset Management
Payroll      → HR Management
Accounting   → Finance Management
Documents    → Document Management
Reporting    → Reporting Suite
```

Inside each Production Stage, we'll organise the work by vertical slices.

**Production Stage 1**
```
Core
 ↓
Master Data
 ↓
Sales
 ↓
Accounting integration
```
**Production Stage 2**
```
Sales
 ↓
CRM
```
The roadmap should optimize for:

- Earliest production deployment (complete Base product).
- Continuous value afterwards (Management capabilities).

rather than:

- Earliest technically complete slice across all layers.

## Step 7 — Documentation Review ✅ COMPLETE

### Added Documents

**Architectural Taxonomy**

`ARCH-004-taxonomy.md`

### Revised Docoments

**Vision v2.0**  ARCH-000-vision.md
**Engineering Principles v1.2** ARCH-001-principles.md
**Business Domain Model v2.0** ARCH-003-domain-model.md

### Commit

S01.M01.05.01 Architectural Review
