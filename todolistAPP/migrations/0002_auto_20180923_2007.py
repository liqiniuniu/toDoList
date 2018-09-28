# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(to='todolistAPP.User'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('Email',)]),
        ),
    ]
