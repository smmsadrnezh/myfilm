# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20150613_0816'),
        ('social', '0005_auto_20150623_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
                ('time', models.TimeField(default=datetime.datetime(2015, 6, 23, 21, 10, 37, 795664, tzinfo=utc))),
                ('username', models.ForeignKey(to='accounts.CustomUser')),
            ],
        ),
    ]
