from django.shortcuts import render

# Create your views here.
from notifications.models import Notification


def ShowNotification(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')

    context = {
        'notifications': notifications,

    }
    return render(request, 'notification/notification.html', context)