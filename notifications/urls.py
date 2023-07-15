from django.urls import path
from notifications.views import ShowNotification, DeleteNotification


app_name = 'notifications'

urlpatterns = [
    path('ShowNotification/', ShowNotification, name='show-notification'),
    path('<noti_id>/delete', DeleteNotification, name='delete-notification'),


]