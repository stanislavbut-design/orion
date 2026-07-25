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