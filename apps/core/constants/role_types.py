from django.db import models


class RoleType(models.TextChoices):
    ORGANIZATION = (
        "ORGANIZATION",
        "Organization",
    )

    COMPANY = (
        "COMPANY",
        "Company",
    )

    PARTNER = (
        "PARTNER",
        "Partner",
    )

    DIRECTOR = (
        "DIRECTOR",
        "Director",
    )

    EMPLOYEE = (
        "EMPLOYEE",
        "Employee",
    )

    CUSTOMER = (
        "CUSTOMER",
        "Customer",
    )

    SUPPLIER = (
        "SUPPLIER",
        "Supplier",
    )

    PROVIDER = (
        "PROVIDER",
        "Provider",
    )

    LENDER = (
        "LENDER",
        "Lender",
    )

    INSURER = (
        "INSURER",
        "Insurer",
    )

    LESSOR = (
        "LESSOR",
        "Lessor",
    )