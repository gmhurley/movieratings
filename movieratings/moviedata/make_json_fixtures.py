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

    with open(ml_dir + '/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split('::'),
                                delimiter='\t')

        genre_lookup = {"action": 1,
                        "adventure": 2,
                        "animation": 3,
                        "childrens": 4,
                        "comedy": 5,
                        "crime": 6,
                        "documentary": 7,
                        "drama": 8,
                        "fantasy": 9,
                        "film_noir": 10,
                        "horror": 11,
                        "musical": 12,
                        "mystery": 13,
                        "romance": 14,
                        "sci_fi": 15,
                        "thriller": 16,
                        "war": 17,
                        "western": 18,}

        for row in reader:
            genres = (row['Genres'].split('|'))
            genres = [x.lower().replace("'", "").replace("-", "_") for x in genres]
            num_genres = [genre_lookup[x] for x in genres]


            movie = {
                'fields': {
                    'title': row['Title'],
                    'genres': num_genres},
                'model': 'moviedata.Movie',
                'pk': row['MovieID'],
            }

            movies.append(movie)


        with open('moviedata/fixtures/movies.json', 'w') as f:
            f.write(json.dumps(movies))

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


def import_genres():
    import json

    genres_load = []

    genres = ['action', 'adventure', 'animation', 'childrens', 'comedy',
              'crime', 'documentary', 'drama', 'fantasy', 'film_noir', 'horror',
              'musical', 'mystery', 'romance', 'sci_fi', 'thriller', 'war',
              'western']

    for x in genres:
        genre = {'fields': {'title': x},
                 'model': 'moviedata.Genre'}
        genres_load.append(genre)

    with open('moviedata/fixtures/genres.json', 'w') as f:
        f.write(json.dumps(genres_load))
