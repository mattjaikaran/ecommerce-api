from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Product

class ProductSerializer(TaggitSerializer, serializers.ModelSerializer):
  tags = TagListSerializerField()
  
  class Meta:
    model = Product
    fields = ('__all__')
