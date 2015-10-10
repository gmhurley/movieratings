from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Movie, Rater

# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    return render(request,
                  'moviedata/movie.html',
                  {'movie': movie})

def user_detail(request, user_id):
    user = Rater.objects.get(pk=user_id)

    return render(request,
                  'moviedata/user.html',
                  {'user': user})
