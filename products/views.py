from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.all()

    def get_serializer_class(self):
        return ProductSerializer