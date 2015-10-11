# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0007_auto_20151011_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='age_group',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'No answer')], null=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.ForeignKey(blank=True, to='moviedata.Occupation', null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
