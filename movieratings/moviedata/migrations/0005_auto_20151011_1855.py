# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moviedata', '0004_auto_20151010_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rater',
            name='id',
        ),
        migrations.AddField(
            model_name='rater',
            name='user',
            field=models.OneToOneField(serialize=False, default='1', to=settings.AUTH_USER_MODEL, primary_key=True),
            preserve_default=False,
        ),
    ]
