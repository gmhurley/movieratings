from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()
ml_dir = '../ml-1m'

def import_users():
    import csv
    import json

    users = []

    field_names = 'UserID::Gender::Age::Occupation::Zip-code'

    with open(ml_dir + '/users.dat') as f:
        reader = csv.DictReader([line.replace("::", '\t') for line in f],
                                fieldnames=field_names.split('::'),
                                delimiter='\t')
        for row in reader:
            while True:
                email = fake.email()
                if User.objects.filter(username=email):
                    continue
                else:
                    break
            auth_user = User.objects.create_user(username=email,
                                                 email=email,
                                                 password=make_password('password'),
                                                 first_name=fake.first_name(),
                                                 last_name=fake.last_name())

            user = {'fields': {'gender': row['Gender'],
                               'age_group': row['Age'],
                               'occupation': row['Occupation'],
                               'zipcode': row['Zip-code']},
                    'model': 'moviedata.Rater',
                    'pk': auth_user.pk}
            users.append(user)
            auth_user.save()

    with open('moviedata/fixtures/users.json', 'w') as f:
        f.write(json.dumps(users))

def import_occupations():
    import json

    occupations = []

    occupation = {'0':  "other or not specified",
                  '1':  "academic/educator",
                  '2':  "artist",
                  '3':  "clerical/admin",
                  '4':  "college/grad student",
                  '5':  "customer service",
                  '6':  "doctor/health care",
                  '7':  "executive/managerial",
                  '8':  "farmer",
                  '9':  "homemaker",
                  '10':  "K-12 student",
                  '11':  "lawyer",
                  '12':  "programmer",
                  '13':  "retired",
                  '14':  "sales/marketing",
                  '15':  "scientist",
                  '16':  "self-employed",
                  '17':  "technician/engineer",
                  '18':  "tradesman/craftsman",
                  '19':  "unemployed",
                  '20':  "writer"}

    for key, title in occupation.items():
        job = {'fields': {'title': title},
               'model': 'moviedata.Occupation',
               'pk': int(key)}
        occupations.append(job)


    with open('moviedata/fixtures/occupations.json', 'w') as f:
        f.write(json.dumps(occupations))


def import_movies():
    import csv
    import json

    movies = []
    movies_genres = []

    with open(ml_dir + '/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split('::'),
                                delimiter='\t')

        for row in reader:
            genres = (row['Genres'].split('|'))

            movie = {
                'fields': {
                    'title': row['Title']},
                'model': 'moviedata.Movie',
                'pk': row['MovieID'],
            }

            movie_genres = {
                'fields':{
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
                'model': 'moviedata.Movie_Genre',
                'pk': row['MovieID']
            }
            # set genre to True if it's in the genre list
            for genre in genres:
                for k in movie_genres['fields'].keys():
                    if k.startswith(genre[:4].lower()):
                        movie_genres['fields'][k] = True

            movies.append(movie)
            movies_genres.append(movie_genres)

        with open('moviedata/fixtures/movies.json', 'w') as f:
            f.write(json.dumps(movies))

        with open('moviedata/fixtures/genres.json', 'w') as f:
            f.write(json.dumps(movies_genres))

def import_ratings():
    import csv
    import json

    ratings = []

    field_names = 'UserID::MovieID::Rating::Timestamp'

    with open(ml_dir + '/ratings.dat') as f:
        reader = csv.DictReader([line.replace("::", '\t') for line in f],
                                fieldnames=field_names.split('::'),
                                delimiter='\t')
        for row in reader:
            rating = {'fields': {'rating': row['Rating'],
                               'rater': row['UserID'],
                               'movie': row['MovieID']},
                    'model': 'moviedata.Rating'}
            ratings.append(rating)

    with open('moviedata/fixtures/ratings.json', 'w') as f:
        f.write(json.dumps(ratings))
