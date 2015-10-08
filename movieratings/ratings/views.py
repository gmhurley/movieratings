from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies, Ratings, Rater

# Create your views here.


def all_movies(request):
    movies = Movies.objects.all()[:20]
    # titles = [str(title) for title in movies]
    return render(request,
                  'ratings/movies.html',
                  {'movies': movies})


def movie_detail(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)
    ratings = movie.ratings_set.all()

    ratings_total = 0.0
    user_ratings = []

    for rating in ratings:
        ratings_total += rating.rating
        user_ratings.append([rating.rater_id, rating.rating])
    avg_rating = round(ratings_total / len(ratings), 2)

    return render(request,
                  'ratings/movie.html',
                  {'avg_rating': avg_rating,
                   'movie': movie,
                   'num_ratings': len(ratings),
                   'user_ratings': user_ratings})
