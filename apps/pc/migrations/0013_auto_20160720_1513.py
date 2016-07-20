# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-20 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc', '0012_auto_20160720_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktop',
            name='estado',
            field=models.ManyToManyField(to='pc.Estado_PC'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='estado',
            field=models.ManyToManyField(to='pc.Estado_PC'),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='am',
            field=models.ManyToManyField(to='pc.Ram', verbose_name='Memorias Ram'),
        ),
    ]