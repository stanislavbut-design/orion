from django.db import models

from ..base.core_entity_base import CoreEntityBase


class Project(CoreEntityBase):
    """
    Core Entity representing a persistent body of work undertaken by an Organization.

    """

    project_code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Project Code",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="Name",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    class Meta:
        ordering = ["project_code", "name"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return (
            f"{self.project_code} - {self.name}"
            if self.project_code
            else self.name
        )