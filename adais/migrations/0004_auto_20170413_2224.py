# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-13 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adais', '0003_auto_20160921_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=140)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OpenHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('openTime', models.TimeField()),
                ('closeTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurantId', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='openhours',
            name='restaurantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adais.Restaurant'),
        ),
        migrations.AddField(
            model_name='deal',
            name='restaurantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adais.Restaurant'),
        ),
    ]
