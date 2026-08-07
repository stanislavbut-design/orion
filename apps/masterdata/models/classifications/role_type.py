from django.core.exceptions import ValidationError
from django.db import models

from apps.core.constants.validation.masterdata import (
    ROLE_TYPE_CODE_REQUIRED_ERROR,
    ROLE_TYPE_NAME_REQUIRED_ERROR,
)


class RoleType(models.Model):
    """
    Defines a business role that may be performed by a Business Actor
    within a Business Relationship.
    """

    id = models.BigAutoField(primary_key=True)

    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Code",
        help_text="Stable internal identifier.",
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Name",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name="Sort Order",
    )

    class Meta:
        verbose_name = "Role Type"
        verbose_name_plural = "Role Types"
        ordering = ["sort_order", "code"]

    def clean(self):
        super().clean()

        self.code = (self.code or "").strip().upper()
        self.name = (self.name or "").strip()

        if not self.code:
            raise ValidationError(ROLE_TYPE_CODE_REQUIRED_ERROR)

        if not self.name:
            raise ValidationError(ROLE_TYPE_NAME_REQUIRED_ERROR)

    def __str__(self):
        return self.name