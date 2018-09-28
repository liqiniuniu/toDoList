# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistAPP', '0004_auto_20180924_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='finished',
            field=models.IntegerField(default=0, choices=[(1, b'finished'), (0, b'not finished')]),
        ),
    ]
