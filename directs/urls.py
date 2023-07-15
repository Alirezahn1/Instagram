from directs.views import inbox, Directs, SendDirect
from django.urls import path

app_name = 'directs'

urlpatterns = [
    path('inbox/', inbox, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-directs"),
]
