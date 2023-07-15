from directs.views import inbox
from django.urls import path

app_name = 'directs'

urlpatterns = [
    path('inbox', inbox, name="message"),


]
