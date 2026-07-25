from django.db import models


class RelationshipType(models.TextChoices):
    BIZ_STRUCTURE = (
        "BIZ_STRUCTURE",
        "Business Composition",
    )

    BIZ_OWNERSHIP = (
        "BIZ_OWNERSHIP",
        "Ownership Relationship",
    )

    CORP_GOV = (
        "CORP_GOV",
        "Director Appointment",
    )

    EMPLOYMENT = (
        "EMPLOYMENT",
        "Employment Agreement",
    )

    SALES = (
        "SALES",
        "Sales Agreement",
    )

    PURCHASE = (
        "PURCHASE",
        "Supply Agreement",
    )

    SERVICE = (
        "SERVICE",
        "Service Agreement",
    )

    LOAN = (
        "LOAN",
        "Loan Agreement",
    )

    INSURANCE = (
        "INSURANCE",
        "Insurance Policy",
    )

    LEASE = (
        "LEASE",
        "Lease Agreement",
    )