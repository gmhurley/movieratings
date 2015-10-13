from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserForm
from moviedata.models import Rater

# Create your views here.

def user_registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)

            # linking to profile
            rater = Rater()
            rater.user = user
            user.save()
            rater.save()

            user = authenticate(username=user.username,
                                password=password)

            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request,
                  'registration/register.html',
                  {'form': form}

    )

def user_logout(request):
    logout(request)
    return redirect('index')
