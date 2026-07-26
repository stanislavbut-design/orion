"""
Business Object lifecycle statuses.

These constants define the generic lifecycle of Business Objects.
Individual modules may introduce additional workflow states where required,
but shall preserve the semantic meaning of these architectural states.
"""


class BusinessObjectStatus:
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    ARCHIVED = "ARCHIVED"


BUSINESS_OBJECT_STATUS_CHOICES = [
    (BusinessObjectStatus.DRAFT, "Draft"),
    (BusinessObjectStatus.ACTIVE, "Active"),
    (BusinessObjectStatus.COMPLETED, "Completed"),
    (BusinessObjectStatus.CANCELLED, "Cancelled"),
    (BusinessObjectStatus.ARCHIVED, "Archived"),
]