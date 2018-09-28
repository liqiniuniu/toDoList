# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistAPP', '0003_auto_20180923_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='endTime',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='startTime',
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(related_name='user_todo', to='todolistAPP.User'),
        ),
    ]
