from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

from apps.core.constants.validation.masterdata import (
    BPR_PARENT_SELF_ERROR,
)

class BusinessProcess(models.Model):
    """
    Defines an organizational business process.

    Business Processes provide operational context for Business Objects.
    They are structural concepts rather than executable workflows.
    """

    id = models.BigAutoField(
        primary_key=True,
    )

    public_id = models.UUIDField(
        default=uuid4,
        editable=False,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        unique=True,
    )

    name = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    parent_process = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="subprocesses",
    )

    class Meta:
        ordering = [
            "code",
        ]

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        if self.parent_process == self:
            raise ValidationError(
                BPR_PARENT_SELF_ERROR
            )