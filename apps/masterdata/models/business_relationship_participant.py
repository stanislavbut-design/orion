import uuid

from django.db import models

from ..constants import RoleType
from .business_relationship import BusinessRelationship
from .organization import Organization
from .party import Party
from .person import Person


class BusinessRelationshipParticipant(models.Model):
    """
    Represents one participant in a Business Relationship.

    Exactly one of organization, party or person shall identify
    the participating Identity.
    """

    id = models.BigAutoField(
        primary_key=True,
    )

    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    business_relationship = models.ForeignKey(
        BusinessRelationship,
        on_delete=models.CASCADE,
        related_name="participants",
    )

    role_type = models.CharField(
        max_length=32,
        choices=RoleType.choices,
    )

    organization = models.ForeignKey(
        Organization,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="relationship_participations",
    )

    party = models.ForeignKey(
        Party,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="relationship_participations",
    )

    person = models.ForeignKey(
        Person,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="relationship_participations",
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
            "business_relationship",
            "role_type",
            "id",
        ]
        verbose_name = "Business Relationship Participant"
        verbose_name_plural = "Business Relationship Participants"

    def __str__(self):
        return (
            f"{self.get_role_type_display()} "
            f"({self.business_relationship})"
        )

    @property
    def participant(self):
        """
        Returns the participating identity.
        """

        return (
            self.organization
            or self.party
            or self.person
        )