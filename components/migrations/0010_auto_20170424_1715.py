# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0009_auto_20170424_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitor',
            name='voltage',
            field=models.FloatField(db_index=True, default=5, verbose_name='Напряжение'),
        ),
    ]
