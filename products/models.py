from uuid import uuid4
from django.db import models
from categories.models import Category
from taggit.managers import TaggableManager

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Name', max_length=255)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, default="Empty description.")
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    picture = models.ImageField(upload_to='products/images', null=True, blank=True)
    category = models.ManyToManyField(Category, blank=False)
    quantity = models.IntegerField(default=10, max_length=4, null=True)
    tags = TaggableManager(blank=True) 
    is_hidden = models.BooleanField(default=False)

    @property
    def out_of_stock(self):
        return self.quantity < 1

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name