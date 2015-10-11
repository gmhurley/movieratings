# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0008_auto_20151011_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rater',
            name='id',
        ),
        migrations.AlterField(
            model_name='rater',
            name='user',
            field=models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False),
        ),
    ]
