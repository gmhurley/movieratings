from django.contrib import admin
from .models import Rater, Movies, Ratings, Occupation

# Register your models here.
admin.site.register(Rater)
admin.site.register(Movies)
admin.site.register(Ratings)
admin.site.register(Occupation)
