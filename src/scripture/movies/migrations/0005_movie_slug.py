# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20160210_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]