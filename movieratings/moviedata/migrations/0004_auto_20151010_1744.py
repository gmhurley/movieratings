# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0003_auto_20151010_1614'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='Movie_Genres',
            new_name='Movie_Genre',
        ),
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
    ]
