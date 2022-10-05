from uuid import uuid4
from django.db import models
from .constants import CATEGORY_CHOICES

class Category(models.Model):
  id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
  name = models.CharField('Name', choices=CATEGORY_CHOICES, max_length=255)

  class Meta:
        verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name