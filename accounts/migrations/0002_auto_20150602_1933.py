# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('follower', models.ForeignKey(related_name='+', to='accounts.CustomUser')),
                ('following', models.ForeignKey(related_name='+', to='accounts.CustomUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('follower', 'following')]),
        ),
    ]
