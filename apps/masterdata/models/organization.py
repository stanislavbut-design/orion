import uuid

from django.core.exceptions import ValidationError
from django.db import models


class Organization(models.Model):
    """
    Represents the entire business managed by an Orion installation.

    An Organization is the highest-level identity in the Orion domain model.
    It defines the ownership boundary for all Parties and Persons.
    """
    SINGLETON_ERROR = (
        "Exactly one Organization may exist in an Orion installation."
    )

    # Duplicated intentionally.
    # A common base entity will be introduced only after shared
    # attributes have been validated across multiple domain entities.
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    name = models.CharField(
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ["name"]
    
    def clean(self):
        super().clean()

        if not self.pk and Organization.objects.exists():
            raise ValidationError(self.SINGLETON_ERROR)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name