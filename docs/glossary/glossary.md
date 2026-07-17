# GLOSSARY



| Property | Value |
|----------|-------|
| Document ID | GLOSSARY |
| Title | Glossary |
| Status | Draft |
| Version | 1.0 |
| Owner | Orion Project |
| Last Updated | 2026-07-14 |



---

## Business Process

**Category:** Business Process

### Definition

A **Business Process** is a repeatable sequence of Business Activities performed to achieve a defined business outcome.

### Description

A Business Process defines how an Organization consistently performs a particular area of business activity. It provides the business context within which Business Relationships are established and Business Objects are created, modified and utilized.

Business Processes may be hierarchical. A Business Process may be decomposed into one or more Business Sub-processes. The lowest-level Business Processes consist of Business Activities.

Every Business Process belongs to exactly one Organization and has exactly one Responsibility Centre accountable for its execution.

Business Processes communicate with one another through Business Objects. Outputs produced by one Business Process may become inputs to other Business Processes.

### Business Rules

- Every Business Process shall achieve a defined business outcome.
- Every Business Process shall have exactly one Responsibility Centre.
- A Business Process may be decomposed into one or more Business Sub-processes.
- The lowest-level Business Processes consist of Business Activities.
- Every Business Process shall produce one or more Business Objects or modify the business state of existing Business Objects.
- Business Processes may consume Business Objects produced by other Business Processes.
- A Business Process may have no identifiable inputs.
- Business Processes shall not communicate directly; they communicate through Business Objects.

### See Also

- Business Activity
- Business Object
- Business Relationship
- Responsibility Centre

---


## Organization

**Category:** Identity

### Definition

An Organization is the highest-level business entity managed by Orion.

### Description

An Organization represents a business group that operates as a single economic subject. It defines the boundary for shared business processes, master data, users, reporting and administration.

### See Also

* Party
* Person
* Business Process

---

## Party

**Category:** Identity

### Definition

A **Party** is an identifiable entity that can participate in one or more business relationships within an Organization.

### Description

A Party represents a stable business identity independently of the roles it performs. A Party may represent a legal entity, an individual acting in a business capacity, a public authority, a financial institution, a non-profit organization or any other identifiable participant with which the Organization interacts.

A Party may simultaneously perform multiple business roles, such as Company, Customer, Supplier or Partner, without changing its underlying identity.

### See Also

* Organization
* Company
* Customer
* Supplier
* Partner

---

## Person

**Category:** Identity

### Definition

A Person is an individual known to Orion.

### Description

A Person represents a human being independently of any business role. A Person may become an employee, customer contact, supplier contact or system user without changing the underlying identity.

### See Also

* Employee
* User

---

## Employment

**Category:** Business Relationship

### Definition

An Employment represents the business relationship between an Employee and a Company.

### Description

Employment defines the terms under which a Person works for a Company, including dates, position, working conditions and payroll participation.

### See Also

* Person
* Employee
* Company

---

## User

**Category:** Role

### Definition

A User is a Person who is authorized to access Orion.

### Description

A User represents an authenticated identity used to interact with the system. Authentication and authorization are independent of the Person's employment status.

### See Also

* Person
* Role

---

## Company

**Category:** Role

### Definition

A **Company** is a business role performed by a Party within an Organization. It represents a Party acting as an operational legal entity responsible for conducting business activities.

### Description

The Company Role enables a Party to participate in the Organization's operational and statutory activities. A Party performing the Company Role may own financial records, enter into contracts, employ people, issue and receive invoices, own assets and assume liabilities, and fulfil statutory reporting obligations.

A single Party may perform the Company Role together with other roles, such as Customer, Supplier or Partner.

### See Also

- Organization
- Party
- Person
- Employment
- Customer
- Supplier

---

## Customer

**Category:** Role

### Definition

A **Customer** is a business role performed by a Party that receives products, services, rights or other business value from one or more Companies within an Organization.

### Description

The Customer Role enables a Party to participate in sales-related business processes. A Customer may request quotations, place orders, receive goods or services, receive invoices and make payments.

A Party may simultaneously perform the roles of Customer, Supplier, Partner or Company.

The Customer Role contains only business data specific to customer activities. General identity information remains part of the Party.

### Business Rules

- A Party may perform the Customer Role at most once within an Organization.
- Commercial arrangements, payment terms, contracts and pricing agreements shall be represented by separate Business Objects.
- A Party may simultaneously perform the Customer Role together with other roles, such as Supplier, Company and/or Partner.

### See Also

- Party
- Company
- Supplier
- Partner
- Invoice
- Assignment

---

## Supplier

**Category:** Role

### Definition

A **Supplier** is a business role performed by a Party that provides products, services, rights or other business value to one or more Companies within an Organization..

### Description

The Supplier Role enables a Party to participate in procurement-related business processes. Depending on the nature of the business relationship, a Supplier may provide products, services, usage rights, financial services, utilities, leased assets or other forms of business value.

A Supplier may respond to requests for quotation, receive purchase orders, conclude contracts, issue invoices and receive payments.

A Party may simultaneously perform the roles of Supplier, Customer, Partner or Company.

The Supplier Role contains only business data specific to supplier activities. General identity information remains part of the Party.

### Business Rules

- A Party may perform the Supplier Role at most once within an Organization.
- Commercial arrangements, payment terms, contracts and pricing agreements shall be represented by separate Business Objects.
- A Party may simultaneously perform the Supplier Role together with other roles, such as Customer, Company and/or Partner.

### See Also

- Party
- Company
- Customer
- Partner
- Invoice
- Assignment

---

## Partner

**Category:** Role

### Definition

A **Partner** is a business role performed by a Party that participates in the business activities of an Organization whose primary participation is not the direct exchange of business value.

### Description

The Partner Role enables a Party to participate in collaborative, regulatory or supporting business relationships that are not primarily based on the exchange of business value.

Examples include strategic partners, regulatory authorities, financial institutions acting in a non-supplier capacity, industry associations, shareholders and other organizations with which the Organization maintains an ongoing business relationship.

A Party may simultaneously perform the roles of Partner, Customer, Supplier or Company.

The Partner Role contains only business data specific to partner-related activities. General identity information remains part of the Party.

### Business Rules

- A Party may perform the Partner Role at most once within an Organization.
- A Party may simultaneously perform the Partner, Customer, Supplier and Company roles.
- Partner-specific agreements and collaborative arrangements shall be represented by separate Business Objects.

### See Also

- Party
- Company
- Customer
- Supplier
- Contract
- Assignment

---

## Employee

**Category:** Role

### Definition

An **Employee** is a business role performed by a Person who is eligible to work for one or more Companies within an Organization.

### Description

The Employee Role represents a Person's capability to participate in employment-related business processes. It establishes that a Person may be employed within the Organization but does not describe a specific employment.

The details of a Person's engagement, including employer, position, department, working hours, compensation and employment period, are represented by one or more Employment Business Relationships.

A Person may simultaneously perform the roles of Employee, User and Contact.

The Employee Role contains only business data specific to the Person's employee status. General personal information remains part of the Person.

### Business Rules

- A Person may perform the Employee role at most once within an Organization.
- A Person may have zero, one or multiple Employment Business Relationships.
- A Person may simultaneously perform the Employee, User and Contact roles.
- Employment-specific information shall be represented by Employment Business Relationships rather than by the Employee role.

### See Also

- Person
- Employment
- Company
- User
- Contact

---

## Employment

**Category:** Business Relationship

### Definition

An **Employment** is a Business Relationship between an Employee and a Company that defines the Employee's engagement by the Company.

### Description

Employment represents the business fact that an Employee is engaged by a Company. It exists independently of how the engagement is formalized or implemented.

An Employment may be established, modified or terminated through one or more Business Objects, such as an Employment Agreement or its amendments.

Employment determines the business context within which employment-related activities take place, including payroll, time recording, leave management and performance management.


### Business Rules

- Every Employment belongs to exactly one Organization.
- Every Employment relates exactly one Employee to exactly one Company.
- An Employee may participate in multiple Employments.
- A Company may participate in multiple Employments.

### See Also

- Employee
- Company
- Employment Agreement

---

## Employment Agreement

**Category:** Constitutive Business Object

### Definition

An **Employment Agreement** is a Constitutive Business Object that establishes an Employment, records and governs the agreed terms of an Employment throughout its lifecycle.

In Orion, an Agreement is a conceptual Business Object representing the agreed business terms governing a Business Relationship. It does not imply any particular legal form or documentation.

### Description

The Employment Agreement records the contractual terms governing an Employment, including employment period, position, compensation, working arrangements and other agreed conditions.

Multiple Employment Agreements or amendments may exist throughout the lifecycle of a single Employment where required by business practice or legislation.

Employment-related operational Business Objects, such as payroll calculations or time entries, operate within the context established by the Employment.

### Business Rules

- Every Employment Agreement belongs to exactly one Employment.
- An Employment may be governed by one or more Employment Agreements.
- Amendments may modify an existing Employment without creating a new Employment where permitted by applicable legislation or organizational policy.

### See Also

- Employment
- Employee
- Company