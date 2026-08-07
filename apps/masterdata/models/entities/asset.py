from django.db import models

from ..base.core_entity_base import CoreEntityBase


class Asset(CoreEntityBase):
    """
    Core Entity representing a fixed asset.

    """

    asset_code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Asset Code",
    )

    name = models.CharField(
        max_length=200,
        verbose_name="Name",
    )

    reference = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Reference",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    class Meta:
        ordering = ["asset_code", "name"]
        verbose_name = "Asset"
        verbose_name_plural = "Assets"

    def __str__(self):
        return (
            f"{self.asset_code} - {self.name}"
            if self.asset_code
            else self.name
        )