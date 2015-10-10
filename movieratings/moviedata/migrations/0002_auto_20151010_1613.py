# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genres',
            old_name='movie_id',
            new_name='movie',
        ),
    ]
