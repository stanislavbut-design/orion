import uuid

from django.core.exceptions import ValidationError
from django.db import models

from apps.core.constants.validation import (
    PER_FIRST_NAME_REQUIRED,
    PER_LAST_NAME_REQUIRED,
)

from apps.core.constants.naming import (
    PER_DEFAULT_FULL_NAME_FORMAT,
    PER_DEFAULT_SHORT_NAME_FORMAT,
    FULL_NAME_FIRST_MIDDLE_LAST,
    FULL_NAME_LAST_FIRST_MIDDLE,    
    FULL_NAME_LAST_COMMA_FIRST_MIDDLE,
    SHORT_NAME_LAST_INITIALS,   
    SHORT_NAME_INITIALS_LAST,
    SHORT_NAME_FIRST_LAST,
)

from .organization import Organization

class Person(models.Model):

    # Duplicated intentionally.
    # A common base entity will be introduced only after shared
    # attributes have been validated across multiple domain entities.
    id = models.BigAutoField(
        primary_key=True,
    )
        
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="persons",
    )

    first_name = models.CharField(
        max_length=40,
    )

    middle_name = models.CharField(
        max_length=40,
        blank=True,
    )

    last_name = models.CharField(
        max_length=40,
    )

    personal_id = models.CharField(
        max_length=20,
        blank=True,
    )

    full_name = models.CharField(
        max_length=200,
        editable=False,
    )

    short_name = models.CharField(
        max_length=80,
        editable=False,
    )

    class Meta:
        ordering = ["last_name", "first_name", "middle_name"]
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self) -> str:
        return self.full_name
    
    def clean(self):
        """
        Validate business rules.
        """

        self.first_name = self.first_name.strip()
        self.middle_name = self.middle_name.strip()
        self.last_name = self.last_name.strip()
        self.personal_id = (self.personal_id or "").strip()

        if not self.first_name:
            raise ValidationError({
                "first_name": PER_FIRST_NAME_REQUIRED
            })

        if not self.last_name:
            raise ValidationError({
                "last_name": PER_LAST_NAME_REQUIRED
            })

    def _compose_names(self):
        """
        Compose Full Name and Short Name.

        Future versions will use Organization naming preferences.
        """

        if PER_DEFAULT_FULL_NAME_FORMAT == FULL_NAME_FIRST_MIDDLE_LAST:
            parts = [
                self.first_name,
                self.middle_name,
                self.last_name,
            ]
        elif PER_DEFAULT_FULL_NAME_FORMAT == FULL_NAME_LAST_FIRST_MIDDLE:
            parts = [
                self.last_name,
                self.first_name,
                self.middle_name,
            ]
        elif PER_DEFAULT_FULL_NAME_FORMAT == FULL_NAME_LAST_COMMA_FIRST_MIDDLE:
            parts = [
                self.last_name + ",",
                self.first_name,
                self.middle_name,
            ]
        else:
            raise ValueError(
                f"Unsupported full name format: "
                f"{PER_DEFAULT_FULL_NAME_FORMAT}"
            )

        full_name = " ".join(part for part in parts if part)

        initials = f"{self.first_name[0]}."

        if self.middle_name:
            initials += " " + self.middle_name[0] + "."

        if PER_DEFAULT_SHORT_NAME_FORMAT == SHORT_NAME_LAST_INITIALS:
            short_name = f"{self.last_name} {initials}"
        elif PER_DEFAULT_SHORT_NAME_FORMAT == SHORT_NAME_INITIALS_LAST:
            short_name = f"{initials} {self.last_name}"
        elif PER_DEFAULT_SHORT_NAME_FORMAT == SHORT_NAME_FIRST_LAST:
            short_name = f"{self.first_name} {self.last_name}"
        else:
            raise ValueError(
                f"Unsupported short name format: "
                f"{PER_DEFAULT_SHORT_NAME_FORMAT}"
            )

        return full_name, short_name

    def save(self, *args, **kwargs):

        self.full_clean()

        self.full_name, self.short_name = (
            self._compose_names()
        )

        super().save(*args, **kwargs)