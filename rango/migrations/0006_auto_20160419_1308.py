# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20160419_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='ph1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufac1', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='phm1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonmode1', models.CharField(max_length=50)),
                ('manu1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.ph1')),
            ],
        ),
        migrations.RemoveField(
            model_name='phm',
            name='manu',
        ),
        migrations.DeleteModel(
            name='ph',
        ),
        migrations.DeleteModel(
            name='phm',
        ),
    ]
