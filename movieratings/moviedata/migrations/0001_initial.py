# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
            name='Occupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'No answer')], null=True, max_length=1)),
                ('age_group', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('zipcode', models.CharField(blank=True, null=True, max_length=10)),
                ('occupation', models.ForeignKey(to='moviedata.Occupation', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('review', models.CharField(blank=True, null=True, max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(to='moviedata.Movie')),
                ('rater', models.ForeignKey(to='moviedata.Rater')),
            ],
        ),
    ]
