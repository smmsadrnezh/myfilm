# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('myfilm', '__first__'),
        ('accounts', '0005_auto_20150603_0758'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField()),
                ('movie', models.ForeignKey(to='myfilm.Movie')),
                ('username', models.ForeignKey(to='accounts.CustomUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='movie_rating',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='movie_rating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='movie_rating',
            name='username',
        ),
        migrations.DeleteModel(
            name='Movie_Rating',
        ),
        migrations.AlterUniqueTogether(
            name='movierating',
            unique_together=set([('username', 'movie')]),
        ),
    ]
