from django.db import models

# Create your models here.


class Occupation(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
            return self.title


class Rater(models.Model):
    age = models.IntegerField(null=True)
    # https://en.wikipedia.org/wiki/ISO/IEC_5218
    # 0 = Unknown, 1 = Male, 2 = Female, 9 = not specified
    gender = models.CharField(max_length=1)
    occupation = models.ForeignKey(Occupation)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return 'Age: {}  Occupation: {}  Zip: {}'.format(self.age,
                                                         self.occupation,
                                                         self.zip_code)


class Movies(models.Model):
    class Meta:
        verbose_name_plural = 'movies'

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

    def __str__(self):
        return self.title


class Ratings(models.Model):
    class Meta:
        verbose_name_plural = 'ratings'

    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movies)
    rating = models.FloatField()

    def __str__(self):
        return 'Movie: {}  Rater: {}  Rating: {}'.format(self.movie,
                                                         self.rater,
                                                         self.rating)
