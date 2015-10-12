from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'movie/(?P<movie_id>\d+)$', views.movie_detail, name='movie'),
    url(r'user/(?P<user_id>\d+)$', views.user_detail, name='user'),
    url(r'^$', views.top_movies, name='index')
]
