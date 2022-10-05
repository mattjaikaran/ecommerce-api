from uuid import uuid4
from django.db import models

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Name', max_length=255)
    content = models.CharField('Name', max_length=255)
