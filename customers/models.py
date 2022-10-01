from uuid import uuid4
from django.db import models

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    email = models.EmailField(max_length=30, null=False, unique=True)

    def __str__(self):
      return self.email