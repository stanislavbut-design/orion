Orion Commit Convention
Format
S<Stage>-M<Milestone>.<Step> Short description
Components
Component	Meaning	Example
S01	Stage	Stage 1 — Core Domain Foundation
M01.01	Milestone	Milestone 1.1 — Master Data Foundation
01	Step	Step 1 — Create masterdata application
Description	Brief imperative summary	Create masterdata application

Example:

S01-M01.01.01 Create masterdata application
Example History
Stage 0 — Foundation
S00-M00.01.01 Reorganize project documentation
Stage 1 — Core Domain Foundation
S01-M01.01.01 Create masterdata application
S01-M01.01.02 Organize masterdata application structure
S01-M01.01.03 Implement Organization
S01-M01.01.04 Implement Party
S01-M01.01.05 Implement Person
S01-M01.01.06 Review Master Data Foundation

Later:

S01-M01.02.01 Implement RoleType
S01-M01.02.02 Implement RoleAssignment
Description Guidelines

The description should:

start with an imperative verb;
be concise;
describe the completed work;
omit a trailing period.

Good examples:

Create masterdata application
Implement Organization
Register Party in Django Admin
Add initial migration
Update domain documentation

Avoid vague descriptions such as:

Changes
Updates
Fixes
Work in progress
Traceability

One of the strengths of this convention is that every commit can be traced back to the project plan:

Project
└── Stage 1
    └── Milestone 1.1
        └── Step 3
            └── Commit

Likewise, when reviewing a milestone, we can immediately identify the commits that implemented it.