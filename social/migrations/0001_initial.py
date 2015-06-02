# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('myfilm', '__first__'),
        ('accounts', '0002_auto_20150602_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField()),
                ('movie', models.ForeignKey(to='myfilm.Movie')),
                ('username', models.ForeignKey(to='accounts.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created_time', models.TimeField()),
                ('movie', models.ForeignKey(to='myfilm.Movie')),
                ('username', models.ForeignKey(to='accounts.CustomUser')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='post_id',
            field=models.ForeignKey(to='social.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='username',
            field=models.ForeignKey(to='accounts.CustomUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(to='social.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(to='accounts.CustomUser'),
        ),
        migrations.AlterUniqueTogether(
            name='movie_rating',
            unique_together=set([('username', 'movie')]),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('username', 'post_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('username', 'post_id')]),
        ),
    ]
