# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150603_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image_path',
            field=models.FilePathField(default=b'default.jpg', null=True),
        ),
    ]
