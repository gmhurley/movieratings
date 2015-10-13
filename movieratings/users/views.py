from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserForm, RaterForm
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


@login_required
def edit_rater(request):
    try:
        rater = request.user.rater
    except Rater.DoesNotExist:
        rater = Rater(user=request.user)

    if request.method == 'GET':
        rater_form = RaterForm(instance=rater)
    elif request.method == 'POST':
        rater_form = RaterForm(data=request.POST, instance=rater)
        if rater_form.is_valid():
            rater_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile has been udpated.')

    return render(request, 'users/edit_rater.html', {'form': rater_form})
