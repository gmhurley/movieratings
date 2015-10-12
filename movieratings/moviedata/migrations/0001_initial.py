# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'No answer')], max_length=1)),
                ('age_group', models.PositiveSmallIntegerField()),
                ('zipcode', models.CharField(max_length=10)),
                ('occupation', models.ForeignKey(to='moviedata.Occupation')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(to='moviedata.Movies')),
                ('rater', models.ForeignKey(to='moviedata.Rater')),
            ],
        ),
        migrations.AddField(
            model_name='genres',
            name='movie_id',
            field=models.ForeignKey(to='moviedata.Movies'),
        ),
    ]
