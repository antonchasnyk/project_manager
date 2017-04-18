# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcb', '0004_auto_20170416_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transistors',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pcb.Component')),
                ('type', models.CharField(max_length=20)),
            ],
            bases=('pcb.component',),
        ),
    ]
