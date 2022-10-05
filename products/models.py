from uuid import uuid4
from django.db import models
from categories.models import Category
from .constants import TAG_CHOICES

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Name', max_length=255)
    category = models.ForeignKey(Category, related_name='Product Category', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, max_length=3, null=True)
    tags = models.CharField(choices=TAG_CHOICES, max_length=50)
    is_hidden = models.BooleanField(default=False)
    out_of_stock = models.BooleanField(default=False)


    def __str__(self):
        return self.name