import uuid

from django.core.exceptions import ValidationError
from django.db import models

from apps.core.constants.relationship_types import RelationshipType
from apps.core.constants.validation.masterdata import (
    BRL_INVALID_DATE_RANGE,
)

from ..organization import Organization


class BusinessRelationship(models.Model):
    """
    Represents a stable business relationship between identities.

    Participants and their roles are stored separately in
    BusinessRelationshipParticipant.
    """

    id = models.BigAutoField(
        primary_key=True,
    )

    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    relationship_type = models.CharField(
        max_length=32,
        choices=RelationshipType.choices,
    )

    effective_from = models.DateField(
        null=True,
        blank=True,
    )

    effective_to = models.DateField(
        null=True,
        blank=True,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = [
            "relationship_type",
            "effective_from",
            "id",
        ]
        verbose_name = "Business Relationship"
        verbose_name_plural = "Business Relationships"

    def __str__(self):
        return f"{self.get_relationship_type_display()}"

    def clean(self):
        super().clean()

        if (
            self.effective_from
            and self.effective_to
            and self.effective_to < self.effective_from
        ):
            raise ValidationError(BRL_INVALID_DATE_RANGE)

