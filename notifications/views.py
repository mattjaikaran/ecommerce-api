from rest_framework import viewsets, mixins
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification.objects.all()

    def get_serializer_class(self):
        return NotificationSerializer