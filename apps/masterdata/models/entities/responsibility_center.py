from django.db import models
from django.core.exceptions import ValidationError

from apps.masterdata.models import CoreEntityBase

from apps.core.constants.validation.masterdata import (
    RES_PARENT_SELF_ERROR,
)

class ResponsibilityCenter(CoreEntityBase):
    """
    Persistent functional area of accountability within an Organization.

    Responsibility Centers form a hierarchical structure. Company assignment and
    Department assignment are managed through Structural
    Relationships rather than stored directly on the Responsibility Center.
    """

    responsibility_center_code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Responsibility Center Code",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="Responsibility Center Name",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    parent_responsibility_center = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="child_responsibility_centers",
        verbose_name="Parent Responsibility Center",
    )

    class Meta:
        verbose_name = "Responsibility Center"
        verbose_name_plural = "Responsibility Centers"
        ordering = ["responsibility_center_code", "name"]

    def __str__(self):
        if self.responsibility_center_code:
            return f"{self.responsibility_center_code} - {self.name}"
        return self.name

    def clean(self):
        super().clean()

        if self.parent_responsibility_center == self:
            raise ValidationError(
                RES_PARENT_SELF_ERROR
            )

    @property
    def is_leaf(self):
        return not self.child_responsibility_centers.exists()