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
    BO_DATE_RANGE_ERROR,
    BO_PARENT_SELF_ERROR,
    BO_PARENT_CYCLE_ERROR,
    BO_PROCESS_INHERITANCE_ERROR,
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

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="children",
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

        if self.parent == self:
            raise ValidationError(
                BO_PARENT_SELF_ERROR
            )

        #
        # Circular hierarchy
        #

        ancestor = self.parent

        while ancestor is not None:

            if ancestor == self:
                raise ValidationError(
                    BO_PARENT_CYCLE_ERROR
                )

            ancestor = ancestor.parent


        if (
            self.effective_from
            and self.effective_to
            and self.effective_to < self.effective_from
        ):
            raise ValidationError(
                BO_DATE_RANGE_ERROR
            )

        if (
            self.business_process
            and self.business_process.subprocesses.exists()
        ):
            raise ValidationError(
                BO_PROCESS_NOT_LEAF_ERROR
            )

        #
        # Business Process inheritance
        #

        if self.parent is not None:

            root = self.root
            
            if root is not self:

                if self.business_process != root.business_process:
                    raise ValidationError(
                        BO_PROCESS_INHERITANCE_ERROR
                    )

    @property
    def is_root(self):
        return self.parent is None

    @property
    def root(self):

        obj = self

        while obj.parent is not None:
            obj = obj.parent

        return obj

