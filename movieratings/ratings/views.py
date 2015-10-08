from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies, Ratings, Rater

# Create your views here.


def movie_detail(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)

    return render(request,
                  'ratings/movie.html',
                  {'movie': movie},)
