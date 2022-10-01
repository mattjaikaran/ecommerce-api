from random import choices
from uuid import uuid4
from django.db import models
from .constants import ORDER_CHOICES

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    status = models.CharField(max_length=50, choices=ORDER_CHOICES, blank=True, null=True)
    is_fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return self.name