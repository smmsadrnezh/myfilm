# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('social', '0006_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='url',
            field=models.URLField(default=b'/post', max_length=50),
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
