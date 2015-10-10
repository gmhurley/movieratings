from django.db import models

# Create your models here.


class Movies(models.Model):
    """Represents the data IRT movies."""
    title = models.CharField(max_length=255)


class Occupation(models.Model):
    """List of the available occupations."""
    title = models.CharField(max_length = 55)


class Rater(models.Model):
    """Represents the users that have rated movies."""
    # Gender::Age::Occupation::Zip-code

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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age_group = models.PositiveSmallIntegerField()
    occupation = models.ForeignKey(Occupation)
    zipcode = models.CharField(max_length=10)


class Ratings(models.Model):
    """Represents users ratings of movies."""
    rating = models.PositiveSmallIntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movies)

    def __str__(self):
        return str(self.id)


class Movie_Genres(models.Model):
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
