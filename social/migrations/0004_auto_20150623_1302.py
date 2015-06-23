# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20150603_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.TextField(default=b'comment title'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(default=b'04:18:18.971000'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('username', 'post', 'time')]),
        ),
    ]
