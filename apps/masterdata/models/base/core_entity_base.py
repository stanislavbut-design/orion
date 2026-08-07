import uuid

from django.db import models


class CoreEntityBase(models.Model):

    id = models.BigAutoField(primary_key=True)
    
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True