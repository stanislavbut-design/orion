import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from .person import Person

from ..base.core_entity_base import CoreEntityBase

from apps.core.constants.validation.masterdata import(
    PTY_INDIVIDUAL_PERSON_REQUIRED,
    PTY_PERSON_NOT_ALLOWED,
    PTY_PERSON_ALREADY_ASSOCIATED,
)

class PartyTypes(models.TextChoices):
    LEGAL_ENTITY = "LEGAL_ENTITY", "Legal Entity"
    INDIVIDUAL = "INDIVIDUAL", "Individual"

class Party(CoreEntityBase):

    party_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        unique=True,
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

    person = models.ForeignKey(
        Person,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="party",
    )

    business_id = models.CharField(
        max_length=20,
        blank=False,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Party"
        verbose_name_plural = "Parties"

        constraints = [
            models.UniqueConstraint(
                fields=["party_code"],
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

    def clean(self):
        """
        Validate business rules.
        """
        super().clean()

        if self.party_type == PartyTypes.INDIVIDUAL and self.person is None:
            raise ValidationError({
                "person": PTY_INDIVIDUAL_PERSON_REQUIRED
            })

        if self.party_type != PartyTypes.INDIVIDUAL and self.person is not None:
            raise ValidationError({
                "person": PTY_PERSON_NOT_ALLOWED
            })

        if self.person is not None:        
            if Party.objects.filter(
                person=self.person,
                party_type=PartyTypes.INDIVIDUAL,
            ).exclude(pk=self.pk).exists():
                raise ValidationError({
                    "person": PTY_PERSON_ALREADY_ASSOCIATED
                })