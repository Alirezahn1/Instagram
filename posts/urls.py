from django.urls import path
app_name = 'posts'

from .views import *


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('newpost/',NewPost,name='newpost'),





]