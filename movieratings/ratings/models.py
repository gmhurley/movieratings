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


def load_ml_users():
    import csv
    import json

    users = []

    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zip_code': row['Zip-code'],
                },
                'model': 'ratings.Rater',
                'pk': row['UserID'],
            }

            users.append(user)

        with open('users.json', 'w') as f:
            f.write(json.dumps(users))


def load_ml_occupations():
    import json

    occupations_lst = []

    occupations = {
        0:  "other or not specified",
        1:  "academic/educator",
        2:  "artist",
        3:  "clerical/admin",
        4:  "college/grad student",
        5:  "customer service",
        6:  "doctor/health care",
        7:  "executive/managerial",
        8:  "farmer",
        9:  "homemaker",
        10:  "K-12 student",
        11:  "lawyer",
        12:  "programmer",
        13:  "retired",
        14:  "sales/marketing",
        15:  "scientist",
        16:  "self-employed",
        17:  "technician/engineer",
        18:  "tradesman/craftsman",
        19:  "unemployed",
        20:  "writer",
    }

    for key, job in occupations.items():
        occupation = {
            'fields': {
                'title': job,
            },
            'model': 'ratings.Occupation',
            'pk': key
        }

        occupations_lst.append(occupation)

    with open('occupations.json', 'w') as f:
        f.write(json.dumps(occupations_lst))


def load_ml_movies():
    import csv
    import json

    movies = []

    with open('ml-1m/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split('::'),
                                delimiter='\t')

        movies = []

        for row in reader:
            genres = (row['Genres'].split('|'))

            movie = {
                'fields': {
                    'title': row['Title'],
                    'action': False,
                    'adventure': False,
                    'animation': False,
                    'childrens': False,
                    'comedy': False,
                    'crime': False,
                    'documentary': False,
                    'drama': False,
                    'fantasy': False,
                    'film_noir': False,
                    'horror': False,
                    'musical': False,
                    'mystery': False,
                    'romance': False,
                    'sci_fi': False,
                    'thriller': False,
                    'war': False,
                    'western': False,
                                },
                'model': 'ratings.Movies',
                'pk': row['MovieID'],
            }
            # set genre to True if it's in the genre list
            for genre in genres:
                for k, v in movie['fields'].items():
                    if k.startswith(genre[:4].lower()):
                        movie['fields'][k] = True

            movies.append(movie)

        with open('movies.json', 'w') as f:
            f.write(json.dumps(movies))


def load_ml_ratings():
    import csv
    import json

    ratings = []

    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating::Timestamp'.split('::'),
                                delimiter='\t')
        for row in reader:
            rating = {
                'fields': {
                    'rating': row['Rating'],
                    'movie_id': row['MovieID'],
                    'rater_id': row['UserID'],
                },
                'model': 'ratings.Ratings',
            }

            ratings.append(rating)

        with open('ratings.json', 'w') as f:
            f.write(json.dumps(ratings))
