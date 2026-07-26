from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

from apps.core.constants.business_object_status import (
    BusinessObjectStatus,
    BUSINESS_OBJECT_STATUS_CHOICES,
)

from .business_process import BusinessProcess

from apps.core.constants.validation.masterdata import (
    BO_PROCESS_NOT_LEAF_ERROR,  
)


class BusinessObject(models.Model):
    """
    Abstract base class for all Business Objects.

    Business Objects are persistent operational artefacts that
    record business information within the context of Business Processes.
    """

    id = models.BigAutoField(
        primary_key=True,
    )

    public_id = models.UUIDField(
        default=uuid4,
        editable=False,
        unique=True,
    )

    business_process = models.ForeignKey(
        BusinessProcess,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    status = models.CharField(
        max_length=20,
        choices=BUSINESS_OBJECT_STATUS_CHOICES,
        default=BusinessObjectStatus.DRAFT,
    )

    effective_from = models.DateField(
        null=True,
        blank=True,
    )

    effective_to = models.DateField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True

    def clean(self):
        super().clean()

        if (
            self.business_process
            and self.business_process.subprocesses.exists()
        ):
            raise ValidationError(
                BO_PROCESS_NOT_LEAF_ERROR
            )