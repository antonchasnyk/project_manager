# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 07:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcb', '0016_auto_20170423_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bom',
            name='components',
            field=models.ManyToManyField(through='pcb.BomComponent', to='components.Component', verbose_name='Компоненты'),
        ),
        migrations.AlterField(
            model_name='bom',
            name='pcb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcb.Pcb', verbose_name='Печатная плата'),
        ),
        migrations.AlterField(
            model_name='bomcomponent',
            name='bom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcb.Bom', verbose_name='Перечень элементов'),
        ),
        migrations.AlterField(
            model_name='bomcomponent',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Component', verbose_name='Элемент'),
        ),
        migrations.AlterField(
            model_name='schematic',
            name='pcb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcb.Pcb', verbose_name='Печатная плата'),
        ),
    ]
