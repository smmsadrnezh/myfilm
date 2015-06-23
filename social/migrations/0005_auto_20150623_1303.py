# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20150623_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.TextField(),
        ),
    ]
