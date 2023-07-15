
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from directs.models import Message
from django.contrib.auth.models import User
from profiles.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None
    profile = get_object_or_404(Profile, user=user)

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, reciepient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    context = {
        'directs':directs,
        'messages': messages,
        'active_direct': active_direct,
        'profile': profile,
    }
    return render(request, 'direct/direct.html', context)