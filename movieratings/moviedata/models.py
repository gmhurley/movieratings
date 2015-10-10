from django.db import models

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

    def __str__(self):
        return str("{}: {}: {}: {}".format(self.gender, self.age_group,
                                           self.occupation, self.zipcode))


class Rating(models.Model):
    """Represents users ratings of movies."""
    rating = models.PositiveSmallIntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return str("{}: {}: {}".format(self.movie, self.rater, self.rating))


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
