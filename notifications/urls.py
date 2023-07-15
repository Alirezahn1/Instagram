from django.urls import path
from notifications.views import ShowNotification

urlpatterns = [
    path('', ShowNotification, name='show-notification'),


]