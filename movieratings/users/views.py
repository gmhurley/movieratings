from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import UserForm
from moviedata.models import Rater

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "You are now logged in as {}".format(user.username))
            return redirect('index')
        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})


    return render(request,
                  'users/login.html')

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
                  'users/register.html',
                  {'form': form}

    )

def user_logout(request):
    logout(request)
    return redirect('index')
