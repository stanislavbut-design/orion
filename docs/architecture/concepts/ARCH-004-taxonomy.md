# Architectural Taxonomy

| Property | Value |
|----------|-------|
| Document ID | ARCH-004 |
| Title | Architectural Taxonomy |
| Status | Approved |
| Version | 1.0 |
| Owner | Orion Project |
| Last Updated | 2026-08-01 |

---

## Purpose

This document defines the canonical architectural terminology used throughout the Orion documentation. 

Where terminology conflicts arise, the definitions in ARCH-004 take precedence unless explicitly superseded by an Architecture Decision Record (ADR).

---

## Domain Terminology

| Dimension             | Preferred term            | Example              |
| --------------------- | ------------------------- | -------------------- |
| Architecture          | Presentation Layer        | Core Layer, Modules Layer |
| Functional Scope      | Capability                | Base Capability, Extended Capability |
| Product Structure     | Module                    | Payroll, Sales, Accounting |
| User Navigation       | Workspace                 | Administration, Operations, Accounting, Reporting |
| Product Maturity      | Stage                     | Stage 1 Operational Orion      |
| Development Planning  | Phase / Milestone / Step  | Milestone 1.5        |

---

## Architecture
```
Presentation Layer
|
├── Core
├── Modules
└── UI
```

---

## Functional Scope
```
Capability
|
├── Base
└── Extended
```

---

## Product Structure
```
Module
|
├── Core
|   ├── Core
|   ├── Administration
|   └── Master Data
|
├── Base
|   ├── Documents
|   ├── Sales
|   ├── Purchases
|   ├── Inventory
|   ├── Assets
|   ├── Payroll
|   ├── Accounting
|   └── Reporting
|
└── Extended
    ├── Document Management
    ├── CRM
    ├── Procurement Management
    ├── Warehouse
    ├── Asset Management
    ├── HR Management
    ├── Finance Management
    └── Reporting Suite
```

---

## User Navigation
```
Workspace
|
├── Administration
├── Operations
├── Accounting
└── Reporting
```

---

## Product Maturity
```
Production Stage
|
├── Stage 1 Operational Orion
└── Stage 2 Management Orion
```

---

## Development Planning
```
Development Roadmap 
|
├── Phase 1
|   ├── Milestone 1.1
|   |   ├── Step 1   
|   |   ├── Step 2    
|   |   └── ...
|   |
|   ├── Milestone 1.2
|   |   ├── Step 1   
|   |   ├── Step 2    
|   |   └── ...
|   └── ...
|
├── Phase 2
|   ├── Milestone 2.1
|   |   ├── Step 1   
|   |   ├── Step 2    
|   |   └── ...
|   |
|   ├── Milestone2.2
|   |   ├── Step 1   
|   |   ├── Step 2    
|   |   └── ...
|   └── ...
|
└── ...
