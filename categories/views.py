from rest_framework import viewsets, mixins
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializer
