from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    """Represents the data IRT movies."""
    title = models.CharField(max_length=255)

    def avg_rating(self):
        return self.rating_set.aggregate(models.Avg('rating'))['rating__avg']

    def num_ratings(self):
        return self.rating_set.aggregate(models.Count('rating'))['rating__count']

    def __str__(self):
        return str(self.title)


class Occupation(models.Model):
    """List of the available occupations."""
    title = models.CharField(max_length = 55)

    def __str__(self):
        return str(self.title)

class Rater(models.Model):
    """Represents the users that have rated movies."""

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (X, 'No answer')
    )
    user = models.OneToOneField(User, primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    age_group = models.PositiveSmallIntegerField(blank=True, null=True)
    occupation = models.ForeignKey(Occupation, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str("{}: {}: {}: {}".format(self.gender, self.age_group,
                                           self.occupation, self.zipcode))


class Rating(models.Model):
    """Represents users ratings of movies."""

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    review = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)


class Movie_Genre(models.Model):
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
