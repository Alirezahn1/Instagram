from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View
from .forms import EditProfileForm, UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Profile.get_or_create(user=request.user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hurray your account was created!!')

            # Automatically Log In The User
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'], )
            login(request, new_user)

            return redirect('posts:home')



    elif request.user.is_authenticated:
        return redirect('posts:home')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'user/sign-up.html', context)
