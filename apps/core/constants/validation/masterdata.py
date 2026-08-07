"""
Validation messages.

These constants are used throughout Orion instead of hard-coded
user-facing messages. Future versions may replace them with
localized translations.
"""

# Organization
ORG_SINGLETON_ERROR = "Exactly one Organization may exist in an Orion installation."
ORG_DELETE_ERROR = "The Organization cannot be deleted."
ORG_NAME_REQUIRED = "Organization Name is required."

# Party
PTY_EMPTY_PERSON_ERROR = "A Party of the Individual type must have the Person associated with it."

# Person
PER_FIRST_NAME_REQUIRED = "First Name is required."
PER_LAST_NAME_REQUIRED = "Last Name is required."

# Department
DEP_PARENT_SELF_ERROR = "A Department cannot be its own parent."
DEP_NO_DIRECT_EDIT_ERROR = "Direct editing of the Department hierarchy is not allowed. Use the DepartmentHierarchyService instead."
DEP_CIRCULAR_HIERARCHY_ERROR = "A Department cannot be moved under one of its descendants."
# DEP-008 — Department Company Association
DEP_ORPHANED_DEPARTMENT_ERROR = "A Department cannot exist without a parent Department or a Company association."
# DEP-009 — Child Department Company Inheritance
DEP_ROOT_COMPANY_ONLY_ERROR = "Only root Departments may be associated with a Company."
# DEP-011 — Responsibility Center Association
DEP_RC_OVERRIDE_ERROR = "A Responsibility Center association established by a parent Department cannot be overridden."
# RCN-009 — Direct Association Target, RCN-011 — No Lower-Level Override
DEP_RC_MUST_BE_LEAF_ERROR = "A Responsibility Center must be a leaf node in the hierarchy."


# ResponsibilityCenter
RES_PARENT_SELF_ERROR = "A Responsibility Center cannot be its own parent."

# BusinessRelationship
BRL_INVALID_DATE_RANGE = "Effective To cannot be earlier than Effective From."

# BusinessRelationshipParticipant
BRP_EXACTLY_ONE_IDENTITY = "Exactly one of Organization, Party or Person shall be specified."
BRP_INVALID_DATE_RANGE = "Effective To cannot be earlier than Effective From."
BRP_ROLE_IDENTITY_MISMATCH = "The selected Role Type is not valid for the specified Identity."
BRP_ROLE_RELATIONSHIP_MISMATCH = "The selected Role Type is not permitted for this Relationship Type."

PTY_INDIVIDUAL_PERSON_REQUIRED = "An Individual Party must be associated with a Person."
PTY_PERSON_NOT_ALLOWED = "Only Individual Parties may be associated with a Person."
PTY_PERSON_ALREADY_ASSOCIATED = "The selected Person is already associated with another Individual Party."

# Role Type
ROLE_TYPE_CODE_REQUIRED_ERROR = "Role Type code is required."
ROLE_TYPE_NAME_REQUIRED_ERROR = "Role Type name is required."

# BusinessProcess
BPR_PARENT_SELF_ERROR = "A Business Process cannot be its own parent."

# BusinessObject
BO_PARENT_SELF_ERROR = "A Business Object cannot be its own parent."
BO_PARENT_CYCLE_ERROR = "A circular Business Object hierarchy is not allowed."
BO_DATE_RANGE_ERROR = "Effective To cannot be earlier than Effective From."
BO_PROCESS_NOT_LEAF_ERROR = (
    "Only lowest-level Business Processes may be associated "
    "with Business Objects."
)
BO_PROCESS_INHERITANCE_ERROR = "Child Business Objects must inherit the Business Process from the Root Business Object."
