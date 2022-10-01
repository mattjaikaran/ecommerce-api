from rest_framework import viewsets, mixins
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Customer.objects.all()

    def get_queryset(self):
        return Customer.objects.all()

    def get_serializer_class(self):
        return CustomerSerializer
