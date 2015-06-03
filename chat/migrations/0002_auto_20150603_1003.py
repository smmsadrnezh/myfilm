# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150603_0758'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('time', models.TimeField(serialize=False, primary_key=True)),
                ('message', models.TextField()),
                ('from_user', models.ForeignKey(related_name='+', to='accounts.CustomUser')),
                ('to_user', models.ForeignKey(related_name='+', to='accounts.CustomUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='chat_message',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='chat_message',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='chat_message',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Chat_Message',
        ),
        migrations.AlterUniqueTogether(
            name='chatmessage',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
