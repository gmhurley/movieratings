from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Movie, Rater, Rating

# Create your views here.


def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    try:
        user_rating = Rating.objects.get(movie_id=movie_id, rater_id=request.user.id)
    except:
        user_rating = ''

    return render(request,
                  'moviedata/movie.html',
                  {'movie': movie,
                   'user_rating': user_rating})

def user_detail(request, user_id):
    user = Rater.objects.get(pk=user_id)

    return render(request,
                  'moviedata/user.html',
                  {'user': user})


def top_movies(request):
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=1000)

    movies = popular_movies.annotate(Avg('rating__rating')) \
                           .order_by('-rating__rating__avg')[:20]

    return render(request,
                  'moviedata/index.html',
                  {'movies': movies})
