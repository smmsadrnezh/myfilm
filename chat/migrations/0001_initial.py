# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_auto_20150603_0758'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('from_user', models.ForeignKey(related_name='+', to='accounts.CustomUser')),
                ('to_user', models.ForeignKey(related_name='+', to='accounts.CustomUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='chatmessage',
            unique_together=set([('time', 'from_user', 'to_user')]),
        ),
    ]
