# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurants'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Uncles',
        ),
        migrations.AlterModelOptions(
            name='restaurants',
            options={'verbose_name': 'Restaurant', 'verbose_name_plural': 'Restaurants'},
        ),
    ]