# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistAPP', '0002_auto_20180923_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='endTime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='startTime',
            field=models.DateField(),
        ),
    ]
