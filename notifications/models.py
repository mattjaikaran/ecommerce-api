from uuid import uuid4
from django.db import models

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Name', max_length=255)
    content = models.CharField('Content', max_length=255)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
