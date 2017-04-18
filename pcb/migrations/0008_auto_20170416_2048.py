# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcb', '0007_auto_20170416_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pcb',
            name='bom',
        ),
        migrations.AddField(
            model_name='bom',
            name='pcb',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pcb.Pcb'),
            preserve_default=False,
        ),
    ]
