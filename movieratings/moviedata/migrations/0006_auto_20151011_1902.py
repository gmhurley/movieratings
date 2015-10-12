# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0005_auto_20151011_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rater',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
