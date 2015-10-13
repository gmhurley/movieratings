# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0010_auto_20151012_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 1, 2, 23, 147751, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
