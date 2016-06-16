# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_cliente_usuario'),
        ('pc', '0004_auto_20160615_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('serial', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('Mini', 'Mini'), ('Laptop', 'Laptop')], max_length=50)),
                ('cargador', models.BooleanField(default=True)),
                ('bolso', models.BooleanField(default=False)),
                ('bateria', models.BooleanField(default=True)),
                ('detalles', models.TextField(default='Ninguno')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
        migrations.AlterField(
            model_name='desktop',
            name='am',
            field=models.ManyToManyField(to='pc.Ram'),
        ),
    ]
