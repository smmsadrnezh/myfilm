# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20150603_0758'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_path', models.FilePathField(default=b'default.jpg', null=True)),
                ('birth_date', models.DateField(null=True)),
                ('user', models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
