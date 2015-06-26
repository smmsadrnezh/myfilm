# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20150613_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image_path',
            field=models.ImageField(default=b'default.jpg', null=True, upload_to=b''),
        ),
    ]
