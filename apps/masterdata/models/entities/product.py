from django.db import models

from ..base.core_entity_base import CoreEntityBase


class Product(CoreEntityBase):
    """
    Core Entity representing a persistent good or service.

    Product defines the business identity of a good or service.
    Operational characteristics (inventory, pricing, accounting,
    procurement, manufacturing, etc.) are provided by capabilities
    built on top of this entity.
    """

    product_code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Product Code",
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
        ordering = ["product_code", "name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return (
            f"{self.product_code} - {self.name}"
            if self.product_code
            else self.name
        )