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
            user = {'fields': {'gender': row['Gender'],
                               'age_group': row['Age'],
                               'occupation': row['Occupation'],
                               'zipcode': row['Zip-code']},
                    'model': 'movieratings.Rater',
                    'pk': int(row['UserID'])}
            users.append(user)

    with open('moviedata/fixtures/users.json', 'w') as f:
        print("here")
        f.write(json.dumps(users))
