# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcb', '0002_auto_20170414_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='BomComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotation', models.CharField(max_length=10, verbose_name='Annotation')),
                ('bom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcb.Bom', verbose_name='Bill of material')),
            ],
            options={
                'verbose_name': 'Bom to Component',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Footprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Resistor',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pcb.Component')),
                ('resistance', models.PositiveIntegerField(default=0)),
            ],
            bases=('pcb.component',),
        ),
        migrations.AddField(
            model_name='component',
            name='footprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcb.Footprint'),
        ),
        migrations.AddField(
            model_name='bomcomponent',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcb.Component', verbose_name='Component'),
        ),
        migrations.AddField(
            model_name='bom',
            name='components',
            field=models.ManyToManyField(null=True, through='pcb.BomComponent', to='pcb.Component', verbose_name='components'),
        ),
        migrations.AlterUniqueTogether(
            name='bomcomponent',
            unique_together=set([('component', 'bom', 'annotation')]),
        ),
    ]
