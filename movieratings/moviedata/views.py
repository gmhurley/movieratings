from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from .models import Movie, Rater, Rating
from django.contrib import messages

from .forms import RatingForm

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
    rater = Rater.objects.get(pk=user_id)

    return render(request,
                  'moviedata/user.html',
                  {'rater': rater})


def top_movies(request):
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=1000)

    movies = popular_movies.annotate(Avg('rating__rating')) \
                           .order_by('-rating__rating__avg')[:20]

    return render(request,
                  'moviedata/index.html',
                  {'movies': movies})

@login_required
def user_rating(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        try:
            user_rating = Rating.objects.get(movie_id=movie_id, rater_id=request.user.id)
            form = RatingForm(request.POST, instance=user_rating)
        except ObjectDoesNotExist:
            form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie_id = movie_id
            rating.rater_id = request.user.id
            rating.save()
            messages.add_message(request, messages.SUCCESS, "Rating saved!")
            url = reverse('movie', kwargs={'movie_id': movie_id})
            return HttpResponseRedirect(url)

    else:
        try:
            user_rating = Rating.objects.get(movie_id=movie_id, rater_id=request.user.id)
            form = RatingForm(instance=user_rating)
        except ObjectDoesNotExist:
            form = RatingForm()

    return render(request, 'moviedata/rating.html', {'movie': movie,
                                                     'form': form})
