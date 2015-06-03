# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('social', '0002_auto_20150603_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='post_id',
            new_name='post',
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('username', 'post')]),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('username', 'post')]),
        ),
    ]
