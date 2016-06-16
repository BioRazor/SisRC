# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pc', '0002_auto_20160615_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='moBo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pc.MoBo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='desktop',
            name='am',
            field=models.ManyToManyField(to='pc.Ram'),
        ),
    ]