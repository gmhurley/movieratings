# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0006_auto_20151011_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='age_group',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1, blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'No answer')]),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.ForeignKey(to='moviedata.Occupation', blank=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
