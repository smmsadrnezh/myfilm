# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('social', '0004_auto_20150612_1750'),
        ('admin', '0001_initial'),
        ('accounts', '0006_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_ptr',
        ),
        migrations.AlterField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
