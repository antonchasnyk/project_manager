# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcb', '0010_component_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacitor',
            name='component_ptr',
        ),
        migrations.RemoveField(
            model_name='component',
            name='footprint',
        ),
        migrations.RemoveField(
            model_name='resistor',
            name='component_ptr',
        ),
        migrations.RemoveField(
            model_name='transistor',
            name='component_ptr',
        ),
        migrations.AlterModelOptions(
            name='bomcomponent',
            options={'verbose_name': 'Component in Bom', 'verbose_name_plural': 'Components in Bom'},
        ),
        migrations.AlterField(
            model_name='bom',
            name='components',
            field=models.ManyToManyField(through='pcb.BomComponent', to='components.Component', verbose_name='components'),
        ),
        migrations.AlterField(
            model_name='bomcomponent',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Component', verbose_name='Component'),
        ),
        migrations.DeleteModel(
            name='Capacitor',
        ),
        migrations.DeleteModel(
            name='Component',
        ),
        migrations.DeleteModel(
            name='Footprint',
        ),
        migrations.DeleteModel(
            name='Resistor',
        ),
        migrations.DeleteModel(
            name='Transistor',
        ),
    ]
