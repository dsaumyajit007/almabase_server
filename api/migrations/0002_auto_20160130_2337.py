# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(),
        ),
    ]
