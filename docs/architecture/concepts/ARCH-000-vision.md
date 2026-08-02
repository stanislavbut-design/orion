# Vision

| Property | Value |
|----------|-------|
| Document ID | ARCH-000 |
| Title | Vision |
| Status | Approved |
| Version | 2.0 |
| Owner | Orion Project |
| Last Updated | 2026-08-01 |
| Related ADRs | None |
| Replaces | ARCH-000 v.1.0 |
| Superseded By | — |

---

## Purpose

Orion aims to be an integrated business management platform for small and medium-sized enterprises (SMEs).

While initially focused on service-oriented businesses and business groups, its architecture is designed to support gradual evolution into a full-fledged ERP platform.

Its purposes are:
- to support to support business growth from micro to small and medium-sized enterprises;
- to support the complete business cycle from client acquisition through service execution to financial reporting and data integration within a single, coherent system built on a common business model.

---

## Progressive Capability

Organizations should be able to start with a small set of core capabilities and progressively adopt more advanced management capabilities without disrupting existing business processes or data.

---

## Vision

Orion aims to become a comprehensive platform that enables business organizations to manage their business using accurate, consistent and integrated information.

The platform is designed to minimize duplication of data, automate repetitive processes and support informed decision-making through reliable reporting and analytics.

Rather than focusing on individual software modules, Orion focuses on the business processes that connect them.

---

## Scope

The initial release focuses on the core business capabilities required to support small, mostly service-oriented, businesses.

The Progressive Enhancement approach envisions gradually adding customer value by building extended business capabilities, such as CRM, HR Management, Finance Management, etc., on the core capabilities without causing disruption.

The detailed module architecture is described in ARCH-007.

The architecture intentionally allows additional business modules to be introduced without requiring changes to the platform itself.

---

## Design Goals

The primary goals of Orion are:
- Business-first architecture
- Automation of business processes
- Reliable reporting
- Modular design
- Strong data integrity
- Extensibility
- Maintainability
- Long-term scalability

---

## Target Users

The primary users of Orion are:

- Professional service businesses
- Other service-oriented businesses
- Business groups consisting of multiple legal entities
- Small and medium-sized organizations

---

## Non-Goals

Orion is not intended to maximize functional breadth for every possible industry or business model.

Instead, Orion focuses on delivering a coherent, extensible platform tailored to its intended business domain while remaining flexible enough to evolve over time.

---

## Long-Term Vision

The long-term objective is to establish Orion as the operational platform for managing business activities, integrating internal and external information sources and providing a single, authoritative source of business information.

Business rules should be implemented once and reused consistently across user interfaces, reports, APIs and integrations.

