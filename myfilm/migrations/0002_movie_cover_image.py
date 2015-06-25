# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfilm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover_image',
            field=models.FilePathField(null=True),
        ),
    ]
