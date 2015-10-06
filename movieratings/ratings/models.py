from django.db import models

# Create your models here.
# Create Django models for users (call the model Rater so as not to
# confuse it with Django users), movies, and ratings. Make sure that
# your models can contain the data from your dataset.


class Rater(models.Model):
    # userId,movieId,rating,timestamp
    rater_id = models.CharField(max_length=11)


class Movies(models.Model):
    class Meta:
        verbose_name_plural = 'movies'

    movie_id = models.CharField(max_length=11)
    title = models.CharField(max_length=255)
    action = models.BooleanField()
    adventure = models.BooleanField()
    animation = models.BooleanField()
    childrens = models.BooleanField()
    comedy = models.BooleanField()
    crime = models.BooleanField()
    documentary = models.BooleanField()
    drama = models.BooleanField()
    fantasy = models.BooleanField()
    film_noir = models.BooleanField()
    horror = models.BooleanField()
    musical = models.BooleanField()
    mystery = models.BooleanField()
    romance = models.BooleanField()
    sci_fi = models.BooleanField()
    thriller = models.BooleanField()
    war = models.BooleanField()
    western = models.BooleanField()


class Ratings(models.Model):
    class Meta:
        verbose_name_plural = 'ratings'

    rater = models.ForeignKey(Rater)
    movid_id = models.ForeignKey(Movies)
    rating = models.FloatField()
