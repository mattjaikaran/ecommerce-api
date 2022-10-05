from uuid import uuid4
from django.db import models

class Review(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField('Name', max_length=50)
    content = models.TextField(max_length=500, blank=False)
    rating = models.IntegerField(max_length=1, null=False)
    fit = models.IntegerField(max_length=3, null=False)
    size = models.CharField('Size', max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
