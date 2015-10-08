# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('action', models.BooleanField()),
                ('adventure', models.BooleanField()),
                ('animation', models.BooleanField()),
                ('childrens', models.BooleanField()),
                ('comedy', models.BooleanField()),
                ('crime', models.BooleanField()),
                ('documentary', models.BooleanField()),
                ('drama', models.BooleanField()),
                ('fantasy', models.BooleanField()),
                ('film_noir', models.BooleanField()),
                ('horror', models.BooleanField()),
                ('musical', models.BooleanField()),
                ('mystery', models.BooleanField()),
                ('romance', models.BooleanField()),
                ('sci_fi', models.BooleanField()),
                ('thriller', models.BooleanField()),
                ('war', models.BooleanField()),
                ('western', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=1)),
                ('zip_code', models.CharField(max_length=10)),
                ('occupation', models.ForeignKey(to='ratings.Occupation')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('movie', models.ForeignKey(to='ratings.Movies')),
                ('rater', models.ForeignKey(to='ratings.Rater')),
            ],
            options={
                'verbose_name_plural': 'ratings',
            },
        ),
    ]
