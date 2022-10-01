from rest_framework import viewsets, mixins
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Order.objects.all()

    def get_queryset(self):
        return Order.objects.all()

    def get_serializer_class(self):
        return OrderSerializer