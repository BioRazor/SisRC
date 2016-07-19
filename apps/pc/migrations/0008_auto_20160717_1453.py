# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc', '0007_auto_20160717_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='adicional',
            field=models.ManyToManyField(blank=True, null=True, to='pc.Adicional', verbose_name='Dispositivos Adicionales'),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='am',
            field=models.ManyToManyField(to='pc.Ram', verbose_name='Memorias Ram'),
        ),
    ]
