from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Movies, Rater

# Create your views here.


def movie_detail(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)

    return render(request,
                  'ratings/movie.html',
                  {'movie': movie},)


def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    movie_ratings = []
    for rating in rater.ratings_set.all():
        movie_ratings.append({
            'movie': rating.movie,
            'rating': rating.rating,
        })

    return render(request,
                  'ratings/user.html',
                  {'rater': rater,
                   'movie_ratings': movie_ratings})


def top_movies(request):
    popular_movies = Movies.objects.annotate(num_ratings=Count('ratings')) \
                                  .filter(num_ratings__gte=100)

    movies = popular_movies.annotate(Avg('ratings__rating')) \
                           .order_by('-ratings__rating__avg')[:20]

    return render(request,
                  'ratings/top_movies.html',
                  {'movies': movies})
