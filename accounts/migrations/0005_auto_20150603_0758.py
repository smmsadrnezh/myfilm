# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150603_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image_path',
            field=models.FilePathField(null=True),
        ),
    ]
