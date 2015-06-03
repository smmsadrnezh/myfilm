# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_auto_20150602_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='real_name',
        ),
    ]
