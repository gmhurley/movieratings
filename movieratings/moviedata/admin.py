from django.contrib import admin
from .models import Movie, Occupation, Rater, Rating, Genre

# Register your models here.
admin.site.register(Movie)
admin.site.register(Occupation)
admin.site.register(Rater)
admin.site.register(Rating)
admin.site.register(Genre)
