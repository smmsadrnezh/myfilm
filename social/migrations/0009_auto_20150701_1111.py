# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('social', '0008_auto_20150623_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierating',
            name='rate',
            field=models.FloatField(),
        ),
    ]
