from rest_framework import viewsets, mixins
from .models import Order
from .serializers import OrderSerializer
from .api import (
    get_customers_list,
    create_customer,
    get_customer,
    modify_customer,
    delete_customer
)
from .webhook import stripe_webhook

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