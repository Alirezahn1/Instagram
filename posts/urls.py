from django.urls import path
app_name = 'posts'

from .views import *


urlpatterns = [
    path('',index,name='home'),
    path('newpost/',NewPost,name='newpost'),
    path('<uuid:post_id>', PostDetail, name='post-details'),
    path('<uuid:post_id>/like', like, name='like'),
    path('<uuid:post_id>/favourite', favourite, name='favourite'),



]