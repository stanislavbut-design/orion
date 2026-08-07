from django.db import models
from django.core.exceptions import ValidationError

from apps.masterdata.models import CoreEntityBase

from apps.core.constants.validation.masterdata import (
    DEP_PARENT_SELF_ERROR,
    DEP_NO_DIRECT_EDIT_ERROR
)

class Department(CoreEntityBase):
    """
    Persistent organizational unit within an Organization.

    Departments form a hierarchical structure.

    Each Department belongs to exactly one Company. Each Department may belong
    to one Responsibility Center. Both associations may be inherited
    through the Department hierarchy.
    """

    department_code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Department Code",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="Department Name",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    parent_department = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="child_departments",
        verbose_name="Parent Department",
    )

    root_department = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="subdepartments",
        verbose_name="Root Department",
    )

    company = models.ForeignKey(
        "masterdata.Party",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="departments",
        verbose_name="Company",
    )

    responsibility_center = models.ForeignKey(
        "masterdata.ResponsibilityCenter",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="departments",
        verbose_name="Responsibility Center",
    )

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["department_code", "name"]

    def __str__(self):
        if self.department_code:
            return f"{self.department_code} - {self.name}"
        return self.name

    def clean(self):
        super().clean()

        if self.parent_department == self:
            raise ValidationError(
                DEP_PARENT_SELF_ERROR
            )

        if self.pk:
            original = Department.objects.get(pk=self.pk)

            service_managed_fields = (
                "parent_department_id",
                "root_department_id",
                "company_id",
                "responsibility_center_id",
            )

            for field in service_managed_fields:
                if getattr(original, field) != getattr(self, field):
                    raise ValidationError(
                        DEP_NO_DIRECT_EDIT_ERROR
                    )