# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='prefijo_telefono',
            field=models.CharField(choices=[('0412', '0412'), ('0426', '0426'), ('0416', '0416'), ('0424', '0424')], max_length=50),
        ),
    ]
