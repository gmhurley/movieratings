from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'movie/(?P<movie_id>\d+)$', views.movie_detail, name='movie'),
    url(r'user/(?P<user_id>\d+)$', views.user_detail, name='user'),
    url(r'rating/(?P<movie_id>\d+)$', views.user_rating, name='user_rating'),
    url(r'^rater/', include('users.urls')),
    url(r'^$', views.top_movies, name='index')
]
