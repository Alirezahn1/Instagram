from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from django.views import View
from django.db.models import Q

from posts.forms import NewPostform
from posts.models import Follow, Stream, Post, Tag
from profiles.models import Profile


class HomeView(View):
    def get(self, request):
        user = request.user.id
        all_users = User.objects.all()
        follow_status = Follow.objects.filter(following=user, follower=request.user.id).exists()

        profile = Profile.objects.all()

        posts = Stream.objects.filter(user=user)
        group_ids = []

        for post in posts:
            group_ids.append(post.post_id)

        post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')

        query = request.GET.get('q')
        if query:
            users = User.objects.filter(Q(username__icontains=query))

            paginator = Paginator(users, 6)
            page_number = request.GET.get('page')
            users_paginator = paginator.get_page(page_number)

        context = {
            'post_items': post_items,
            'follow_status': follow_status,
            'profile': profile,
            'all_users': all_users,
            # 'users_paginator': users_paginator,
        }
        return render(request, 'base/home.html',context)


@login_required
def NewPost(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    tags_obj = []

    if request.method == "POST":
        form = NewPostform(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tags')
            tag_list = list(tag_form.split(','))

            for tag in tag_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_obj.append(t)
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user=user)
            p.tags.set(tags_obj)
            p.save()
            return redirect('posts:home')
    else:
        form = NewPostform()
    context = {
        'form': form
    }
    return render(request, 'post/newpost.html', context)