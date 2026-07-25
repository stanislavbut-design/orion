import uuid

from django.core.exceptions import ValidationError
from django.db import models

from apps.core.constants.role_types import RoleType

from .business_relationship import BusinessRelationship
from .organization import Organization
from .party import Party
from .person import Person

from apps.core.constants.relationship_matrix import (
    ROLE_IDENTITY_MAP,
    RELATIONSHIP_ROLE_MAP,
)

from apps.core.constants.validation.masterdata import (
    BRP_EXACTLY_ONE_IDENTITY,
    BRP_INVALID_DATE_RANGE,
    BRP_ROLE_IDENTITY_MISMATCH,
    BRP_ROLE_RELATIONSHIP_MISMATCH,
)

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

    def clean(self):

        super().clean()

        #
        # Exactly one Identity
        #

        identities = [
            self.organization,
            self.party,
            self.person,
        ]

        identity_count = sum(
            identity is not None
            for identity in identities
        )

        if identity_count != 1:
            raise ValidationError(
                BRP_EXACTLY_ONE_IDENTITY
            )

        #    raise ValidationError(
        #        f"Org={self.organization_id}, "
        #        f"Party={self.party_id}, "
        #        f"Person={self.person_id}, "
        #        f"Count={identity_count}"
        #    )
        #
        # Effective dates
        #

        if (
            self.effective_from
            and self.effective_to
            and self.effective_to < self.effective_from
        ):
            raise ValidationError(
                BRP_INVALID_DATE_RANGE
            )

        #
        # Role ↔ Identity
        #

        expected_identity = ROLE_IDENTITY_MAP.get(
            self.role_type
        )

        if expected_identity == "organization":
            valid = self.organization is not None

        elif expected_identity == "party":
            valid = self.party is not None

        elif expected_identity == "person":
            valid = self.person is not None

        else:
            valid = False

        if not valid:
            raise ValidationError(
                BRP_ROLE_IDENTITY_MISMATCH
            )

        #
        # Relationship ↔ Role
        #

        allowed_roles = RELATIONSHIP_ROLE_MAP.get(
            self.business_relationship.relationship_type,
            set(),
        )

        if self.role_type not in allowed_roles:
            raise ValidationError(
                BRP_ROLE_RELATIONSHIP_MISMATCH
            )

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