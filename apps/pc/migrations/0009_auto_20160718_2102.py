# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc', '0008_auto_20160717_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='am',
            field=models.ManyToManyField(to='pc.Ram', verbose_name='Memorias Ram'),
        ),
    ]
