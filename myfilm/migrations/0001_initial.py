# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('image_path', models.FilePathField()),
                ('birth_date', models.DateField()),
                ('biography', models.TextField()),
                ('birth_place', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
                ('image_path', models.FilePathField()),
                ('imdb_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieArtist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=30)),
                ('artist_name', models.ForeignKey(to='myfilm.Artist')),
                ('movie', models.ForeignKey(to='myfilm.Movie')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='movieartist',
            unique_together=set([('artist_name', 'movie')]),
        ),
    ]
