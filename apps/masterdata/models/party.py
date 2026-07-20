import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from .organization import Organization

PTY_EMPTY_PERSON_ERROR = (
        "A Party of the Individual type must have the Person associated with it."
    )

class PartyTypes(models.TextChoices):
    LEGAL_ENTITY = "LEGAL_ENTITY", "Legal Entity"
    INDIVIDUAL = "INDIVIDUAL", "Individual"

class Party(models.Model):

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
        related_name="parties",
    )

    name = models.CharField(
        max_length=60,
        unique=True,
    )

    legal_name = models.CharField(
        max_length=200,
        blank=True,
    )

    party_type = models.CharField(
        max_length=20,
        choices=PartyTypes.choices,
        default=PartyTypes.LEGAL_ENTITY,
    )

    business_id = models.CharField(
        max_length=20,
        blank=False,
    )

    party_code = models.CharField(
        max_length=10,
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Party"
        verbose_name_plural = "Parties"

        constraints = [
            models.UniqueConstraint(
                fields=["organization", "party_code"],
                name="uq_party_party_code",
            ),
            
            models.CheckConstraint(
                condition=Q(party_type__in=[
                    PartyTypes.LEGAL_ENTITY,
                    PartyTypes.INDIVIDUAL,
                ]),
                name="chk_party_party_type",
            ),
        ]

    def __str__(self) -> str:
        return self.name