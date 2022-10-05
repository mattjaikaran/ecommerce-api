from django.urls import path
from .views import NotificationViewSet

urlpatterns = [
    path('notifications/', NotificationViewSet.as_view()),
]