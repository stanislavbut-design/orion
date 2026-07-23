# Business Relationship Framework

# 1. Purpose

The Business Relationship Framework defines how Orion models stable business relationships between Identities.

It establishes:

- the predefined Relationship Types provided by Orion;
- the Role Types permitted within each Relationship Type;
- the Identity Types permitted to perform each Role Type;
- the relationship matrix governing valid combinations.

The framework provides the semantic foundation upon which Business Objects create, modify and terminate Business Relationships.

# 2. Definition

A **Business Relationship** is a stable semantic relationship between two or more Identities.

Every Business Relationship:

- belongs to exactly one Relationship Type;
- consists of two or more participants;
- assigns exactly one Role Type to each participant;
- restricts each Role Type to one Identity Type.

Business Relationships are independent of the Business Objects that create or modify them.

# 3. Relationship Matrix

## 3.1 Overview

The Relationship Matrix defines every Relationship Type supported by Orion.

For each Relationship Type it specifies:

- Business Domain;
- Canonical Code;
- permitted Identity Types;
- permitted Role Types.

Every Business Relationship shall conform to this matrix unless explicitly extended by a future Orion release.

<table border="1" cellspacing="0" cellpadding="0">
    <tbody><table border="0" cellspacing="0" cellpadding="0" width="663">
    <tbody>
        <tr>
            <td width="115" valign="top">
                <p align="center">
                    <strong>Business Domain</strong>
                </p>
            </td>
            <td width="175" valign="top">
                <p align="center">
                    <strong>Relationship Type</strong>
                </p>
            </td>
            <td width="164" valign="top">
                <p align="center">
                    <strong>Canonical Code</strong>
                </p>
            </td>
            <td width="103" valign="top">
                <p align="center">
                    <strong>Identity Type</strong>
                </p>
            </td>
            <td width="106" valign="top">
                <p align="center">
                    <strong>Role Type</strong>
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Organizational   structure
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Business   Composition
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    BIZ_STRUCTURE
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Organization
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Organization
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Business   Ownership
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Ownership   Relationship
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    BIZ_OWNERSHIP
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Partner
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Corporate Governance
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Director   Appointment
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    CORP_GOV
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Person
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Director
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Employment
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Employment Agreement
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    EMPLOYMENT
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Person
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Employee
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Sales
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Sales   Agreement
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    SALES
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Customer
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Purchase
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Supply   Agreement
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    PURCHASE
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Supplier
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Service
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Service   Agreement
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    SERVICE
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Provider
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Finance
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Loan   Agreement
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    LOAN
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Lender
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Insurance
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Insurance   Policy
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    INSURANCE
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Insurer
                </p>
            </td>
        </tr>
        <tr>
            <td width="115" rowspan="2" valign="top">
                <p>
                    Leasing
                </p>
            </td>
            <td width="175" rowspan="2" valign="top">
                <p>
                    Lease   Agreement
                </p>
            </td>
            <td width="164" rowspan="2" valign="top">
                <p>
                    LEASE
                </p>
            </td>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Company
                </p>
            </td>
        </tr>
        <tr>
            <td width="103" valign="top">
                <p>
                    Party
                </p>
            </td>
            <td width="106" valign="top">
                <p>
                    Lessor
                </p>
            </td>
        </tr>
    </tbody>
</table>

# 4. Core Concepts

## 4.1 Business Domain

A Business Domain groups Relationship Types according to their business purpose.

Business Domains provide operational classification only.

They do not affect the semantics or behaviour of Business Relationships.

## 4.2 Relationship Type

A Relationship Type defines the semantic nature of a Business Relationship.

Each Relationship Type:

- belongs to one Business Domain;
- has one Canonical Code;
- defines the permitted Role Types.

Relationship Types are predefined by Orion.

## 4.3 Canonical Code

The Canonical Code uniquely identifies a Relationship Type within Orion.

Canonical Codes are stable identifiers intended for implementation, integration and internal referencing.

Their values shall remain stable across Orion versions.

## 4.4 Role Type

A Role Type defines the capacity in which an Identity participates in a Business Relationship.

Every Role Type:

- belongs to exactly one Relationship Type;
- is associated with exactly one Identity Type.

Examples include:

- Company
- Customer
- Supplier
- Provider
- Employee
- Director
- Partner
- Lender
- Insurer
- Lessor

## 4.5 Identity Type

Identity Type defines the category of Identity permitted to perform a Role.

Within the current framework, the permitted Identity Types are:

- Organization
- Party
- Person

## 4.6 Business Relationship

A Business Relationship is an instance of a Relationship Type.

Each instance records the participating Identities together with the Role performed by each participant.

The lifecycle of a Business Relationship is governed by Business Objects.

# 5. Business Rules

## BRF-001

Relationship Types shall be predefined by Orion.

## BRF-002

Every Business Relationship shall belong to exactly one Relationship Type.

## BRF-003

Each Relationship Type shall define two or more permitted Role Types.

## BRF-004

Each Role Type shall be associated with exactly one Identity Type.

## BRF-005

A Business Relationship shall contain exactly one participant for every mandatory Role Type unless otherwise specified by the Relationship Type.

## BRF-006

An Identity shall perform only Role Types permitted for its Identity Type.

## BRF-007

Canonical Codes are immutable identifiers.

## BRF-008

Business Domains classify Relationship Types but do not affect their semantics.

# 6. Notes

The current Relationship Matrix represents the initial set of Relationship Types required by Orion.

Future Orion releases may extend the matrix by introducing additional Relationship Types and Role Types.

Extensions shall preserve the architectural principles defined in ARCH-003.

# 7. Related Documents

ARCH-003 — Domain Model
Organization Specification
Party Specification
Person Specification