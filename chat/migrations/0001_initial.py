# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_auto_20150602_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_Message',
            fields=[
                ('time', models.TimeField(serialize=False, primary_key=True)),
                ('message', models.TextField()),
                ('from_user', models.ForeignKey(related_name='+', to='accounts.CustomUser')),
                ('to_user', models.ForeignKey(related_name='+', to='accounts.CustomUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='chat_message',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
